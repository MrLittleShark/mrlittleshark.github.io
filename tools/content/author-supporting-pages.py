"""Reviewed introductions, resource entries and topic overviews."""
from pathlib import Path
import json,re
from bs4 import BeautifulSoup
from wolf_media import figure_html

HERE=Path(__file__).parent
OUT=HERE/'authored-pages';OUT.mkdir(exist_ok=True)
META={}
def write(slug,title,summary,body):
    (OUT/(slug+'.md')).write_text(body.strip()+'\n',encoding='utf-8')
    META[slug]={'title':title,'summary':summary}
def load(name):return json.loads((HERE/name).read_text(encoding='utf-8'))

write('sources-and-validation','资料来源','官方文档、培训讲义与示例源码的出处。',r'''
本站课程使用 **OpenFOAM v2512**。

| 资料 | 内容与入口 |
| --- | --- |
| OpenFOAM 官方文档 | [v2512 下载目录](https://dl.openfoam.com/source/v2512/)、[源码与教程](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512) |
| Wolf Dynamics 培训 | [基础培训讲义与算例](https://www.wolfdynamics.com/tutorials.html?id=181&layout=edit)，用于有限体积方法、网格和流动模型教学 |
| Basic OpenFOAM Programming Tutorials | Artur K. Lidtke 及贡献者编写的 C++ 实例，见[编程资料](/read/?slug=resource-basic-programming) |
| OF_material | 网格、求解器和边界条件实例，见[资料目录](/read/?slug=resource-of-material-catalog) |

## 图片与源码

Wolf 基础培训配图在图下标注原作者、页码和 CC BY-SA 4.0 许可；裁剪仅用于突出相关内容。OpenFOAM 和 BasicOFProgramming 的源码包保留原版权头与 GPL 许可证。

方腔、标量输运等计算图在相应课程中给出计算设置。封面为 CFD 主题插画。

## 本站方腔示例

![方腔网格](/assets/science/cavity-mesh.png)

采用 `icoFoam`，网格为 $20\times20\times1$，计算至 $t=0.5\,\mathrm{s}$。顶盖速度为 $1\,\mathrm{m/s}$，边长为 $0.1\,\mathrm{m}$，运动黏度为 $0.01\,\mathrm{m^2/s}$，因此 $\mathrm{Re}=10$。

[课程与配置](/read/?slug=first-cavity-result) · [日志与绘图脚本](/read/?slug=resource-cavity-evidence)

## 引用与纠错

引用本站内容时，请附文章名称和链接。反馈示例问题时，可在评论区提供相关文件、运行命令和错误日志。
''')
write('release-2026-10-rebuild','课程与参考库更新','课程重写，增加 Linux、C++ 和算法理论，补充字典与命令实例。','''
本次更新包括：

- 重写 29 节 OpenFOAM 基础与应用课程，补充实例、参数解释和练习。
- 更新 17 节 OpenFOAM 编程课程，增加源码分析和可修改的代码。
- 新增 [Linux 入门](/linux/)、[C++ 入门](/cpp/) 和[算法理论](/topics/finite-volume/)。
- 重整命令与字典参考：用法放入代码块，示例后紧接说明，完整配置支持展开和下载。
- 阅读页增加课程目录，保留首章、上一章、下一章和末章导航。

GitHub 登录后可保存学习进度、发表评论，在[讨论中心](/community/)提问和回答。课程、资料和文章通过[管理平台](/admin/)维护。
''')

