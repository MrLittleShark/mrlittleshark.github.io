from pathlib import Path
import json,re,shutil,html,hashlib,zipfile
ROOT=Path(r'E:\Hexo')
SRC=Path(r'F:\UbuntuShareFolder\.foamlab-build\programming\sources')
ORIG=Path(r'F:\UbuntuShareFolder\BasicOFProgramming')
DEST=ROOT/'source-openfoam/assets/science'
DIAG=ROOT/'source-openfoam/assets/diagrams'
DEST.mkdir(parents=True,exist_ok=True); DIAG.mkdir(parents=True,exist_ok=True)
OUT=ROOT/'tools/content'
L=[]
def lesson(n,title,summary,stages,body,source,casefile,exercise,minutes=60):
    L.append(dict(n=n,title=title,summary=summary,stages=stages,body=body,source=source,casefile=casefile,exercise=exercise,minutes=minutes))

lesson(0,'编程 00｜OpenFOAM 应用程序结构与 wmake 编译','说明程序入口、OpenFOAM 环境、Make 文件与编译目标，检查程序启动和执行路径。',['C++ 源文件','Make/files','wmake 编译','用户 bin 目录','argList 初始化','Info 输出'],r'''
## 这段程序解决什么问题

本例只打印信息，用来确认编译器、头文件、动态库和执行路径是否一致。它不读取网格，不组装离散方程，也不计算流场。先完成这个最小闭环，可以把后续的数值问题与安装问题区分开。

`main(int argc, char *argv[])` 是 C++ 入口。`argc` 给出参数数量，`argv` 保存参数字符串。`fvCFD.H` 汇集常用有限体积类型；初学时便于使用，开发较大的库时可换成实际需要的头文件，以减少编译依赖。

```cpp
#include "fvCFD.H"
int main(int argc, char *argv[])
{
    #include "setRootCase.H"
    Info << "Hello OpenFOAM v2512" << nl << endl;
    return 0;
}
```

这里的 `#include "setRootCase.H"` 在函数体内插入初始化代码，建立参数解析和算例路径。它不是在调用一个名为 `setRootCase` 的函数。本例没有 `createTime.H` 和 `createMesh.H`，所以不能据此推断所有求解器都不需要 `controlDict` 或网格。

## 源码如何成为可执行文件

`Make/files` 的第一部分列出参与编译的 `.C`，最后的 `EXE` 决定目标位置。`Make/options` 中，`-I` 指定头文件搜索目录，`-l` 指定链接库。缺少头文件是编译阶段错误，`undefined reference` 是链接阶段错误，运行时找不到 `.so` 则发生在动态加载阶段，三个问题应分别检查。

```make
OFtutorial0.C
EXE = $(FOAM_USER_APPBIN)/ofTutorial0
```

```bash
echo "$WM_PROJECT_VERSION"
echo "$FOAM_USER_APPBIN"
bash Allwmake
command -v ofTutorial0
ofTutorial0 -help
```

版本输出应为 `v2512`。程序存在但执行的仍是旧版本时，用 `command -v` 检查 PATH，修改源码后重新编译；不要仅凭终端的欢迎横幅判断当前程序来自哪个源码目录。

## 怎样判断练习完成

运行 `testCase/Allrun` 后应出现自定义信息和 `End`，进程正常退出。本例没有结果时间目录是预期行为。把打印文本改为自己的名字并重新编译，输出随之改变，才能说明源码、编译目标和运行程序属于同一条路径。
''','OFtutorial0.C','system/controlDict','将输出分成三行，分别显示程序名称、用途和版本。再故意写错一处变量名，记录编译器定位的文件与行号，修复后重新编译。',35)

lesson(1,'编程 01｜字典、类型与可追溯的输入输出','把算例字典转换成强类型数据，理解 IOobject、IOdictionary、默认值和结果文件。',['constant 字典','IOobject 路径','IOdictionary','类型检查','HashTable / List','OFstream 文件'],r'''
## 从文件路径到物理参数

一个可复用的程序应把参数放在算例里。`IOobject` 描述文件名、所在时间或目录、所属对象注册表及读写策略；`IOdictionary` 才负责以字典结构保存条目。二者的分工有助于理解“文件存在，但读取失败”的原因。

本例先创建 `Time` 和 `fvMesh`，再读取 `constant/customProperties`。因此必须先执行 `blockMesh`。`MUST_READ` 表示输入必需；`NO_WRITE` 可用于只读配置。`typeHeaderOk<dictionary>(true)` 检查对象头是否符合预期，但不能代替对每一个参数范围的检查。

```cpp
IOdictionary settings
(
    IOobject("customProperties", runTime.constant(), mesh,
             IOobject::MUST_READ, IOobject::NO_WRITE)
);
scalar gain = settings.lookupOrDefault<scalar>("someScalar", 1.0);
Switch enabled = settings.lookupOrDefault<Switch>("someBool", true);
```

`word` 用于无空白的名称；`scalar` 是与编译精度一致的浮点数；`label` 用于索引；`Switch` 接受 `on/off` 等布尔写法。默认值适合可选参数，关键物性参数应明确要求输入，并检查正负或范围，避免“程序运行成功但用了错误的默认物性”。

## 列表和哈希表分别适合什么

`List<scalar>` 通过整数索引访问，适合有明确次序的数据。`HashTable<vector,word>` 通过名称关联向量，适合用边界名、测点名查找数据。哈希表的迭代顺序不构成稳定的物理顺序，绘图前应明确排序。

```cpp
List<scalar> values(settings.lookup("someList"));
HashTable<vector, word> points(settings.lookup("someHashTable"));
points.insert("probeA", vector(0.1, 0, 0));
```

## 输出文件不是场文件

本例在 `postProcessing/customOutputFile.dat` 中写入文本。`fileName` 负责路径拼接，`mkDir` 创建目录，`autoPtr<OFstream>` 管理文件流的生命周期。这种文件适合标量历史数据，不包含 OpenFOAM 场的网格关联和边界条件。

```cpp
fileName outDir = runTime.path()/"postProcessing";
mkDir(outDir);
OFstream data(outDir/"summary.dat");
data << "# gain enabled" << nl << gain << ' ' << enabled << nl;
```

并行程序应由主进程写同一个总输出文件，或让不同进程写不同路径。本例按串行教学使用；直接把串行文件输出放进 MPI 程序，会产生竞争写入。

## 两个输入实验

先将 `someScalar` 从 `0.01` 改为 `0.1`，确认程序输出改变，再删除这个可选条目，确认读到默认值。另一次把 `someList` 的一个数字改为普通单词，应看到类型读取错误；这比只检查文件是否存在更接近真实输入验证。
''','OFtutorial1.C','constant/customProperties','增加名为 samplingInterval 的正整数条目；当它小于 1 时用 FatalIOError 报错，并把实际采用的值写入输出头。',55)

