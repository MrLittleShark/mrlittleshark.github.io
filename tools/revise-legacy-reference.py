"""Reconcile the original 37 reference chapters with the pinned v2512 library."""
from pathlib import Path
import html
import json
import re
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'source-openfoam'
BACKUP=ROOT/'.openfoam-work/replan/legacy-reference-originals'
BACKUP.mkdir(parents=True,exist_ok=True)
GIT='https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/'

REVISIONS={
 '为什么必须先分清':'OpenCFD v2512 与 Foundation 发行版是不同的代码分支。较新的 Foundation 版本使用模块化求解器及不同配置接口；不能把其命令和字典名称直接移植到 v2512。本网站以 OpenCFD v2512 的实际程序、源码标签和教程为准，版本号外观只用于初步识别。',
 '为什么第 ③ 步不能省':'激活 etc/bashrc 会设置可执行程序、共享库和教程等路径。环境未激活时，终端可能找不到 blockMesh，或者错误调用其他版本的程序。激活后应同时检查 WM_PROJECT_VERSION、WM_PROJECT_DIR 和 command -v blockMesh。',
 '正确做法是在 ~/.bashrc':'可在 ~/.bashrc 中为不同安装定义别名，并在使用时显式激活所需版本。别名中的路径必须与实际安装位置一致：',
 '为什么是这三个目录':'一个典型算例由时间目录中的场、constant 中的网格或模型数据、system 中的离散和运行控制组成。0 是常用初始时刻，但续算可以从其他时间目录读取；动态网格还可能写入后续时间目录。建议先检查 controlDict 中的运行设置，再对照场边界、物性和网格，最后确认求解器实际读取哪些文件。',
 '为什么值得专门记一章':'环境变量提供稳定的安装、教程和用户工作目录入口。使用 FOAM_TUTORIALS、FOAM_RUN、FOAM_USER_LIBBIN 等变量，可以减少脚本对个人绝对路径的依赖；首次使用仍需确认变量已定义且指向预期版本。',
 '为什么需要它：初学者':'边界条件类型取决于场类型、已加载的库和当前版本。foamHelp 能查询当前安装注册的类型；查询结果仍需结合对应模型的必需条目与物理适用条件。',
 '为什么需要它：写 functionObject':'从 v2512 自带模板开始配置，可以保留必要的库和参数结构。模板中的场名、patch 名、坐标与物性仍需根据具体算例修改，模板存在也不代表任意求解器都能使用它。',
 '为什么需要它：OpenFOAM 的配置':'配置查找可能经过用户、站点与安装目录。foamEtcFile 可用于查看匹配文件及搜索层级；诊断覆盖关系时，应同时检查环境变量与实际展开的字典。',
 '为什么不用 cp -r':'复制已有计算时，应明确是否需要网格、初始场和结果。foamCloneCase 可以按选项选择复制范围，减少把旧时间目录带入新算例的情况。普通 cp 也可以使用，但应检查目标目录和 startFrom 设置。',
 '为什么常用：调参阶段':'重复计算前要确定目标是从初始状态重新运行，还是从已有结果续算。清理命令会删除相应生成文件；先保留需要的结果，再检查时间目录与 startFrom，避免无意从旧时刻启动。',
 '为什么需要它：写批量脚本':'foamDictionary 可按条目路径读取或修改字典，适合参数扫描和批量算例设置。脚本应记录修改前后的值，并在运行前检查字典语法和参数量纲。',
 '为什么需要它：回答':'foamSearch 用于比较多个算例中特定条目的取值。其他教程的参数提供实例，不能替代本算例的模型选择、量纲分析和敏感性检查。',
 '为什么需要它：判断算例':'残差曲线有助于识别迭代停滞、周期性变化和发散。收敛判断还应包括质量与能量守恒、关注目标量以及适当的网格和时间步检查。',
 '为什么需要 foamExec':'foamExec 位于安装目录的 bin/tools，通常不会作为独立命令加入 PATH。它根据自身路径定位安装并激活 etc/bashrc，再执行传入程序；作业脚本通常也可以直接 source 已知安装的 bashrc。',
 '为什么用它而不是手写':'代码生成工具可以建立与 OpenFOAM 运行时选择机制相配套的类结构和 Make 配置。生成后仍需实现物理逻辑，检查基类接口、库依赖和边界更新条件，并通过小算例验证。',
 '0.orig/ 是什么':'0.orig 常用来保存可重复恢复的初始场模板。setFields 等工具可能修改工作目录中的场；restore0Dir 从保留模板恢复初始条件，有助于避免连续多次操作的相互影响。重复运行 setFields 是否改变结果，取决于其默认值与区域赋值方式，不能一概认为第二次运行必然错误。',
 '为什么它是入门第一课':'blockMesh 将顶点、块连接关系、网格数量和边界保存在文本字典中，适合学习局部编号与网格拓扑。snappyHexMesh 需要背景网格，该网格可以由 blockMesh 等工具提供。',
 '为什么需要它：snappyHexMesh':'显式特征边可帮助 snappyHexMesh 保持尖锐边缘。是否需要预先提取特征，还取决于显式/隐式特征捕捉设置、几何质量与局部分辨率。',
 '为什么是三步而不是一步':'分阶段检查切割细化、表面贴合和加层，有助于区分几何选择、特征捕捉、质量约束和层厚设置的问题。这些原因并非一一对应，应结合各阶段日志、网格质量和截面图定位。',
 '为什么需要它：二维算例':'挤出工具可以构造薄层、轴对称 wedge 或独立的薄壁区域。挤出方向、层数和前后边界类型必须与目标模型的二维或轴对称假设一致。',
 '为什么必须每次都跑':'网格修改后应运行 checkMesh，并查看网格与边界。拓扑检查通过并不保证所用数值格式具有足够精度；还需关注非正交、扭曲、尺寸突变和目标区域的分辨率。',
 '为什么能提速':'重编号改变矩阵的编号结构，可能改善带宽、局部性或求解性能。实际收益取决于网格、线性求解器和硬件，应以相同算例的计时和收敛结果比较，不能预设固定加速比例。',
 '为什么需要它：很多操作':'topoSet 通过几何或已有集合选择单元、面和点，为局部加密、区域源项、挡板或分区等操作准备集合。集合与 zone 的类型和用途不同，后续工具需要的名称必须一致。',
 '为什么不用手改 0/alpha.water':'setFields 按几何区域批量赋值，比直接修改按单元编号排列的数据更便于复现。操作后应检查相分数范围、所选体积和积分质量，并确认边界条件仍符合模型。',
 '为什么需要它：粗网格':'mapFields 可把已有结果插值到另一张网格，用于构造初值或衔接计算。它可能减少初始调整时间，但映射误差、守恒与边界变化仍需检查，不能保证所有工况都更快收敛。',
 '为什么需要它：共轭传热':'多区域算例含有多个网格和相互耦合的边界。使用脚本或字典批量更新可减少重复编辑，但仍需逐一核对区域名、patch 对应关系和耦合条件。',
 '为什么用 & 放后台':'末尾的 & 使任务在当前 shell 后台运行，并不保证 SSH 断开后任务仍继续。长任务应采用作业调度器、tmux 或按环境配置的 nohup，并明确日志与退出状态的保存方式。',
 '为什么要用 -postProcess':'通用 postProcess 与求解器的 -postProcess 模式创建的模型对象可能不同。yPlus、壁面剪切应力等量需要湍流或输运模型；应按函数对象要求选择能构建这些对象的入口，而不是假定只要已有 U、p 就足够。',
 '为什么要控制 Courant 数':r'Courant 数衡量单步输运相对于网格尺度的大小，简单一维估计为 \(\mathrm{Co}=|U|\Delta t/\Delta x\)。稳定性限制取决于时间积分、空间离散和多维通量；不能把 Co 大于 1 一概视为必然发散。隐式方法允许较大时间步也不代表时间精度足够。VOF 计算还应检查界面输运的时间步限制。',
 '为什么这么方便':'预配置函数来自 etc/caseDicts/postProcessing；#includeFunc 按模板或本地文件展开配置。使用 foamGetDict 复制所需模板后，应明确场名、边界名称和执行/输出频率。postProcess -list 列出预配置入口，不等于所有已编译函数对象类型的全集。',
 '输出在 postProcessing/forceCoeffs':r'forceCoeffs 的输出目录由函数对象实例名和起始时刻决定。使用运动学压力的不可压缩求解器时，应按 forces/forceCoeffs 的接口配置密度引用（常见为 rho rhoInf 与 rhoInf 数值）；如果使用热力学压力或可压缩密度场，则应采用相应处理。还应检查参考面积、参考长度、来流速度与力矩中心。',
 'writeResidualFields 很值得开':'writeResidualFields 可以输出初始残差的空间分布，辅助定位离散误差或局部迭代困难，同时会增加输出量。高残差区域也可能来自启动瞬态或物理源项，需要结合网格、边界和方程分析。',
 '大算例（千万网格）':'大规模结果可评估 redistributePar -reconstruct 的并行重构流程。是否优于串行重构取决于文件处理器、并行文件系统、进程数和字段数量，应在代表性数据上比较内存与耗时。',
 '为什么必须放在':'建议将自定义源码放在独立的用户工作目录，并通过版本控制管理。代码不必限定在一个固定目录，但编译输出与运行时库路径应按 FOAM_USER_APPBIN、FOAM_USER_LIBBIN 等配置，避免把个人修改混入安装源码。',
 '编译报 error:':'找不到头文件可能来自包含路径、文件名大小写、缺失依赖或尚未生成的 lnInclude。undefined reference 还可能来自源文件未参与编译、库依赖、链接顺序或 ABI 不匹配，应结合完整编译/链接命令定位。',
 '为什么重要：给一个抛物线':'codedFixedValue 可以在字典中嵌入 C++ 实现定制边界，并在运行时编译相关代码。使用时仍需正确设置 name、code、包含项和库依赖，并确认代码在当前 v2512 API 下能够编译。',
 '为什么 OpenFOAM 要检查量纲':r'许多场运算会进行量纲一致性检查；压力 Pa 与运动学压力 \(p/\rho\) 的量纲不同。遇到 incompatible dimensions，应先确认求解器对 p 的定义，再核对物性、源项与边界。量纲检查不能发现所有物理设置错误，也不应替代单位记录。',
 '为什么要知道 nonuniform':'nonuniform 按网格位置逐项保存场值，适合非均匀初始场和计算结果。批量修改宜使用 setFields、setExprFields 或其他明确的场处理流程，避免改变元素数量或破坏网格编号对应关系。',
 '为什么 LES 不能用 Euler':'LES 需要控制时间与空间离散的数值耗散。一阶 Euler 时间格式并非语法上禁止，但通常需要更严格的时间步敏感性检查；backward 或合适的 CrankNicolson 配置也必须结合稳定性、网格分辨率和统计量验证。',
 '为什么压力方程要特殊对待':'压力方程的长波误差可能使迭代收敛较慢。GAMG 通过网格聚合与多层修正加速误差消除，但性能依赖矩阵、聚合参数、平滑器和并行划分。应比较实际迭代次数与求解耗时，不采用固定的耗时比例判断。',
 'relTol 在瞬态里':'tolerance 是绝对残差阈值，relTol 是相对初始残差的下降阈值。可以对中间修正与最终修正采用不同精度，但需确认求解器会选择 pFinal 等配置；relTol 0 表示关闭相对提前停止，并不要求残差等于零。',
 '为什么稳态需要松弛':r'SIMPLE 等外迭代可使用场松弛或方程松弛降低更新幅度，提高某些非线性耦合问题的稳健性。松弛因子 \(\alpha\) 应结合收敛表现调整；压力与速度的松弛因子没有“相加应等于 1”的通用条件。',
 'wall 与 patch 的区别':'网格边界类型与场边界条件承担不同职责。壁面距离计算和许多壁面函数需要网格 patch 为 wall，某些错误组合会直接报错。forces 按配置的 patches 选择积分边界，不应笼统描述为所有后处理都只按 wall 自动识别。',
 '为什么它重要':'fvOptions 提供了许多区域源项、约束和修正模型。是否需要改写求解器，取决于已有模型是否覆盖目标方程和耦合方式；先检查求解器是否构造并使用 fvOptions，再选择合适的模型。',
 '为什么壁面上不能简单写 zeroGradient':'压力边界应与离散动量方程和法向通量约束一致。fixedFluxPressure 可在支持该更新流程的求解器中设置与通量相容的压力梯度；含重力或网格运动时尤其需要核对 p 与 p_rgh 的定义。zeroGradient 是否合理，应按具体方程和边界条件判断。',
 '入口湍流量怎么估':'入口湍流量可以根据湍流强度和特征长度估算；下式依赖各向同性及所选湍流模型的常见假设，实验数据可用时应优先核对：',
 'rm -rf 的两条纪律':'删除算例文件前，应先核对当前目录、匹配文件列表与保留需求。对于重复计算，优先使用可审查的算例清理脚本，并把原始几何、初始条件和自定义源码保存在生成结果之外。',
 '为什么强烈建议用 tmux':'tmux 会话在服务器端维持终端任务，可减少客户端断线对交互会话的影响。批量或共享集群计算仍应遵守作业调度方式，并独立记录日志、任务状态与退出码。',
 '长算例前先看一眼':'长计算前应估计结果输出量并检查磁盘空间。磁盘写满可能产生不完整时间目录；重启前应确认待读取文件完整。',
 '为什么大结果用 rsync':'rsync 可以按变化传输并支持指定排除规则，适用于重复同步大型结果。与 scp 比较时，应同时考虑连接方式、文件数量、权限以及断点恢复选项。',
 '遇到教程时先看它是哪个分支':'foamRun、momentumTransport 等名称可作为分支差异的线索，但最终应检查教程来源、版本和实际读取接口。迁移时逐项核对求解器、物性、湍流、源项和边界类型，而不是只替换文件名。'
}

