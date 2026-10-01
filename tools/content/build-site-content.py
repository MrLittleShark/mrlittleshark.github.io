from pathlib import Path
import json,shutil,zipfile
from urllib.parse import urlencode
R=Path(__file__).resolve().parents[2];S=R/'source-openfoam';work=Path(r'F:\UbuntuShareFolder\.foamlab-build')
rows=[]
def add(slug,kind,title,summary,body,track='站点与实践',order=0,**extra):
 rows.append(dict(slug=slug,kind=kind,title=title,summary=summary,body=body,track=track,series='FoamLab',author_name='FoamLab',status='published',sort_order=order,comments_enabled=True,cover_url='/assets/science/cavity-velocity.png',metadata=extra))
add('sources-and-validation','resource','资料来源、版本与核验说明','区分官方源码、Wolf 培训材料、适配示例和本站计算结果；说明每一种验证记录可以支持的结论。',r'''## 本站的软件基准

本站使用 **OpenCFD OpenFOAM v2512**。OpenFOAM Foundation 9 与 v2512 来自不同发行分支，版本数字不能直接比较大小。教程迁移必须检查应用名称、库接口、字典格式和模型实现。

![从资料到可复现结果](/assets/science/cavity-mesh.png)

上图是本站在 v2512 下生成的方腔网格，20 × 20 × 1 个单元。图片由 ParaView 读取实际 OpenFOAM 输出获得。

## 主要资料及其用途

| 资料 | 本站用途 | 使用边界 |
| --- | --- | --- |
| [OpenCFD v2512 发布与源码](https://www.openfoam.com/news/main-news/openfoam-v2512) | 软件版本、命令目标、配置实例与源码路径 | 固定 v2512 tag；不把第三方扩展混入核心安装承诺 |
| [Wolf Dynamics OpenFOAM 培训](https://www.wolfdynamics.com/tutorials.html?id=181&layout=edit) | 教学顺序、有限体积方法、算例与编程思路 | 原培训主要基于 Foundation 9，本站重写并核对 v2512 |
| BasicOFProgramming 本地资料 | 17 个 C++ / OpenFOAM 编程单元 | 逐例检查，兼容修订仅作用于本站下载副本 |
| OF_material 本地资料 | v2512 配置与算例资源 | 迁移报告的短时运行不能代替长期计算验证 |
| 本站示意图与真实计算图 | 解释网格、算法、接口与结果 | 各图明确说明示意、资料图或实际计算 |

Wolf 基础培训页面及基础幻灯片标注 CC BY-SA 4.0。本站提供重新组织的中文说明，并保留来源；源码示例遵守其原许可证。高级资料中的版权声明不同，不将所有本地 PDF 无差别重新公开分发。BasicOFProgramming 下载包包含原许可证与迁移说明。

## 命令清单如何建立

从 v2512 的 `applications/solvers` 与 `applications/utilities` 下 `Make/files` 提取 278 个编译目标，并单独列出 `applications/tools` 中的辅助程序。官方脚本、shell 函数、构建辅助与 Linux 配套工具分别标识。每一条详情给出源码位置或实际帮助信息；程序未安装时明确标注。

源码清单可以说明“这个目标在该版本源码中存在”，`-help-full` 成功可以说明“本机程序能够启动并显示帮助”。这两种证据都不能证明特定物理算例已经通过验证。

## 真实方腔计算的范围

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
echo "$WM_PROJECT_VERSION"
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
icoFoam > log.icoFoam 2>&1
```

本次从官方 `incompressible/icoFoam/cavity/cavity` 复制，在独立目录运行，终止时间为 0.5 s。计算图保留原始单元分辨率；没有把插值平滑当成更精细的计算。

\[
\mathrm{Re}=\frac{U L}{\nu}
\]

本例 \(U=1\,\mathrm{m/s}\)、\(L=0.1\,\mathrm{m}\)、\(\nu=0.01\,\mathrm{m^2/s}\)，因此 \(\mathrm{Re}=10\)。不要把其他教程中的 Re=100 或 Re=1000 直接写到这个算例上。单次运行还未完成网格独立性、时间步敏感性或与基准数据的定量对照。

## 图像与引用规范

1. **真实计算图：**给出求解器、版本、网格、时刻和物理量单位。
2. **方法示意图：**解释结构与关系，不表示真实网格质量或计算精度。
3. **原资料图：**保留资料归属，不将其描述为本站新运行的结果。
4. **封面：**AI 生成的 CFD 主题插图，用于视觉识别，不代表经过验证的流场。

如果发现分支差异或示例错误，欢迎在评论区或讨论中心附上版本、最小复现和实际日志。''',verification='资料归属、核心源码清单和本站方腔运行记录已核对；不同证据的适用范围分别说明。')
add('release-2026-10-rebuild','announcement','学习站重构：课程、参考与社区统一入口','新版课程采用稳定内容编号，管理平台支持课程、资料、文章、评论与讨论的独立维护。',r'''## 本次调整

- 重新组织环境、网格、数值方法、模型与后处理课程，编程专题采用 17 个分步实例。
- 将命令清单与 v2512 源码对照，提供完整帮助、官方配置实例与版本标记。
- 开启站内讨论与文章评论。所有人可以阅读，GitHub 登录用户可以提问和回答。
- 增加作者工作台、作者日志、工具生态与资料目录。
- 管理平台支持建立、修改、发布、归档、删除、恢复内容，上传文件和管理社区。

## 学习记录

旧版 28 讲与新版单元不一一对应，因此旧完成记录没有自动折算成新版完成情况。历史记录保留在原数据库表；新版课程使用内容 ID 跨设备同步。

## 内容范围

电极气泡专题暂不纳入当前课程。先建立通用 CFD 与 OpenFOAM 的基础、编程能力和数值验证方法，后续专题再单独规划。

开始学习时，可先阅读[版本与环境](/read/?slug=start-openfoam-v2512)、[第一个方腔算例](/read/?slug=first-cavity-result)，再按目录进入专题。''',order=-100)
for i,(slug,title,body) in enumerate([
 ('practice-cavity','实践 01：重现方腔流动并提交证据',r'''## 任务与前置知识

阅读[方腔课程](/read/?slug=first-cavity-result)。从 v2512 官方教程复制独立工作目录，完成网格生成、检查、求解和后处理。

![方腔速度场](/assets/science/cavity-velocity.png)

## 需要提交的内容

1. `echo "$WM_PROJECT_VERSION"`、`icoFoam -help` 的输出摘要。
2. `system/blockMeshDict`、`controlDict`、`fvSchemes`、`fvSolution` 与 `constant/transportProperties`。
3. `checkMesh` 检查结论、求解结束日志，以及速度模云图。
4. 根据实际长度、顶盖速度和运动黏度计算雷诺数，并解释采用的单位。
5. 说明本次计算可以支持的结论，以及尚未进行的敏感性检查。

## 验收要点

- 能从提交文件复现设置，而不只是看到一张图片。
- 速度场的单位、时刻和网格数量清楚。
- 网格检查与求解日志没有被截图裁掉关键失败信息。
- 不以残差下降一项代替所有验证。

建议命名 `cavity-v2512-yourname.zip`，保留 `0/`、`constant/`、`system/` 与关键日志；不要上传全部临时时间目录。'''),
 ('practice-mesh','实践 02：网格与时间步的敏感性对比',r'''## 任务

在完成基础方腔算例后建立三个独立副本，使用 20 × 20 × 1、40 × 40 × 1、80 × 80 × 1 网格。保持物理尺寸、边界条件和黏度一致。

![网格结构](/assets/science/cavity-mesh.png)

## 对比方法

先选择一个共同的物理时刻，在同一中心线上采样速度。网格加密后还需检查 Courant 数；不要把空间误差与过大的时间步误差混在一起。

\[
\mathrm{Co}\approx\frac{U\Delta t}{\Delta x}
\]

式子用于均匀一维网格的数量级估计，实际多维有限体积 Co 以求解器定义与日志为准。

## 提交

给出各网格的单元数、时间步、最大 Co、结束时刻、运行时间与中心线速度曲线。所有曲线用相同坐标轴与单位。选择一个积分量或测点值，报告两次加密之间的相对变化。

## 验收

必须解释为何可以比较这些数据；不能仅凭三张“看起来差不多”的云图宣称网格独立。若计算成本不允许完成 80 × 80，报告实际完成范围和瓶颈，不补造结果。'''),
 ('practice-programming','实践 03：编译并检查自定义边界条件',r'''## 前置课程

先完成[编译与库](/read/?slug=programming-07)以及[自定义边界条件](/read/?slug=programming-08)。使用编程资料包中针对 v2512 修订的副本。

## 任务

编译边界条件库，说明 `Make/files`、`Make/options` 与 `controlDict` 中 `libs` 各自承担什么作用。运行测试算例，检查入口抛物线速度分布。

\[
u(r)=u_{\max}\left[1-\left(\frac{r}{R}\right)^2\right]
\]

解释峰值速度与截面平均速度的区别。对于圆截面轴对称抛物线，\(\bar u=u_{\max}/2\)；不要把这个关系直接移植到所有平面通道或任意离散截面。

## 提交

上传修改后的 `.H`、`.C`、`Make/`、边界字典、编译日志和入口采样数据。写出每个可配置参数的类型、单位、默认值与不合法输入的处理方式。

## 验收

边界必须真实参与算例；单独编译成功不能证明入口条件正确。比较理论剖面与实际采样，报告几何离散、法向方向和归一化方式。''')]):
 link='https://github.com/MrLittleShark/MrLittleShark.github.io/issues/new?'+urlencode({'title':'[作业提交] '+title,'body':'对应作业：https://mrlittleshark.github.io/read/?slug='+slug+'\n\n## 版本与运行命令\n\n## 配置与附件\n\n## 结果与检查\n\n## 问题与反思\n'})
 add(slug,'assignment',title,'提交最小配置、计算结果与检查依据；支持 GitHub 公开提交和站内评论反馈。',body+'\n\n## 提交与反馈\n\n[使用 GitHub 提交此作业]('+link+')。附件可拖到 GitHub 提交框中。提交后将链接粘贴到下方评论区，便于讨论。\n\n这是自主实践作业，暂不设截止日期。\n',track='实践作业',order=i)