lesson(2,'编程 02｜设计可检查的命令行接口','声明位置参数、布尔开关和带值选项；让自定义工具具有清楚的帮助信息。',['声明参数','注册选项','构造 argList','读取并检查','应用覆盖值','执行功能'],r'''
## 参数在什么时候注册

命令行接口必须先声明，再构造 `argList`。否则程序解析输入时还不知道某个选项的含义。`argList::addNote()` 为 `-help` 添加用途说明；`validArgs.append()` 声明必需的位置参数；`addBoolOption()` 表示只检查是否出现的开关。

```cpp
argList::noParallel();
argList::validArgs.append("someWord");
argList::validArgs.append("someScalar");
argList::addBoolOption("someSwitch", "Enable the alternative calculation");
argList::addOption("someInt", "label", "Number of samples");
argList args(argc, argv);
```

本例主动禁用并行。添加 `-parallel` 并不会使任意 C++ 代码自动具备分布式数据处理能力，后面的并行课程会补充通信与规约。

## 位置参数与可选参数

`args[1]` 对应第一个位置参数，`args.argRead<scalar>(2)` 把第二个位置参数转换为浮点数。选项读取使用 `optionReadIfPresent`，调用前应设置默认值。类型转换检查并不等于业务检查，例如负的采样数量仍可能是合法整数，但不是合法输入。

```cpp
const word name = args[1];
const scalar value = args.argRead<scalar>(2);
label count = 10;
args.optionReadIfPresent("someInt", count);
if (count <= 0)
{
    FatalErrorInFunction << "someInt must be positive" << exit(FatalError);
}
```

## 对照运行

```bash
ofTutorial2 -help
ofTutorial2 probeA 5.0 -someSwitch -someInt 2
ofTutorial2 probeA 5.0 -someInt 4 -dict system/customDict
```

原例的 `-dict` **只演示路径解析**，并不读取该字典。看到 `Would read dict from ...` 不能说明文件被加载。要实现真正的覆盖机制，还要构造相应的 `IOobject` 或输入流，并明确命令行与字典的优先级。

建议约定：程序内默认值优先级最低，算例字典居中，用户显式传入的命令行选项最高。启动时打印最终采用的参数，计算记录才具备可追溯性。

## 失败也是接口的一部分

分别省略第二个位置参数、把浮点数改为文字、传入未知选项，观察退出状态和帮助文本。一个工具应在开始修改结果之前拒绝无效参数。参数名区分大小写，带空格的路径应在 shell 中加引号。
''','OFtutorial2.C','system/controlDict','增加 -scale scalar 选项，默认值为 1；输出 scale 与输入标量的乘积，并在 -help 中解释单位与允许范围。',50)

lesson(3,'编程 03｜网格拓扑、几何量与 patch 数据访问','区分网格拓扑与几何数据，说明内部面、边界面、owner/neighbour 和 patch 局部索引的访问方法。',['points 顶点','faces 连接','owner / neighbour','cell centres','patch 局部编号','面通量方向'],r'''
## 网格不是一个坐标数组

OpenFOAM 多面体网格由连接关系和几何量共同描述。`points` 存坐标，`faces` 存组成面的点编号，`owner/neighbour` 把面连接到单元，`boundary` 则把连续的一段边界面归入 patch。有限体积离散需要的不只是“这个面在哪里”，还包括“它连接哪两个控制体”。

对内部面，面积向量 $\mathbf{S}_f$ 从 owner 指向 neighbour；边界面的面积向量指向计算域外。因此 $\phi_f=\mathbf{U}_f\cdot\mathbf{S}_f$ 为正时，表示相对于 owner 的外流。通量符号和速度坐标分量不是同一个概念。

```cpp
for (label facei = 0; facei < mesh.nInternalFaces(); ++facei)
{
    label own = mesh.owner()[facei];
    label nei = mesh.neighbour()[facei];
    Info << facei << ' ' << own << ' ' << nei << nl;
}
```

`mesh.faces()`、`mesh.faceCentres()` 包含完整的拓扑或几何列表，而 `mesh.Cf()` 是带边界场结构的有限体积面场，其内部数组与边界数组分开。不能把全局边界面编号直接用作内部数组索引。原教学代码依赖给定算例的尺寸；扩展时应显式使用 `nInternalFaces()` 等边界条件。

## patch 的三种编号

`patchi` 是边界块编号，`localFacei` 是该边界块内的面编号，全局面编号为 `patch.start()+localFacei`。patch 邻接单元由 `faceCells()` 获取。`findPatchID(name)` 在找不到名称时返回负值，必须先检查再索引。

```cpp
label patchi = mesh.boundaryMesh().findPatchID("movingWall");
if (patchi < 0) FatalErrorInFunction << "Patch missing" << exit(FatalError);
const fvPatch& patch = mesh.boundary()[patchi];
forAll(patch, localFacei)
{
    Info << patch.start()+localFacei << ' '
         << patch.faceCells()[localFacei] << nl;
}
```

`empty` 代表降维假设，不是“可以随意当作普通壁面”的边界。访问第 0 个面以前还应检查 patch 是否为空。分解网格新增的 `processor` patch 也不是物理壁面。

## 用文件和程序交叉检查

运行 `blockMesh` 和 `checkMesh`，记录单元、内部面和边界面的数量。随后选择一个内部面，对照 `faces` 中的顶点编号、`points` 坐标以及程序打印的面中心。最后确认 owner、neighbour 中的单元确实位于该面的两侧。这个小实验比只看彩色网格更能揭示数据结构。
''','OFtutorial3.C','system/blockMeshDict','编写一个检查函数，输出每个 patch 的总面积及面积向量和。解释封闭边界整体面积向量和为什么应接近零。',80)

lesson(4,'编程 04｜场、量纲和显式微分算子','创建与读取体场，通过解析表达式赋值，理解 fvc::grad 与真实动量方程的区别。',['读取 p 与 U','定义量纲','计算半径场','时间函数赋值','fvc::grad','按控制字典输出'],r'''
## 场保存了哪些信息

`volScalarField` 在单元中心保存标量，并携带网格引用、量纲和各 patch 的边界条件；`volVectorField` 保存三分量向量。它们不等于普通的 `List<scalar>`。本例读取 `p` 和 `U`，用解析表达式重设 `p`，再将其梯度转换成一个演示用向量场。

本例采用不可压缩求解器常见的运动压力量纲 $[p]=L^2T^{-2}$。这不是 Pa，不能直接与实验表压比较。`dimensionedScalar` 让字段表达式带量纲，`.value()` 取出的裸数会失去这层检查。

```cpp
const dimensionedVector x0("x0", dimLength, vector(0.05,0.05,0.005));
volScalarField r(mag(mesh.C()-x0));
U = fvc::grad(p)*dimensionedScalar("timeScale", dimTime, 1.0);
```

因为 $[\nabla p]=LT^{-2}$，乘以时间后才得到速度量纲。这个运算没有求解动量方程和连续性方程，所以得到的 `U` 只是教学构造场，不能解释为真实压力驱动流动。

## 从逐单元循环到场表达式

原例按单元计算到参考点的距离，构造形如

$$p(\mathbf{x},t)\propto\frac{\sin(2\pi f t)}{r/r_{\max}+\varepsilon}.$$

逐单元循环便于观察索引；场表达式通常更简洁，并保留量纲信息。分母的小数只避免零除，并不自动消除中心附近的巨大梯度。网格中存在非常接近参考点的单元时，结果会对 $\varepsilon$ 和网格位置敏感。

`fvc` 算子直接从已有场计算新场，`fvm` 算子构造包含待求变量的矩阵。本例没有 `solve()`，因此它是场操作程序，不是流动求解器。

## 时间循环和输出时刻

`runTime.loop()` 推进当前时间，`runTime.write()` 根据 `controlDict` 决定是否写盘。`AUTO_WRITE` 表示对象参与自动写出，并不代表每一行赋值后都写文件。

在 ParaView 中，用等值线观察 `p`，再用 Glyph 显示 `U`。检查正弦符号变化时，箭头是否反向。读取量纲、色标和时间值后再解释图像，避免把正负色块误认为压力单位已完成转换。

## 两个检查

在远离参考点的位置，比较相邻单元压力差与 `grad(p)` 的方向；把时间步减半，观察同一物理时刻的解析值是否一致。这里的时间步实验检查的是采样，不是时间离散误差，因为压力直接由解析函数赋值。
''','OFtutorial4.C','0/p','把半径分母改成光滑的平方根形式，并在纸上推导径向导数；比较解析梯度与 fvc::grad，排除参考点及边界附近后计算误差。',75)

