from pathlib import Path
import os,re,json,zipfile,hashlib,shutil
ROOT=Path(r'E:\Hexo'); SRC=Path(r'F:\UbuntuShareFolder\OF_material')
OUT=ROOT/'source-openfoam/downloads/programming';OUT.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'tools/content'
catalog=[]
def skip(name):
    return name.startswith(('.', 'processor', 'linux64')) or name in ('postProcessing','VTK','dynamicCode','polyMesh','lnInclude') or '_backup_' in name or bool(re.fullmatch(r'\d+(?:\.\d+)?',name))
for base,dirs,files in os.walk(SRC):
    dirs[:]=[d for d in dirs if not skip(d)]
    p=Path(base)
    if p.name=='system' and 'controlDict' in files:
        text=(p/'controlDict').read_text(errors='replace');text=re.sub(r'/\*.*?\*/','',text,flags=re.S);text=re.sub(r'//[^\n]*','',text)
        app=re.search(r'\bapplication\s+([^;]+);',text)
        catalog.append(dict(path=p.parent.relative_to(SRC).as_posix(),application=app[1].strip() if app else '未直接声明',verification='目录与controlDict静态清点；不是独立运行认证'))
catalog.sort(key=lambda x:x['path'])
(OUT/'of-material-case-catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(SRC/'V2512_MIGRATION_REPORT.md',OUT/'OF_material-V2512_MIGRATION_REPORT.md')
for folder,name in [('101programming','of-material-programming-migration.md'),('101OF_extended','of-material-extended-migration.md'),('101OF/cavity2D','of-material-cavity-migration.md')]:
    shutil.copy2(SRC/folder/'README.v2512.md',OUT/name)

selected=['101OF/cavity2D','101programming/codeStream_INIT/cylinder','101programming/codeStream_INIT/elliptical_IC','101programming/codeStream_INIT/rayleigh_taylor','101programming/codeStream_BC/2Delbow_UparabolicInlet','101programming/my_solvers/my_laplace/my_laplace_v1','101programming/my_solvers/my_laplace/my_laplace_v2','101programming/my_solvers/my_laplace/my_laplace_v3']
files=[]
for folder in selected:
    for base,dirs,names in os.walk(SRC/folder):
        dirs[:]=[d for d in dirs if not skip(d) or d=='0']
        for name in names:
            f=Path(base)/name;rel=f.relative_to(SRC)
            if name.startswith(('log','core')) or f.suffix.lower() in ('.png','.mp4','.vtk','.vtp','.vtu','.o','.dep','.so','.foam','.openfoam','.pdf'):continue
            if f.stat().st_size>8_000_000:continue
            files.append((f,rel.as_posix()))
mesh=SRC/'meshes_and_geometries/fluent_elbow2d_1/ascii.msh';files.append((mesh,mesh.relative_to(SRC).as_posix()))
readme='''# OF_material v2512 selected source cases

Source: the user's OF_material collection, adapted from Wolf Dynamics OpenFOAM training examples.
The archive includes selected initialisation / boundary / Laplace / cavity examples and the small external Fluent mesh required by the elbow case. Original file headers and attribution are retained.

The parent directory hierarchy is intentional: the elbow run script uses ../../../meshes_and_geometries. Keep it when extracting.
Compiled binaries, solution time directories, postProcessing, processor directories and generated polyMesh files are excluded. Run scripts may clean old results: work on a disposable copy and read the scripts first.

Version: OpenCFD OpenFOAM v2512. The original project notes report migration checks; this web distribution does not represent a new full-duration validation of every selected case. See the enclosed migration reports and the website's precise scope statement. Source compatibility and physical validation are distinct.

The original basic training materials are attributed to Wolf Dynamics; their slides identify CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/). Individual C++ files retain their original GPL notices and apply GPL-3.0-or-later where specified; a GPL licence copy is included. The distribution does not relicense third-party code. FoamLab's additions consist of the source-only packaging, index and explanatory documentation.

Typical use: load /usr/lib/openfoam/openfoam2512/etc/bashrc (adjust to local installation), enter a selected case, inspect run_solver.sh, then execute bash run_solver.sh. Custom Laplace applications must first be built with wmake from their application directories. Some examples use four MPI ranks and gnuplot.
'''
zpath=OUT/'OF_material-v2512-selected-examples.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
    for f,rel in sorted(files,key=lambda x:x[1]):
        info=zipfile.ZipInfo('OF_material/'+rel);info.external_attr=(0o100755 if f.suffix=='.sh' or f.name.startswith('All') else 0o100644)<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,f.read_bytes())
    z.writestr('OF_material/FOAMLAB-README.md',readme)
    z.write(SRC/'V2512_MIGRATION_REPORT.md','OF_material/V2512_MIGRATION_REPORT.md')
    z.write(SRC/'101programming/README.v2512.md','OF_material/101programming/README.v2512.md')
    z.write(Path(r'F:\UbuntuShareFolder\BasicOFProgramming\LICENSE'),'OF_material/LICENSE-GPL-3.0.txt')