def make_figure():
    out=SRC/'assets/diagrams/reference-workflow.svg'
    stages=[('算例与版本','环境 · 配置 · 初始场'),('网格与初始化','几何质量 · 字段范围'),('求解与监测','残差 · 守恒 · 目标量'),('后处理与复现','坐标 · 单位 · 验证')]
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1120 196" role="img" aria-labelledby="title"><title id="title">OpenFOAM 算例的准备、求解和验证关系</title><rect width="1120" height="196" rx="18" fill="#f0f6fc"/>'
    for i,(title,caption) in enumerate(stages):
        x=20+i*278
        svg+=f'<rect x="{x}" y="35" width="244" height="126" rx="11" fill="white" stroke="#b4cde2"/><text x="{x+17}" y="65" font-family="Arial" font-size="12" fill="#477ba4">0{i+1}</text><text x="{x+17}" y="100" font-family="Arial,Microsoft YaHei,sans-serif" font-size="19" fill="#173b54">{title}</text><text x="{x+17}" y="133" font-family="Arial,Microsoft YaHei,sans-serif" font-size="13" fill="#52728a">{caption}</text>'
        if i<3:svg+=f'<path d="M{x+250} 99 H{x+272} m-6 -5 l6 5 -6 5" fill="none" stroke="#477ba4" stroke-width="2"/>'
    out.write_text(svg+'</svg>',encoding='utf-8')