lesson(5,'编程 05｜MPI 场操作、数据通信与一致性检查','区分局部量与全局量，使用 reduce、Pstream 和 processor 边界完成通信，并比较串行与并行结果。',['分解网格','每个 rank 独立场','局部统计','全局 reduce','更新 processor 边界','比较串并行结果'],r'''
## 一个程序，多个局部网格

MPI 并行下，每个进程持有自己子域的 `mesh`、`p` 和 `U`。`mesh.V().size()` 是当前子域的单元数，不是整个算例的单元数。串行代码中看似合理的 `max`、求和、文件写入，迁移到并行时必须检查其作用范围。

```cpp
scalar volume = 0;
forAll(mesh.V(), celli) volume += mesh.V()[celli];
reduce(volume, sumOp<scalar>());
Info << "Global volume = " << volume << nl;
```

体积是各子域局部体积之和；全局最大半径则使用最大值规约。不能用子域各自的最大半径归一化同一个解析场，否则结果会在分区界面出现人为不连续。

## 通信必须由参与进程一致调用

`Pstream::myProcNo()` 返回进程编号，`Pout` 输出带进程标识的诊断信息，`Info` 通常只由主进程输出。`gatherList` 汇集每个进程的条目，`scatterList` 把结果传播给各进程。规约、汇集等集体操作不能随意放进只有一个进程进入的条件分支，否则可能等待不到其他进程。

```cpp
label localCells = mesh.nCells();
label totalCells = returnReduce(localCells, sumOp<label>());
Pout << "local=" << localCells << nl;
if (Pstream::master()) Info << "total=" << totalCells << nl;
```

## 为什么还要修正边界

分区界面以 `processor` patch 表达相邻子域间的联系。内部压力赋值后调用 `p.correctBoundaryConditions()`，让后续梯度算子获得一致的界面数据。它不是“修正物理模型”的操作，而是执行该字段边界类型定义的更新过程。

```bash
blockMesh
decomposePar
mpirun -np 4 ofTutorial5 -parallel
reconstructPar -latestTime
```

`-np` 应与 `numberOfSubdomains` 一致，机器也必须提供相应进程槽位。本资料的 `Allrun` 在结束时删除 `processor*`；若需要对照并行场，应按上面逐步执行，在清理前重构。下载包只在其独立教学目录中使用。

## 并行正确性怎样验证

分别在串行和四分区运行相同的时间与网格，比较全局体积、最大最小值和同一组测点上的场值。浮点求和顺序变化会带来微小差别，因此用合理容差比较，不要求文本文件逐字节一致。若出现只沿分区边界分布的误差，应优先检查局部归一化和边界同步。
''','OFtutorial5.C','system/decomposeParDict','增加全局平均压力：先计算局部的压力乘体积之和与体积之和，再分别规约，不能直接平均各进程的平均压力。',80)

lesson(6,'编程 06｜自定义类与 IOdictionary 扩展','通过构造函数、访问控制、引用和继承组织程序状态，核对接口声明、实现与源码注释。',['声明 .H','实现 .C','构造状态','传递 mesh 引用','继承 IOdictionary','编译多个源文件'],r'''
## 什么时候需要一个类

当一组操作共同维护同一个状态时，用类把状态和行为组织起来。`customClass` 用私有成员 `myInt_` 保存整数，构造函数将其初始化，`get()` 读取它，`set()` 修改它。外部代码通过公开接口访问，避免直接依赖内部实现。

```cpp
class customClass
{
    label myInt_ = 0;
public:
    label get() const { return myInt_; }
    void set(label value) { myInt_ = value; }
};
```

`get() const` 表示该成员函数不修改对象状态；`set()` 需要修改状态，因此不是 `const`。原资料有一处注释把这两者混淆，判断时应以声明和实现为准。`inline` 允许头文件中的定义被多个翻译单元使用，并不保证编译器一定展开，也不表示“避免链接”。

## 引用与复制

`meshOpFunction(fvMesh& mesh)` 接收网格引用，不复制整个网格。若函数仅查询网格，接口更适合写成 `const fvMesh&`，让编译器约束误修改。本例通过读取单元数量更新 `myInt_`，所以它修改的是类自身的状态，并非网格。

## 派生字典保留了什么

`myDict : public IOdictionary` 保留原有字典查找功能，额外添加 `printTokensInTheDict()`。构造函数的初始化列表把 `IOobject` 交给基类，完成文件读取。不能只在派生类函数体中保存文件名就认为基类已初始化。

```cpp
myDict::myDict(const IOobject& io)
:
    IOdictionary(io)
{}
```

该例把 `tokens()` 中的 `word` 类型条目列出，用于观察解析结果；它不会完整打印所有数字，也不是配置文件的结构化校验器。若希望检查关键参数，应按键名读取并验证，而非搜索打印文本。

## 编译单元为什么重要

头文件给出接口，`.C` 给出定义。`Make/files` 必须同时列出 `customClass.C`、`derivedClass.C` 和主程序，否则编译可能成功而链接缺少函数定义。改类声明后，应重新编译所有依赖它的应用和库，不能继续使用旧 ABI 的共享库。

运行后检查默认值为 0，设置后为 10，网格操作后为单元数。再确认派生字典仍可读取 `nu`，这同时验证新增功能和继承功能。
''','customClass.H','constant/transportProperties','给 customClass 添加 reset()，再把 meshOpFunction 的参数改成 const fvMesh&。解释为什么这两个变化不要求改变调用端的网格数据。',65)

lesson(7,'编程 07｜共享库与对象注册表','把计算函数移入独立共享库，理解编译依赖、链接路径和通过名称查找已注册的场。',['库接口 .H','wmake libso','用户 lib 目录','应用链接 -l','objectRegistry 查找','计算并输出 U'],r'''
## 为什么拆分共享库

多个求解器都需要同一段几何计算时，把它复制到各个应用会增加维护成本。本例将 `computeR` 和 `computeU` 放进 `customLibrary`，先编译 `libcustomLibrary.so`，再链接 `ofTutorial7`。主程序保留时间循环和场的创建，库负责可复用的运算。

```make
# customLibrary/Make/files
customLibrary.C
LIB = $(FOAM_USER_LIBBIN)/libcustomLibrary
```

应用的 `Make/options` 同时添加 `-IcustomLibrary` 和 `-L$(FOAM_USER_LIBBIN) -lcustomLibrary`。前者解决编译时声明查找，后者解决链接时符号查找。运行时仍需动态加载器能找到 `.so`；正常加载 v2512 环境会配置相关路径。

## 参数哪些只读，哪些会被修改

```cpp
scalar computeR(const fvMesh& mesh, volScalarField& r, dimensionedVector x0);
void computeU(const fvMesh& mesh, volVectorField& U, word pName = "p");
```

`mesh` 是只读引用，`r` 和 `U` 是输出引用。`computeR` 写入各单元到参考点的距离，并返回全局最大距离。函数接口清楚表达数据流，调用者就不必阅读整个实现才能知道哪个场会被改动。

## 对象注册表不是从磁盘自动加载

`mesh.lookupObject<volScalarField>(pName)` 从网格关联的对象注册表查找已经存在的场。它不会因为磁盘上有 `0/p` 就自动创建压力场。调用前必须构造并注册正确名称与类型的对象。

```cpp
const volScalarField& p = mesh.lookupObject<volScalarField>(pName);
U = fvc::grad(p)*dimensionedScalar("timeScale", dimTime, 1);
```

按名称查找减少参数数量，但也隐藏了依赖。开发复杂模块时，可以显式传入 `const volScalarField& p`，让依赖由函数签名体现；需要通用函数对象时，再使用注册表和可配置字段名。

## 两类加载错误

`cannot open shared object file` 通常需要检查库文件和运行时搜索路径；`undefined symbol` 还可能来自版本、编译选项或 ABI 不一致。不要把 Foundation 的已编译 `.so` 复制到 OpenCFD v2512 中使用，应从源码重新编译。

运行结果应与同样表达式的单文件程序一致。这个比较验证的是代码拆分没有改变计算，而不是验证演示向量场满足流体方程。
''','customLibrary/customLibrary.C','constant/transportProperties','为库增加 computeMeanPressure(const volScalarField&)；实现体积加权与并行规约，并让两个不同应用复用该函数。',75)