summary=dict(files=len(files),bytes=zpath.stat().st_size,sha256=hashlib.sha256(zpath.read_bytes()).hexdigest(),selected=selected,scope='source-only; migration reports are historical supplied evidence')
(OUT/'OF_material-selected-manifest.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'OF_material-selected-README.md').write_text(readme,encoding='utf-8')

resources=[]
def add(slug,title,brief,body,cover='/assets/diagrams/programming-00.svg',download=None):
    resources.append(dict(slug=slug,kind='resource',title=title,summary=brief,body=body,track='源码与算例',series='v2512 资料库',sort_order=300+len(resources),status='published',cover_url=cover,metadata=dict(source='用户提供的 BasicOFProgramming / OF_material',verification='来源和核验范围见正文；目录清点不等同于运行验证',download=download)))

rows=[]
for n,p in enumerate(sorted(Path(r'F:\UbuntuShareFolder\BasicOFProgramming').glob('OFtutorial*'))):rows.append(f'| {n:02} | [{p.name.split("_",1)[1]}](/read/?slug=programming-{n:02}) | [精简源码](/downloads/programming/{p.name}-v2512.zip) |')
add('resource-basic-programming','BasicOFProgramming：17 个编程实验与可复现源码','按应用、数据结构、扩展库、边界条件、方程和算法组织 17 个 C++ 实验，附逐例源码包和真实 v2512 核验范围。',r'''
![应用程序的构建链](/assets/diagrams/programming-00.svg)

这组材料适合已经能运行基本算例、准备阅读或修改 OpenFOAM 源码的学习者。前 8 课建立程序、字典、场、并行和类库的基础；08—12 进入边界条件、函数对象、输运方程、网格与源项；13—16 讨论时间推进、SIMPLE、离散格式和轨迹积分。

## 使用方法

每课包含概念图、中文解释、当前源码片段、实际算例字典、编译命令及验收任务。先在未修改的副本中重现基本流程，再一次只修改一个参数或一段代码。提交结果时同时记录环境版本、日志与定量检查，图片应标注字段、单位和时刻。

| 编号 | 课程 | 下载 |
| --- | --- | --- |
'''+ '\n'.join(rows)+r'''

## 为何需要单独核验“已适配”

原资料总说明标注 v2512，但逐例编译发现部分文件仍包含另一 OpenFOAM 分支的接口。本站在独立副本中修复了处理器 patch 头文件、边界字段写出、日志文件接口、网格点移动接口、动量源基类和采样类型，并保存编译与运行证据。原资料目录保持不变。

| 实验 | 原始内容或实际问题 | 网站下载副本的修订 |
| --- | --- | --- |
| 05 并行 | processorPolyPatch 未显式声明 | 加入对应头文件，四进程运行通过 |
| 08 边界 | writeEntry(os, "value", *this) 与 v2512 不匹配 | 使用 writeEntry("value", os)，编译、短运行与后处理通过 |
| 09 函数对象 | 旧 logFiles::file(index) 接口 | 改为 files(index)，显式写文件头 |
| 11 网格 | clone(points) 不匹配；三维外表面被设为 empty | 使用 pointField(points) 与 patch；仍有 1 项 underdeterminedCells 检查失败，明确作为拓扑演示 |
| 12 动量源 | 仍继承 Foundation fvModel 并读 fvModels | 迁移至 OpenCFD fv::option/fvOptions，修改构造、字段注册及 addSup 签名 |
| 15 插值格式 | lineCell 采样类型已不可用 | 使用 v2512 cellCentre，执行至原设定结束时刻 |

共 17 个目标在本机 v2512 编译通过。执行脚本结束不是所有网格都合格的证明：第 11 课的质量检查失败保留在报告与正文中，没有以退出码 0 覆盖这一事实。

源码包保留 GPL-3.0-or-later 许可证和原作者信息，不提供跨版本预编译 `.so`。不同 OpenFOAM 分支、编译器和精度配置之间应从源码重新编译。

## 核验的边界

每课的核验记录区分编译、启动与运行。部分流动例缩短到 20 次迭代，波动例缩短到 0.1；这些检查不能证明生产时长内稳定，也不能证明网格无关或物理模型正确。资料中的旧截图与本次计算图使用不同图注。

[下载清单与 SHA-256](/downloads/programming/manifest.json) · [核验与迁移记录](/downloads/programming/VERIFICATION.md)
''',download='/downloads/programming/manifest.json')

add('resource-of-material-migration','OF_material：v2512 迁移范围与验证分级','把语法检查、网格检查、启动检查和长时间模拟区分开，准确理解已有迁移报告的证据。',r'''
![从输入到计算的验证链](/assets/diagrams/programming-10.svg)

`OF_material` 是已做 v2512 适配的课程代码与算例集合。使用它可以减少从 Foundation 9 直接复制旧字典带来的接口差异，但仍应针对具体求解器和物理模型检查设置。一个目录的报告不应扩展解释成整个资料库均已完成相同级别的验证。

## 2026-09-04 总迁移报告实际记录了什么

| 层级 | 报告中的证据 | 能说明什么 |
| --- | --- | --- |
| 字典解析 | 49 个主 controlDict 成功解析 | 这些字典的基本读取通过 |
| Shell 语法 | 149 个目标脚本通过 bash -n | Shell 语法成立，不代表外部命令执行成功 |
| 基础网格 | 37 个 blockMesh 算例完成生成和 checkMesh | 已检查这些网格的生成与质量诊断 |
| 表面特征 | 18 份配置通过 surfaceFeatureExtract | 对应输入表面与特征提取接口已执行 |
| SHM 配置 | 26 份配置通过 snappyHexMesh -dry-run | 配置检查通过，不等于完整层网格生成通过 |
| 求解启动 | 22 个代表算例初始化并完成至少一步或一次迭代 | 基本求解链可启动，不代表充分收敛和长时间稳定 |

报告明确指出没有开展长生产时长计算。它覆盖列出的 `101postprocessing`、`advanced_physics`、`advanced_postprocessing`、`advanced_SHM` 和 `101SHM_basic` 等迁移目标，另有 `101programming` 与 `101OF_extended` 的独立说明。

## 主要版本差异

迁移涉及 `fvModels/fvConstraints` 与 `fvOptions` 的分支差异、湍流配置、函数对象与采样关键字、特征提取工具、网格字典以及无图形环境绘图。不能把所有 `momentumTransport` 机械替换成 `turbulenceProperties`，应先查所选 v2512 求解器实际读取的模型接口。

程序编译成功和算例读取成功是不同证据。尤其对于自定义边界条件，应进一步检查运行时类型注册、构造、并行映射和重启写出。

## 下载原始记录

- [总迁移报告](/downloads/programming/OF_material-V2512_MIGRATION_REPORT.md)
- [101programming 的迁移说明](/downloads/programming/of-material-programming-migration.md)：报告称 143 个构建目标通过，本站按原报告表述，未将其改写为本次重新编译的结果。
- [101OF_extended 的迁移说明](/downloads/programming/of-material-extended-migration.md)
- [cavity2D 的计算与采样说明](/downloads/programming/of-material-cavity-migration.md)：独立记录了运行至 t=50 和统计比较，应与总报告的短启动检查区分。

新增算例推荐记录四类信息：源码或字典版本、实际执行命令与退出状态、网格及守恒诊断、与解析或基准数据的差异。不要用一个“已验证”标签代替这些具体证据。
''',cover='/assets/diagrams/programming-10.svg',download='/downloads/programming/OF_material-V2512_MIGRATION_REPORT.md')

groups={}
for x in catalog:groups[x['path'].split('/')[0]]=groups.get(x['path'].split('/')[0],0)+1
table='\n'.join(f'| `{k}` | {v} |' for k,v in sorted(groups.items()))
add('resource-of-material-catalog','OF_material 导航：按学习任务选择源码与算例','从基础算例、网格、编程到后处理定位材料；目录条目提供可检索清单与版本检查建议。',f'''
![编程模块的数据关系](/assets/diagrams/programming-07.svg)

本页按照资料目录中实际出现的 `system/controlDict` 清点算例入口。已排除显式备份目录、处理器子域与结果时间目录。同一物理问题的不同参数版本仍可能是不同入口，因此条目数不能解释为独立物理模型数量或全部已验证算例数。

| 资料目录 | 找到的 controlDict 入口 |
| --- | ---: |
{table}

## 按目标选择材料

- **初次运行与后处理**：先看 `101OF/cavity2D`，理解网格、初值、时间控制、中心线采样与基准比较。
- **改变网格拓扑**：进入 `101BLOCKMESH`、`101SHM_basic`，分别学习结构化块网格和表面驱动网格；先运行网格检查，再运行求解器。
- **初始化与边界编程**：看 `101programming/codeStream_INIT`、`codeStream_BC`；它们把小段 C++ 嵌入字典，适合理解字段构造。
- **修改方程**：看 `101programming/my_solvers`，从 Laplace、对流扩散到 icoFoam 的修改逐步增加复杂度。
- **统计与批处理**：看 `101postprocessing`、`advanced_postprocessing`，留意采样文件名、列号和函数对象的版本变化。
- **复杂物理与网格**：`advanced_physics`、`advanced_SHM` 包含更高成本的算例。按对应报告核对短启动、完整网格及长时间求解分别是否执行过。

[下载完整目录清单 JSON](/downloads/programming/of-material-case-catalog.json)。清单记录入口路径和 controlDict 中的 application，仅作导航，不替代逐例运行说明。

## 源码阅读次序

先读脚本确定命令链，再读 `controlDict` 确定实际应用程序，然后看 `0/`、`constant/`、`fvSchemes` 和 `fvSolution`。自定义求解器进一步检查 `Make/files` 的目标名称及 `createFields.H`。若脚本导入外部网格，应保留相对目录结构和输入网格文件。

本网站提供下列精选源包；其他大体积结果与生产网格不重复放入 GitHub Pages 静态站点。

[下载精选源码与算例](/downloads/programming/OF_material-v2512-selected-examples.zip) · [包内目录、校验值与范围](/downloads/programming/OF_material-selected-manifest.json)
''',cover='/assets/diagrams/programming-07.svg',download='/downloads/programming/of-material-case-catalog.json')

add('resource-coded-initialization','初始条件编程：用 codeStream 构造椭圆标量场','将几何判据写成单元场，解释动态编译、初值体积误差与版本接口，并提供实际算例源码。',r'''
![从初值到时间推进](/assets/diagrams/programming-13.svg)

复杂初值不一定需要开发独立求解器。`OF_material/101programming/codeStream_INIT/elliptical_IC` 在 `internalField` 中使用 `#codeStream`，读取网格中心后生成标量列表。这一机制在字典读取期间编译并执行代码，与时间循环中反复更新的边界条件不同。

## 从几何定义到单元判断

椭圆内域满足

$$\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}\leq1.$$

原例取中心 `(0.5,0.5)`、半轴 `0.3` 与 `0.15`。对每个单元中心计算该判据，内部赋 1，外部赋 0。示意实现为：

```cpp
scalarField alpha(mesh.nCells(), 0);
forAll(alpha, celli)
{
    const vector& c = mesh.C()[celli];
    scalar q = sqr((c.x()-0.5)/0.3) + sqr((c.y()-0.5)/0.15);
    alpha[celli] = q <= 1 ? 1 : 0;
}
alpha.writeEntry("", os);
```

这里的 `writeEntry("", os)` 将结果作为当前字典条目的值输出，不是在磁盘上创建另一份独立场文件。原例的 `codeInclude` 提供头文件，`codeOptions` 提供编译包含目录，`codeLibs` 提供链接库，三者分别对应编译依赖中的不同阶段。

## 为什么初始化仍然有离散误差

单元中心判据把每个单元整体设为 0 或 1，不等于精确计算椭圆与单元的交叠体积分数。因此边界呈现阶梯形，积分 $\sum_P\alpha_PV_P$ 与几何体积存在网格误差。加密网格后比较积分与 $\pi ab$ 乘实际厚度，才能定量评估初值表示。

若需要平滑过渡，可令 $\alpha$ 随带符号距离平滑变化，但这会改变初始界面厚度和体积，需要重新归一化或评估。不能把平滑图像直接等同于更准确的几何体积分数。

## v2512 使用注意

检查相名称与场名称是否一致。该材料保留部分旧文件头，例如文件名为 `alpha.phase1` 而头中的 `object` 仍可能写 `alpha.water`；运行前应与 `transportProperties` 中 phases、求解器读取字段及边界名称交叉核对，而不是只改一个文件名。

动态代码需要可写的编译目录和完整开发环境。应只执行可信算例中的 C++；这类条目是程序代码，不是纯数值配置。原资料脚本会恢复 `0_org` 并清理旧结果，因此使用独立副本。

## 三种初始化方法怎样选择

| 方法 | 合适情形 | 主要检查 |
| --- | --- | --- |
| uniform / nonuniform | 直接给定场值 | 列表长度、量纲和 patch |
| setFields | 基于已有几何选择规则赋值 | 区域覆盖顺序及字段名 |
| codeStream | 自定义解析几何或空间函数 | 编译接口、网格引用和输出类型 |

[下载含 cylinder、elliptical_IC、rayleigh_taylor 的精选源包](/downloads/programming/OF_material-v2512-selected-examples.zip)。本页依据 v2512 适配材料解释代码，目录内历史迁移报告与本次逐例编译证据应分别阅读。
''',cover='/assets/diagrams/programming-13.svg',download='/downloads/programming/OF_material-v2512-selected-examples.zip')

add('resource-wolf-programming-pack','Wolf 编程精选：Laplace 求解器、初值与入口条件','一个保留目录依赖的精简源码包，连接 Wolf 的代码示例与本站编程课程。',r'''
![求解器的构成](/assets/diagrams/programming-10.svg)

此包来自用户提供的 v2512 适配目录，保留 8 个教学入口及弯管例所需的小型 Fluent 输入网格，移除生成网格、历史解、并行分区、编译对象和可视化结果。它用于逐步理解代码与字典，不是完整 OF_material 镜像。

## 包含哪些示例

| 入口 | 适合研究的问题 |
| --- | --- |
| cavity2D | 标准求解、统计、中心线采样和 Ghia 对照 |
| codeStream_INIT/cylinder | 几何区域与初值列表 |
| codeStream_INIT/elliptical_IC | 椭圆判据和体积离散误差 |
| codeStream_INIT/rayleigh_taylor | 扰动界面初值的构造 |
| codeStream_BC/2Delbow_UparabolicInlet | 入口剖面和动态代码 |
| my_laplace_v1、v2、v3 | 自定义方程、字段创建和控制循环的递进 |

## 运行前检查

解压后保留 `OF_material/101programming` 与 `OF_material/meshes_and_geometries` 的相对关系，弯管脚本通过相对路径导入网格。先阅读 `run_solver.sh`：有些例采用四个 MPI 进程，有些脚本会清理已有结果。首次实验复制到独立目录，保留源包作为基线。

Laplace 应用在对应源码目录执行 `wmake`，再进入 `test_case` 运行脚本。应用目标名由 `Make/files` 决定，不能假设源码目录名就是 PATH 中的可执行名。

## 怎么把它用于课程

先完成[标量输运求解器](/read/?slug=programming-10)，再比较 Laplace 例去掉对流项后剩余的矩阵与字典。接着完成[初值 codeStream](/read/?slug=resource-coded-initialization)和[自定义入口边界](/read/?slug=programming-08)，比较“读取时生成一个场”和“边界更新时计算面值”的区别。

包内迁移说明是原资料的历史记录。本站没有将全包每个案例重新跑到生产时长，用户应按任务选择网格、时间步和守恒诊断。课程资料图的来源与版本应写入图注。

[下载精选源包](/downloads/programming/OF_material-v2512-selected-examples.zip) · [下载说明](/downloads/programming/OF_material-selected-README.md) · [SHA-256 与包范围](/downloads/programming/OF_material-selected-manifest.json)

来源：Wolf Dynamics 基础培训与用户提供的 v2512 适配代码。原文件版权与许可声明保留；基础课件标注 CC BY-SA 4.0，包含 GPL 声明的 C++ 文件沿用其原许可。此包不包含高级培训的整本课件，也不将第三方材料重新声明为本站原创。
''',cover='/assets/diagrams/programming-10.svg',download='/downloads/programming/OF_material-v2512-selected-examples.zip')

(DATA/'programming-resources-content.json').write_text(json.dumps(resources,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(resources=len(resources),catalog_entries=len(catalog),package=summary),ensure_ascii=False))