write('topic-turbulence','湍流','RANS、LES、入口湍流量和近壁网格。',r'''
## RANS 与 LES

计算平均压降、阻力或换热量时，RANS 是常见起点。它对流动方程作平均，用湍流模型计算雷诺应力等未知量。LES 则直接计算较大的涡，并用亚格子模型描述较小尺度的作用，需要更细的网格和时间步。

'''+figure_html('wolf-turbulence-rans-les-fields')+r'''

## 模型、入口与壁面

在 `constant/turbulenceProperties` 中选择模型后，还要准备对应的场。`kEpsilon` 使用 `k`、`epsilon`，`kOmegaSST` 使用 `k`、`omega`；壁面条件与近壁网格一起设置。

例如入口速度 $U=10\,\mathrm{m/s}$、湍流强度 $I=5\%$ 时，

\[
k=\frac32(IU)^2=0.375\,\mathrm{m^2/s^2}.
\]

耗散率还需要长度尺度。各参数的估算、量纲和边界例子见[湍流模型课程](/read/?slug=laminar-turbulence-model-choice)。

壁面附近常用 $y^+=u_\tau y/\nu$ 衡量网格分辨率。第一层高度由目标 $y^+$ 初估，计算后再用实际分布调整。详细步骤见[近壁网格](/read/?slug=wall-resolution-yplus)。

## 配套练习

先使用 pitzDaily 比较入口湍流量和压降，再用 motorBike 练习外流网格、壁面分辨率与阻力监测。LES 结果还需选定统计时间段，比较平均值、脉动量和采样时长。

[turbulenceProperties 配置](/dictionaries/constant-turbulenceproperties/) · [采样与时间平均](/read/?slug=sampling-functions-and-observables)
''')
write('topic-multiphase','多相流','VOF、两流体模型、颗粒跟踪与界面计算。',r'''
## 选择相的描述方法

水面、气泡群和喷雾包含不同尺度的相分布。VOF 用体积分数表示网格能分辨的界面；Euler–Euler 方法将多相都描述为连续场；Euler–Lagrange 方法跟踪颗粒或液滴的运动。

'''+figure_html('wolf-multiphase-model-families')+r'''

## 从溃坝算例认识 VOF

水相体积分数 `alpha.water` 为 1 时，单元充满水；为 0 时，单元内为空气；中间值表示水占据了部分体积。`setFields` 根据初始水柱的几何范围写入这个场。

```bash
blockMesh
setFields
interFoam > log.interFoam 2>&1
```

这三步用于已经配置好的 damBreak 算例：建立网格、设置水柱、求解界面运动。先查看初始体积分数，确认水柱位置和高度，再比较后续水面变化。

'''+figure_html('wolf-vof-volume-fraction')+r'''

## 界面与体积

液体总体积由每个单元的相分数与单元体积求和：

\[
V_\mathrm{water}=\sum_P\alpha_P V_P.
\]

封闭容器中，这个量应随时间保持稳定；开放边界中则结合相通量计算流入和流出。对比不同网格和时间步时，同时记录体积变化、水面位置和压力。

[VOF 课程与案例下载](/read/?slug=vof-interface-dambreak) · [alpha.water 配置](/dictionaries/0-alpha-water/)
''')

# Remaining topic texts already contain useful geometry and motion explanations.
# Keep their mathematics and examples, replacing only the repeated study rhetoric.
for row in load('topics-content.json'):
    if row['slug'] in META:continue
    body=row['body']
    body=re.sub(r'本专题下面[^\n]*','',body)
    body=re.sub(r'学习时建议[^\n]*','',body)
    body=body.replace('从几何开始，逐步走向可求解的网格','网格生成与质量检查')
    write(row['slug'],row['title'],{'topic-meshing':'结构网格、贴体网格、局部细化与质量检查。','topic-dynamic-mesh':'网格运动、区域接口与拓扑变化。'}[row['slug']],body)