lesson(8,'编程 08｜可运行时选择的入口边界条件','从 fixedValue 派生空间非均匀速度边界，理解构造函数、updateCoeffs、映射和写出接口。',['字典 type 名称','运行时选择表','读取几何参数','逐面计算剖面','更新 patch 值','写出可重启参数'],r'''
## “固定值”也可以在空间上变化

`fixedValueFvPatchVectorField` 表示指定每个边界面的速度值，不要求所有面取同一个向量。本例根据圆管入口面中心到轴线中心的距离构造剖面，并沿面法向的反方向施加入流。

$$\mathbf{U}_f=-U_0\,g(\eta_f)\frac{\mathbf{S}_f}{|\mathbf{S}_f|},\qquad
\eta_f=\frac{1-r_f/R}{\delta/R}.$$

`flowSpeed` 是核心区速度尺度，不是自动归一化的截面平均速度。若希望给定体积流量，应积分离散剖面后再缩放，不能直接令 `flowSpeed=Q/(\pi R^2)` 并假定结果严格相等。

## 字典怎样找到 C++ 类型

头文件的 `TypeName("prescribedPipeInlet")` 给出字典使用的名称；`.C` 中的 `makePatchTypeField` 注册构造方法；`controlDict` 的 `libs ("libprescribedPipeInlet.so");` 触发共享库加载。三者缺少任何一个，都不能仅靠在 `0/U` 中写 `type` 来启用边界。

```foam
inlet
{
    type prescribedPipeInlet;
    approximationType parabolic;
    R 0.05;
    flowSpeed 1;
    deltaByR 0.2;
    centrepoint (0 0 0);
    lambda 0;
    value uniform (0 0 0);
}
```

以上是参数结构示例，`R` 和 `centrepoint` 必须改为实际入口几何。原实现的键名是小写 `centrepoint`，不是部分旧注释中的 `centrePoint`。

## updateCoeffs 的工作顺序

先用 `updated()` 避免在同一更新周期重复计算；再根据 `patch().Cf()` 和几何参数得到每个面的速度；用 `operator==` 强制赋值；最后调用基类 `updateCoeffs()` 标记更新完成。普通赋值运算符在某些固定值边界中有特殊语义，不能机械替换这里的调用。

原例提供抛物线、`Polhausen` 和七分之一次幂剖面。它们只在靠壁区域应用，核心区保留速度尺度。参数必须满足 $R>0$、$\delta/R>0$；面位于假定圆管外时，幂函数可能出现非法值，教学例不能替代通用几何检查。

## v2512 迁移细节

本次实测发现原资料的 `writeEntry(os, "value", *this)` 不符合当前 OpenCFD 接口。下载包已改为 `writeEntry("value", os)` 并保留原始许可。构造与映射函数应与当前 `fvPatchField` 接口一致；库能编译后，还要验证字典构造、分区映射、重构和重新读取。

建议先画入口剖面，再运行管流。`yPlus` 是壁面分辨率相关诊断，不能单独证明自定义入口正确。至少核对速度方向、壁面附近趋势和截面积分流量。
''','prescribedPipeInletFvPatchVectorField.C','0.org/U','比较 parabolic 与 exponential 的入口流量。增加离散面积积分归一化，使两种剖面具有同一个指定 Q；并行情况下积分必须做全局规约。',110)

lesson(9,'编程 09｜流量监测 functionObject 的实现','在求解过程中读取注册场、计算截面流量，并管理监测频率、文件输出与并行规约。',['controlDict functions','查找 faceZone','插值 U 到面','积分 U · Sf','MPI 规约','主进程写文件'],r'''
## 监测功能不必写进求解器

函数对象由求解器的运行时控制系统调用，可以在不改主求解循环的情况下记录流量、力或统计量。本例 `pipeCalc` 继承 `fvMeshFunctionObject` 和 `logFiles`：前者提供网格上下文，后者管理日志文件。

`TypeName` 与 `addToRunTimeSelectionTable` 让 `controlDict/functions` 能选择该对象。`read()` 读取参数，`execute()` 适合计算供其他对象使用的量，`write()` 负责实际写出；本例将主要计算也放在 `write()` 中，因此输出频率直接决定监测频率。

## 流量公式对应哪一行代码

$$Q=\int_A\mathbf{U}\cdot\mathbf{n}\,\mathrm dA
\approx\sum_{f\in A}\mathbf{U}_f\cdot\mathbf{S}_f.$$

```cpp
const volVectorField& U = obr_.lookupObject<volVectorField>(UName_);
surfaceVectorField Uf = fvc::interpolate(U);
scalar Q = 0;
forAll(faces_, i) Q += Uf[faces_[i]] & mesh_.Sf()[faces_[i]];
reduce(Q, sumOp<scalar>());
```

这里得到体积流量，量纲为 $L^3T^{-1}$。可压缩质量流量需要密度加权，不能只更改输出文件表头。若求解器已有守恒修正后的 `phi`，使用该通量积分通常更适合检查离散质量守恒；由 `U` 再插值得到的通量不一定与求解器使用的 `phi` 完全相同。

## 这个教学实现的边界

原例假定 faceZone 中的面都能按内部面数组访问。它没有完整处理 processor 边界面、边界场索引和 faceZone 的 `flipMap` 方向；当截面跨越分区或面的朝向不一致时，直接照搬会得到错误符号，甚至越界。课程提供这个例子用于学习函数对象结构，生产使用优先对照 v2512 的 `surfaceFieldValue` 等成熟实现。

查找 faceZone 后应检查 `findZoneID()` 是否小于零。原代码在构造列表引用时就索引该编号，因此缺失 zone 需要在建立对象以前通过 `topoSet` 正确生成。

## 文件输出与重启

只有主进程写合并后的时间序列，其他进程参与积分规约。输出头应记录 zone 名称、方向约定和单位。重启计算时应检查输出时间是否重复，以及下游脚本是追加读取还是覆盖读取。

验证时选用直管或已知均匀速度截面，比较 $Q=UA$、自定义对象的积分和标准函数对象输出。结果一致后再增加更复杂的分区或弯曲截面。
''','pipeCalc.C','system/topoSetDict','增加 zone 存在性检查，并用标准 surfaceFieldValue 对同一截面计算 phi 的和，解释两种通量在未收敛阶段可能出现差异的原因。',100)

