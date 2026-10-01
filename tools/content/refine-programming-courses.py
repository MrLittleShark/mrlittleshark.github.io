"""Refine the 17 programming lessons after build-programming-content.py.

Only the programming lesson JSON is changed. Existing executable code, TeX,
source attribution and verification statements are preserved. Every download is
validated against its actual ZIP, README, Make/files and published manifest.
Re-running this script is idempotent and does not require the review backup.

Build order: build-programming-content.py, then refine-programming-courses.py.
The second step also reapplies the v2512-only teaching language and the lesson
12 title; it must follow any earlier title-generation script.
"""
from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'tools/content/programming-content.json'
DOWNLOADS = ROOT / 'source-openfoam/downloads/programming'
REPORT = ROOT / '.openfoam-work/course-refinement/programming-review.json'

# Each edit belongs to the relevant explanation, rather than a common appendix.
REVISIONS = {
0: {
    'prerequisite': '能运行一个已有算例，了解 C++ 的 main、变量和输出语句',
    'intro': '已有求解器可以直接运行，自编程序则还需要完成编译和链接。本课先用一个只输出文字的小程序检查这条执行路径。这样，后续遇到错误时，可以先判断是程序没有正确生成，还是网格、参数或离散方程出了问题。完成本课后，再进入[字典输入输出](/read/?slug=programming-01)，给程序提供可修改的算例参数。',
    'summary': '从一个只输出文字的程序开始，说明源码、Make 文件、可执行文件和运行日志之间的关系。',
    'edits': [
        ('`main(int argc, char *argv[])` 是 C++ 入口。`argc` 给出参数数量，`argv` 保存参数字符串。`fvCFD.H` 汇集常用有限体积类型；初学时便于使用，开发较大的库时可换成实际需要的头文件，以减少编译依赖。',
         '`main(int argc, char *argv[])` 是 C++ 入口：运行程序后，执行从这个函数开始。`argc` 给出命令行参数数量，`argv` 保存各个参数的文字内容，例如后面会用到的 `-help`。目前只需理解参数从终端传入程序，具体读取方法将在编程 02 中展开。\n\n`fvCFD.H` 汇集常用有限体积类型，使下面的代码能够使用 OpenFOAM 的输出流和数据结构。它并不表示程序已经开始计算流体。初学时使用这个汇总头文件较方便；开发较大的库时，可换成实际需要的头文件，以减少编译依赖。'),
        ('`Make/files` 的第一部分列出参与编译的 `.C`，最后的 `EXE` 决定目标位置。`Make/options` 中，`-I` 指定头文件搜索目录，`-l` 指定链接库。缺少头文件是编译阶段错误，`undefined reference` 是链接阶段错误，运行时找不到 `.so` 则发生在动态加载阶段，三个问题应分别检查。',
         '`Make/files` 回答两个问题：哪些 `.C` 文件参与编译，以及最终程序放在哪里。最后的 `EXE` 指定可执行文件路径。`Make/options` 则提供编译和链接所需的信息：`-I` 帮助编译器找到头文件中的声明，`-l` 帮助链接器找到已经实现的库函数。\n\n因此，报错出现在哪一步，会决定检查哪个文件。找不到头文件时，先查 `-I` 路径；出现 `undefined reference` 时，先查源文件是否漏列、库是否正确链接；程序已经生成但运行时找不到 `.so`，再查运行环境和动态库路径。按阶段定位，通常比反复执行 `wmake` 更有效。'),
        ('运行 `testCase/Allrun` 后应出现自定义信息和 `End`，进程正常退出。本例没有结果时间目录是预期行为。把打印文本改为自己的名字并重新编译，输出随之改变，才能说明源码、编译目标和运行程序属于同一条路径。',
         '运行 `testCase/Allrun` 后，先在日志中找到自定义信息，再检查是否正常出现 `End` 并退出。本例没有读取网格或写出场，所以不会产生新的结果时间目录；这里需要观察的是终端文字。\n\n接着只修改一处打印文本，重新编译并运行。若新文字出现，就说明当前修改的源码确实生成了当前执行的程序；若仍显示旧文字，应先核对 `command -v ofTutorial0`，而不是继续修改算例字典。这是后续调试自定义求解器时同样需要做的检查。'),
    ],
    'package': '包内入口是 `OFtutorial0.C`，`Make/files` 生成 `ofTutorial0`。先在教程根目录编译，再进入 `testCase` 运行；这个程序的主要结果是文字输出，不需要寻找速度或压力云图。',
    'evidence': '本课提交三项对应记录即可：修改后的打印语句、成功编译日志，以及显示新文字的运行日志。故意引入编译错误时，记录编译器首次指出的文件和行号，再说明如何修复；本课尚未求解物理量，不要求提供流场数值。',
},
1: {
    'prerequisite': '已完成编程 00，理解变量类型和键值形式的算例字典',
    'intro': '[上一课](/read/?slug=programming-00)把输出文字写在源码中；若每改一个参数都重新编译，程序就很难重复使用。本课把参数移到算例字典，再把实际读到的值写进文本文件。沿着“字典中的条目—程序中的变量—输出文件”逐项核对，可以理解一个计算结果使用了哪些输入。',
    'summary': '把字典条目读成有明确类型的变量，比较默认值、列表与哈希表，并核对实际输入和文本输出。',
    'edits': [
        ('一个可复用的程序应把参数放在算例里。`IOobject` 描述文件名、所在时间或目录、所属对象注册表及读写策略；`IOdictionary` 才负责以字典结构保存条目。二者的分工有助于理解“文件存在，但读取失败”的原因。',
         '先区分“在哪里读文件”和“读出的内容怎样保存”。`IOobject` 描述文件名、所在时间或目录、所属对象注册表及读写策略；`IOdictionary` 根据这些信息读取文件，并按字典结构保存条目。对于 `constant/customProperties`，`customProperties` 是对象名，`constant` 是所在目录，二者共同确定读取位置。\n\n这种分工也给出了排错顺序：先确认路径和文件头正确，再检查键名及其数据类型。磁盘上有同名文件，只能说明文件存在，不能说明程序已经按预期读取它。'),
        ('`List<scalar>` 通过整数索引访问，适合有明确次序的数据。`HashTable<vector,word>` 通过名称关联向量，适合用边界名、测点名查找数据。哈希表的迭代顺序不构成稳定的物理顺序，绘图前应明确排序。',
         '`List<scalar>` 通过整数索引访问。例如，第 0、1、2 项可以分别对应按顺序布置的三个采样位置，只要程序与字典约定相同的次序即可。`HashTable<vector,word>` 则把名称与向量关联起来，适合直接查询名为 `probeA` 的测点坐标，不必先记住它排在第几项。\n\n两者对结果解释的影响在于顺序：列表有明确的位置次序，哈希表遍历的次序却不能当作空间或时间顺序。把哈希表内容导出为曲线前，应根据坐标、测点名或其他明确规则排序。'),
        ('先将 `someScalar` 从 `0.01` 改为 `0.1`，确认程序输出改变，再删除这个可选条目，确认读到默认值。另一次把 `someList` 的一个数字改为普通单词，应看到类型读取错误；这比只检查文件是否存在更接近真实输入验证。',
         '先将 `someScalar` 从 `0.01` 改为 `0.1`。只改字典、不重新编译，然后再次运行；输出随之变化，说明参数是在运行时从算例读取的。再删除这个可选条目，核对程序是否采用源码规定的默认值。注意：默认值取决于实际源码，不能由删掉前的数值推断。\n\n另一次把 `someList` 的一个数字改为普通单词，观察类型读取错误。这个实验说明读取成功还包含类型要求。检查 `postProcessing/customOutputFile.dat` 时，应把其中的数据与本次输入对应；它是普通文本结果，不能因为放在算例目录中就按 OpenFOAM 体场载入。'),
    ],
    'package': '重点对照 `OFtutorial1.C`、`testCase/constant/customProperties` 和生成的 `testCase/postProcessing/customOutputFile.dat`。包内 `testCase/Allrun` 先建立程序需要的网格，再运行输入输出示例；不要因为本课主要讲字典就跳过这一步。',
    'evidence': '提交新增 `samplingInterval` 的字典条目、正常输入时的输出头，以及输入小于 1 时的首条错误。把这三项放在一起，才能说明参数既被读取，也经过范围检查，而不只是显示了一段固定文字。',
},
2: {
    'prerequisite': '已完成编程 01，能区分字典参数、字符串与数值类型',
    'intro': '字典适合保存一套算例配置，命令行则适合在某一次运行中临时指定名称、数值或开关。本课在[字典输入](/read/?slug=programming-01)的基础上，说明程序怎样识别这些输入，并在计算开始前发现缺项或类型错误。阅读时先看 `-help`，再把每个选项与源码中的注册、读取位置对应起来。',
    'summary': '区分位置参数、布尔开关和带值选项，通过帮助信息及错误输入检查自定义工具的接口行为。',
    'edits': [
        ('命令行接口必须先声明，再构造 `argList`。否则程序解析输入时还不知道某个选项的含义。`argList::addNote()` 为 `-help` 添加用途说明；`validArgs.append()` 声明必需的位置参数；`addBoolOption()` 表示只检查是否出现的开关。',
         '程序看到的命令行最初只是若干字符串，必须先声明这些字符串怎样解释，再构造 `argList` 开始解析。`validArgs.append()` 规定必须按顺序出现的位置参数；`addBoolOption()` 声明只需判断有无的开关；`addOption()` 声明后面还要跟一个值的选项。`argList::addNote()` 则补充显示在 `-help` 中的用途说明。\n\n因此，注册语句的先后位置具有实际作用：若先解析、后注册，解析器遇到自定义选项时还不知道它是否合法。下面代码把这些声明放在构造 `argList args` 之前，正是为了解决这个问题。'),
        ('原例的 `-dict` **只演示路径解析**，并不读取该字典。看到 `Would read dict from ...` 不能说明文件被加载。要实现真正的覆盖机制，还要构造相应的 `IOobject` 或输入流，并明确命令行与字典的优先级。',
         '第一条命令用于查看接口，后两条用于比较带值选项与开关如何改变本次输入。`someSwitch` 后面不用再写 `true`；`someInt` 后面则必须提供能读成整数的值。位置参数的顺序也不能与带名称的选项混为一谈。\n\n原例的 `-dict` **只演示路径解析**，并不读取该字典。因此，日志中的 `Would read dict from ...` 只能证明程序得到了路径字符串，不能证明文件内容已参与计算。若要实现真正的字典覆盖，还要使用上一课介绍的 `IOobject` 或输入流，并明确命令行与字典的优先级。'),
        ('分别省略第二个位置参数、把浮点数改为文字、传入未知选项，观察退出状态和帮助文本。一个工具应在开始修改结果之前拒绝无效参数。参数名区分大小写，带空格的路径应在 shell 中加引号。',
         '分别省略第二个位置参数、把浮点数改为文字、传入未知选项，每次只改变一种输入，并记录首条诊断。这样可以区分“缺少必需信息”“类型不匹配”和“选项未注册”三类问题，而不是把它们都归为程序无法运行。\n\n检查这些失败路径的目的，是让无效输入在修改结果文件之前被拒绝。参数名区分大小写，带空格的路径应在 shell 中加引号；如果参数在进入程序前就被 shell 错误拆分，应先修正调用命令。'),
    ],
    'package': '主程序为 `OFtutorial2.C`。先参考 `testCase/Allrun` 中的调用，再在 `testCase` 内逐条尝试本页命令。`-dict system/customDict` 是接口演示，不要求据此声称包内字典已经被读取。',
    'evidence': '为新增的 `-scale` 保留一次默认值运行、一次显式赋值运行及一次非法输入运行。分别写出输入、预期乘积和实际输出，并附更新后的 `-help`；这样可以同时检查接口说明与程序行为是否一致。',
},
3: {
    'prerequisite': '已完成编程 01，理解单元、面和边界块的基本含义',
    'intro': '读入一个数值参数后，程序还需要知道这个数属于哪个单元或哪个面。本课因此转向网格的数据结构：先确定点、面和单元怎样连接，再读取中心坐标与面积。[下一课的场操作](/read/?slug=programming-04)正是把数值存放在这些网格位置上；本课若能分清编号，后面就更容易定位场访问越界或通量符号错误。',
    'summary': '沿着点、面、单元和 patch 的连接关系读取网格，解释编号范围、面积向量方向及程序输出。',
    'topics': ['meshing'],
    'edits': [
        ('OpenFOAM 多面体网格由连接关系和几何量共同描述。`points` 存坐标，`faces` 存组成面的点编号，`owner/neighbour` 把面连接到单元，`boundary` 则把连续的一段边界面归入 patch。有限体积离散需要的不只是“这个面在哪里”，还包括“它连接哪两个控制体”。',
         '可以从一个内部面开始理解网格，而不必一开始就遍历全部数据。先在 `faces` 中查到组成这个面的点编号，再去 `points` 取出坐标；随后通过 `owner/neighbour` 确定它连接的两个单元。前两步给出面的几何形状，后一步给出流量会从哪个单元流向哪个单元。\n\nOpenFOAM 用这些连接关系与几何量共同描述多面体网格。`boundary` 进一步把连续的一段边界面归入 patch。有限体积方法要对每个单元计算各面的通量，所以既需要面的面积和方向，也需要它与单元的连接关系。'),
        ('`patchi` 是边界块编号，`localFacei` 是该边界块内的面编号，全局面编号为 `patch.start()+localFacei`。patch 邻接单元由 `faceCells()` 获取。`findPatchID(name)` 在找不到名称时返回负值，必须先检查再索引。',
         '`patchi` 选择哪个边界块，`localFacei` 选择这个边界块内的哪个面，而 `patch.start()+localFacei` 才是完整面列表中的编号。三者都是整数，却不能互换。例如，某个 patch 从全局面 100 开始，它的局部第 0 个面对应全局面 100，而不是全局面 0。这个数字只是编号示例，不是下载网格的固定设置。\n\n如果接下来要找该面旁边的单元，使用的是 `faceCells()`。`findPatchID(name)` 找不到名称时会返回负值，必须先检查再索引；否则“拼错边界名”可能表现为后面的数组访问错误，掩盖真正原因。'),
        ('运行 `blockMesh` 和 `checkMesh`，记录单元、内部面和边界面的数量。随后选择一个内部面，对照 `faces` 中的顶点编号、`points` 坐标以及程序打印的面中心。最后确认 owner、neighbour 中的单元确实位于该面的两侧。这个小实验比只看彩色网格更能揭示数据结构。',
         '运行 `blockMesh` 和 `checkMesh` 后，先记录单元数、内部面数与边界面数，再阅读程序打印的编号。单元编号应落在单元列表范围内，内部面的 owner 和 neighbour 应各自指向有效单元；边界面只连接计算域内的一侧，不能照内部面的方式索引 neighbour 列表。\n\n随后选择一个内部面，对照 `faces` 的顶点编号、`points` 的坐标和程序打印的面中心，在可视化中确认相邻单元确实位于该面两侧。这样，日志中的整数就有了明确的几何含义。图像用于确认位置，数量和编号用于检查连接关系，两者应能相互对应。'),
    ],
    'package': '对照 `OFtutorial3.C` 与 `testCase/system/blockMeshDict`。运行后生成的 `testCase/constant/polyMesh` 不在下载包内，需要由 `blockMesh` 建立。先保留默认网格完成编号检查，再改变分块数量，避免把旧网格编号误套到新网格。',
    'evidence': '提交所选内部面的点编号、owner/neighbour 编号和可视化位置，再附各 patch 的面积统计。说明面积的标量求和与面积向量求和含义不同；后者用于检查封闭边界的方向平衡，不能解释成边界面积为零。',
},
4: {
    'prerequisite': '已完成编程 03，了解标量、向量和基本量纲运算',
    'intro': '[网格课程](/read/?slug=programming-03)确定了单元和面的位置，本课给这些位置赋予数值，形成压力场和向量场。先用已知解析函数生成数据，再调用离散梯度，可以把“场怎样存储”和“算子怎样作用”分开观察。这里暂不求解流体方程；等理解了这些场操作，再在[编程 10](/read/?slug=programming-10)中组装真正的待求方程。',
    'summary': '在网格上读取和构造场，结合量纲与解析赋值解释梯度、时间输出以及教学向量场的物理限制。',
    'edits': [
        ('`volScalarField` 在单元中心保存标量，并携带网格引用、量纲和各 patch 的边界条件；`volVectorField` 保存三分量向量。它们不等于普通的 `List<scalar>`。本例读取 `p` 和 `U`，用解析表达式重设 `p`，再将其梯度转换成一个演示用向量场。',
         '`volScalarField` 不仅保存每个单元中心的一个数，还记录它属于哪张网格、具有何种量纲，以及各个 patch 如何处理边界值。`volVectorField` 的结构类似，只是每个位置保存三分量向量。普通 `List<scalar>` 没有这些额外关系，所以不能直接代替有限体积场。\n\n本例先读取 `p` 和 `U`，再按解析表达式重新给 `p` 赋值，最后计算梯度并构造 `U`。因此，输入文件主要提供字段类型、量纲和边界结构，而程序中的赋值表达式决定了本例输出的内部场分布。阅读结果时需要沿着这条赋值顺序追踪。'),
        ('`fvc` 算子直接从已有场计算新场，`fvm` 算子构造包含待求变量的矩阵。本例没有 `solve()`，因此它是场操作程序，不是流动求解器。',
         '`fvc` 算子直接从已有场计算新场。例如，给定各单元的 `p` 后，`fvc::grad(p)` 利用网格和离散格式得到梯度数值。`fvm` 算子则把未知场的系数放进矩阵，之后还需要求解才能得到未知值。\n\n这一差别决定了怎样理解输出：本例已经用解析函数指定 `p`，并没有通过压力方程求出它；源码中也没有 `solve()`。所以图中的变化说明赋值和离散求导在工作，不能据此声称模拟了一个真实的压力驱动流动。'),
        ('在 ParaView 中，用等值线观察 `p`，再用 Glyph 显示 `U`。检查正弦符号变化时，箭头是否反向。读取量纲、色标和时间值后再解释图像，避免把正负色块误认为压力单位已完成转换。',
         '在 ParaView 中先选择一个明确的输出时间，用等值线观察 `p`，再用 Glyph 显示 `U`。不要只比较两幅颜色图：先检查色标是否相同，再看压力变化较快的区域是否对应较大的梯度。正弦因子换符号时，同一位置的梯度方向也应相应改变。\n\n如果动画中缺少某个时间点，应先检查 `writeInterval`，因为程序推进一次不代表每次都写盘。若要与压力测量值比较，还必须先处理运动压力与实际压力的关系；切换色标本身不会改变量纲。'),
    ],
    'package': '重点阅读 `OFtutorial4.C`、`testCase/0/p`、`testCase/0/U` 和 `testCase/system/controlDict`。算例脚本生成网格后执行场赋值程序；生成的时间目录包含教学构造场，初始 `p` 的数值不能当作整个时间序列中保持不变的输入。',
    'evidence': '选择远离参考点和边界的几个位置，记录解析梯度与离散梯度的比较，并说明排除这些区域的原因。时间步减半的结果要在同一物理时刻比较；本例的压力是解析赋值，应把时间采样差异与空间梯度误差分别讨论。',
},
5: {
    'prerequisite': '已完成编程 04，能运行 decomposePar 和基本 MPI 命令',
    'intro': '上一课的解析场在一张完整网格上计算。将网格分成多个子域后，同一段代码只会看到当前进程拥有的数据；原来正确的最大值、平均值和边界读取因此可能改变含义。本课保留相同的场构造思路，重点检查哪些数据需要跨进程汇总，以及怎样比较[串行场操作](/read/?slug=programming-04)与并行结果。',
    'summary': '把串行场操作扩展到多个子域，解释局部统计、全局规约、processor 边界更新及结果一致性。',
    'edits': [
        ('MPI 并行下，每个进程持有自己子域的 `mesh`、`p` 和 `U`。`mesh.V().size()` 是当前子域的单元数，不是整个算例的单元数。串行代码中看似合理的 `max`、求和、文件写入，迁移到并行时必须检查其作用范围。',
         'MPI 并行运行时，每个进程执行同一个程序，但读取的是自己的子域网格和字段。因此，`mesh.V().size()` 只给出当前子域的单元数。若四个子域分别包含不同数量的单元，任何一个进程打印的这个数都不能直接作为全网格单元数。\n\n需要全局量时，先在每个进程上计算局部结果，再用通信操作合并。下面的体积统计先对本进程的 `mesh.V()` 求和，再用 `reduce` 将各进程的局部体积相加；规约结束后的 `volume` 才具有全域体积的含义。'),
        ('体积是各子域局部体积之和；全局最大半径则使用最大值规约。不能用子域各自的最大半径归一化同一个解析场，否则结果会在分区界面出现人为不连续。',
         '选择哪种规约取决于物理量怎样组合：总体积用求和，全局最大半径用取最大值。这里的“全局”不是变量名自动带来的性质，而是通信后覆盖所有子域的数据范围。\n\n这对本课的归一化尤其重要。如果每个子域都除以自己的最大半径，同一个解析表达式就会在不同区域采用不同尺度。分区界面两侧即使位置很近，也可能得到不连续的场值；这种跳变来自程序的数据范围错误，不是新的物理现象。'),
        ('分别在串行和四分区运行相同的时间与网格，比较全局体积、最大最小值和同一组测点上的场值。浮点求和顺序变化会带来微小差别，因此用合理容差比较，不要求文本文件逐字节一致。若出现只沿分区边界分布的误差，应优先检查局部归一化和边界同步。',
         '先在串行算例记录全局体积、场的最大最小值和几个固定测点，再用相同网格与物理时间运行四分区算例。重构之后比较同一位置的数据，而不是拿某个 `processor` 目录中的局部范围与整个串行域比较。\n\n若全局体积不一致，先查统计是否漏做规约；若误差集中在分区界面，先查归一化尺度和边界同步；若只剩很小的末位差别，再考虑浮点求和顺序的影响。合理容差应结合数值精度和量值规模给出，不要求两个结果文件逐字节一致。'),
    ],
    'package': '下载包包含 `OFtutorial5.C`、`createFields.H` 和 `testCase/system/decomposeParDict`。原 `Allrun` 完成后会清理 `processor*`；若要检查每个子域或重构场，请按本页分步命令执行，并让 `mpirun -np` 与 `numberOfSubdomains` 一致。',
    'evidence': '对新增的平均压力，分别记录各子域的压力体积积分和体积，再给出规约后的比值。解释为什么单元数或体积不同的子域不能直接等权平均。保留串行与并行同一时刻的对照，说明采用的容差。',
},
6: {
    'prerequisite': '已完成编程 01 和 03，了解 C++ 类、成员函数和引用',
    'intro': '字典读取和网格操作逐渐增多后，把所有变量与操作都放在 `main` 中会使依赖关系难以检查。本课用一个只保存整数的类说明状态怎样被初始化、读取和修改，再扩展[编程 01 的 IOdictionary](/read/?slug=programming-01)。例子刻意保持简单，便于在编写边界条件类之前先理解构造函数、引用和继承。',
    'summary': '通过整数状态和派生字典两个小例子，解释类的初始化、只读接口、引用及多个源文件的编译关系。',
    'edits': [
        ('当一组操作共同维护同一个状态时，用类把状态和行为组织起来。`customClass` 用私有成员 `myInt_` 保存整数，构造函数将其初始化，`get()` 读取它，`set()` 修改它。外部代码通过公开接口访问，避免直接依赖内部实现。',
         '先把注意力放在一个问题上：这个整数由谁保存，哪些操作允许改变它？`customClass` 用私有成员 `myInt_` 保存状态，初始化时给出确定值，`get()` 负责读取，`set()` 负责修改。这样，调用端不需要知道成员在类内怎样存放，只需要使用公开接口。\n\n在更复杂的 OpenFOAM 模型中，状态可能是模型参数、选中单元列表或边界字段，但组织方式相同。先用整数观察“调用前后状态是否改变”，比同时引入一个完整物理模型更容易分清类本身的作用。'),
        ('`meshOpFunction(fvMesh& mesh)` 接收网格引用，不复制整个网格。若函数仅查询网格，接口更适合写成 `const fvMesh&`，让编译器约束误修改。本例通过读取单元数量更新 `myInt_`，所以它修改的是类自身的状态，并非网格。',
         '`meshOpFunction(fvMesh& mesh)` 中的 `&` 表示接收已有网格的引用，不复制整个网格。若这个函数只查询网格，把参数写成 `const fvMesh&` 可以进一步限制函数修改网格。这里的 `const` 约束的是传入的网格，与类自身能否更新成员不是同一件事。\n\n本例读取网格单元数量，并把该数写入 `myInt_`。因此调用前后，类保存的整数发生了变化，网格却没有被修改。跟踪这两个对象各自的状态，有助于理解后面共享库函数为什么会同时出现只读参数和输出参数。'),
        ('运行后检查默认值为 0，设置后为 10，网格操作后为单元数。再确认派生字典仍可读取 `nu`，这同时验证新增功能和继承功能。',
         '运行时按调用顺序记录三次整数输出：初始化后为 0，调用设置操作后为 10，执行网格操作后变为单元数。第三个值应与当前网格一致；更改网格划分后，它可能改变，这说明程序真正查询了网格，而不是固定输出某个数字。\n\n再检查派生字典的输出。新增函数列出词元，并不代替原有的按键读取；仍能读取 `nu`，才说明继承的字典功能保留了下来。将新增行为与原有行为分开检查，是扩展基类时应保持的习惯。'),
    ],
    'package': '依次查看 `OFtutorial6.C` 的调用位置、`customClass.H/.C` 的声明与实现，以及 `derivedClass.H/.C` 的字典扩展。它们属于同一个程序，`Make/files` 必须包含需要编译的各个 `.C`，不能只编译主文件。',
    'evidence': '给出 `reset()` 调用前后的整数值，并说明把网格参数改成 `const fvMesh&` 后编译是否通过。报告中明确区分“修改类保存的状态”和“修改传入网格”，再附派生字典仍能读取原条目的结果。',
},
7: {
    'prerequisite': '已完成编程 04 和 06，理解函数参数、类接口与引用',
    'intro': '[上一课](/read/?slug=programming-06)把相关操作放进类，本课进一步把可复用运算编译为共享库。计算内容仍与[场操作课程](/read/?slug=programming-04)相联系，这样可以把“程序结构改变”与“数学表达式改变”分开。重点是确认谁创建场、谁修改场，以及库在编译、链接和运行三个阶段分别怎样被找到。',
    'summary': '将已有场运算拆成共享库，沿参数与对象注册表追踪数据依赖，并用相同计算检查重构前后的结果。',
    'edits': [
        ('`mesh` 是只读引用，`r` 和 `U` 是输出引用。`computeR` 写入各单元到参考点的距离，并返回全局最大距离。函数接口清楚表达数据流，调用者就不必阅读整个实现才能知道哪个场会被改动。',
         '从函数声明就能先判断数据流：`mesh` 是只读引用，函数用它查询几何；`r` 和 `U` 是可以被修改的引用，计算结果通过它们返回给调用端。`computeR` 还返回一个 `scalar`，表示全局最大距离。这个返回值与写入 `r` 的逐单元距离是两类输出，不应混淆。\n\n阅读主程序时，可以先标出“创建 `r`—调用 `computeR`—使用最大距离”这几个位置。这样无需同时逐行阅读所有源码，也能知道某个场在何时具有了有效数据。随后再进入库实现，检查计算细节。'),
        ('`mesh.lookupObject<volScalarField>(pName)` 从网格关联的对象注册表查找已经存在的场。它不会因为磁盘上有 `0/p` 就自动创建压力场。调用前必须构造并注册正确名称与类型的对象。',
         '`mesh.lookupObject<volScalarField>(pName)` 查询的是程序运行时已经创建、并登记在网格对象注册表中的场。磁盘上的 `0/p` 只是文件；主程序读入并构造 `volScalarField p` 之后，库才可能按名称查到对应对象。\n\n所以，遇到“找不到对象”时应分两步检查：主程序有没有创建该场，以及注册名称和类型是否与查询一致。仅在目录中补放一个同名文件，并不能自动补上缺少的 C++ 构造过程。'),
        ('运行结果应与同样表达式的单文件程序一致。这个比较验证的是代码拆分没有改变计算，而不是验证演示向量场满足流体方程。',
         '确认共享库加载成功后，再比较拆分前后的计算。保持网格、参考点、字段和输出时间一致，核对距离场的最大值及几个单元上的向量值。若只有库版本的结果不同，应先检查函数传参、对象名称及计算调用顺序。\n\n这个对照回答的是“把代码移入库后，原来的运算是否保持一致”。因为计算仍是教学场表达式，即使结果完全一致，也不能据此证明该向量场满足流体运动方程。'),
    ],
    'package': '`customLibrary/Make/files` 生成共享库，教程根目录的 `Make/files` 生成调用它的应用。包内 `Allwmake` 按依赖顺序构建；单独重新编译应用不能补救尚未生成的库。测试入口仍是 `testCase/Allrun`。',
    'evidence': '给出新增平均压力函数的声明、实现和两个应用的调用位置，再记录相同输入下的输出。若设计为通用函数，应说明它是否需要并行规约、如何取得体积权重，以及是否隐含依赖某个注册字段名。',
},
8: {
    'prerequisite': '已完成编程 03、06 和 07，能检查 0/U 的边界设置',
    'intro': '在字典中写 `uniform` 可以指定常量入口，但入口速度若需要按空间位置变化，就要说明每个边界面如何计算数值。本课把[网格几何访问](/read/?slug=programming-03)、[类继承](/read/?slug=programming-06)与[共享库](/read/?slug=programming-07)结合起来，实现一个可由 `0/U` 选择的入口边界。先验证入口本身，再讨论它对管内流动的影响。',
    'summary': '根据入口面的位置构造速度剖面，解释边界类的选择、更新和写出，并检查方向、分布与积分流量。',
    'edits': [
        ('`fixedValueFvPatchVectorField` 表示指定每个边界面的速度值，不要求所有面取同一个向量。本例根据圆管入口面中心到轴线中心的距离构造剖面，并沿面法向的反方向施加入流。',
         '`fixedValueFvPatchVectorField` 中的“固定值”指边界数值由给定条件决定，并不要求所有边界面取相同向量。常见的 `uniform` 只是其中一种空间分布。本例读取每个入口面的中心位置，计算它到管轴中心的距离，再按该距离赋予不同的速度大小。\n\n速度方向也需要单独确定。边界面的面积向量通常指向计算域外，所以本例沿其反方向施加入流。先检查法向和流入方向，再检查剖面数值，可以避免把符号错误误判为入口模型不合理。'),
        ('头文件的 `TypeName("prescribedPipeInlet")` 给出字典使用的名称；`.C` 中的 `makePatchTypeField` 注册构造方法；`controlDict` 的 `libs ("libprescribedPipeInlet.so");` 触发共享库加载。三者缺少任何一个，都不能仅靠在 `0/U` 中写 `type` 来启用边界。',
         '从字典到 C++ 对象需要经过三个环节。首先，`controlDict` 的 `libs ("libprescribedPipeInlet.so");` 使程序加载共享库；库加载后，`.C` 中的 `makePatchTypeField` 注册该边界的构造方法；当程序读取 `0/U` 的 `type prescribedPipeInlet` 时，再按头文件中 `TypeName("prescribedPipeInlet")` 给出的名称选择它。\n\n因此，“找不到库”和“未知边界类型”应分开排查。前者先查编译产物和搜索路径；后者还要核对库是否加载、类型名是否一致，以及注册代码是否参与了编译。'),
        ('建议先画入口剖面，再运行管流。`yPlus` 是壁面分辨率相关诊断，不能单独证明自定义入口正确。至少核对速度方向、壁面附近趋势和截面积分流量。',
         '结果检查可以按由局部到整体的顺序进行：先只显示入口 patch，确认速度指向域内；再沿入口直径采样，检查靠壁区域与核心区域怎样衔接；最后按各面的面积对法向速度积分，计算整个入口的流量。\n\n若两种剖面的 `flowSpeed` 相同而积分流量不同，这不一定是错误，因为它们在截面上的分布不同，`flowSpeed` 也不是自动归一化后的平均速度。完成这些入口检查后，再查看管内发展和 `yPlus`。本次短运行只检查接口和流程，不能用 20 次迭代的管内云图认定流动已经充分收敛。'),
    ],
    'package': '共享库源码是 `prescribedPipeInletFvPatchVectorField.H/.C`。初始字段模板放在 `testCase/0.org`，运行脚本会据此准备 `0`；重复运行前若只修改生成的 `0/U`，修改可能被模板覆盖。应对照 `0.org/U`、`controlDict/libs` 和 `Allrun` 一起检查。',
    'evidence': '保存两种入口剖面的径向曲线与离散积分流量，注明面积、法向及参数。若实现给定流量归一化，再报告归一化前后流量误差；并行运行时必须说明积分是在全域完成，而不是只统计一个子域。',
},
9: {
    'prerequisite': '已完成编程 05 和 07，理解面通量及 functionObject 字典位置',
    'intro': '上一课给入口施加速度，本课回答怎样在计算过程中检查某个截面实际通过了多少流体。直接修改每个求解器会重复代码，因此这里使用函数对象挂接监测功能。它继续使用[共享库与注册表](/read/?slug=programming-07)读取已有场，并用[并行规约](/read/?slug=programming-05)合并统计；真正需要先确定的是截面位置和通量方向。',
    'summary': '将截面流量监测写成函数对象，沿面集合、速度插值、求和与日志输出解释数据流和适用限制。',
    'edits': [
        ('函数对象由求解器的运行时控制系统调用，可以在不改主求解循环的情况下记录流量、力或统计量。本例 `pipeCalc` 继承 `fvMeshFunctionObject` 和 `logFiles`：前者提供网格上下文，后者管理日志文件。',
         '函数对象不是一个单独推进流场的求解器。它由已有求解器在指定时刻调用，读取当时的网格和字段，再计算需要的统计量。这样，同一段监测代码可以用于不同算例，而不必分别改写它们的主求解循环。\n\n本例 `pipeCalc` 继承 `fvMeshFunctionObject` 和 `logFiles`：前者使监测代码能够访问相应网格，后者管理输出文件。阅读源码时，可以先沿“读取截面名称—查找字段—积分—写出”追踪，再查看各个基类的实现。'),
        ('这里得到体积流量，量纲为 $L^3T^{-1}$。可压缩质量流量需要密度加权，不能只更改输出文件表头。若求解器已有守恒修正后的 `phi`，使用该通量积分通常更适合检查离散质量守恒；由 `U` 再插值得到的通量不一定与求解器使用的 `phi` 完全相同。',
         '代码先把单元中心速度插值到面，再与有方向的面面积向量点乘，最后把截面上各面的贡献相加。因而面积更大的面贡献通常也更大，不能把面速度的简单平均当作流量。这里得到体积流量，量纲为 $L^3T^{-1}$；可压缩质量流量还需要密度加权，不能只更改输出文件表头。\n\n若求解器已有守恒修正后的 `phi`，用它做截面积分通常更适合检查离散质量守恒。由 `U` 重新插值得到的是另一种通量计算路径，两者在未充分收敛或通量修正不一致时可能有差异。比较结果前，必须先说明所积分的究竟是哪个量。'),
        ('只有主进程写合并后的时间序列，其他进程参与积分规约。输出头应记录 zone 名称、方向约定和单位。重启计算时应检查输出时间是否重复，以及下游脚本是追加读取还是覆盖读取。',
         '输出文件中的一行应能回答“哪个时刻、哪个截面、沿哪个正方向、流量是多少”。方向约定很关键：同一个物理流动，截面法向反转后，流量符号也会反转；负值本身并不能说明出现了反向流动。\n\n并行时，其他进程仍需参与积分规约，只由主进程写合并后的时间序列。重启计算后，再检查是否出现重复时间段，以及绘图脚本怎样处理这些记录。当前教学实现对跨分区截面存在前文说明的限制，不能因为加入了 `reduce` 就视为任意 faceZone 都已支持并行。'),
    ],
    'package': '先查看 `pipeCalc.H/.C`，再对照 `testCase/system/topoSetDict` 如何建立所需 zone，以及 `controlDict/functions` 如何调用对象。运行脚本应先生成 zone，再开始带监测的求解；缺失 zone 不能靠改变输出频率解决。',
    'evidence': '将同一截面上的自定义输出、标准函数对象输出与均匀流动的面积乘速度对照，写清通量来源和法向约定。若数值不一致，先区分方向、插值和未收敛误差，再讨论程序问题；保留 zone 缺失时的诊断。',
},
10: {
    'prerequisite': '已完成编程 04 和 07，理解对流、扩散与场边界条件',
    'intro': '[编程 04](/read/?slug=programming-04)直接给定场值并计算导数，本课则把标量作为未知量，通过方程求出它。速度场已经给定，因此可以暂时避开压力速度耦合，集中理解面通量、矩阵组装和字典配置怎样共同决定结果。阅读顺序建议从方程开始，再对应源码，最后检查结果文件中的字段名。',
    'summary': '在给定速度场中求解稳态标量输运，说明方程、离散字典和线性求解器的分工，并解释 result 输出。',
    'edits': [
        ('有限体积对流项使用面通量 $\\phi_f$，而不是直接把单元速度传给 `fvm::div`。`fvm` 将未知 `beta` 的系数组装进矩阵，边界条件已经包含在场对象中，参与边界系数和源项的处理。',
         '有限体积方法先统计穿过单元各面的输运，所以对流项接收面通量 $\\phi_f$，而不是直接接收单元中心速度。上面先对 `U` 做面插值，再与面面积向量点乘，正是把已知速度转换为方程需要的通量。\n\n此时 `beta` 仍是待求变量。`fvm::div` 和 `fvm::laplacian` 把相邻单元之间的关系写成矩阵系数，`solve` 再解这个代数系统。边界条件已经包含在 `beta` 场对象中，会参与边界系数和源项的处理；不能只检查这一行方程，而忽略 `0/beta`。'),
        ('`0/beta` 给出左边界为 1、下边界为 0、右和上边界零梯度、前后 `empty`。`fvSchemes` 指定 `div(phi,beta)`、`laplacian(gamma,beta)` 和 `interpolate(U)` 的离散格式。`fvSolution` 决定 `beta` 方程的线性求解器和停止条件。',
         '这三个文件分别决定边界约束、离散方法和代数求解方式。`0/beta` 把左边界设为 1、下边界设为 0、右和上边界设为零梯度、前后设为 `empty`；它规定哪些边界向域内提供什么标量条件。\n\n`fvSchemes` 决定 `div(phi,beta)`、`laplacian(gamma,beta)` 和 `interpolate(U)` 怎样离散。`fvSolution` 则控制生成矩阵之后如何求解以及何时停止。因此，收紧线性求解容差可以减小代数求解误差，却不会自动消除粗网格或离散格式引入的误差。'),
        ('程序只求解一次稳态线性方程，没有时间循环。它将已求出的 `beta` 复制成名为 `result` 的场并显式 `write()`，因此初始 `beta` 保留，结果写入当前时间目录。看到结果不在 `1/` 或 `100/` 不意味着计算没执行。',
         '程序只求解一次稳态线性方程，没有向下一个物理时间推进的循环。求解后，它将 `beta` 的结果复制成名为 `result` 的场并显式 `write()`，因此初始 `beta` 文件保留，而新结果写入当前时间目录。看到结果不在 `1/` 或 `100/`，并不意味着求解没有执行。\n\n在 ParaView 中应明确选择 `result`，再查看与左右、上下边界对应的空间分布。如果误选初始 `beta`，即使求解日志正常，也可能只看到初始设置。先核对字段名、时间目录和边界位置，再比较数值范围，能避免把文件选择问题误判为方程求解失败。'),
    ],
    'package': '本包包含 `OFtutorial10.C`、`testCase/0/beta`、`0/U` 及配套 `fvSchemes`、`fvSolution`。解压后的主目录是 `OFtutorial10_transportEquation`；运行后重点检查当前时间目录内新增的 `result`。压缩包不附带本次生成的解场，正文中的实测图仅用于对照。',
    'evidence': '记录两种格式下 `result` 的最小值、最大值和同一截面的数据，并保持比较时间、边界与网格一致。说明误差来自线性求解、空间离散还是更换物理参数；不能用更低残差替代网格与格式比较。',
},
11: {
    'prerequisite': '已完成编程 03，能够解释 points、faces、owner/neighbour 与 patch',
    'intro': '[编程 03](/read/?slug=programming-03)读取已有网格，本课反过来用点坐标和连接关系构造网格。目标是理解网格数据怎样建立，以及为什么“成功写出”与“适合计算”是不同判断。下载例只含 5 个混合单元，便于逐个观察；它仍有已记录的质量检查失败，应作为拓扑教学例研究。',
    'summary': '用少量顶点和标准单元形状生成混合网格，逐项解释连接、patch 与质量诊断，并保留已知失败说明。',
    'topics': ['meshing'],
    'edits': [
        ('本例显式创建 17 个顶点，组合六面体、棱柱、棱锥和四面体，并为部分外表面命名。`cellModeller::lookup()` 获取标准单元模型，`cellShape` 将模型和有次序的顶点列表关联，最后构造 `polyMesh`。',
         '构造时可以把几何和连接分开理解：先用 17 个顶点的坐标确定可用位置，再说明哪些顶点组成一个单元，以及它们按什么次序连接。本例组合六面体、棱柱、棱锥和四面体，并为部分外表面命名。\n\n`cellModeller::lookup()` 取得标准单元模型，`cellShape` 把模型要求的连接次序与具体点编号关联起来，最后交给 `polyMesh` 构造网格。因此，点坐标正确并不够，顶点编号次序也必须满足所选单元模型的约定。'),
        ('`faceListList` 保存每个 patch 的面，每个面又由点编号组成。`boundaryPatchNames`、`boundaryPatchTypes` 和 `boundaryPatchPhysicalTypes` 应与 patch 数量和次序一一对应。遗漏的外表面进入默认 patch，并不会自动获得合理的物理边界条件。',
         '单元建立后，还要识别哪些外表面属于同一个边界块。`faceListList` 的外层对应各个 patch，内层列出这个 patch 包含的面，而每个面再由点编号组成。与此同时，`boundaryPatchNames`、`boundaryPatchTypes` 和 `boundaryPatchPhysicalTypes` 必须采用相同的 patch 次序。\n\n可以选一个容易辨认的外表面，先核对它的点编号，再核对它属于哪个 patch。遗漏的外表面会进入默认 patch，但这种归类并不等于已经指定了合适的壁面、入口或出口条件。网格边界类型与将来字段的边界设置还需要配合检查。'),
        ('拓扑检查关注闭合、连接和重复面；几何检查关注体积、面方向、非正交性、扭曲等。程序可能成功写出文件，但 `checkMesh` 报告失败。此时应回到点连接和 patch 定义定位问题，不能以 ParaView 能打开为合格标准。',
         '先区分检查所回答的问题。拓扑检查关注单元是否闭合、连接是否一致以及是否有重复面；几何检查再考察体积、面方向、非正交性和扭曲等量。成功生成 `polyMesh` 说明构造过程完成，并不意味着这些检查都会通过。\n\n阅读 `checkMesh` 日志时，不要只看开头的单元数量或最后的进程退出状态，应逐项找到失败名称。ParaView 能显示一个网格，也只能说明可视化工具能够读取它，不能代替离散计算所需的质量检查。'),
        ('先用 Surface With Edges 显示各单元，再逐个提取 patch，检查名称、类型及面位置。随后输出每个 cell 的体积，确认所有预期单元体积为正。最后扰动一个顶点，观察几何质量指标如何变化，从而把“网格看起来歪了”转换成可计算的指标。',
         '先用 Surface With Edges 显示各单元，确认能把源码中的点和单元编号对应到图上；再逐个提取 patch，核对面的位置、名称与类型。随后读取单元体积和失败检查，理解为什么本例即使体积为正，仍可能出现 `underdeterminedCells`。不同指标检查的是不同条件，不能用某一项正常去抵消另一项失败。\n\n最后只在副本中扰动一个顶点，比较修改前后的诊断。每次只改变一个因素，并保留原始网格，才能把指标变化与这次几何修改建立对应关系。本课练习的产物应是诊断说明，而不是一个未经复查就投入流动计算的网格。'),
    ],
    'package': '完整点与连接数据在 `OFtutorial11.C` 中，`meshPoints.geo/.pdf` 可辅助观察。`testCase/Allrun` 会先清理并生成演示网格；请在独立副本运行。源码包对应的是仍有 1 项 `underdeterminedCells` 失败的教学网格，不是修复后的生产网格。',
    'evidence': '提交未修改网格的 `checkMesh` 完整结论，以及交换编号、移动顶点两次实验的差异。保留原例已存在的 1 项失败，明确哪些诊断由新增修改引入；不得把“程序完成”或“体积为正”写成全部网格质量通过。',
},
12: {
    'prerequisite': '已完成编程 05 和 07，理解动量方程、体积积分与源项概念',
    'intro': '并非所有作用都需要在网格中解析出详细几何。执行器盘模型把设备对流体的作用近似成一片区域内的动量源，本课用它说明怎样选单元、分配总源项并接入求解器。它延续[共享库](/read/?slug=programming-07)的编译方式，通过 v2512 的 `fvOptions` 接口作用于动量方程。先确认源区和方程调用，再解释速度变化。',
    'title': '编程 12｜fvOptions 自定义动量源与执行器盘模型',
    'summary': '通过 v2512 的 fvOptions 实现执行器盘动量源，解释单元选区、总量分配、方程调用及结果检查。',
    'edits': [
        ('仅把字典文件重命名不足以完成移植：基类、构造参数次序、虚函数签名和运行时选择表都必须一致。',
         '可以把移植分成“字典如何创建对象”和“求解器如何调用对象”两部分：运行时选择表与构造参数负责前者，基类提供的虚函数接口负责后者。只把 `fvModels` 文件改名为 `fvOptions`，不会自动改变 C++ 的调用约定。\n\n因此，应先确认库能够按字典创建，再确认动量方程确实调用了相应源项接口。编译成功只检查了源码之间的类型与符号关系，仍不能证明源项已经作用到指定的 `U` 方程。'),
        ('用位移直接点乘，可以避免原例在盘心处先计算单位径向向量造成零除。盘厚过小可能选不到任何单元；下载副本会拒绝无效几何与空选择，而不是静默地施加零源项。',
         '这两个距离分别回答“单元是否在盘的厚度范围内”和“单元是否在圆盘半径内”。只有同时满足条件的单元才属于源区。这里按单元中心选取，因此离散源区会随网格变化，并不精确等于连续几何中的圆盘体积。\n\n直接用位移做点乘，还能避免在盘心处先构造单位径向向量造成零除。若盘厚小于局部单元尺度，可能没有任何单元中心落入选区；下载副本会拒绝无效几何与空选择。这时应检查盘的位置、厚度和网格分辨率，而不是先调求解器容差。'),
        ('`eqn.source()` 是离散方程的体积积分源数组，不是单位体积力。正负号还与 `fvOptions` 如何出现在方程中有关。应从单元动量预算和速度变化验证阻力方向，不能只看变量名 `diskDir`。',
         '`eqn.source()` 保存离散方程的体积积分源数组，不能把它直接当作单位体积力。理解分配时，先看所有选中单元的源项之和是否恢复预期总量，再看每个单元因体积不同分到了多少。若把总力完整地加到每个单元上，网格越细总作用就越大，显然改变了原模型。\n\n正负号还取决于 `fvOptions` 在方程中的位置。应结合单元动量预算和施加源项前后的速度变化确认阻力方向，不能只看变量名 `diskDir`。对于不可压缩方程，还应说明使用的是相应的运动学形式，而不是把数组输出一律标成 N。'),
    ],
    'package': '本包的 `customActuationDiskSource.H/.C` 与模板实现已按 v2512 `fv::option` 整理，参数位于 `testCase/constant/fvOptions`。应整体使用该副本的源码与字典，不要把旧 `fvModel` 库和新字典混用。修改盘几何后按正文要求重新启动。',
    'evidence': '先记录选中单元数、选区体积和总源项，再改变盘厚与网格进行对照。若总量或方向发生异常，优先检查区域选择、分配权重与方程符号。20 次迭代记录只能支持启动和接口检查，不应写成已验证风机性能或尾流收敛。',
},
13: {
    'prerequisite': '已完成编程 04 和 10，理解时间步、初始场与二阶导数',
    'intro': '[稳态输运例](/read/?slug=programming-10)只求解一次代数系统，本课加入时间推进，并使用二阶时间导数描述扰动传播。这里特别需要把“初始场是什么”与“它一开始怎样变化”区分开。先理解标量方程和初值，再观察传播速度、振幅与边界反射，避免仅凭波形外观判断模型含义。',
    'summary': '在时间循环中求解标量波动方程，说明两类初值、离散配置，以及传播速度和边界反射的检查方法。',
    'edits': [
        ('`d2dt2` 是二阶时间导数算子，不代表其离散方案自动具有任意阶时间精度。实际格式从 `fvSchemes/d2dt2Schemes` 读取，求解器容差从 `fvSolution` 读取。',
         '每轮时间循环都要根据已有时间层构造当前的矩阵，求解新的 `h`，再按写出设置保存结果。这里 `d2dt2` 中的“二阶”指方程里对时间求了两次导数，不是对最终数值误差阶数的保证。实际离散格式从 `fvSchemes/d2dt2Schemes` 读取，矩阵求解容差从 `fvSolution` 读取。\n\n因此，看到时间目录不断增加，只能说明程序正在推进并输出。要知道传播是否准确，还需比较同一扰动到达测点的时间与幅值，检查它们随时间步和网格改变的情况。'),
        ('二阶时间方程需要初始幅值和初始变化率。`setFields` 只直接设置当前 `h` 的空间分布；历史时间层的初始化影响第一步采用的时间变化率。应明确检查所用离散格式的启动行为，不能从只有一个 `0/h` 文件就推断任意初始速度已被设定。',
         '同样的初始幅值可以对应不同的后续传播，因为扰动在起始时刻可能静止，也可能已经向某个方向变化。因此，二阶时间方程需要初始幅值和初始变化率两类信息。\n\n`setFields` 只直接修改当前 `h` 的空间分布；第一步采用的变化率还取决于历史时间层如何初始化以及离散格式如何启动。检查 `0/h` 能确认幅值设置，却不能据此推断任意初始速度已经指定。要改变初始变化率，必须明确处理相应的时间层或采用下面的扩展方程。'),
        ('观察脉冲传播时，先记录色标范围与时间，再测量波峰位置。将网格和时间步分别加密，比较到达同一测点的时间与峰值。不要对每帧自动缩放色标后再判断振幅是否守恒。',
         '结果分析先固定色标，并记录当前时间，再追踪波峰位置与固定测点的数值。峰值降低和峰值到达时间偏移是两种不同现象：前者与幅值误差相关，后者反映传播相位误差，不能只用一张云图概括。\n\n将时间步减半时保持网格不变，将网格加密时明确控制时间步，分别比较同一测点的到达时间与峰值。若每帧自动调整色标，即使实际幅值已经明显衰减，图像仍可能看起来同样鲜明。本次运行仅推进至 0.1，不代替这些误差检查。'),
    ],
    'package': '入口为 `ofTutorial13.C`，`createFields.H` 创建字段；`testCase/system/setFieldsDict` 与 `0/h` 共同决定本例的幅值初始化。脚本中的初值恢复与 `setFields` 操作可能覆盖手工修改，复现实验前应先核对 `Allrun` 的执行顺序。',
    'evidence': '对正弦模态给出理论周期、固定测点的数值周期和振幅变化，再分别比较时间步与网格加密结果。说明初始变化率如何处理，以及观测时段内是否已有边界反射；不要把线性标量波动例标注为两相自由面模拟。',
},
14: {
    'prerequisite': '已完成编程 10，理解连续性方程、动量方程和稀疏矩阵',
    'intro': '[编程 10](/read/?slug=programming-10)把速度当作已知输入，本课进一步考虑速度和压力都需要确定的情形。动量方程给出的速度还必须满足不可压缩连续性条件，因此需要压力修正。下面按对角系数、压力方程、速度与通量更新的联系阅读代码，同时对照标准求解器，区分教学化简与完整实现。',
    'summary': '从动量矩阵的对角系数出发解释压力修正、欠松弛和连续性检查，并分析教学实现与 simpleFoam 的差异。',
    'edits': [
        ('这里的 $A$ 是每个单元的对角系数场；`H()` 汇集非对角作用及源项，并不是完整稠密矩阵。`1/A` 因此是逐单元操作，不是在对整个稀疏矩阵求逆。',
         '可以先把每个单元的速度关系分成两部分：本单元未知速度的系数归入 $A$，其他单元的影响及源项归入 `H()` 所构造的量。这样，压力梯度变化会怎样修正本单元速度，就能用对角系数的倒数表示。\n\n这里的 $A$ 是每个单元的对角系数场，`H()` 也不是完整稠密矩阵。因此 `1/A` 是逐单元计算倒数，不是在求整个稀疏矩阵的逆。这个区别对于理解下面的 `rAU`、`HbyA` 及其插值非常重要。'),
        ('参考压力消除某些边界组合下的压力零空间，不等于增加一个物理压差。若模型的压力边界已确定参考，应确认额外参考处理是否必要。',
         '当边界条件只约束压力梯度时，给整个压力场加同一个常数可能不会改变速度。此时压力的绝对水平尚未确定，参考压力用于消除这种不唯一性，并不等于给入口与出口额外施加一个物理压差。\n\n读 `setReference` 时，应先检查边界是否已经确定了参考水平，再解释 `pRefCell` 与 `pRefValue` 的作用。否则可能把用于代数求解的参考处理误认为驱动流动的边界条件。'),
        ('较小的 $\\alpha$ 限制迭代更新幅度，可能提高鲁棒性，但也可能增加迭代次数。欠松弛不是物理时间推进；稳态求解器输出的 `Time` 在这里主要用于迭代计数。',
         '上式把本轮新求出的压力与上一轮压力组合起来。较小的 $\\alpha$ 表示每轮只接受较小幅度的更新，可能减轻耦合迭代的振荡，但通常也需要更多轮才能接近稳定结果。它并不会把错误的方程或边界条件自动变正确。\n\n这里的迭代目的是使稳态方程彼此一致，欠松弛不代表流体经历了一个更短的物理时间步。因此，日志中的 `Time` 主要用于迭代计数，不应直接解释为真实瞬态发展过程。'),
        ('从低 Reynolds 数平面通道开始，比较解析抛物线剖面、流量及压降。每轮记录残差和 $\\sum_f\\phi_f$ 的单元不平衡。速度看似稳定但连续性误差不降时，优先检查通量修正及边界处理。',
         '从低 Reynolds 数平面通道开始，在相同网格、物性与边界下比较解析抛物线剖面、流量及压降。每轮还应记录残差和 $\\sum_f\\phi_f$ 的单元不平衡。前者说明当前线性系统求解到什么程度，后者检查流入流出是否满足离散连续性；两者回答的问题不同。\n\n如果速度云图变化已经很小，但连续性误差没有下降，应优先检查压力通量修正和边界处理。本教学例存在前文列出的化简，本次也只运行了 20 次迭代；应把与标准 `simpleFoam` 的差异作为分析内容，而不是预先假定两者等价。'),
    ],
    'package': '查看 `OFtutorial14.C`、`createFields.H` 和 `testCase/system/fvSolution`。本例从 `fvSolution` 顶层读取 `alpha`、`pRefCell`、`pRefValue`，应使用包内配套字典。与标准 `simpleFoam` 比较时，在两个独立算例目录中保存各自配置与结果。',
    'evidence': '提交线性残差、离散连续性误差和同一截面速度三组结果，并区分内层线性求解与外层压力速度迭代。对标准 `simpleFoam` 的比较应列出方程和通量处理的差异，不以短运行云图相似代替一致性验证。',
},
15: {
    'prerequisite': '已完成编程 03、07 和 10，理解面插值与对流离散',
    'intro': '前面的求解器通过 `fvSchemes` 选择已有格式，本课进入格式内部，查看单元值怎样组合成面值。它复用[共享库加载](/read/?slug=programming-07)和[输运方程](/read/?slug=programming-10)的知识，只改变插值权重来观察结果。先算清一个面的权重，再比较完整输运算例，才能把过冲或扩散与离散选择联系起来。',
    'summary': '从一个面的插值权重理解线性与上风混合，实现可选择的格式，并比较过冲、数值扩散和误差。',
    'edits': [
        ('因此这里是 80% 线性与 20% 上风，不能把 0.2 解释为“80% 上风”。更重要的是，固定混合比例并不是基于局部解的通量限制器，不自动保证阶跃输运严格有界。',
         '把式子中的系数逐项对应即可看清：线性权重乘以 0.8，上风权重乘以 0.2，所以这里是 80% 线性与 20% 上风。可以先选 owner 到 neighbour 通量为正的一个均匀网格面，代入线性权重 0.5 与上风权重 1，手算混合权重为 0.6，再核对程序打印。\n\n通量反向时，上风侧随之改变，不能一直使用同一个 owner 权重。此外，固定混合比例没有根据局部解自动限制通量，因此它不是通用的有界格式证明。即使某一次算例没有过冲，也不能据此认定所有阶跃输运都严格有界。'),
        ('`tmp<surfaceScalarField>` 用于临时场管理，减少不必要的深复制。引用或取值后要注意临时对象是否仍有效。教学代码为打印权重额外创建了几个实际场，便于观察，但不是性能最优实现。',
         '`weights()` 需要返回一个面标量场，而这个场常常只在当前表达式计算期间使用。`tmp<surfaceScalarField>` 用于管理这种临时结果，减少不必要的深复制。理解它时，先确认结果由谁持有、引用何时被使用，再判断临时对象是否仍有效。\n\n教学代码为了打印和比较权重，额外创建了几个实际场。这有利于观察线性、上风和混合值之间的关系，但也带来额外存储。先检查计算关系正确，再考虑减少临时场，不宜在尚未理解生命周期时直接改成悬空引用。'),
        ('上风通常更耗散，中心插值在强对流阶跃附近可能振荡。记录最小值、最大值、积分总量和界面厚度，并同时固定时间步、网格与求解容差。与解析平移解比较时，应对齐物理时间和采样位置。',
         '对于阶跃输运，一条更平滑的曲线可能意味着数值振荡减小，也可能意味着数值扩散把原本较陡的过渡抹宽了。只看外观无法区分这两种情况，因此应同时记录最小值、最大值、积分总量和过渡区域厚度。\n\n比较不同混合比例时，先固定网格、时间步、初值和求解容差，只改变格式参数。再与解析平移解在相同物理时间、相同采样位置对照。若随后加密网格，应把新旧网格的误差变化也记录下来，避免把一次设置下的表现推广成格式的普遍结论。'),
    ],
    'package': '`OFtutorial15.H/.C` 编译成 `libofTutorial15.so`，并不生成名为 `ofTutorial15` 的求解器。实际算例由 `scalarTransportFoam` 加载该库，配套设置在 `testCase/system/fvSchemes` 与 `controlDict`。`refData` 是原参考曲线，应核对初值和采样时刻后使用。',
    'evidence': '给出一个具体面的手算权重与程序输出，再比较三种混合比例的极值、积分量和过渡厚度。每次修改源码参数后重新编译库；若只改字典中未被源码读取的名称，不能假定混合比例已经改变。',
},
16: {
    'prerequisite': '已完成编程 03 和 04，了解常微分方程的显式 Euler 积分',
    'intro': '前面的课程主要在固定网格上查看场，本课改为沿一个运动质点的位置读取速度，并逐步更新其坐标。流场已经存在，所以需要把“求解流场”和“在流场中积分轨迹”分成两个步骤。它使用[网格单元定位](/read/?slug=programming-03)与[字段访问](/read/?slug=programming-04)，重点检查步长、越界处理和轨迹文件的物理含义。',
    'summary': '在已有速度场中定位质点、推进坐标并输出轨迹，解释时间步、出界判断以及无质量粒子模型的限制。',
    'edits': [
        ('示意代码省略了合法性检查，下载源包含零速度和最大步数防护。`findCell()` 找不到单元时返回 -1，在读取 `U[celli]` 以前必须检查。原例采用单元中心速度和显式 Euler 更新，时间精度是一阶，空间速度也未在粒子位置插值。',
         '一次推进包含三个环节：先确定质点当前位于哪个单元，再读取该单元的速度，最后用速度乘时间步得到位移。`findCell()` 返回 -1 时，说明没有找到有效单元，必须在读取 `U[celli]` 之前处理这个情况；否则出界会演变成数组访问错误。\n\n示意代码省略了合法性检查，下载源包含零速度和最大步数防护。当前实现直接使用单元中心速度，并采用显式 Euler 更新，时间精度是一阶。质点在同一个单元内的不同位置会读到同一个速度，这也说明它尚未进行粒子位置处的空间插值。'),
        ('改进方向是引入小于 1 的步长系数、在粒子位置插值速度、采用更高阶积分，并根据当前单元面交点做局部追踪。OpenFOAM 的拉格朗日框架提供更完整的数据与并行处理机制，不能把教学循环扩展到大量粒子后仍期待良好效率。',
         '这时可以先做最小改动：把原步长乘以小于 1 的系数，观察轨迹和离域时间是否明显改变。若改变很大，说明原来的单步位移过粗；增加轨迹输出点只能让线条更密，不能代替更准确的积分。\n\n进一步改进包括在粒子位置插值速度、采用更高阶积分，以及计算与当前单元面的交点来处理跨面追踪。OpenFOAM 的拉格朗日框架还提供更完整的数据与并行处理机制；本课的循环主要用于解释基本过程，不宜直接推广为大量粒子的高效通用实现。'),
        ('程序扫描时间目录并读取最后一个时间的 `U`。最新目录存在不保证其中有完整的求解结果，应检查 `U` 可读且与当前网格一致。脚本先运行 `simpleFoam`，再执行追踪，把轨迹写为 `VTK/particle_path.vtk` 的一条 polyline。',
         '脚本先运行 `simpleFoam` 得到速度场，再执行追踪程序。追踪程序扫描时间目录并读取最后一个时间的 `U`，随后把轨迹写为 `VTK/particle_path.vtk` 的一条 polyline。这里生成的是连接一系列位置点的折线，不是新的体积流场。\n\n因此，应先检查读取的是哪个时间的 `U`、该字段是否完整、网格是否对应，再在 ParaView 中叠加显示流场和轨迹。对于本次只迭代 20 次的流动运行，轨迹反映的是那份短运行速度场，不能直接视为充分收敛稳态流动中的定量路径。'),
        ('输出的总行程时间由各步 $\\Delta t$ 累加。离域的最后一步可能越过边界，因此它是此粗积分的估计，不是精确的出口到达时间。定量停留时间应裁剪到边界交点并做步长收敛性检查。',
         '输出的总行程时间由各步 $\\Delta t$ 累加，不等于读取流场的那个目录时间。前者是本次轨迹积分累计的运动时间，后者用于选择作为输入的速度场。\n\n最后一步可能已经跨出边界，所以累计值仍是粗积分的估计，不是精确出口到达时间。若要报告停留时间，应把最后一段裁剪到边界交点，并通过缩小步长检查结果是否趋于稳定。'),
    ],
    'package': '入口为 `OFtutorial16.C`，`testCase/Allrun` 包含流场计算与随后追踪的顺序。下载包不含已生成的 `VTK/particle_path.vtk`，应运行后自行生成。若改变网格或初始位置，先确认新位置处于网格内，并核对程序实际读取的最新 `U`。',
    'evidence': '对三个步长系数记录起点、所用流场时间、累计行程时间和最后一段位置。使用均匀流动检验直线轨迹后，再比较非均匀流场；明确是否做了出口交点裁剪，以及速度场本身是否达到所需收敛程度。',
},
}