add('resource-cavity-evidence','resource','方腔 v2512：真实运行记录与绘图脚本','获取本次 blockMesh、checkMesh、icoFoam 日志与 ParaView 绘图脚本，按相同设置重现图片。',r'''## 下载

[下载运行记录与绘图脚本](/downloads/cavity-v2512-evidence.zip)

![实际方腔速度场](/assets/science/cavity-velocity.png)

压缩包包含网格检查、求解日志、绘图脚本和复现说明。标准算例来自 v2512 自带教程；绘图脚本采用 ParaView 6.1.1。在其他版本的 ParaView 中，颜色预设与属性名称可能不同。

## 复现

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
mkdir -p "$HOME/OpenFOAM-reproduce"
cd "$HOME/OpenFOAM-reproduce"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity
cd cavity
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
icoFoam > log.icoFoam 2>&1
touch cavity.foam
```

在 ParaView 打开 `cavity.foam`，选择内部网格与 `U`、`p`，切换到最后时刻并显示速度模。脚本参数使用你自己的算例目录和输出目录。

## 核验范围

实际执行网格生成、检查和求解至 0.5 s，成功读取最终场并出图。没有将这一次运行称为网格独立性验证。''',track='可复现实例',verification='v2512实际运行；日志与出图保留。')
download=S/'downloads';download.mkdir(exist_ok=True)
with zipfile.ZipFile(download/'cavity-v2512-evidence.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in work.glob('log.*'):
  z.write(p,p.name)
 script=(work/'render-cavity.py').read_text(encoding='utf-8').replace("root='/home/shark/foamlab-website-20261002/cavity'","import sys\nroot=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else 'cavity')").replace("output='/mnt/hgfs/UbuntuShareFolder/.foamlab-build'","output=os.path.abspath(sys.argv[2] if len(sys.argv)>2 else '.')")
 z.writestr('render-cavity.py',script)
 z.writestr('README.txt','OpenFOAM OpenCFD v2512 cavity; icoFoam; 20x20x1; t=0.5 s; Re=10.\nReproduce from $FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity.\nUse: pvpython --force-offscreen-rendering render-cavity.py /path/to/cavity /path/to/output\nRun logs demonstrate execution, not mesh independence.\n')
(R/'tools/content/site-content.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Site content:',len(rows))