lesson(10,'编程 10｜对流扩散方程的求解器实现','将守恒方程对应到 fvm 矩阵、面通量和离散配置，通过稳态标量算例检查编译、求解与结果输出。',['读 beta 与 U','建立面通量 phi','读取扩散系数','组装 div − laplacian','fvSolution 线性求解','写出 result'],r'''
## 先明确所求方程

本例求解给定速度场中的稳态标量输运：

$$\nabla\cdot(\mathbf{U}\beta)-\nabla\cdot(\gamma\nabla\beta)=0.$$

`beta` 在算例中无量纲，$\gamma$ 的量纲为 $L^2T^{-1}$，`U` 的量纲为 $LT^{-1}$。程序读取速度而不求解它，所以这是被动标量输运例，不包含标量对流场的反馈。

```cpp
surfaceScalarField phi
(
    IOobject("phi", runTime.timeName(), mesh,
             IOobject::READ_IF_PRESENT, IOobject::AUTO_WRITE),
    fvc::interpolate(U) & mesh.Sf()
);
solve(fvm::div(phi, beta) - fvm::laplacian(gamma, beta));
```

有限体积对流项使用面通量 $\phi_f$，而不是直接把单元速度传给 `fvm::div`。`fvm` 将未知 `beta` 的系数组装进矩阵，边界条件已经包含在场对象中，参与边界系数和源项的处理。

## 三个文件共同定义一次求解

`0/beta` 给出左边界为 1、下边界为 0、右和上边界零梯度、前后 `empty`。`fvSchemes` 指定 `div(phi,beta)`、`laplacian(gamma,beta)` 和 `interpolate(U)` 的离散格式。`fvSolution` 决定 `beta` 方程的线性求解器和停止条件。

```foam
divSchemes
{
    default none;
    div(phi,beta) bounded Gauss upwind;
}
laplacianSchemes
{
    default none;
    laplacian(gamma,beta) Gauss linear corrected;
}
```

`default none` 有助于暴露遗漏项。缺少某个名称时，先对照求解器真正构造的算子名称，而不是把所有 default 改成一个通用格式掩盖错误。

## 为什么结果仍在初始时间目录

程序只求解一次稳态线性方程，没有时间循环。它将已求出的 `beta` 复制成名为 `result` 的场并显式 `write()`，因此初始 `beta` 保留，结果写入当前时间目录。看到结果不在 `1/` 或 `100/` 不意味着计算没执行。

定义网格 Peclet 数 $Pe_h=|U|\Delta x/\gamma$，可以判断对流与扩散在单元尺度上的相对强度。增大它后，上风格式的数值扩散更明显。更换格式时同时观察范围、剖面和网格加密结果，不能仅以残差较小判断精度更高。

本次 v2512 实测中，该程序完成编译与给定算例求解；线性残差下降只证明代数系统被求解到设定容差，还需要网格和格式比较验证离散误差。
''','OFtutorial10.C','system/fvSolution','将 gamma 缩小为原来的十分之一，比较 upwind 与 linearUpwind 的标量截面；记录 min/max，检查是否超过入口标量范围。',100)

lesson(11,'编程 11｜用 C++ 构造多面体网格','从点、单元形状和边界面生成 polyMesh，理解拓扑合法性与几何质量是两类检查。',['定义 17 个顶点','组织 cellShape','指定边界面','建立 polyMesh','写出网格','checkMesh 检查'],r'''
## 从读取网格转向生成网格

本例显式创建 17 个顶点，组合六面体、棱柱、棱锥和四面体，并为部分外表面命名。`cellModeller::lookup()` 获取标准单元模型，`cellShape` 将模型和有次序的顶点列表关联，最后构造 `polyMesh`。

```cpp
const cellModel& hex = *cellModeller::lookup("hex");
pointField points(8);
// 按给定模型约定填写 points 与顶点编号。
List<label> vertices(8);
List<cellShape> cells;
cells.append(cellShape(hex, vertices));
```

这只是结构示意，不能把未赋值的点或编号作为可运行网格。下载例提供完整顶点与连接数据。顶点顺序决定面方向、单元朝向和体积，不能因为坐标点相同就任意置换编号。

## patch 是面列表及其物理语义

`faceListList` 保存每个 patch 的面，每个面又由点编号组成。`boundaryPatchNames`、`boundaryPatchTypes` 和 `boundaryPatchPhysicalTypes` 应与 patch 数量和次序一一对应。遗漏的外表面进入默认 patch，并不会自动获得合理的物理边界条件。

原教学例为默认面设置 `empty`，主要用于展示网格结构。`empty` 的数值含义是降维约束，不能用于这个包含多种三维单元的默认外表面。本站下载副本将默认类型改为 `patch`，并以 `pointField(points)` 向 v2512 的移动构造接口传递点数据。准备流动计算时还必须重新核对每一个 patch 类型及相应场边界。

## 构造成功不等于网格质量合格

```bash
ofTutorial11
checkMesh -constant -allTopology -allGeometry
```

拓扑检查关注闭合、连接和重复面；几何检查关注体积、面方向、非正交性、扭曲等。程序可能成功写出文件，但 `checkMesh` 报告失败。此时应回到点连接和 patch 定义定位问题，不能以 ParaView 能打开为合格标准。

本次检查中，5 个单元的演示网格写出成功，体积为正；完整检查仍报告 **1 项网格检查失败**：单元连接不足导致几何行列式检查中的 underdeterminedCells。它适合展示混合单元构造，不能直接标为合格生产网格。`checkMesh` 命令的退出状态也不能替代对 `Failed ... mesh checks` 文本的检查。

原脚本在运行前调用 `Allclean`，因此应在下载副本中工作，并先保存需要比较的网格。直接运行主程序也会写出网格，本课不在重要生产算例中进行。

## 建议的观察顺序

先用 Surface With Edges 显示各单元，再逐个提取 patch，检查名称、类型及面位置。随后输出每个 cell 的体积，确认所有预期单元体积为正。最后扰动一个顶点，观察几何质量指标如何变化，从而把“网格看起来歪了”转换成可计算的指标。
''','OFtutorial11.C','system/blockMeshDict','仅在副本中交换一个单元的两个顶点编号，记录 checkMesh 的诊断；恢复后再移动同一顶点，比较拓扑错误和几何质量变化。',100)

lesson(12,'编程 12｜自定义动量源向 v2512 fvOptions 的迁移','以执行器盘为例说明区域选择、源项量纲和运行时接口，并核对 Foundation 与 OpenCFD 的迁移差异。',['选择盘区单元','上游速度采样','计算推力','按体积分配','fv::option::addSup','检查总源项'],r'''
## 先区分 API 分支

提供的原始文件虽在总 README 中标注 v2512，实际仍使用 Foundation 的 `fvModel.H`、`addSupFields()` 与 `constant/fvModels`。OpenCFD v2512 的本例应使用 `fv::option`、`fieldNames_`、`resetApplied()`、带字段索引的 `addSup()`，并放入 `constant/fvOptions`。本课程下载包包含独立迁移副本，原材料不被覆盖。

```cpp
// v2512 的构造次序：name, modelType, dict, mesh
option(name, modelType, dict, mesh)
// 注册受作用场并复位应用标志
fieldNames_ = wordList(1, Uname_);
resetApplied();
```

仅把字典文件重命名不足以完成移植：基类、构造参数次序、虚函数签名和运行时选择表都必须一致。

## 几何选择怎样表达圆盘

设盘心为 $\mathbf{x}_0$，单位法向为 $\mathbf{n}$，单元中心位移为 $\mathbf{r}=\mathbf{x}_P-\mathbf{x}_0$。法向距离 $d_n=\mathbf{r}\cdot\mathbf{n}$，径向距离 $d_r=\sqrt{\max(|\mathbf r|^2-d_n^2,0)}$。选择 $|d_n|<t/2$ 且 $d_r<D/2$ 的单元。

用位移直接点乘，可以避免原例在盘心处先计算单位径向向量造成零除。盘厚过小可能选不到任何单元；下载副本会拒绝无效几何与空选择，而不是静默地施加零源项。

## 总力与单元源项

理想执行器盘关系写为

$$a=1-\frac{C_p}{C_t},\qquad
T=2\rho A U_n^2a(1-a),\qquad
\mathbf{F}_P=\frac{V_P}{\sum_{j\in\Omega_d}V_j}\,T\mathbf n.$$

其中 $U_n$ 是上游速度在盘法向的投影。源项模型把总量按单元体积分配，求和后应恢复总力。不可压缩动量方程使用运动学形式，密度常以单位场表示；解释数值单位时必须查看求解器方程，不能直接把数组值都称为 N。

`eqn.source()` 是离散方程的体积积分源数组，不是单位体积力。正负号还与 `fvOptions` 如何出现在方程中有关。应从单元动量预算和速度变化验证阻力方向，不能只看变量名 `diskDir`。

## 迁移后的字典组织

```foam
actuationDisk
{
    type customActuationDiskSource;
    active yes;
    customActuationDiskSourceCoeffs
    {
        Uname U;
        diskCentre (0 0 0);
        diskDir (-1 0.5 0);
        D 1;
        thickness 0.1;
        upstreamPoint (-1.5 0 0);
        Cp 0.386;
        Ct 0.58;
    }
}
```

这些参数对应下载算例的教学设置，不是通用风机性能数据。本模型没有叶片几何、旋转诱导速度或完整湍流闭合验证。原资料截图仅说明预期的流场变化，不能作为迁移后定量正确性的证据。

修改几何后需要重新建立选择区域；旧版 `read()` 只更新部分成员，不会完整重建选择集合。因此本课要求改字典后重新启动算例，动态改盘位置需另行实现。
''','customActuationDiskSource.C','constant/fvOptions','统计选中单元数与总源项；保持盘面积和上游速度不变，改变盘厚及网格尺寸，检查总源项是否近似保持，而源区分布是否收敛。',130)