COMMON_PREREQUISITE = '能够运行一个基本算例，了解 C++ 变量、函数与引用；涉及类、模板或并行时先完成前置课程。'
COMMON_EVIDENCE = '提交时附环境版本、修改后的源码或字典、执行命令、关键日志和至少一项定量检查。出现错误时保留第一条编译或运行错误及上下文，末尾的 make error 通常只是上游失败的结果。'
OLD_ENV_COMMENT = '# 先加载本机 OpenCFD v2512 环境，确认不是 Foundation 9。'
NEW_ENV_COMMENT = '# 先加载本机 OpenCFD OpenFOAM v2512 开发环境。'

V2512_FOCUS = {
    7: [
        ('不要把 Foundation 的已编译 `.so` 复制到 OpenCFD v2512 中使用，应从源码重新编译。',
         '自定义 `.so` 应在当前 v2512 环境中从源码编译，避免沿用其他安装环境生成的二进制文件。'),
    ],
    8: [
        ('## v2512 迁移细节', '## 字段写出与库的运行检查'),
        ('本次实测发现原资料的 `writeEntry(os, "value", *this)` 不符合当前 OpenCFD 接口。下载包已改为 `writeEntry("value", os)` 并保留原始许可。构造与映射函数应与当前 `fvPatchField` 接口一致；库能编译后，还要验证字典构造、分区映射、重构和重新读取。',
         '在 v2512 中，本边界使用 `writeEntry("value", os)` 写出当前边界值。它的作用是使结果字段保留可重新读取的边界数据，而不只是把内部速度写入文件。下载包采用这一有效接口，并保留原始许可。\n\n构造与映射函数同样应符合当前 `fvPatchField` 接口。库能编译后，还要检查字典构造、分区映射、重构和重新读取；这些步骤分别涉及边界对象的创建、重新分配和保存，不能相互替代。'),
    ],
    12: [
        ('## 先区分 API 分支', '## v2512 中源项如何接入动量方程'),
        ('提供的原始文件虽在总 README 中标注 v2512，实际仍使用 Foundation 的 `fvModel.H`、`addSupFields()` 与 `constant/fvModels`。OpenCFD v2512 的本例应使用 `fv::option`、`fieldNames_`、`resetApplied()`、带字段索引的 `addSup()`，并放入 `constant/fvOptions`。本课程下载包包含独立迁移副本，原材料不被覆盖。',
         '本课直接使用 OpenCFD v2512 的 `fvOptions` 接口。自定义类型继承 `fv::option`，由 `constant/fvOptions` 提供配置；`fieldNames_` 登记作用字段，`resetApplied()` 初始化应用标志，带字段索引的 `addSup()` 接收需要增加源项的方程。下载包提供与这些接口配套的源码和字典。\n\n这里有两个需要对应的名称：字典中的 `type` 选择源项模型，而 `Uname` 指定模型要作用的速度场。前者决定创建哪个 C++ 对象，后者决定它登记处理哪个字段。'),
        ('可以把移植分成“字典如何创建对象”和“求解器如何调用对象”两部分：运行时选择表与构造参数负责前者，基类提供的虚函数接口负责后者。只把 `fvModels` 文件改名为 `fvOptions`，不会自动改变 C++ 的调用约定。',
         '先把接口分成“字典如何创建对象”和“求解器如何调用对象”两部分：运行时选择表与构造参数负责前者，基类提供的虚函数接口负责后者。仅在目录中放入 `fvOptions` 字典还不够，求解器必须创建并调用相应的选项对象，源项才会参与方程。'),
        ('## 迁移后的字典组织', '## 源项字典与参数设置'),
        ('原资料截图仅说明预期的流场变化，不能作为迁移后定量正确性的证据。',
         '原资料截图仅说明预期的流场变化，不能作为当前实现定量正确性的证据。'),
        ('修改几何后需要重新建立选择区域；旧版 `read()` 只更新部分成员，不会完整重建选择集合。因此本课要求改字典后重新启动算例，动态改盘位置需另行实现。',
         '修改几何后需要重新建立选择区域。本教学实现的运行时重新读取机制没有完整重建选区，因此本课要求修改盘几何后重新启动算例。若需要在运行中移动盘的位置，还需实现选区更新，不能只改变字典数值。'),
    ],
}