def text_tag(soup,name,text):
    tag=soup.new_tag(name);tag.string=text;return tag

def code_language(s):
    if re.search(r'\b(?:fvm::|fvc::|fvCFD.H|forAll\(|operator==)',s):return 'cpp'
    if re.search(r'\b(?:EXE_INC|EXE_LIBS|LIB_LIBS)\b',s) and not re.search(r'^wmake',s,re.M):return 'makefile'
    if re.search(r'(?m)^(?:#include(?:Func|Etc|IfPresent)?\s|FoamFile\s|dimensions\s|internalField\s|boundaryField\s|functions\s|application\s|solvers\s|ddtSchemes\s|vertices\s|castellatedMesh\s)',s):return 'openfoam'
    if re.search(r'(?m)^(?:\$ |source |printf |echo |foam\w+|\w+Foam\b|\.?/?Allrun|blockMesh|checkMesh|postProcess|setFields|topoSet|snappyHexMesh|mpirun|cd |cp |mkdir |rm |git |sudo |curl |wmake|export |#SBATCH|#!/.*sh)',s):return 'bash'
    if re.search(r'\b(?:type|value|solver|dimensions|internalField|writeControl)\s+[^\n]+;',s):return 'openfoam'
    return 'plaintext'

make_figure()
records=[]; edits=[]
for i,file in enumerate(sorted((SRC/'reference').glob('*/index.md'))):
    old=BACKUP/file.parent.name/'index.md'
    if not old.exists():old.parent.mkdir(parents=True,exist_ok=True);old.write_bytes(file.read_bytes())
    source=old.read_text(encoding='utf-8')
    title=json.loads(re.search(r'^title:\s*(.+)',source,re.M).group(1))
    title=title.replace('版本号长相','版本标识').replace('大全','参考').replace('文件都放在哪儿','文件位置与职责')
    match=re.search(r'{% raw %}\s*(.*?)\s*{% endraw %}',source,re.S)
    body=match.group(1) if match else re.sub(r'^---.*?---\s*','',source,flags=re.S)
    soup=BeautifulSoup(body,'html.parser')
    source_note=soup.find('p',class_='source-note')
    if source_note:source_note.decompose()
    for heading in soup.find_all('h4'):
        heading.name='h2'
    for element in list(soup.find_all('p')):
        txt=element.get_text(' ',strip=True)
        for prefix,replacement in REVISIONS.items():
            if txt.startswith(prefix):
                element.clear();element.append(replacement.replace('\\\\','\\'));edits.append([file.parent.name,prefix]);break
        else:
            if txt.startswith('注意顺序问题') or txt.startswith('推荐方式二的原因'):
                element.clear();element.append('v2512 的 paraFoam 最终调用 PATH 中的 paraview。-vtk（与 -builtin 等价）使用 ParaView 内置 OpenFOAM 读取器；-block 需要匹配的 blockReader 插件。可以用 command -v paraview 核对实际程序，使用 .foam 标记文件并不能保证所有版本都支持全部场与网格功能。')
            elif txt.startswith('paraFoam -block 能把'):
                element.clear();element.append('配置了相容的 blockReader 插件时，paraFoam -block 可用于检查块结构。若插件缺失，可先运行 blockMesh，再用 paraFoam -vtk 查看生成的网格；这两种显示对象不同。')
            elif txt.startswith('常用 -func 名字：'):
                element.clear();element.append('函数对象类型与预配置模板名称需要区分。先用 postProcess -list 查询预配置入口；mag、grad、Q、probes、forces 等功能还需要各自的字段和参数。fieldAverage 等类型通常应在 functions 中显式配置。线性求解器历史使用 solverInfo，并在求解时记录。')
            elif txt.startswith('如果你的版本没有这个命令'):
                element.clear();element.append('先用 command -v foamGetDict 检查当前环境。若安装未提供该脚本，可从正确的 etc/caseDicts 子目录复制对应模板；模板仍可能通过 #includeEtc 引用其他文件。')
    for element in soup.find_all(['td','th','h2','h3','h4']):
        for node in list(element.find_all(string=True)):
            value=str(node).replace('版本号长相','版本标识').replace('ESI / OpenCFD 版','OpenCFD 版').replace('命令大全','命令参考')
            if value.strip()=='residuals':value=value.replace('residuals','solverInfo')
            value=value.replace('#includeFunc residuals','#includeFunc solverInfo')
            if value=='foamRun -solver ...，物性文件叫 physicalProperties、momentumTransport':value='较新版本采用模块化求解入口；物性和湍流配置接口需分别核对'
            if value=='simpleFoam、interFoam，物性文件叫 transportProperties':value='simpleFoam、interFoam 等独立程序；物性文件由模型决定'
            if value=='统一为 foamRun -solver <模块>':value='较新版本提供 foamRun -solver <模块> 等入口'
            if value!=str(node):node.replace_with(value)
    for pre in soup.find_all('pre'):
        c=pre.find('code')
        if not c:continue
        text=c.get_text()
        text=re.sub(r'(?m)^\$ (?=\S)','',text)
        text=text.replace('OpenFOAM-v2512 (www.openfoam.com) version v2512','# 示例输出：v2512')
        text=re.sub(r'(?m)^foamVersion(?:\s*#.*)?$',lambda _: "printf '%s\\n' \"$WM_PROJECT_VERSION\"  # 版本变量不依赖交互式别名",text)
        text=re.sub(r'#includeFunc\s+residuals(?:\([^\n)]*\))?', '#includeFunc solverInfo',text)
        text=re.sub(r'\btype\s+residuals\s*;','type solverInfo;',text)
        text=text.replace('foamExec simpleFoam -help','"/usr/lib/openfoam/openfoam2512/bin/tools/foamExec" simpleFoam -help')
        text=text.replace('foamGetDict -list                 # 列出所有可取的模板','find "$WM_PROJECT_DIR/etc/caseDicts" -type f | less  # 查看安装中的模板文件')
        text=text.replace('foamSearch $FOAM_TUTORIALS fvSolution solvers/p/solver','foamSearch "$FOAM_TUTORIALS" solvers.p.solver fvSolution')
        text=text.replace('foamSearch $FOAM_TUTORIALS fvSchemes ddtSchemes/default','foamSearch "$FOAM_TUTORIALS" ddtSchemes.default fvSchemes')
        text=text.replace('foamNewSource app myApp','foamNew source H MyClass')
        text=text.replace('foamNewBC -f myBC','foamNewBC fixedValue vector myBC')
        text=text.replace('用旧算例最后时刻做新算例的初场','选择并复制最后时间目录；不会自动改名为 0')
        text=text.replace('endTime         0.5;','# 输出示例：endTime 0.5;')
        text=re.sub(r'(?m)^0\.5$', '# 输出示例：0.5',text)
        text=text.replace('Ux_0  Uy_0  p_0  contCumulative_0  contGlobal_0  ...','# 输出示例：Ux_0 Uy_0 p_0 contCumulative_0 contGlobal_0 ...')
        text=text.replace('这是必须养成的习惯','保存标准输出与错误输出')
        text=text.replace('foamMonitor -l postProcessing/residuals/0/residuals.dat','foamLog log.simpleFoam\nfoamMonitor -l logs/p_0')
        text=text.replace('paraFoam -touch ', 'paraFoam -vtk -touch ')
        text=text.replace('# 只生成 <算例名>.foam 文件，不启动','# 只生成 .foam 标记文件，不启动 ParaView')
        text=text.replace('postProcess -list                    # 列出所有可用功能','postProcess -list                    # 列出预配置函数对象入口')
        text=text.replace('结果在 1/ 目录，可单独查看','查看本次生成的网格时间目录，具体名称由时间设置决定')
        text=text.replace('foamListTimes -rm                               # 清理重来','foamListTimes                                   # 先列出时间目录\n# 确认保留需求后，才按帮助选择 -rm 删除结果')
        text=text.replace('三行就完事','按接口编译执行')
        # Keep the template interface exact: the v2512 patchAverage template uses
        # name and fields, not a universal patch=/field= API.
        text=text.replace('#includeFunc  patchAverage(patch=outlet, field=p)', '#includeFunc  patchAverage(name=outlet,fields=(p))')
        text=text.replace('patchAverage(patch=', 'patchAverage(name=')
        text=re.sub(r'\bfoamGet\b','foamGetDict',text)
        c.clear();c.append(text);c['class']='language-'+code_language(text)
    for a in soup.find_all('a',href=True):
        if re.match(r'^/(?:lessons|bubble)/',a['href']):
            a['href']='/courses/'
            if '电极' in a.get_text():a.string='课程学习路径'
    # Restore author TeX from any compiled HTML, if future source imports contain it.
    for span in soup.select('.math-formula[data-tex],.tex-source[data-tex]'):
        tex=span.get('data-tex','');display='math-display' in span.get('class',[]) or span.get('data-display')=='true'
        span.replace_with(('\\[' if display else '\\(')+tex+('\\]' if display else '\\)'))
    intro='<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div>'
    intro+='<figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure>'
    appendix=''
    if file.parent.name in ['guide-01','guide-02','guide-04','guide-05','guide-22','manual-11','manual-14']:
        appendix+='<h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p>'
        appendix+='<p><a href="'+GIT+'etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="'+GIT+'bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>'
    if 'residuals' in source or file.parent.name in ['guide-08','manual-10']:
        appendix+='<h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>'
    if file.parent.name=='guide-05':
        appendix+='<h2>未安装的官方目标</h2><p><code>foamCalc</code> 与 <code>foamExprParserInfo</code> 存在于 v2512 的 applications/tools，但当前虚拟机安装没有找到其可执行文件。请先用 command -v 核对，不能把源码中存在的程序等同于已安装程序。</p>'
        appendix+='<p><code>foamHelp boundary -field U</code> 需要能够读取相应网格和字段的算例。源码工具中的浏览器文档功能还依赖可用的文档索引及浏览器设置。</p>'
    body=intro+str(soup)+appendix
    # Plain source/paths containing shell dollars must not become accidental TeX.
    body=re.sub(r'(?<!\\)\$(?=[A-Za-z_{(])','&#36;',body)
    summary='OpenCFD v2512 '+re.sub(r'^(?:第\s*\d+\s*章\s*|\d+\s*)','',title)+'；包含原理、示例与版本核对。'
    front='---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\nlayout: reference\ndescription: '+json.dumps(summary,ensure_ascii=False)+'\n---\n'
    file.write_text(front+'{% raw %}\n'+body+'\n{% endraw %}\n',encoding='utf-8')
    records.append(dict(slug='reference-'+file.parent.name,kind='reference',title=title,summary=summary,body=body,track='命令与配置',series='主题参考手册' if file.parent.name.startswith('guide-') else '配置与命令综述',status='published',sort_order=2000+i,metadata={'format':'html','canonical_path':'/reference/'+file.parent.name+'/','version':'v2512','source_url':GIT,'review':'source-and-runtime-crosscheck'}))

out=ROOT/'tools/content/legacy-reference-content.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'.openfoam-work/replan/legacy-reference-review.json').write_text(json.dumps({'pages':len(records),'paragraph_corrections':edits},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(records),'corrected_paragraphs':len(edits),'cms':str(out)},ensure_ascii=False))