lesson(13,'编程 13｜波动方程、初始场与二阶时间导数','实现标量波动求解器，区分物理波速、数值传播误差和二阶时间问题所需的初始条件。',['setFields 初始峰','读取波速 C','历史时间层','fvm::d2dt2','隐式 Laplacian','传播与反射'],r'''
## 本课求的是标量波动方程

$$\frac{\partial^2h}{\partial t^2}=C^2\nabla^2h.$$

`h` 是演示幅值，`C` 是给定传播速度。这个模型没有气液界面重构、重力自由面或非线性水波色散，不能把所有呈现波形的结果都解释为 VOF 水波模拟。

```cpp
while (runTime.loop())
{
    fvScalarMatrix hEqn
    (
        fvm::d2dt2(h) == fvm::laplacian(sqr(C), h)
    );
    hEqn.solve();
    runTime.write();
}
```

`d2dt2` 是二阶时间导数算子，不代表其离散方案自动具有任意阶时间精度。实际格式从 `fvSchemes/d2dt2Schemes` 读取，求解器容差从 `fvSolution` 读取。

## 初始位移还不够

二阶时间方程需要初始幅值和初始变化率。`setFields` 只直接设置当前 `h` 的空间分布；历史时间层的初始化影响第一步采用的时间变化率。应明确检查所用离散格式的启动行为，不能从只有一个 `0/h` 文件就推断任意初始速度已被设定。

一种更便于显式控制两组初值的扩展，是引入 $v=\partial h/\partial t$，分别求解 $\partial h/\partial t=v$ 与 $\partial v/\partial t=C^2\nabla^2h$，并提供 `0/h` 与 `0/v`。这改变了时间积分结构，应独立做稳定性和误差验证。

## 时间步与波长分辨率

定义波传播 Courant 数 $Co_w=C\Delta t/\Delta x$。即使使用隐式格式，较大的 $Co_w$ 仍可能引入明显的相位误差与数值阻尼。稳定并不等于准确。空间上还要保证每个关注波长具有足够网格点。

观察脉冲传播时，先记录色标范围与时间，再测量波峰位置。将网格和时间步分别加密，比较到达同一测点的时间与峰值。不要对每帧自动缩放色标后再判断振幅是否守恒。

## 边界反射是模型的一部分

`zeroGradient` 与固定幅值边界会产生不同的反射条件，都不自动等价于无反射出口。本例适合认识传播与边界作用。若需要开放边界，应另行推导特征或吸收边界，并用一维解析波验证反射系数。
''','ofTutorial13.C','system/setFieldsDict','设置一个正弦模态，记录固定测点的周期并与理论值比较。分别减半时间步与网格间距，区分时间误差和空间误差。',110)

lesson(14,'编程 14｜SIMPLE 压力速度耦合的矩阵实现','解释 A、H、压力方程、欠松弛与速度修正，比较教学实现和标准求解器的通量处理。',['动量预测','取 A 与 H','构造压力方程','压力欠松弛','修正 U 和 phi','连续性检查'],r'''
## 为什么需要压力方程

不可压缩流动要求 $\nabla\cdot\mathbf U=0$，但压力没有独立的状态方程。将离散动量关系写成 $A\mathbf U=\mathbf H-\nabla p$，可得到

$$\mathbf U=\frac{\mathbf H}{A}-\frac{1}{A}\nabla p,\qquad
\nabla\cdot\left(\frac{1}{A}\nabla p\right)=\nabla\cdot\left(\frac{\mathbf H}{A}\right).$$

这里的 $A$ 是每个单元的对角系数场；`H()` 汇集非对角作用及源项，并不是完整稠密矩阵。`1/A` 因此是逐单元操作，不是在对整个稀疏矩阵求逆。

## 对照求解循环

```cpp
volScalarField A = UEqn.A();
volVectorField H = UEqn.H();
volScalarField rAU = 1.0/A;
volVectorField HbyA = rAU*H;
fvScalarMatrix pEqn
(
    fvm::laplacian(fvc::interpolate(rAU), p) == fvc::div(HbyA)
);
pEqn.setReference(pRefCell, pRefValue);
pEqn.solve();
```

参考压力消除某些边界组合下的压力零空间，不等于增加一个物理压差。若模型的压力边界已确定参考，应确认额外参考处理是否必要。

原例读 `fvSolution` 顶层的 `alpha`、`pRefCell` 和 `pRefValue`。它没有照搬标准 `simpleFoam` 的所有字典结构，因此把标准 SIMPLE 子字典直接复制进来可能不被这段代码读取。

## 欠松弛的作用

$$p^{k+1}\leftarrow\alpha p^{k+1}+(1-\alpha)p^k.$$

较小的 $\alpha$ 限制迭代更新幅度，可能提高鲁棒性，但也可能增加迭代次数。欠松弛不是物理时间推进；稳态求解器输出的 `Time` 在这里主要用于迭代计数。

## 为什么本例不能直接代替 simpleFoam

本例用于展示矩阵操作，省略了生产求解器中的多项处理：严格一致的压力通量修正、完整非正交循环、边界约束、残差控制和湍流模型等。代码把压力梯度直接放进动量矩阵构造后再读取 `H()`，分析时尤其应核对源项是否已包含压力贡献，不能仅凭变量名照抄标准推导。

标准求解器通常保留不含当前压力梯度的动量算子，通过 `solve(UEqn == -fvc::grad(p))` 做预测，再利用压力矩阵通量修正 `phi`。课程建议将两套源码并排阅读，用离散连续性误差检查差异，而不是仅凭速度云图相似就认定实现完全等价。

## 验证路径

从低 Reynolds 数平面通道开始，比较解析抛物线剖面、流量及压降。每轮记录残差和 $\sum_f\phi_f$ 的单元不平衡。速度看似稳定但连续性误差不降时，优先检查通量修正及边界处理。
''','OFtutorial14.C','system/fvSolution','在相同网格和物性下运行标准 simpleFoam，与教学例比较中心线速度、流量和连续性误差；说明单看线性残差为什么不足以证明 SIMPLE 外迭代收敛。',130)