def replace_once(body, old, new, slug):
    if new in body:
        return body
    if body.count(old) != 1:
        raise ValueError(f'{slug}: expected exactly one prose anchor: {old[:70]!r}')
    return body.replace(old, new, 1)


def protected_content(body):
    """Keep code fences and mathematical expressions byte-identical."""
    # The only permitted code-fence edit is the environment comment; commands do not change.
    code = re.findall(r'```[^\n]*\n.*?```', body.replace(OLD_ENV_COMMENT, NEW_ENV_COMMENT), flags=re.S)
    outside_code = re.sub(r'```[^\n]*\n.*?```', '', body, flags=re.S)
    tex = re.findall(r'\$\$.*?\$\$|(?<!\$)\$(?!\$)[^\n$]+\$(?!\$)', outside_code, flags=re.S)
    return code, tex


def download_for(item, index, revision, manifest):
    metadata = item['metadata']
    url = metadata['download']
    filename = Path(url).name
    expected_root = metadata['source'].split('/')[-1]
    assert expected_root.startswith(f'OFtutorial{index:02d}_')
    assert filename == expected_root + '-v2512.zip'
    assert url == '/downloads/programming/' + filename
    file_path = DOWNLOADS / filename
    data = file_path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    entry = manifest[url]
    assert entry['tutorial'] == expected_root
    assert entry['size'] == len(data) and entry['sha256'] == sha
    with zipfile.ZipFile(file_path) as package:
        assert package.testzip() is None
        names = package.namelist()
        assert names and all(n.startswith(expected_root + '/') for n in names)
        assert all('..' not in Path(n).parts for n in names)
        required = ['Allwmake', 'Make/files', 'Make/options', 'testCase/Allrun',
                    'testCase/system/controlDict', 'LICENSE', 'README.md', 'FOAMLAB-README.md']
        for name in required:
            assert expected_root + '/' + name in names, (filename, name)
        readme = package.read(expected_root + '/FOAMLAB-README.md').decode('utf-8')
        assert expected_root in readme and f'/read/?slug=programming-{index:02d}' in readme
        assert 'GNU GENERAL PUBLIC LICENSE' in package.read(expected_root + '/LICENSE').decode('utf-8')
        files = package.read(expected_root + '/Make/files').decode('utf-8')
        assert re.search(r'^(EXE|LIB)\s*=', files, flags=re.M)
        for line in files.splitlines():
            source = line.strip()
            if source.endswith('.C') and not source.startswith(('#', '//')):
                assert expected_root + '/' + source in names, (filename, source)
        forbidden = [n for n in names if re.search(r'/(processor\d+|postProcessing|VTK|linux[^/]*)/', n)
                     or n.endswith(('.o', '.so', '.exe'))]
        assert not forbidden, (filename, forbidden)
    download = {
        'label': f'编程 {index:02d} 配套源码与算例（ZIP）',
        'url': url,
        'description': revision['package'].replace('`', '') + ' 含原始归属、GPL 许可证及说明；不含编译产物与历史解。',
        'size_bytes': len(data),
        'sha256': sha,
        'kind': 'case',
        'verification': metadata['verification'],
    }
    return download, {'slug': item['slug'], 'root': expected_root, 'url': url,
                      'files': len(names), 'size_bytes': len(data), 'sha256': sha,
                      'verified': ['CRC', 'course-number', 'single-root', 'README-course-link',
                                   'source-target', 'Make', 'Allrun', 'controlDict', 'GPL',
                                   'no-build-results', 'manifest-size-and-sha256']}