# Resource entries keep all download targets and useful compatibility details.
for row in load('programming-resources-content.json'):
    body=row['body']
    body=re.sub(r'## 核验的边界[\s\S]*$', '', body)
    body=re.sub(r'共 17 个目标在本机[^\n]*','17 个示例的编译步骤和运行入口见各节课程。第 11 课用于演示网格构造，其 5 单元网格仍有 `underdeterminedCells` 质量问题，课内给出定位方法。',body)
    body=body.replace('## 为何需要单独核验“已适配”','## v2512 接口调整')
    body=re.sub(r'每课包含概念图[^\n]*','每课提供代码讲解、配置实例和源码包。下载后先运行原例，再修改代码比较结果；编译命令和修改位置在课程中说明。',body)
    body=body.replace('不提供跨版本预编译 `.so`。不同 OpenFOAM 分支、编译器和精度配置之间应从源码重新编译。','请在自己的 v2512 环境中从源码编译。')
    body=re.sub(r'\[下载清单与 SHA-256\]\([^)]*\)\s*·?\s*','',body)
    changes={
      'resource-basic-programming':('BasicOFProgramming：17 个编程实例与源码','字典、场、类库、边界条件、源项和求解器的课程与下载。'),
      'resource-of-material-migration':('OF_material：v2512 算例与适配记录','算例目录、使用方法和接口调整。'),
      'resource-of-material-catalog':('OF_material 资料目录','按网格、模型、编程和后处理查找算例。'),
      'resource-coded-initialization':('用 codeStream 设置椭圆初始场','根据单元坐标生成初值，解释几何判据、动态编译和网格误差。'),
      'resource-wolf-programming-pack':('Wolf 编程实例：求解器、初值与边界','Laplace 求解器、codeStream 初值和自定义入口的配套源码。')}
    title,summary=changes[row['slug']];write(row['slug'],title,summary,body)

SUMMARIES={
'recommend-openfoam-v2512-release':'v2512 新增功能、变更说明与下载入口。',
'recommend-openfoam-v2512-userguide':'算例结构、网格、离散格式、求解设置与后处理的官方手册。',
'recommend-openfoam-v2512-source':'浏览 v2512 应用程序、C++ 库和教程源码。',
'recommend-openfoam-v2512-api':'查询类、成员函数、继承关系和对应源码。',
'recommend-openfoam-v2512-tutorials':'按物理模型查找完整算例与运行脚本。',
'recommend-wolf-introductory-training':'Linux、有限体积法、网格和 OpenFOAM 培训讲义。',
'recommend-paraview-documentation':'数据读取、切片、曲线、色标和批量出图。',
'recommend-gmsh-manual':'几何建模、物理分组和网格尺寸控制。',
'recommend-salome-platform':'几何处理、分组和网格生成平台。',
'recommend-freecad-project':'参数化建模与几何导出。',
'recommend-pyvista-documentation':'用 Python 读取、采样和绘制科学数据。',
'recommend-pyfoam-package':'辅助组织算例、分析日志和开展参数计算的 Python 工具。',
'recommend-openfoamwiki':'社区使用经验、扩展项目和工具索引。',
'recommend-cfd-online-openfoam':'安装、网格、求解和开发问题的社区讨论。',
'recommend-openfoam-journal':'OpenFOAM 方法、模型与应用研究论文。'}
for row in load('recommendations-content.json'):
    soup=BeautifulSoup(row['body'],'html.parser');sections={};name='intro'
    for el in soup.children:
        if getattr(el,'name',None)=='h2':name=el.get_text(strip=True);sections.setdefault(name,[])
        elif getattr(el,'name',None):sections.setdefault(name,[]).append(str(el))
    body='<p>'+SUMMARIES[row['slug']]+'</p><h2>资源入口</h2>'+''.join(sections.get('资源入口',[]))
    usage=''.join(sections.get('阅读与使用顺序',[]))
    if usage:body+='<h2>使用方法</h2>'+usage
    practice=''.join(sections.get('建议练习',[]))
    if practice:body+='<h2>配合本站学习</h2>'+practice
    body+='<p class="figure-source">来源：'+row.get('metadata',{}).get('source','官方文档')+'。</p>'
    write(row['slug'],row['title'],SUMMARIES[row['slug']],body)

META_PATH=OUT/'supporting-metadata.json'
META_PATH.write_text(json.dumps(META,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Supporting pages:',len(META))