lesson(15,'编程 15｜混合插值格式的实现与评估','根据 owner/neighbour 权重构造面插值，比较数值扩散、过冲、积分误差与网格敏感性。',['读取面通量','计算线性权重','计算上风权重','混合 0.8 / 0.2','运行时选择格式','比较剖面与范围'],r'''
## 面值如何来自相邻单元

对内部面，标量插值写为

$$T_f=w_fT_P+(1-w_f)T_N.$$

均匀正交网格上的线性插值取 $w_f=0.5$。上风插值根据 owner 到 neighbour 的通量符号取权重 1 或 0。本例组合两种权重：

$$w_f=(1-f_b)w_f^{\mathrm{linear}}+f_bw_f^{\mathrm{upwind}},\qquad f_b=0.2.$$

因此这里是 80% 线性与 20% 上风，不能把 0.2 解释为“80% 上风”。更重要的是，固定混合比例并不是基于局部解的通量限制器，不自动保证阶跃输运严格有界。

## 模板类与运行时选择

`myCustomScheme<Type>` 继承 `surfaceInterpolationScheme<Type>`，覆盖 `weights()`；`.C` 中 `makeSurfaceInterpolationScheme(myCustomScheme)` 注册相关类型。`Make/files` 的目标是共享库，不是一个新的可执行求解器；本例实际由 `scalarTransportFoam` 加载库后运行。

```foam
divSchemes
{
    default none;
    div(phi,T) Gauss myCustomScheme;
}
```

`controlDict/libs` 还要加载 `libofTutorial15.so`。仅在 `fvSchemes` 写新名称并不会触发源代码编译。

## tmp 与返回值的生命周期

`tmp<surfaceScalarField>` 用于临时场管理，减少不必要的深复制。引用或取值后要注意临时对象是否仍有效。教学代码为打印权重额外创建了几个实际场，便于观察，但不是性能最优实现。

原例固定打印内部面 `iFace=10`。把网格缩小到不足 11 个内部面时会越界；生产实现应检查索引或移除教学打印。并行情况下各子域的局部面数量也可能不足，因此本练习默认串行使用。

## 比较不能只看曲线是否平滑

上风通常更耗散，中心插值在强对流阶跃附近可能振荡。记录最小值、最大值、积分总量和界面厚度，并同时固定时间步、网格与求解容差。与解析平移解比较时，应对齐物理时间和采样位置。

资料中的 `refData` 是既有参考曲线，改变初值或时间后不再构成相同问题的对照。建议把新的参数、版本和采样时刻写到输出文件头，避免将不同算例画在同一张图后得出格式优劣结论。
''','OFtutorial15.H','system/fvSchemes','分别取 fBlend=0、0.2、1，比较阶跃输运的过冲和厚度；随后改变网格，检查结论是否仍成立。不要把一次无过冲当作普遍有界性证明。',110)

lesson(16,'编程 16｜在已知流场中追踪无质量粒子','实现位置更新、单元定位与 VTK 轨迹输出，理解路径积分的精度和适用范围。',['读取最新 U','定位粒子单元','获取局部速度','显式位置推进','判断离开计算域','写 VTK polyline'],r'''
## 先明确粒子模型

本例只追踪随已知速度场运动的质点：

$$\frac{\mathrm d\mathbf x_p}{\mathrm dt}=\mathbf U(\mathbf x_p).$$

它没有粒子惯性、重力沉降、阻力关联式、碰撞、扩散或对流体的反馈，适合认识轨迹积分，不是完整的离散相求解器。对稳态流场，路径线与流线几何一致；若速度随时间变化，仅冻结某一时刻的场不能得到真实非定常路径线。

## 当前实现怎样前进一步

```cpp
label celli = mesh.findCell(position);
vector velocity = U[celli];
scalar dt = Foam::cbrt(mesh.V()[celli])/mag(velocity);
position += velocity*dt;
```

示意代码省略了合法性检查，下载源包含零速度和最大步数防护。`findCell()` 找不到单元时返回 -1，在读取 `U[celli]` 以前必须检查。原例采用单元中心速度和显式 Euler 更新，时间精度是一阶，空间速度也未在粒子位置插值。

## 体积立方根不是通用网格尺度

$\Delta t=V_P^{1/3}/|\mathbf U|$ 在近各向同性三维单元中可作为粗略步长尺度；在薄层二维网格或高长宽比单元上，它与沿轨迹方向的距离可能相差很大。一步跨过很多单元时，局部速度假设和壁面穿越判断都不可靠。

改进方向是引入小于 1 的步长系数、在粒子位置插值速度、采用更高阶积分，并根据当前单元面交点做局部追踪。OpenFOAM 的拉格朗日框架提供更完整的数据与并行处理机制，不能把教学循环扩展到大量粒子后仍期待良好效率。

## 时间选择与结果文件

程序扫描时间目录并读取最后一个时间的 `U`。最新目录存在不保证其中有完整的求解结果，应检查 `U` 可读且与当前网格一致。脚本先运行 `simpleFoam`，再执行追踪，把轨迹写为 `VTK/particle_path.vtk` 的一条 polyline。

输出的总行程时间由各步 $\Delta t$ 累加。离域的最后一步可能越过边界，因此它是此粗积分的估计，不是精确的出口到达时间。定量停留时间应裁剪到边界交点并做步长收敛性检查。

## 怎样验证最小追踪器

先用均匀速度直线流动，检查轨迹方向与解析位置。再对抛物线通道流选不同起点，比较快慢区域的停留时间。分别将步长系数减半，记录轨迹和到达时间变化；比只看“曲线穿过通道”更有说服力。
''','OFtutorial16.C','system/controlDict','将初始位置和步长系数移到字典，比较 1、0.5、0.25 三个系数下的离域时间；增加出界前线段与边界交点处理。',100)

IMAGES={10:'2DconvectionDiffusion.png',11:'cellTypes.png',12:'Umagnitude.png',13:'waveElevation.png',14:'velocity_field.png',15:'tutorial15.png',16:'particlePath.png'}