def main():
    lessons = json.loads(CONTENT.read_text(encoding='utf-8'))
    assert len(lessons) == 17
    manifest = {row['path']: row for row in json.loads((DOWNLOADS / 'manifest.json').read_text(encoding='utf-8'))}
    backup = ROOT / '.openfoam-work/course-refinement/programming-content.json'
    baseline = {row['slug']: row for row in json.loads(backup.read_text(encoding='utf-8'))} if backup.is_file() else {}
    report = []
    for index, item in enumerate(lessons):
        slug = f'programming-{index:02d}'
        assert item['slug'] == slug
        revision = REVISIONS[index]
        before = item['body']
        code_before, math_before = protected_content(before)
        body = replace_once(before, COMMON_PREREQUISITE, revision['prerequisite'] + '。', slug)
        illustration = f'![本课数据与执行关系](/assets/diagrams/{slug}.svg)'
        if revision['intro'] not in body:
            body = replace_once(body, illustration, revision['intro'] + '\n\n' + illustration, slug)
        for old, new in revision['edits']:
            for focus_old, focus_new in V2512_FOCUS.get(index, []):
                new = new.replace(focus_old, focus_new)
            body = replace_once(body, old, new, slug)
        body = replace_once(body, COMMON_EVIDENCE, revision['evidence'], slug)
        download, verified = download_for(item, index, revision, manifest)
        link = f'[下载本课精简源码与算例]({download["url"]}) · [下载清单与 SHA-256](/downloads/programming/manifest.json)'
        if revision['package'] not in body:
            body = replace_once(body, link, link + '\n\n' + revision['package'], slug)
        body = replace_once(body, OLD_ENV_COMMENT, NEW_ENV_COMMENT, slug)
        for old, new in V2512_FOCUS.get(index, []):
            body = replace_once(body, old, new, slug)
        code_after, math_after = protected_content(body)
        assert code_before == code_after, f'{slug}: existing code changed'
        # Explanations may mention an existing mathematical symbol again, but the
        # full ordered sequence of original expressions must remain unchanged.
        cursor = 0
        for expression in math_before:
            while cursor < len(math_after) and math_after[cursor] != expression:
                cursor += 1
            assert cursor < len(math_after), f'{slug}: existing TeX removed/changed: {expression}'
            cursor += 1
        assert item['metadata']['verification'] in body
        assert 'GPL-3.0-or-later' in body and 'Artur K. Lidtke' in body
        if index == 11:
            assert '1 项网格检查失败' in body and 'underdeterminedCells' in body
        item['body'] = body
        item['summary'] = revision['summary']
        if revision.get('title'):
            item['title'] = revision['title']
        item['metadata']['prerequisite'] = revision['prerequisite']
        item['metadata']['downloads'] = [download]
        if revision.get('topics'):
            item['metadata']['topics'] = revision['topics']
        elif 'topics' in item['metadata']:
            assert set(item['metadata']['topics']).issubset({'turbulence', 'multiphase', 'meshing', 'dynamic-mesh'})
        verified.update({'body_chars': len(body), 'body_before_chars': len(baseline.get(slug, {}).get('body', before)),
                         'code_blocks': len(code_after), 'tex_expressions': len(math_after),
                         'main_explanations_revised': len(revision['edits']),
                         'verification': item['metadata']['verification']})
        report.append(verified)
    CONTENT.write_text(json.dumps(lessons, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({'lessons': 17, 'downloads': report,
                                  'examples': [{'slug': f'programming-{index:02d}', 'before': REVISIONS[index]['edits'][edit][0],
                                                'after': REVISIONS[index]['edits'][edit][1]} for index, edit in [(3, 1), (7, 1), (10, 2)]],
                                  'note': 'Archive inspection and prose revision only; no additional OpenFOAM runtime or physical verification is claimed.'},
                                 ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'lessons': len(lessons), 'downloads': len(report),
                      'bytes': sum(r['size_bytes'] for r in report),
                      'prose_sections': sum(r['main_explanations_revised'] for r in report),
                      'report': str(REPORT)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