def diagram(item):
    n=item['n']; stages=item['stages']
    # SVG diagrams are explanatory original vectors, not simulation output.
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(item["title"])}</title><desc id="desc">数据与程序执行关系示意图，不表示计算场。</desc>', '<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#2286bd" stroke-width="1.4"/></marker></defs><rect width="1200" height="470" rx="24" fill="#eef5fa"/>','<text x="50" y="58" font-family="Arial,sans-serif" font-size="17" fill="#37617d">OPENFOAM v2512 · PROGRAMMING</text>',f'<text x="50" y="102" font-family="Arial,Microsoft YaHei,sans-serif" font-size="28" font-weight="700" fill="#123552">{html.escape(item["title"].split("｜")[-1])}</text>']
    for i,label in enumerate(stages):
        x=50+(i%3)*382; y=150+(i//3)*143
        s.append(f'<rect x="{x}" y="{y}" width="334" height="94" rx="12" fill="white" stroke="#b4cee1"/><circle cx="{x+29}" cy="{y+30}" r="14" fill="#145a87"/><text x="{x+29}" y="{y+35}" text-anchor="middle" fill="white" font-size="13" font-family="Arial">{i+1:02}</text><text x="{x+22}" y="{y+70}" font-family="Arial,Microsoft YaHei,sans-serif" font-size="22" fill="#193f5e">{html.escape(label)}</text>')
        if i%3<2:s.append(f'<path d="M{x+340},{y+47} H{x+375}" stroke="#2286bd" stroke-width="2" fill="none" marker-end="url(#a)"/>')
    s.append('<path d="M1134,250 V267 H217 V287" fill="none" stroke="#2286bd" stroke-width="2" marker-end="url(#a)"/><text x="50" y="442" font-family="Arial,Microsoft YaHei,sans-serif" font-size="15" fill="#45647a">概念图 · 请结合源代码、输入字典与日志逐步核对</text></svg>')
    path=DIAG/f'programming-{n:02}.svg';path.write_text(''.join(s),encoding='utf-8');return '/assets/diagrams/'+path.name

def clean_code(path):
    s=path.read_text(encoding='utf-8',errors='replace')
    s=re.sub(r'/\*.*?\*/','',s,flags=re.S)
    s=re.sub(r'^\s*//.*$','',s,flags=re.M)
    s=re.sub(r'\n[ \t]*\n+', '\n\n',s).strip()
    return s

def build():
    roots=sorted(SRC.glob('OFtutorial*')); data=[]
    logdir=Path(r'F:\UbuntuShareFolder\.foamlab-build\programming')
    status={}
    for filename in ('packages-validation.log','retest-validation.log','final-validation.log','meshfinal-validation.log'):
        logp=logdir/filename
        if logp.exists():
            for name,kind,result in re.findall(r'^(OFtutorial\S+) (BUILD|RUN)_(PASS|FAIL)$',logp.read_text(errors='replace'),re.M):
                status[(name,kind)]=result
    for item in L:
        n=item['n']; root=roots[n];cover=diagram(item)
        imageblock=''
        if n in IMAGES:
            p=ORIG/root.name/'testCase'/IMAGES[n]
            if p.exists():
                target=DEST/f'programming-{n:02}-reference.png';shutil.copy2(p,target)
                imageblock=f'\n\n![原资料中的教学结果图](/assets/science/{target.name})\n\n图：BasicOFProgramming 随附教学结果图，保留用于解释现象；它不是本次 v2512 运行新生成的结果，不能单独用作版本验证。\n'
        verification='已逐项核对 README、源码、Make 文件及算例字典；尚未对本课完整流程做独立运行验证。'
        if status.get((root.name,'BUILD'))=='PASS':verification='已在 OpenCFD OpenFOAM v2512 中独立编译通过；运行状态以本页记录为准。'
        if status.get((root.name,'RUN'))=='PASS':
            verification='已在独立工作目录用 OpenCFD OpenFOAM v2512 编译并执行教学算例。'
            if n in (8,9,12,14,16):verification+='流动计算缩短至 20 次迭代，仅验证启动、接口及基本流程，不代表充分收敛或物理验证。'
            elif n==13:verification+='波动算例缩短至 0.1，仅检查启动和时间推进，不代表传播误差已收敛。'
            else:verification+='该记录是软件运行检查，不代替误差与物理验证。'
        if status.get((root.name,'BUILD'))=='FAIL':verification='已发现 v2512 编译问题，本课保留源码分析与迁移说明；下载包当前不能标注为已通过运行验证。'
        if status.get((root.name,'RUN'))=='FAIL':verification+='算例执行存在待核实问题，不能视为完整可运行验证。'
        if n==11:verification='已在 OpenCFD v2512 编译并生成 5 个单元的混合网格；checkMesh 完整检查仍有 1 项 underdeterminedCells 失败。本例为拓扑教学演示，不是合格生产网格。'
        newfig=logdir/'transport-beta-v2512.png'
        if n==10 and newfig.exists():
            target=DEST/'programming-10-v2512-result.png';shutil.copy2(newfig,target)
            imageblock='\n\n![本次 v2512 计算的稳态标量结果](/assets/science/programming-10-v2512-result.png)\n\n图：本次独立运行 `ofTutorial10` 后，由 foamToVTK 和 ParaView 6.1.1 导出的 `result` 单元场，标量无量纲。20×20×1 网格，单元值范围约 3.56275×10⁻⁵—0.999964，采用算例原始上风格式与扩散参数；图中方块来自单元数据，未以平滑外观代替网格加密。\n'+imageblock
        sourcepath=root/item['source']; code=clean_code(sourcepath)
        # Keep the main explanation readable; the complete source remains in the archive.
        lines=code.splitlines();snippet='\n'.join(lines[:75]);snippet+='\n// 完整实现与许可证见下载包。' if len(lines)>75 else ''
        cp=root/'testCase'/item['casefile'];case=clean_code(cp) if cp.exists() else ''
        body=f'''适用版本：**OpenCFD OpenFOAM v2512**。预计学习时间：{item['minutes']} 分钟。先修：能够运行一个基本算例，了解 C++ 变量、函数与引用；涉及类、模板或并行时先完成前置课程。

![本课数据与执行关系]({cover})

{item['body'].strip()}
{imageblock}
## 对照源码

下面摘取 `{item['source']}` 的前段实现，便于把正文概念与真实接口对应。代码来自下载包，删除部分注释后展示；完整声明、实现与原始版权头保留在包内。

```cpp
{snippet}
```

## 算例配置实例：{item['casefile']}

```foam
{case}
```

## 编译与复现实验

[下载本课精简源码与算例](/downloads/programming/{root.name}-v2512.zip) · [下载清单与 SHA-256](/downloads/programming/manifest.json)

```bash
# 先加载本机 OpenCFD v2512 环境，确认不是 Foundation 9。
echo "$WM_PROJECT_VERSION"
cd {root.name}
chmod u+x All* testCase/All*
bash Allwmake
cd testCase
bash Allrun
```

源码应放在用户可写目录中；无需以 root 编译。压缩包不含预编译程序、共享库、processor 目录和历史解，因此需要本机的 v2512 开发环境。按课程中的检查项阅读日志和字段，不以出现图片或生成时间目录作为唯一通过标准。

**本页核验记录：**{verification}

## 练习与验收

{item['exercise']}

提交时附环境版本、修改后的源码或字典、执行命令、关键日志和至少一项定量检查。出现错误时保留第一条编译或运行错误及上下文，末尾的 make error 通常只是上游失败的结果。

## 来源与延伸

本课依据用户提供的 **Basic OpenFOAM Programming Tutorials** 源码独立整理，原作者 Artur K. Lidtke（2017–2021）及项目贡献者；其中 13、14、16 的贡献者包括 Ramkumar。源代码按 **GPL-3.0-or-later** 分发，原版权头与 LICENSE 保留。网站中文讲解和概念图用于解释当前文件的行为；不将旧注释或旧截图作为 v2512 兼容性的充分证据。

下一步：[编程 {min(n+1,16):02}](/read/?slug=programming-{min(n+1,16):02}) · [精简源码与迁移说明](/read/?slug=resource-basic-programming)
'''
        data.append(dict(slug=f'programming-{n:02}',kind='lesson',title=item['title'],summary=item['summary'],body=body,track='OpenFOAM 编程',series='BasicOFProgramming',sort_order=200+n,status='published',cover_url=cover,metadata=dict(source=f'BasicOFProgramming/{root.name}',license='GPL-3.0-or-later for source code; original attribution retained',verification=verification,prerequisite=f'programming-{n-1:02}' if n else 'OpenFOAM 基本算例与 C++ 入门',duration=f"{item['minutes']} 分钟",download=f'/downloads/programming/{root.name}-v2512.zip')))
    (OUT/'programming-content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(lessons=len(data),characters=sum(len(x['body']) for x in data),verified=[x['slug'] for x in data if '编译并执行' in x['metadata']['verification']]),ensure_ascii=False))
    return data

if __name__=='__main__':build()
