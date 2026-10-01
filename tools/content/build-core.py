"""Authoring source for the v2512 learning library. No generated AI prose placeholders.

Run with Python 3; writes core-content.json and original explanatory SVG figures.
The site content is Chinese; numerical-result images are produced independently.
"""
from pathlib import Path
import json
import math
import html

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'source-openfoam/assets/diagrams'
OUT.mkdir(parents=True, exist_ok=True)
ITEMS = []
BLUE, INK, CYAN, MUTED = '#1667ba', '#14334e', '#08a5bb', '#62798c'

def txt(x, y, s, size=20, color=INK, anchor='start', weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(s))}</text>'

def line(x1, y1, x2, y2, color=BLUE, width=3, arrow=False, dash=False):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+ (' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 6"' if dash else '')+'/>'

def box(x,y,w,h,title,sub='',fill='#edf5fd'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#c5d9ec"/>'+txt(x+w/2,y+38,title,21,anchor='middle',weight=650)+(txt(x+w/2,y+69,sub,16,MUTED,anchor='middle') if sub else '')

def svg(name,title,body,note='FoamLab · 原创教学示意图，非计算结果'):
    p=OUT/f'core-{name}.svg'
    p.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="480" viewBox="0 0 960 480" role="img" aria-label="{html.escape(title)}"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{BLUE}"/></marker></defs><rect width="960" height="480" rx="18" fill="#f8fbff"/><g font-family="Arial,Microsoft YaHei,sans-serif">{txt(40,49,title,26,weight=650)}{body}{txt(40,451,note,15,MUTED)}</g></svg>''',encoding='utf-8')
    return '/assets/diagrams/'+p.name

def poly(points,fill='#d9eafa',stroke=BLUE,width=2):
    return f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'

fig={}
fig['architecture']=svg('architecture','OpenFOAM：问题、算例、程序与结果',box(45,110,190,90,'物理问题','假设 · 参数 · 边界')+box(285,110,190,90,'算例文件','0 · constant · system')+box(525,110,190,90,'求解器与库','离散方程 · 算法')+box(765,110,150,90,'数值结果','场 · 曲线 · 积分')+line(236,155,280,155,arrow=True)+line(476,155,520,155,arrow=True)+line(716,155,760,155,arrow=True)+box(285,290,430,85,'工具程序贯穿整个流程','建网格 → 检查 → 分区 → 采样 → 转换')+line(500,287,500,218,arrow=True)+txt(480,410,'版本与构建信息必须随算例记录',20,anchor='middle'))
fig['tree']=svg('case-tree','一个算例的三个输入层',box(55,170,150,80,'case/','当前工作目录')+line(208,208,285,208)+line(285,125,285,330)+line(285,125,330,125,arrow=True)+line(285,230,330,230,arrow=True)+line(285,330,330,330,arrow=True)+box(340,80,200,80,'0/','场与初始条件')+box(340,185,200,80,'constant/','网格与物性')+box(340,290,200,80,'system/','时间与离散算法')+txt(585,121,'U、p、T、k、omega …',22)+txt(585,227,'polyMesh、transportProperties …',20)+txt(585,332,'controlDict、fvSchemes、fvSolution',20))
body=poly('280,150 610,150 610,360 280,360')+line(290,133,599,133,arrow=True)+txt(445,112,'移动顶盖 U = 1 m/s',21,anchor='middle')+txt(445,392,'L = 0.1 m，ν = 0.01 m²/s，Re = 10',20,anchor='middle')+txt(80,250,'固定壁面',20)+line(170,244,273,244,arrow=True)+txt(652,235,'二维截面',20)+txt(652,268,'前后：empty',20)+f'<path d="M 373 213 C 535 169 572 306 451 322 C 348 337 335 267 383 237" fill="none" stroke="{CYAN}" stroke-width="5" marker-end="url(#arrow)"/>'
fig['cavity']=svg('cavity','顶盖驱动方腔：边界做功形成内部环流',body)
fig['dimensions']=svg('dimensions','量纲指数的排列顺序', ''.join(box(45+i*125,140,112,100,v,s) for i,(v,s) in enumerate([('M','质量'),('L','长度'),('T','时间'),('Θ','温度'),('N','物质的量'),('I','电流'),('J','发光强度')]))+txt(480,303,'速度 U：[0 1 −1 0 0 0 0]  →  m/s',26,anchor='middle')+txt(480,355,'运动学压力 p：[0 2 −2 0 0 0 0]  →  m²/s²',24,anchor='middle'))
fig['time']=svg('time','时间步、输出间隔与物理时间',line(90,210,875,210,arrow=True)+''.join(line(110+i*8.5,199,110+i*8.5,221,'#839db6',1) for i in range(85))+''.join(f'<circle cx="{110+i*170}" cy="210" r="9" fill="{BLUE}"/>'+txt(110+i*170,264,f'{i*0.1:.1f} s',20,anchor='middle') for i in range(5))+txt(480,127,'每个小刻度：计算推进一个 Δt；蓝点：写出一个时间目录',22,anchor='middle')+txt(480,334,'固定 Δt = 0.005 s，writeInterval = 20 → 每 0.1 s 保存一次',23,anchor='middle'))
pts={0:(275,320),1:(550,320),2:(550,160),3:(275,160),4:(355,270),5:(630,270),6:(630,110),7:(355,110)}
body=''.join(line(*pts[a],*pts[b],width=2,dash=(a,b) in [(0,4),(4,5),(4,7)]) for a,b in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)])+''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{BLUE}"/>'+txt(x-13,y+25,i,23) for i,(x,y) in pts.items())+txt(480,392,'hex (0 1 2 3 4 5 6 7)；顶点顺序决定单元局部方向',23,anchor='middle')
fig['block']=svg('block-vertices','blockMesh 的八顶点六面体',body)
body=poly('100,145 300,145 300,350 100,350')+poly('300,145 500,145 500,350 300,350')+f'<circle cx="200" cy="248" r="6" fill="{BLUE}"/><circle cx="400" cy="248" r="6" fill="{BLUE}"/>'+line(200,248,400,248,arrow=True)+txt(190,225,'P')+txt(390,225,'N')+txt(300,395,'中心连线与面法向平行',20,anchor='middle')+poly('585,165 705,125 770,340 610,360')+poly('705,125 875,180 900,360 770,340')+line(674,251,821,250,arrow=True)+line(737,241,816,216,CYAN,4)+txt(770,395,'非正交：两方向不一致',20,anchor='middle')
fig['quality']=svg('mesh-quality','网格质量影响面通量的离散误差',body)
body=''
for j,label in enumerate(['1. castellated','2. snap','3. addLayers']):
 x=55+j*305;body+=box(x,98,270,280,label)
 for k in range(8):body+=line(x+25+k*30,155,x+25+k*30,337,'#b4cadf',1)+line(x+25,155+k*24,x+235,155+k*24,'#b4cadf',1)
 if j==0:
  body+=poly(' '.join(f'{x+u},{v}' for u,v in [(75,217),(105,217),(105,187),(165,187),(165,217),(195,217),(195,277),(165,277),(165,307),(105,307),(105,277),(75,277)]),fill='#f8fbff',width=3)
 else:
  body+=f'<circle cx="{x+135}" cy="245" r="58" fill="#f8fbff" stroke="{BLUE}" stroke-width="3"/>'
 if j==2:body+=f'<circle cx="{x+135}" cy="245" r="66" fill="none" stroke="{CYAN}" stroke-width="2"/><circle cx="{x+135}" cy="245" r="76" fill="none" stroke="{CYAN}" stroke-width="2"/>'
fig['snappy']=svg('snappy-stages','snappyHexMesh 三个阶段分别检查',body)
body=''
for i in range(3):
 for j in range(3):body+=f'<rect x="{215+i*170}" y="{100+j*92}" width="170" height="92" fill="'+('#daedf8' if i==1 and j==1 else '#f0f6fc')+'" stroke="#a5bed7"/>'
body+=txt(470,247,'P',27,anchor='middle')+line(480,210,480,157,arrow=True)+line(507,238,592,238,arrow=True)+line(480,265,480,324,arrow=True)+line(452,238,359,238,arrow=True)+txt(745,181,'面通量出入相抵',22)+txt(745,222,'内部面共享',22)+txt(745,263,'源项留在单元内',22)+txt(480,410,'对每个控制体积应用守恒；相邻单元共享同一个面通量',21,anchor='middle')
fig['fvm']=svg('finite-volume','有限体积：把守恒方程积分到单元',body)
fig['convection']=svg('convection','输运间断：耗散与振荡的两类误差',line(100,360,875,360,arrow=True)+line(100,360,100,110,arrow=True)+f'<path d="M110 355 L360 355 L360 160 L590 160 L590 355 L850 355" fill="none" stroke="{INK}" stroke-width="3"/><path d="M110 355 C250 355 290 325 345 235 C395 135 540 145 600 235 C665 340 760 355 850 355" fill="none" stroke="{BLUE}" stroke-width="4"/><path d="M110 355 L290 355 Q315 410 342 355 L360 160 Q380 103 403 160 L550 160 Q580 110 590 160 L610 355 Q635 401 660 355 L850 355" fill="none" stroke="{CYAN}" stroke-width="3"/>'+txt(150,95,'黑：参考剖面   蓝：数值扩散   青：过冲 / 欠冲',21)+txt(840,389,'x',20))
fig['diffusion']=svg('diffusion','一维稳态导热：线性解检验扩散离散',poly('130,140 770,140 770,320 130,320')+line(130,340,130,115,'#e56d5d',4)+line(770,340,770,115,BLUE,4)+line(132,150,768,300,BLUE,4)+txt(130,376,'T₀ = 400 K',22,anchor='middle')+txt(770,376,'T₁ = 300 K',22,anchor='middle')+txt(440,240,'T(x) = T₀ + (T₁ − T₀)x/L',23,anchor='middle')+txt(445,112,'常导热系数、无体积热源、稳态',20,anchor='middle'))
fig['cfl']=svg('courant','Courant 数比较“时间推进距离”和“网格尺度”',''.join(f'<rect x="{90+i*145}" y="175" width="145" height="110" fill="'+('#d7edfb' if i==2 else '#f1f6fc')+'" stroke="#9ebbd7"/>' for i in range(5))+line(390,144,478,144,arrow=True)+txt(435,117,'U Δt',24,anchor='middle')+line(380,322,523,322,arrow=True)+txt(450,364,'Δx',24,anchor='middle')+txt(480,407,'Co = U Δt / Δx；稳定性还与时间格式和方程耦合有关',23,anchor='middle'))
fig['coupling']=svg('coupling','压力—速度耦合：用连续性约束修正通量',box(65,135,235,105,'动量预测','已知压力 → 预测 U')+box(365,135,235,105,'压力校正','连续性 → 压力方程')+box(665,135,235,105,'通量与速度更新','校正 φ 和 U')+line(303,187,360,187,arrow=True)+line(603,187,660,187,arrow=True)+line(785,242,785,324)+line(785,324,184,324)+line(184,324,184,248,arrow=True)+txt(480,374,'SIMPLE：稳态外迭代   PISO：时间步内校正   PIMPLE：增加外层耦合',21,anchor='middle'))
fig['residual']=svg('residual','线性残差下降，不等于物理量已经收敛',line(100,360,870,360,arrow=True)+line(100,360,100,105,arrow=True)+f'<path d="M110 132 C170 160 185 200 230 217 C300 250 370 276 450 307 C540 335 680 344 850 348" fill="none" stroke="{BLUE}" stroke-width="4"/><path d="M110 310 C260 170 340 255 440 195 C535 228 700 219 850 221" fill="none" stroke="{CYAN}" stroke-width="4"/>'+txt(635,150,'蓝：归一化残差',21,BLUE)+txt(635,188,'青：监测量（独立纵轴）',21,CYAN)+txt(480,407,'同时检查残差、质量守恒、压降 / 力 / 温度等目标量',23,anchor='middle'))
fig['wall']=svg('wall','壁面分辨率：第一层单元位置决定处理方法',line(105,347,850,347,INK,8)+''.join(line(105,347-d,850,347-d,'#bdd4e7',1) for d in [12,29,53,91,145,216])+f'<path d="M110 345 C125 260 280 214 480 167 C610 136 733 110 832 92" fill="none" stroke="{BLUE}" stroke-width="4"/>'+txt(620,303,'第一层中心距 y',23)+line(592,339,592,329,CYAN,3)+txt(650,230,'近壁区不能只靠着色判断',22)+txt(480,406,'y⁺ = uτ y / ν；根据模型与壁面处理选择目标范围',23,anchor='middle'))
body=''
for j in range(6):
 for i in range(12):
  a=max(0,min(1,(3+0.14*i)-j));c='#187cbe' if a==1 else ('#e9f5fc' if a==0 else '#70c4d5')
  body+=f'<rect x="{110+i*60}" y="{99+j*45}" width="60" height="45" fill="{c}" stroke="#ffffff" stroke-width="1"/>'
body+=txt(480,411,'α = 1：相 A；α = 0：相 B；0 < α < 1：界面穿过单元',23,anchor='middle')
fig['vof']=svg('vof','VOF 的体积分数表示界面占据情况',body)
fig['heat']=svg('heat','流固耦合传热：界面同时满足温度与热流条件',box(100,135,355,210,'流体区域','对流 + 导热','#e8f4fc')+box(455,135,355,210,'固体区域','导热','#e1edf5')+line(455,150,455,329,CYAN,5)+line(245,248,644,248,arrow=True)+txt(450,302,'界面热流连续',22,anchor='middle')+txt(480,398,'接触热阻为零时温度连续；有接触热阻时应显式建模',22,anchor='middle'))
body=''
for i,(x,y,c) in enumerate([(170,110,'#dceffa'),(450,110,'#c9e2f3'),(170,245,'#d0e7eb'),(450,245,'#bedbe8')]):body+=box(x,y,280,135,f'rank {i}','局部网格 + 场',c)
body+=line(450,115,450,375,BLUE,3,False,True)+line(177,245,725,245,BLUE,3,False,True)+txt(805,211,'跨分区',20,anchor='middle')+txt(805,242,'交换面数据',20,anchor='middle')
fig['parallel']=svg('parallel','域分解：计算量与通信量共同决定效率',body)
fig['sampling']=svg('sampling','从彩色场图到可比较的线、面和积分',poly('160,150 720,150 720,340 160,340')+line(160,245,720,245,CYAN,5)+line(430,150,430,340,BLUE,3,False,True)+txt(770,244,'line：剖面',22)+txt(435,115,'plane：截面',22,anchor='middle')+txt(480,402,'保持采样位置、分量、时间与归一化方式一致，再比较不同算例',22,anchor='middle'))
body=''
for j,n in enumerate([4,8,16]):
 x=80+j*290;body+=txt(x+108,116,f'{n} × {n}',23,anchor='middle')
 for k in range(n+1):body+=line(x+k*216/n,146,x+k*216/n,362,'#75a9d2',1)+line(x,146+k*216/n,x+216,146+k*216/n,'#75a9d2',1)
fig['refine']=svg('refinement','网格研究比较目标量，而不只比较单元数',body)
fig['uncertainty']=svg('uncertainty','区分四种来源：每一种都需要不同证据',box(55,120,390,110,'离散误差','网格、时间步、数值格式')+box(500,120,390,110,'模型误差','湍流、界面、物性假设')+box(55,275,390,110,'输入不确定性','流量、几何尺寸、材料参数')+box(500,275,390,110,'实验不确定性','标定、分辨率、重复性'))
fig['repro']=svg('reproducibility','可复现计算记录：输入—运行—证据',box(55,140,230,125,'固定输入','版本 · 字典 · 网格')+box(365,140,230,125,'记录运行','日志 · 进程数 · 时间步')+box(675,140,230,125,'保存证据','数据 · 图 · 检查结果')+line(288,199,360,199,arrow=True)+line(598,199,670,199,arrow=True)+txt(480,351,'同样的截图不代表同样的算例；图需要能追溯到输入与数据',23,anchor='middle'))
fig['tools']=svg('ecosystem','扩展工具围绕数据接口协作',box(55,110,260,100,'几何与网格','FreeCAD · Gmsh · SALOME')+box(355,110,250,100,'计算核心','OpenFOAM v2512')+box(645,110,260,100,'可视化与分析','ParaView · PyVista')+line(318,159,350,159,arrow=True)+line(608,159,640,159,arrow=True)+box(260,292,440,90,'批处理与记录','Shell · Python · PyFoam · Git')+line(480,287,480,220,arrow=True))
fig['cad']=svg('cad-tessellation','CAD 曲面与离散三角面并不等价',f'<path d="M140 330 C160 95 440 95 460 330" fill="none" stroke="{BLUE}" stroke-width="5"/>'+poly('540,330 560,225 610,155 680,130 750,155 800,225 820,330',fill='none',stroke=CYAN,width=4)+line(560,225,680,130,CYAN,2)+line(560,225,750,155,CYAN,2)+line(560,225,800,225,CYAN,2)+txt(300,389,'连续几何：STEP / 原生 CAD',22,anchor='middle')+txt(680,389,'表面三角化：STL / OBJ',22,anchor='middle'))

TAG='https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/'
WOLF='Wolf Dynamics 基础培训（Foundation 9），概念与教学顺序参考；示例接口按 OpenCFD v2512 核对'

def add(slug,title,summary,body,track,diagram,source,pre='',minutes=55,kind='lesson',verification='依据 OpenCFD v2512 官方教程与源码核对；扩展练习未逐项运行',series=None):
    ITEMS.append(dict(slug=slug,kind=kind,title=title,summary=summary,body=body.strip(),track=track,series=series or ("OpenFOAM v2512 系统课程" if kind=="lesson" else track),sort_order=len(ITEMS)+1,status='published',cover_url=fig.get(diagram,diagram),owner='FoamLab',metadata=dict(source=source,verification=verification,prerequisite=pre or '无',duration=f'{minutes} 分钟',version='OpenCFD OpenFOAM v2512',figure_type='教学示意图；真实计算图另见图注')))

add('start-openfoam-v2512','01 · OpenFOAM v2512 软件组成与环境配置','介绍求解器、工具程序、C++ 库与算例的关系，检查发行分支、环境变量和实际运行版本。',r'''
OpenFOAM 是用于连续介质计算的一组程序、库和工具。以不可压缩流动为例，求解器读取速度、压力、网格和算法设置，组装离散方程并推进计算；`blockMesh`、`checkMesh` 等工具完成求解前后的独立工作。学习时应始终同时回答：**物理问题是什么、哪个程序读取哪些文件、结果如何检查**。

![问题、算例、程序和结果之间的关系](/assets/diagrams/core-architecture.svg)

### 本站版本边界

本站主线是 **OpenCFD OpenFOAM v2512**。Wolf Dynamics 培训采用的 Foundation 9 有助于理解有限体积、网格和算例结构，但版本号不是同一条发布序列。旧教程中的文件名、边界条件参数、库名和求解器调用方法需要逐项核对，不能仅把文件头的 `Version` 改成 v2512。

安装文件来自 [v2512 官方下载目录](https://dl.openfoam.com/source/v2512/)，安装路线以 [OpenCFD Linux 安装说明](https://www.openfoam.com/download/openfoam-installation-on-linux) 为准。Windows 初学者可使用已有 VMware Ubuntu 或 WSL2 Ubuntu；本课程的 Shell 命令在 Linux 终端运行。WSL/虚拟机是运行环境，不是另一个 OpenFOAM 分支。

若已配置 OpenCFD 软件源，可先检查包是否存在，再安装固定版本：

```bash
apt-cache policy openfoam2512-default
# 仅当上一步存在可安装的 Candidate 时执行：
sudo apt install openfoam2512-default
```

不同分发方式的环境脚本位置可能不同。本网站实际验证的 Ubuntu 包路径如下：

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
echo "$WM_PROJECT_VERSION"
echo "$WM_PROJECT_DIR"
command -v blockMesh
blockMesh -help
```

应看到 v2512 对应的环境、可执行文件路径及帮助信息。程序启动横幅还给出构建标识；本站方腔图使用 `build_bd2b6720-20260127`。只检查文件夹名称不足以确认真正执行的二进制版本。

### 从软件安装到第一个可用环境

先在当前终端加载环境并运行帮助，再考虑把 `source` 命令加入个人 `~/.bashrc`。同时安装多个版本时，只在一个新终端中加载一个版本。混用 PATH 与动态库路径可能导致程序存在却无法加载库、参数表不一致或编译链接失败。

**完成标志：**保存上述四项输出，说明 v2512 属于哪个发行分支，并指出自己使用的是 VMware、WSL2、原生 Linux 还是容器。此时还没有证明任何具体物理算例已经正确。
''','起步与算例','architecture','OpenCFD v2512 发布与安装文档；'+WOLF,minutes=40)

add('terminal-and-source-map','02 · 终端、环境变量与源码目录','学习可靠地复制算例、记录日志和追踪命令来源，避免把安装目录当作工作目录。',r'''
终端中的“当前目录”决定程序默认读取哪个算例。`blockMesh` 无参数时会在当前算例读取字典；在其他位置运行时，可使用帮助中列出的 `-case` 选项。路径错误常表现为找不到 `controlDict`，不是求解器安装损坏。

![OpenFOAM 工具链与文件之间的关系](/assets/diagrams/core-architecture.svg)

```bash
pwd
printf 'version=%s\nroot=%s\ntutorials=%s\n' \
  "$WM_PROJECT_VERSION" "$WM_PROJECT_DIR" "$FOAM_TUTORIALS"
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
ls
```

`cp -r` 复制的是整个目录。以后修改 `cavity-first`，安装自带的教程仍可作为对照。路径中的变量放在双引号内，可以保留包含空格的完整路径。

### 将命令输出变成可检查的记录

```bash
blockMesh > log.blockMesh 2>&1
tail -n 20 log.blockMesh
checkMesh > log.checkMesh 2>&1
```

`>` 保存标准输出，`2>&1` 将错误输出保存到同一日志。若需要一边显示一边保存，可用 `tee`；在自动化脚本中同时设置 `set -o pipefail`，使前面的求解器失败不会被 `tee` 的成功退出掩盖。**日志文件存在只说明重定向发生，不能替代退出码和日志内容检查。**

### 命令、源码和库的位置

| 目录或变量 | 用途 | 适合回答的问题 |
| --- | --- | --- |
| `$WM_PROJECT_DIR/applications/solvers` | 求解器源码 | 方程在哪里组装？ |
| `$WM_PROJECT_DIR/applications/utilities` | 工具源码 | 参数到底怎样解析？ |
| `$WM_PROJECT_DIR/src` | 可复用 C++ 库 | 某边界条件有哪些系数？ |
| `$FOAM_TUTORIALS` | 随版本提供的算例 | 哪个完整案例使用这一功能？ |
| `$WM_PROJECT_DIR/etc` | 环境与模板配置 | 当前环境怎样建立？ |
| `$FOAM_USER_APPBIN` | 用户编译的程序 | 新求解器安装到哪里？ |

```bash
command -v icoFoam
ls "$WM_PROJECT_DIR/applications/solvers/incompressible/icoFoam"
icoFoam -help-full
```

完成一个追踪练习：找出 `icoFoam.C`、`createFields.H`、一个官方 `cavity` 算例和真实可执行文件。把四个路径写在同一份记录中。这比记住大量终端命令更有助于定位问题。
''','起步与算例','architecture','v2512 applications/solvers/incompressible/icoFoam；Wolf module1 / Linux 破冰','start-openfoam-v2512',45)

add('case-structure-dimensions','03 · 算例结构、字典语法与量纲','说明 0、constant、system 的职责，以及 FoamFile、列表、宏替换与量纲指数的读取方法。',r'''
一个完整算例不需要某种特殊工程文件。OpenFOAM 通过目录约定和文本字典组织输入。**读取路径由实际程序及模型决定**，所以不能认为每个求解器都必须具有同一套 `*Properties` 文件。

![算例的三个输入层](/assets/diagrams/core-case-tree.svg)

以 `icoFoam/cavity` 为例：`0/U` 与 `0/p` 给出初始场和边界条件；`constant/transportProperties` 给出运动黏度；`system` 中的三个主要字典分别控制运行、离散格式和方程求解。`blockMesh` 运行后生成 `constant/polyMesh`，其中的 `points`、`faces`、`owner`、`neighbour`、`boundary` 描述网格。

下面是速度文件中的关键片段，并非整个文件：

```foam
FoamFile
{
    format      ascii;
    class       volVectorField;
    object      U;
}
dimensions      [0 1 -1 0 0 0 0];
internalField   uniform (0 0 0);
```

`class` 表示文件存储的场类型；`object` 应与读取对象相符。分号结束一个普通条目，花括号围成子字典，圆括号用于列表或向量，方括号用于量纲指数。`//` 与 `/* ... */` 分别表示行注释和块注释。

![七个基本量纲的排列](/assets/diagrams/core-dimensions.svg)

量纲依次为质量、长度、时间、温度、物质的量、电流和发光强度。速度的量纲是 $LT^{-1}$，运动黏度为 $L^2T^{-1}$。`icoFoam` 中的 `p` 是以密度归一化的压力，量纲为 $L^2T^{-2}$；它不能直接当作 Pa 读出。

```bash
foamDictionary 0/U -entry dimensions -value
foamDictionary constant/transportProperties -entry nu -value
foamDictionary system/controlDict -entry application -value
```

读字典时不要把宏替换误认为普通字符串。例如 `pFinal` 子字典里的 `$p;` 会复用 `p` 的设置，随后写出的 `relTol 0;` 覆盖对应条目。`#include` 引入的文件也是输入的一部分；发布算例时应一起保存。

**检查练习：**说明 `U`、运动学 `p`、`nu` 的量纲；指出哪个文件决定网格、哪个文件决定线性求解器。故意删掉一个分号只能在算例副本中做，记录报错指出的文件和行号后恢复。
''','起步与算例','tree','v2512 tutorials/incompressible/icoFoam/cavity/cavity；Wolf module1','terminal-and-source-map',55)

add('first-cavity-result','04 · 顶盖驱动方腔：计算流程与结果分析','使用官方方腔完成网格生成、检查与求解，分析 Reynolds 数、二维 empty 边界和速度场，并说明验证范围。',r'''
顶盖驱动方腔没有入口和出口。上壁向右运动，通过黏性剪切给内部流体输入动量，其余三面固定。这个算例适合学习完整工作流，因为几何、材料参数和边界条件容易追踪。

![顶盖驱动方腔的边界和参数](/assets/diagrams/core-cavity.svg)

官方 v2512 基础方腔使用 $L=0.1\,\mathrm{m}$、$U_\mathrm{lid}=1\,\mathrm{m/s}$、$\nu=0.01\,\mathrm{m^2/s}$，因此

\[
Re=\frac{U_\mathrm{lid}L}{\nu}=10.
\]

这里的基础算例**不是**常见文献中 $Re=100$、$1000$ 的方腔设置。比较基准数据之前，必须先匹配几何、雷诺数、边界定义与采样位置。

在已加载 v2512 环境的 Linux 终端运行：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-run
cd cavity-run
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
icoFoam > log.icoFoam 2>&1
touch cavity.foam
```

依次查看每一步日志。先确认网格确有 $20\times20\times1=400$ 个单元、几何尺度正确、二维方向按 `empty` 处理，再检查求解器是否推进到 `endTime`。若前一步失败，停止并修复输入；不要继续执行后续命令来掩盖错误。

![官方方腔速度场：本站 v2512 实际计算结果](/assets/science/cavity-velocity.png)

图为本站在 OpenCFD v2512 `build_bd2b6720-20260127` 上运行官方 `icoFoam` 方腔得到的速度大小图，网格 $20\times20\times1$，显示 $t=0.5\,\mathrm{s}$。它展示首次计算与后处理已贯通；单张图不能证明时间收敛、网格独立或与实验一致。

### 看图时要回答的问题

顶盖附近速度较大是否与边界值一致？固定壁面的速度是否趋于零？主回流的方向是否与顶盖运动一致？颜色表示速度大小还是某个分量？“看起来平滑”可能来自点插值，不代表网格足够精细。

保存三份日志、原始字典和一个带色标的结果图。再把顶盖速度改为 $0.5\,\mathrm{m/s}$，在新副本中计算，并先预测雷诺数如何变化。扩展算例需要自己运行并记录，不可沿用原图作为新结果。

原始输入可对照 [v2512 官方 cavity](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity)。
''','起步与算例','/assets/science/cavity-velocity.png','v2512 官方 icoFoam/cavity；本站 VMware 验证','case-structure-dimensions',65,verification='官方基础方腔已在 v2512 运行到 0.5 s；20×20×1，Re=10；不代表网格独立验证')

add('fields-and-boundaries','05 · 场文件、初始条件与边界条件的配合','区分内部初值和边界约束，解释 fixedValue、zeroGradient、noSlip 与 empty 的物理含义。',r'''
初始条件规定起始时刻域内的状态，边界条件规定计算域边界上的约束。将 `internalField` 设置为零，并不意味着之后所有位置都保持零；移动顶盖持续驱动内部速度变化。

![方腔速度边界示意](/assets/diagrams/core-cavity.svg)

官方 `0/U` 的边界部分是：

```foam
boundaryField
{
    movingWall
    {
        type    fixedValue;
        value   uniform (1 0 0);
    }
    fixedWalls
    {
        type    noSlip;
    }
    frontAndBack
    {
        type    empty;
    }
}
```

`movingWall` 等名称必须对应 `constant/polyMesh/boundary` 中的 patch 名称。网格 patch 的类型与场边界类型处于不同层次：网格上 `wall` 表示几何边界类别，速度场上 `noSlip` 表示物理约束。

对于标量 $\phi$，`fixedValue` 约束 $\phi=\phi_b$；`zeroGradient` 约束 $\partial\phi/\partial n=0$。后者不是“数值等于零”。二维方腔的前后面必须在网格及各场中采用一致的 `empty` 设置，并且网格在该方向满足二维要求。

### 为什么压力不能随意全部设为零

不可压缩求解器主要通过压力梯度作用于速度。封闭腔体在全部压力边界采用梯度约束时，压力存在任意加常数的不唯一性，通常通过 `pRefCell` 与 `pRefValue` 确定参考。把每面压力都设置为任意固定值，会改变数学问题。

```foam
PISO
{
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    pRefCell 0;
    pRefValue 0;
}
```

这里是 `fvSolution` 片段，不应放进 `0/p`。练习时为每个 patch 制作“网格类型、U 条件、p 条件、物理解释”四列表。再解释为什么入口速度已指定时，通常不能同时任意指定入口质量流量和所有压力条件。
''','起步与算例','cavity','v2512 icoFoam/cavity/0/U、0/p、system/fvSolution；Wolf module6 边界条件','first-cavity-result',55)

add('control-time-restart','06 · 时间控制、结果写出与续算','解释 controlDict 的时间参数、writeInterval 的含义与 latestTime 续算条件，检查重启所需的完整状态。',r'''
求解器推进的时间和硬盘中保存的时间目录不是同一个概念。计算可以每 $0.005\,\mathrm{s}$ 更新一次，但每 20 步才写出一个场。采样输出频率过低会遗漏瞬态特征；过高则增加存储和 I/O 成本。

![时间步与结果写出时刻](/assets/diagrams/core-time.svg)

基础方腔的主要设置如下，位于 `system/controlDict`：

```foam
application     icoFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         0.5;
deltaT          0.005;
writeControl    timeStep;
writeInterval   20;
purgeWrite      0;
writeFormat     ascii;
writePrecision  6;
runTimeModifiable true;
```

当 `writeControl timeStep` 时，`writeInterval` 是步数；改成基于运行物理时间的控制方式后，含义随之改变。不要只改一个数字而忽略控制模式。`purgeWrite 0` 保留输出；非零会使旧时间目录按规定清理，所以保留策略需要在长计算前确定。

### 续算需要保留完整状态

基础方腔可将以下条目改为：

```foam
startFrom latestTime;
endTime   1.0;
```

求解器会从已有的最新有效时间目录读场，再继续到新的结束时间。`startTime` 在该模式下不负责选择起点。多相、动网格、拉格朗日粒子等问题还可能需要更多状态；不能只复制 `U`、`p` 就假定可准确重启。

运行中修改文件是否生效还取决于求解器和模型是否重新读取该条目。`runTimeModifiable true` 不意味着任意拓扑、模型或物性变更均可安全热加载。结构性变更应在算例副本中停止并重启。

**练习：**在方腔副本计算到 $0.5\,\mathrm{s}$，随后续算到 $1\,\mathrm{s}$；从日志核实新进程的初始时间。同时用另一份算例一次计算到同一时间，比较相同位置的数据。考虑 ASCII 输出精度与重启状态造成的差别。
''','起步与算例','time','v2512 icoFoam/cavity/system/controlDict；OpenFOAM Time 类接口','fields-and-boundaries',55)

add('blockmesh-first-principles','07 · blockMesh 结构网格生成与尺度检查','解释 blockMeshDict 的顶点、块连接、单元数、分级与边界面定义，并以官方方腔检查几何尺度。',r'''
`blockMesh` 从少量六面体块生成结构化网格。字典中的顶点定义几何，`blocks` 定义连接与分辨率，`boundary` 将外边界面分配给 patch。每部分都应能与手绘几何对应。

![六面体顶点编号示意](/assets/diagrams/core-block-vertices.svg)

下面是官方方腔 `blockMeshDict` 的几何与块定义片段：

```foam
scale 0.1;
vertices
(
    (0 0 0)   (1 0 0)   (1 1 0)   (0 1 0)
    (0 0 0.1) (1 0 0.1) (1 1 0.1) (0 1 0.1)
);
blocks
(
    hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)
);
edges ();
```

乘以 `scale` 后，域为 $0.1\times0.1\times0.01\,\mathrm{m}$。网格数为 $20\times20\times1$；`simpleGrading (1 1 1)` 表示三个局部方向均匀分布。非单位 expansion ratio 表示该局部方向末端与起始端的单元尺寸比，方向取决于块顶点顺序，不能凭屏幕上的左右判断。

官方移动顶盖面写为：

```foam
movingWall
{
    type wall;
    faces ((3 7 6 2));
}
```

这是 `boundary (...)` 内的片段。一个外表面不应被重复分配给两个 patch，内部共享面也不应误放到外边界。前后两面采用 `empty`，与所有场中的二维边界定义保持一致。

```bash
blockMesh > log.blockMesh 2>&1
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
```

![方腔实际网格与速度场](/assets/science/cavity-mesh.png)

图中为本站 v2512 方腔实际 $20\times20\times1$ 网格。练习时另建 $40\times40\times1$ 网格，检查单元数应为 1600，且物理域尺寸不变。改变单元数与改变几何尺度是两种不同实验；不要在网格研究中同时修改两者。

参考：[v2512 官方 blockMeshDict](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/blockMeshDict)。
''','几何与网格','block','v2512 cavity/system/blockMeshDict；Wolf supplement1_blockmesh','case-structure-dimensions',75)

add('checkmesh-and-quality','08 · checkMesh 网格质量检查与异常定位','分析非正交、偏斜、负体积和边界连通性，结合日志与异常单元位置评估网格问题。',r'''
网格质量不是一个单独分数。网格既需要拓扑有效，又需要几何形状适合所用离散。`checkMesh` 的检查通过表示满足相应检查条件，不等于任何方程、格式和雷诺数都能准确稳定求解。

![正交与非正交网格的几何差别](/assets/diagrams/core-mesh-quality.svg)

相邻单元中心连线与公共面法向不平行，产生非正交性；面中心与用于插值的中心连线交点偏离，涉及偏斜。两者都会影响面值与法向梯度重建。它们可能同时存在，但不是同一个指标。

```bash
checkMesh -help-full
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
```

优先阅读：域包围盒、网格维数、单元数与单元类型、面朝向、体积、非正交与偏斜统计、失败检查及其位置。发现负体积、面连接错误、非封闭域等问题时，应先修复几何或网格拓扑，不能通过放宽线性残差阈值解决。

还要检查日志末尾是否写着 `Failed ... mesh checks`。本网站的混合单元编程演示实际出现过“命令退出状态为 0，但完整质量检查仍有失败项”的情况，因此仅用 Shell 的 `set -e` 不能把所有网格质量问题拦截下来。程序执行完成、网格检查通过和数值精度满足要求是三个不同结论。

### 为什么只看最大值不够

少量坏单元如果恰好位于壁面剪切层、激波、界面或狭窄间隙，可能直接支配目标量。相同最大非正交角的两张网格，其误差分布也可能完全不同。需要把相关单元集合导入可视化工具，对照局部流动结构。

在非正交网格上，扩散项常需要对应的法向梯度修正。以下是教学对比片段，不能不经检查直接替换所有算例：

```foam
laplacianSchemes
{
    default Gauss linear corrected;
}
snGradSchemes
{
    default corrected;
}
```

`corrected` 引入非正交修正，不会把坏网格自动变成好网格。过大的修正还会影响稳定性，应结合网格改进和必要的限制策略分析。

**数值实验：**参考 Wolf `nonorthoCavity` 的正交、轻度非正交与 Kershaw 网格思想，在同一物理问题上比较质量统计、中心线速度及计算代价。OF9 源案例须迁移后再运行。验收报告至少说明最差单元位于何处，以及对哪个结果量有影响。
''','几何与网格','quality','v2512 checkMesh；Wolf module3、101FVM/nonorthoCavity（概念参考，OF9 算例须适配）','blockmesh-first-principles',65)

add('surface-geometry-preparation','09 · CAD、STL、单位与封闭流体域','在网格生成之前检查尺度、法向、开口和区域名称；解释为什么显示正常的模型仍可能无法划分体网格。',r'''
CAD 实体、表面三角网格和体网格是三个不同对象。STEP 可以表达连续曲面与拓扑关系；STL 是三角面集合，通常没有可靠的物理单位与边界语义；OpenFOAM 求解需要的是填充流体域的体单元。

![连续 CAD 与离散表面表示](/assets/diagrams/core-cad-tessellation.svg)

对一根内径 $10\,\mathrm{mm}$ 的管道，导出的几何坐标可能是 10，也可能是 0.01。若把前者按米解释，几何尺度将放大 1000 倍。相同速度和运动黏度下，雷诺数也随尺度放大 1000 倍。这不是后处理显示单位能修复的问题。

```bash
surfaceCheck constant/triSurface/pipe.stl
surfaceTransformPoints -help
```

在帮助确认语法后，可在保留原文件的前提下生成以米为单位的副本：

```bash
surfaceTransformPoints -write-scale '(0.001 0.001 0.001)' \
  pipe-mm.stl pipe-m.stl
surfaceCheck pipe-m.stl
```

实际输入和输出文件名要与自己的目录对应。检查包围盒、边界边、重复面、退化三角形及表面区域数量。内流问题要明确入口、出口和壁面组成哪个封闭域；外流问题则还需要背景计算域。一个有意保留的入口开口，与意外裂缝，不应使用同一种修补逻辑。

### 几何精度应服务于计算目标

把 CAD 三角化得极细并不自动提高 CFD 精度。三角面弦高误差应小于所需几何分辨率，但过多小面会增加存储、求交及特征提取成本。保留控制分离、压降或换热的重要细节，去除明显小于模型尺度且不影响目标量的装饰结构，并记录简化依据。

完成一次尺度审计：记录 CAD 原始单位、导出设置、STL 包围盒与 OpenFOAM 网格包围盒。再说明你的 `locationInMesh` 为什么位于应保留的流体区域，而不是固体内部或表面上。
''','几何与网格','cad','v2512 surfaceCheck、surfaceTransformPoints；Wolf module2 CAD 与 module3','checkmesh-and-quality',55)

add('snappyhexmesh-workflow','10 · snappyHexMesh 分阶段网格生成与检查','分别说明背景网格、局部细化、表面贴合与边界层生成，检查各阶段的几何匹配和网格质量。',r'''
`snappyHexMesh` 在背景体网格上细化并裁剪单元，再移动点使网格贴近表面，最后尝试增加近壁层。把所有功能一次打开，容易不知道失败发生在哪个阶段。

![snappyHexMesh 的三个阶段示意](/assets/diagrams/core-snappy-stages.svg)

以下是 `snappyHexMeshDict` 的结构示意，省略的控制项必须从相近的 v2512 完整官方算例补齐，不能作为独立可运行字典：

```foam
castellatedMesh true;
snap            true;
addLayers       false;

geometry
{
    body.stl
    {
        type triSurfaceMesh;
        name body;
    }
}
// 后续还需 castellatedMeshControls、snapControls、
// addLayersControls、meshQualityControls 等完整子字典。
```

基础流程为：

```bash
blockMesh > log.blockMesh 2>&1
surfaceFeatureExtract > log.surfaceFeatureExtract 2>&1
snappyHexMesh -overwrite > log.snappyHexMesh 2>&1
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
```

`surfaceFeatureExtract` 需要对应的 `surfaceFeatureExtractDict`。某些案例使用特征捕捉的其他配置方式，不能无条件套用这一步。`-overwrite` 会更新当前网格，应在独立工作副本运行。

### 每一阶段检查一个明确问题

首先只生成 castellated 网格，确认保留的是目标流体区域，局部细化覆盖尾迹、缝隙或曲率变化处。其次启用 snap，比较几何贴合与网格质量；背景网格太粗时，增加迭代次数不能代替必要分辨率。最后增加 layers，观察目标壁面覆盖率、层数和厚度，尤其检查凹角与狭窄间隙。

近壁层总厚度、首层厚度和增长率相互关联。以等比增长为例，$n$ 层、首层厚度 $h_1$、增长率 $r\ne1$ 时，总厚度为

\[
H=h_1\frac{r^n-1}{r-1}.
\]

字典是否使用相对厚度，要看 `relativeSizes` 设置；不能把以背景单元尺寸为基准的数值直接当成米。验收时保存三个阶段的网格截面、单元数、质量统计和层覆盖情况。

可查阅 [v2512 注释版 snappyHexMeshDict](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/snappyHexMeshDict)，并使用本站配置索引按条目检索。
''','几何与网格','snappy','v2512 etc/caseDicts/annotated/snappyHexMeshDict；Wolf module3 与 OF_material/advanced_SHM','surface-geometry-preparation',90)

add('finite-volume-conservation','11 · 有限体积方法：从守恒积分到离散方程','理解单元、面、通量和源项的关系，追踪 div(phi,U) 与 laplacian(nu,U) 的物理含义。',r'''
有限体积方法从控制体积上的守恒关系出发。对于密度 $\rho$、被输运量 $\phi$、扩散系数 $\Gamma$ 和体积源项 $S$，常见形式为

\[
\frac{\partial(\rho\phi)}{\partial t}
+\nabla\cdot(\rho\mathbf{u}\phi)
=\nabla\cdot(\Gamma\nabla\phi)+S.
\]

把方程在单元 $V_P$ 内积分，再利用散度定理，把散度项变成单元各面的通量求和。于是一个空间连续问题变成“单元内储存变化 = 通过面的净输运 + 体积源”。

![有限体积的控制体积与面通量](/assets/diagrams/core-finite-volume.svg)

### 内部面为什么特别重要

相邻两个单元共享同一内部面。一侧流出的通量，应以相反符号进入另一侧。因此全域求和时，内部面通量相消，剩下外边界通量和源项。这是守恒离散的核心，不是把每个点上的微分公式分别近似后自动得到的性质。

以不可压缩体积通量 $F_f=\mathbf{u}_f\cdot\mathbf{S}_f$ 为例，对流项近似为

\[
\int_{V_P}\nabla\cdot(\mathbf{u}\phi)\,dV
\approx\sum_f F_f\phi_f.
\]

OpenFOAM 不可压缩求解器里常见的 `phi` 是面体积通量对象，其名字恰好与教科书通用标量符号相同，二者含义应通过上下文区分。可压缩情形中对应通量可能含密度，量纲必须检查。

```foam
divSchemes
{
    default none;
    div(phi,U) Gauss linear;
}
laplacianSchemes
{
    default Gauss linear orthogonal;
}
```

这里 `Gauss` 表示通过面求和实现相应空间算子；`linear` 关联面插值；`orthogonal` 适用于对应的法向梯度假设。不能把这一组正交方腔设置不加分析地复制到任意非正交工业网格。

最终每个单元贡献一个离散方程，可写为

\[
a_P\phi_P+\sum_N a_N\phi_N=b_P.
\]

`fvSchemes` 决定如何构造系数，`fvSolution` 决定如何解组装后的代数系统。练习时在三单元一维网格上标出每个面的方向，写出中间单元的收支式，再验证左右内部面在全域求和中消失。
''','数值方法','fvm','Wolf module6 FVM；v2512 finiteVolume 算子与 cavity/fvSchemes','case-structure-dimensions',70)

add('advection-schemes-boundedness','12 · 对流格式：迎风、中心插值与有界性','以被输运的方波为例，分析数值扩散、过冲与局部梯度，并设计一次受控格式比较。',r'''
一个无扩散的标量波随均匀速度移动时，解析解只平移而不改变形状。如果计算结果越来越平缓，说明存在数值扩散；如果出现高于初始最大值或低于最小值的新极值，则需要分析离散振荡或有界性。

![对流格式产生数值扩散或过冲的示意](/assets/diagrams/core-convection.svg)

对于一维常速 $u>0$，迎风近似用上游单元值构造面输运。在光滑区域做 Taylor 展开，其空间截断误差包含一个与 $u\Delta x$ 成比例的扩散项。完整数值扩散还与时间离散有关，不能只凭空间格式名称给出普适数值。

中心插值在光滑、规则网格上通常具有较高空间精度，但强对流和不连续剖面会暴露无界振荡问题。限制器在高阶重建和有界性之间调整，不意味着在所有区域保持同一个形式上的高阶精度。

### 从方腔设置开始识别语法

下面三行是分别用于对比的选择，不应同时使用相同键：

```foam
// 方案 A：稳健但耗散较强
div(phi,U) Gauss upwind;

// 方案 B：正交基础方腔中的线性插值
div(phi,U) Gauss linear;

// 方案 C：速度梯度用于线性迎风重建
div(phi,U) Gauss linearUpwind grad(U);
```

方案 C 依赖 `grad(U)` 的梯度计算设置。格式键必须与求解器实际离散的项相符；没有某个输运方程时，添加对应键并不会凭空生成该方程。

### 设计一个有意义的比较

参考 Wolf `pureConvection_profiles` 的高斯、阶跃和方波思想，固定速度、网格、边界与 Courant 数，只改变对流格式。在相同物理时刻，比较峰值、总积分、剖面形状以及

\[
E_1=\frac{\sum_i V_i\lvert\phi_i-\phi_i^{\mathrm{ref}}\rvert}{\sum_i V_i}.
\]

平滑高斯与方波应分别测试：一个格式在光滑解上的收敛阶，不能替代其处理间断的表现。旧 Foundation 9 演示求解器应先按 v2512 编程课程迁移和编译；本页不声称该旧程序可直接运行。

**验收：**提交同一坐标轴上的三条剖面，列出极值、积分误差、时间步与单元数。解释你选择的格式对当前问题为什么合适，而不是简单写“二阶比一阶好”。
''','数值方法','convection','Wolf module6 数值实验；v2512 src/finiteVolume/finiteVolume/divSchemes','finite-volume-conservation',75)

add('diffusion-gradients-laplacian','13 · 扩散项、梯度重建与界面通量','用一维导热的线性解建立检查基准，再理解非正交修正与材料交界处的连续热流。',r'''
对无源、常导热系数的一维稳态导热问题，控制方程为 $d^2T/dx^2=0$。两端温度给定时，解析解是直线：

\[
T(x)=T_0+(T_L-T_0)\frac{x}{L},\qquad
q''=-k\frac{T_L-T_0}{L}.
\]

取 $T_0=400\,\mathrm{K}$、$T_L=300\,\mathrm{K}$、$L=0.1\,\mathrm{m}$、$k=10\,\mathrm{W/(m\,K)}$，热流密度沿正 $x$ 方向为 $10000\,\mathrm{W/m^2}$。正负号来自 Fourier 定律，而不是色标高低。

![一维导热的解析温度分布](/assets/diagrams/core-diffusion.svg)

### 两种误差应分开处理

单元中心值需要插值到面上，梯度还需要投影到面法向。正交网格中中心连线与面法向一致，表达较简单；非正交网格需要附加修正。字典中的 `gradSchemes`、`laplacianSchemes` 与 `snGradSchemes` 分别控制相关算子的不同环节。

```foam
gradSchemes
{
    default Gauss linear;
}
laplacianSchemes
{
    default Gauss linear corrected;
}
snGradSchemes
{
    default corrected;
}
```

这是非正交教学设置片段。不能因为单次计算稳定就认为修正误差可忽略；应同时检查网格与网格细化趋势。

### 材料交界不能只比较温度图是否平滑

两种材料串联时，稳态热流取决于总热阻

\[
q''=\frac{T_0-T_L}{L_1/k_1+L_2/k_2}.
\]

温度在两种材料内部各自线性，斜率通常不同。若无接触热阻，界面温度连续、热流连续；导热系数跳变时，用简单算术平均代替合适的面导热处理可能导致错误通量。

练习分两步：先在均匀网格检验常系数线性解，再处理两材料并检查界面两侧热流。`laplacianFoam` 的温度扩散示例使用的扩散参数与完整能量方程中的导热系数不是同一个量，应根据方程中是否已除以 $\rho c_p$ 检查单位。
''','数值方法','diffusion','Wolf module6、101FVM/laplace；v2512 laplacianFoam 与 finiteVolume 梯度算子','finite-volume-conservation',70)

add('time-discretisation-courant','14 · 时间离散、Courant 数与瞬态分辨率','区分稳定性和时间精度，以固定空间网格的时间步研究检验真实瞬态。',r'''
Courant 数将一个时间步内的信息输运距离与网格尺度联系起来。一维均匀网格上的直观定义是

\[
Co=\frac{|u|\Delta t}{\Delta x}.
\]

一般有限体积网格常通过每个单元面通量的绝对值和构造相应度量。平均 Co 很小并不保证局部最大 Co 很小，特别是在小单元、窄缝和高速区。

![Courant 数的几何意义](/assets/diagrams/core-courant.svg)

对方腔 $\Delta x=0.005\,\mathrm{m}$，取速度尺度 $1\,\mathrm{m/s}$ 和 $\Delta t=0.005\,\mathrm{s}$，简单尺度估计给出 $Co\sim1$。求解器日志中的实际统计基于网格和面通量，不必与这个手算估计完全相同。

```foam
ddtSchemes
{
    default Euler;
}
```

OpenFOAM 的 `Euler` 表示其对应的一阶隐式时间离散，不能与所有教科书里的显式 Forward Euler 混为一谈。`backward` 使用多时间层的后向差分形式；`CrankNicolson` 的具体偏心参数和历史层处理应查 v2512 实现与教程。

### 隐式不等于可以任意放大时间步

隐式处理可以改变稳定性约束，但时间精度仍受分辨率限制。若涡脱落周期只有几个时间步，平均速度看起来合理也不能证明振动频率、相位和峰值正确。多相界面与声学问题还可能有额外的时间尺度。

对支持自动步长的求解器，可在相应算例使用类似设置：

```foam
adjustTimeStep yes;
maxCo          0.5;
maxDeltaT      0.001;
```

这不是所有求解器的通用开关。是否读取这些条目，应查求解器源码、完整教程及运行日志；给不支持它们的程序加字典键不会自动启用控制。

**时间步研究：**固定网格、物性和格式，分别使用 $\Delta t$、$\Delta t/2$、$\Delta t/4$，在相同物理时间采样。比较峰值、周期、均值与计算量。若同时细化网格，应将它作为另一组实验，否则无法区分空间误差和时间误差。
''','数值方法','cfl','Wolf module6 CFL；v2512 ddtSchemes 与 CourantNo 实现','advection-schemes-boundedness',65)

add('simple-piso-pimple','15 · SIMPLE、PISO 与 PIMPLE 的工作过程','理解压力方程为何出现、速度与通量为何需要校正，避免将迭代次数当作物理精度保证。',r'''
不可压缩流动同时满足动量方程和 $\nabla\cdot\mathbf{u}=0$。直接用旧压力解动量方程，得到的预测速度一般不自动满足连续性；压力校正的作用，是使修正后的面通量满足离散质量守恒。

![压力—速度耦合的校正循环](/assets/diagrams/core-coupling.svg)

SIMPLE 常用于稳态迭代；PISO 在一个时间步内进行压力与速度校正；PIMPLE 将时间步内的外层耦合迭代与压力校正结合。具体控制项和方程重组装位置仍由对应求解器决定。

官方基础 `icoFoam` 方腔使用：

```foam
PISO
{
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    pRefCell 0;
    pRefValue 0;
}
```

`nCorrectors` 控制该算法中的压力校正；`nNonOrthogonalCorrectors` 对应非正交压力修正循环。正交网格上写零不代表忽略连续性，而是无需额外非正交校正。

对于使用 PIMPLE 的具体求解器，常见结构片段为：

```foam
PIMPLE
{
    nOuterCorrectors 2;
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    momentumPredictor yes;
}
```

这段用于理解层次，不能直接替换 `icoFoam` 的 `PISO` 来把程序变成 PIMPLE 求解器。算法在 C++ 实现中，字典只提供它读取的参数。

### 怎样判断校正是否足够

检查每步连续性误差、目标量对校正次数的敏感性，以及时间步收敛性。增加外循环可能降低同一时间步的耦合误差，但也增加代价；它不能修复错误边界、极差网格或不适合的物理模型。

稳态求解器中“时间”经常作为迭代计数使用，不能把该目录值直接解释成真实物理秒数。若流动本身具有持续非定常结构，残差不降可能是在提示稳态假设不合适，而不只是需要更小松弛因子。

### 改字典不能增加求解器没有实现的方程

v2512 的 `simpleFoam` 以稳态动量方程配合 SIMPLE 迭代；`pimpleFoam` 包含瞬态项并使用 PIMPLE 控制。二者通过 `createFvOptions.H` 建立源项管理，并在动量方程中调用 `fvOptions(U)`、约束与修正接口。基础 `icoFoam` 没有这套调用：仅在方腔中添加 `constant/fvOptions`，不会自动给它增加源项物理。应选择支持该源项的完整 v2512 求解器或显式修改程序。

同样，Foundation 教程的 `fvModels/fvConstraints` 不能靠改文件名就变成 OpenCFD 的 `fvOptions`。需要同时检查字典层次、C++ 基类与方程中的调用位置，详见[动量源迁移实例](/read/?slug=programming-12)。

练习：画出你正在使用的求解器的三层关系——时间推进、外循环、压力校正。记录每层哪个设置负责控制，并用日志证明程序实际执行了你预期的循环。
''','数值方法','coupling','Wolf module6 pressure-velocity coupling；v2512 icoFoam、pimpleFoam 与 solutionControl','time-discretisation-courant',75)

add('linear-solvers-residuals','16 · 线性求解器、残差与收敛判据','解释 tolerance、relTol、pFinal 和初始、最终残差，区分代数求解误差、非线性迭代误差与离散误差。',r'''
离散后得到 $A\mathbf{x}=\mathbf{b}$。给定当前近似解，代数残差为 $\mathbf{r}=\mathbf{b}-A\mathbf{x}$。求解器打印的残差通常经过归一化，不能将数值 $10^{-6}$ 直接解释为速度误差 $10^{-6}\,\mathrm{m/s}$。

![残差与物理监测量可能不同步](/assets/diagrams/core-residual.svg)

官方方腔压力设置为：

```foam
solvers
{
    p
    {
        solver PCG;
        preconditioner DIC;
        tolerance 1e-06;
        relTol 0.05;
    }
    pFinal
    {
        $p;
        relTol 0;
    }
    U
    {
        solver smoothSolver;
        smoother symGaussSeidel;
        tolerance 1e-05;
        relTol 0;
    }
}
```

`tolerance` 是对应归一化残差的绝对停止阈值；`relTol` 相对于该次线性求解的初始残差。满足停止条件之一时可结束，另有最大迭代数等控制。`relTol 0` 通常用于禁用相对阈值提前退出。`pFinal` 仅在程序选择最终求解设置时使用，不是一个新的压力场。

### 选择算法要先看矩阵性质

PCG 面向适用的对称正定系统；加入不同物理、边界或耦合后，不应只因一个压力案例可用就套到任意方程。对流项可能形成非对称矩阵，应选择支持相应性质的求解方法。GAMG 利用多层次消除不同尺度误差，但其性能也与网格、并行分区、平滑器及粗网格配置有关。

线性残差低只说明当前线性系统解得较充分。外迭代系数仍可能变化，连续性可能尚未满足，网格误差也可能很大。因此至少保留三类证据：残差历史；质量或其他守恒收支；压降、力或平均温度等目标量的历史。

### 在运行时保存解算信息

v2512 主线使用 `solverInfo` 函数对象保存字段的解算信息，可将以下子对象合并到 `controlDict/functions`：

```foam
solverHistory
{
    type solverInfo;
    libs (utilityFunctionObjects);
    fields (p U);
    executeControl timeStep;
    executeInterval 1;
    writeResidualFields false;
}
```

它读取求解过程中产生的信息。v2512 的 `solverInfo` 在 `execute()` 中更新并记录解算信息，`write()` 本身不执行额外操作，因此这里用 `executeControl` 和 `executeInterval` 明确控制记录频率；不要把通用的 `writeInterval` 自动解释为每个函数对象的采样间隔。计算结束后，仅凭最终 `U`、`p` 场无法重建完整历史残差；因此监测应在计算前配置，或者从保留的原始求解日志分析。不应沿用其他分支或旧资料中未经核对的 `type residuals`。

本站已在独立 v2512 方腔副本中执行前三个时间步，确认生成 `postProcessing/solverHistory/0/solverInfo.dat`，其中包含时间、求解器、初始与最终残差、迭代数等列；相同测试也验证了本课程的 `probes` 配置。这项短测确认接口与文件输出，不代表算例已到稳态。

**诊断练习：**在相同算例副本中收紧压力容差一个数量级，比较目标量与总运行时间。若目标量几乎不变而耗时显著增加，说明该指标下代数误差可能已小于其他误差；若变化明显，继续检查耦合与守恒，不能立刻宣称细网格结果正确。
''','数值方法','residual','v2512 cavity/system/fvSolution、lduMatrix solvers；Wolf module6 linear solvers / residuals','simple-piso-pimple',75)

add('relaxation-stability-diagnosis','17 · 松弛、稳定性与发散诊断','从受控迭代更新理解松弛作用，建立按输入、网格、时间步、离散与算法排序的排错流程。',r'''
迭代求解非线性问题时，一次更新过大可能导致系数与解相互放大。场松弛的直观形式为

\[
\phi^{k+1}=\phi^k+\alpha\bigl(\phi^{*}-\phi^k\bigr),
\qquad 0<\alpha\le1.
\]

$\phi^*$ 是本次计算得到的候选更新。较小的 $\alpha$ 减少单次变化，通常提高迭代稳定性，但也可能拖慢收敛。方程松弛通过修改代数系统实现，不应与场松弛当作完全相同的操作。

![残差和目标量要联合观察](/assets/diagrams/core-residual.svg)

常见稳态算例片段如下，具体场名依求解器与模型而定：

```foam
relaxationFactors
{
    fields
    {
        p 0.3;
    }
    equations
    {
        U 0.7;
        "(k|omega)" 0.7;
    }
}
```

这组数字只是教学起点，不是任何问题的推荐最优值。正则键必须匹配真实场名。实际求解器还要在相应位置调用松弛，字典才能发挥作用。

### 发散时先寻找第一个异常

按照因果关系检查：几何单位与物性量纲是否正确；入口流量与出口/压力约束是否矛盾；网格是否有负体积或关键区域坏单元；起始条件是否造成极端梯度；局部 Courant 数或源项时间尺度是否过大；对流与扩散格式是否适合；最后再调整线性容差、耦合次数和松弛。

`Floating point exception` 通常只是最后的失败表现。更有价值的是失败前第一个不合理的温度、密度、湍流变量、连续性误差或 Courant 数。保留完整日志比只截最后五行更有效。

建立一个最小变更实验：复制算例、一次只改变一个设置，记录“原值、新值、假设、观测结果”。不要同时换网格、换湍流模型和换全部离散格式，再把成功归因于其中某一项。

**验收：**提交一份真实或受控故障的诊断表，说明最先出现的异常是什么、为什么它比最终报错更接近根因，以及你用什么独立结果确认修复有效。
''','数值方法','residual','v2512 fvSolution relaxationFactors 与 fvMatrix；Wolf module6','linear-solvers-residuals',60)

add('grid-time-verification','18 · 网格与时间步细化及误差分析','建立目标量的细化序列，分析观测收敛阶与外推条件，报告网格和时间步变化造成的数值差异。',r'''
网格研究的对象是具体目标量，例如平均压降、壁面力、中心线速度或热流，而不是“整个彩色图看起来差不多”。不同目标量对局部网格的敏感性不同，壁面梯度常比全域平均值更难收敛。

![保持几何不变的系统网格细化](/assets/diagrams/core-refinement.svg)

建立至少三组有规则关联的网格，保持几何、物性、边界、离散格式与相同物理时刻一致。时间步和迭代误差需要控制在不会掩盖空间差别的水平。每组至少记录：单元数、代表尺度、质量指标、目标量、运行时间。

设最细、中等、最粗网格尺度满足 $h_2/h_1=h_3/h_2=r>1$，目标量为 $Q_1,Q_2,Q_3$。在进入渐近区、误差具有单一主导阶且单调收敛等条件下，可估计

\[
p_\mathrm{obs}=\frac{\ln\left|\dfrac{Q_3-Q_2}{Q_2-Q_1}\right|}{\ln r},
\qquad
Q_\mathrm{ext}=Q_1+\frac{Q_1-Q_2}{r^{p_\mathrm{obs}}-1}.
\]

这不是无条件可用的精度证书。目标量振荡收敛、差值接近舍入误差、网格质量模式变化或未进入渐近区时，简单公式可能失效。

### 一个可复算的算术演示

以下数字是**人为构造的公式演示**，不是 OpenFOAM 计算结果：$Q_1=1.01$、$Q_2=1.04$、$Q_3=1.16$、$r=2$。则差值比为 4，得到 $p_\mathrm{obs}=2$，外推值为 1.00。演示只说明计算方法。

```python
from math import log
q1, q2, q3, r = 1.01, 1.04, 1.16, 2.0
p = log(abs((q3-q2)/(q2-q1))) / log(r)
q_ext = q1 + (q1-q2)/(r**p - 1)
print(p, q_ext)
```

### 方腔练习的合格报告

使用 $20^2$、$40^2$、$80^2$ 个平面单元，分别记录中心线 $u/U_\mathrm{lid}$、$v/U_\mathrm{lid}$ 与采样方式。必须先检查运行时间是否足够达到所需状态，并对时间步敏感性做独立研究。本站展示的单张 $20^2$ 方腔图不满足这一完整验证要求。

报告应写出“在当前目标量与测试序列下变化为多少”，避免无条件写“已达到网格无关”。
''','验证与研究方法','refine','Wolf module6 数值实验；经典 Richardson 外推原理，公式使用条件显式说明','linear-solvers-residuals',80)

add('physical-boundary-design','19 · 设计入口、出口、壁面与周期边界','从物理信息和约束数量出发选择边界条件，处理回流、入口发展段和压力参考。',r'''
边界条件决定模拟的是哪个物理问题。对于一段内流管道，“给定入口速度、出口参考压力”与“给定压差、让流量成为结果”是两种不同实验。不要把所有已知数值都同时设成强制约束。

![沿流向采样并检查入口和出口影响](/assets/diagrams/core-sampling.svg)

对层流充分发展圆管，压降与平均速度满足

\[
\frac{\Delta p}{L}=\frac{32\mu\bar U}{D^2},
\qquad
u(r)=2\bar U\left[1-\left(\frac{r}{R}\right)^2\right].
\]

这里 $\Delta p$ 是物理压力差，$\mu$ 是动力黏度。若求解器存储运动学压力，需按该模型的密度约定换算。利用这个关系可以检查边界、单位和压降提取是否一致。

### 常见入口出口组合的含义

指定入口 `fixedValue` 速度，出口采用适合出流的速度条件和参考压力，是常见起点。但如果涡流持续穿过出口，简单零梯度外推可能不合适。应先判断域是否过短，再按实际回流场景选择边界模型。

```foam
// 标量 C 的可回流出口片段：流出时零梯度，流入时给定 C=0
outlet
{
    type inletOutlet;
    inletValue uniform 0;
    value uniform 0;
}
```

这是标量字段示例，向量场需使用相应向量值。`inletValue` 指定回流时进入域内的值；`value` 还承担初始化等作用。不同变量不应机械地使用同一类型。

对称边界约束法向速度与相应梯度，只适用于物理上确实可对称的场景。周期边界还涉及成对 patch 的几何映射及场连续关系；不能把两个独立出口改名后就视为周期。

**检查实验：**保持入口流量不变，适度延长出口段并比较观测区压降和速度。如果核心结果显著变化，说明原出口位置或边界正在影响目标区。对充分发展假设，应同时核查入口发展长度与流动状态。
''','物理模型','sampling','v2512 finiteVolume/fields/fvPatchFields；Wolf module6 边界条件','fields-and-boundaries',70)

add('laminar-turbulence-model-choice','20 · 层流、RANS、LES 与模型选择','通过尺度、目标量和可用分辨率选择建模层次，区分瞬时速度、平均速度与湍流闭合。',r'''
模型选择从目标问题开始：关心平均压降、瞬时载荷、混合时间还是壁面传热？同一个几何，在不同雷诺数、入口扰动和关注尺度下，可能需要不同处理。

![物理模型误差与其他误差的区别](/assets/diagrams/core-uncertainty.svg)

雷诺数比较惯性和黏性作用，但转捩阈值受几何、扰动及边界条件影响。不能用一个管流经验阈值判断所有流动。低雷诺数方腔可以从层流方程学习；工程高雷诺数问题通常需要考虑湍流的多尺度影响。

RANS 将速度分解为平均和脉动，产生 Reynolds 应力等未闭合项；LES 解析较大的涡尺度、建模未解析尺度；DNS 则要求直接解析相关小尺度。**把网格加密一点并不会自动把 RANS 变成 LES，也不会把 LES 变成 DNS。**

v2512 中某些传统求解器使用 `constant/turbulenceProperties`，示意如下：

```foam
simulationType RAS;
RAS
{
    RASModel kOmegaSST;
    turbulence on;
    printCoeffs on;
}
```

这只是相应求解器家族的设置片段。具体模型文件名、可用模型、必需场和物性接口，应从相近 v2512 完整教程确定；不能把其他发行分支的新文件名机械搬入。

### 模型选择必须带着网格计划

RANS 的近壁处理决定第一层网格需求；LES 需要满足空间与时间分辨率、入口扰动和统计收敛要求。瞬态计算运行很久，也可能因为域宽太窄、网格太粗或平均窗口太短而得到错误统计。

建立一张选择表：目标量、主要流动特征、候选模型、需要的输入、网格与时间分辨率、可用验证数据。至少写出一个你明确没有建模的机制，例如转捩、粗糙度或可压缩性，并说明它是否可能影响结论。

**练习：**比较低 Re 方腔、弯管平均压降、绕流瞬态升力三个问题，说明为什么不能只用同一套 `kOmegaSST` 字典解决全部需求。
''','物理模型','uncertainty','v2512 turbulenceModels 与不可压缩教程；Wolf module8 湍流模型','physical-boundary-design',65)

add('wall-resolution-yplus','21 · 近壁网格、壁面函数与 y⁺','把首层单元尺寸与摩擦速度联系起来，理解近壁解析和壁面函数策略的差异。',r'''
壁面附近存在很强的速度和温度梯度，通常也是阻力与换热最敏感的区域。只在主流区加密，而保留过粗的首层单元，未必改善壁面目标量。

![壁面法向网格与第一层中心距](/assets/diagrams/core-wall.svg)

常用无量纲距离为

\[
y^+=\frac{u_\tau y}{\nu},\qquad
u_\tau=\sqrt{\frac{|\tau_w|}{\rho}}.
\]

这里 $y$ 是壁面到第一层单元中心的距离，不是整个边界层厚度。粗略估算首层高度后，还需要使用初步计算得到的壁面剪切反算实际 $y^+$ 分布。

低雷诺数近壁解析通常需要第一层落在黏性底层附近；采用适用的壁面函数时则需要与其假设一致的壁面距离。具体范围取决于模型、壁面函数和流动状态，不能把“所有场景 $y^+=1$”或“所有场景 $y^+>30$”作为普遍规则。

### 字典是成套设置

使用 `kOmegaSST` 时要同时检查 `k`、`omega`、`nut` 的壁面条件；换模型后只改 `RASModel` 往往不够。下面是官方 `pitzDaily` 中 `k` 壁面条件的形式，数值来自该案例而非通用推荐：

```foam
upperWall
{
    type kqRWallFunction;
    value uniform 0.375;
}
```

对应求解器和模型已正确建立后，可以尝试求解器的后处理模式：

```bash
simpleFoam -postProcess -func yPlus -latestTime
```

`yPlus` 需要湍流/输运模型等运行环境；把它用于仅有 `U`、`p` 的任意目录，未必能构造所需对象。若缺场或缺模型，应先读错误信息并回到完整算例。

### 验收不只写一个平均数

显示整个目标壁面上的 $y^+$ 分布，报告范围及关键区域。分离点、再附着区和曲率变化附近应单独观察；面积平均值可能掩盖局部严重失配。同时记录首层厚度、增长率、总层数和层覆盖率，再比较壁面剪切或热流对网格的敏感性。
''','物理模型','wall','v2512 simpleFoam/pitzDaily/0/k 与 yPlus functionObject；Wolf module8','laminar-turbulence-model-choice',65)

add('vof-interface-dambreak','22 · VOF 两相流：体积分数、初始化与质量守恒','以溃坝为例解释 alpha.water、setFields、界面压缩和毛细时间尺度，不将界面截图当作定量验证。',r'''
VOF 使用单元内某一相的体积分数 $\alpha$ 表示界面：$\alpha=1$ 表示该单元充满该相，$\alpha=0$ 表示没有该相，介于两者之间表示界面穿过单元。界面并非额外的一层实体薄膜。

![VOF 单元体积分数示意](/assets/diagrams/core-vof.svg)

`interFoam` 的官方溃坝算例位于 `multiphase/interFoam/laminar/damBreak/damBreak`。水相通常使用 `alpha.water`；相名来自案例配置，不能随意写成 `alpha1` 后期待所有 v2512 模型自动识别。

初始化时，`setFields` 根据几何区域覆盖默认场。官方基础溃坝的关键设置是：

```foam
defaultFieldValues
(
    volScalarFieldValue alpha.water 0
);
regions
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues
        (
            volScalarFieldValue alpha.water 1
        );
    }
);
```

必须先生成体网格，再初始化场。阅读该教程 `Allrun`，确认是否需要先从 `0.orig` 恢复 `0`；不要缺少初始字段就直接运行 `setFields`。

### 需要同时控制三类行为

第一，输运过程应保持合理的有界性，检查 $\alpha$ 是否偏离 $[0,1]$。第二，无质量源且边界不交换该相时，应检查其总体积

\[
V_\alpha(t)=\sum_i\alpha_i(t)V_i.
\]

第三，界面运动、表面张力和重力可能引入不同时间尺度。降低普通流动 Co 不一定充分控制毛细效应；还应核查求解器使用的相分数步进、子循环和相关控制。

界面压缩是数值处理，不是额外的真实物理吸引力。过强压缩与不合适的网格、时间步可能造成锯齿或寄生流。接触角、壁面润湿和表面张力的设置也要与具体物理场景一致。

**溃坝练习：**保存起始水柱截面、多个时刻的 $\alpha=0.5$ 界面、总体积历史与前沿位置。改变网格和时间步后，用同样提取规则比较前沿轨迹。未经实验和细化研究，不应声称界面形状已被验证。

参考：[v2512 官方 damBreak](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak)。
''','物理模型','vof','v2512 interFoam/damBreak；Wolf module8 多相流；OF_material/advanced_physics','time-discretisation-courant',80)

add('heat-and-multiregion','23 · 传热、多区域耦合与能量收支','区分温度扩散、流体能量与流固耦合传热，检查区域定义、界面条件和整体热量平衡。',r'''
仅求解温度扩散方程，与求解可压缩流体的能量方程，不是同一个模型。前者可使用热扩散率 $a=k/(\rho c_p)$；后者还可能包含对流、压缩功、黏性耗散、辐射或相变，具体由求解器决定。

![流体和固体交界的传热约束](/assets/diagrams/core-heat.svg)

对于流固耦合传热，流体区域解流动与能量，固体区域解导热。区域可以使用独立网格和物性，但界面要通过对应边界模型交换信息。在无接触热阻且采用一致法向约定的情形，界面满足温度连续以及两侧热流守恒。

```text
constant/
  regionProperties
  fluid/   ...区域物性与网格...
  solid/   ...区域物性与网格...
system/
  controlDict
  fluid/fvSchemes
  fluid/fvSolution
  solid/fvSchemes
  solid/fvSolution
```

这是结构示意，`fluid` 和 `solid` 应替换成案例真正的区域名称。v2512 官方 `chtMultiRegionFoam/multiRegionHeater` 提供完整示例；不要只新建两个同名文件夹，就认为耦合关系自动成立。

### 用热量收支检查结果

稳态时，域内发热量、入口出口携带的焓差、壁面热流和其他模型项应按一致符号平衡。瞬态时还需考虑系统储能率：

\[
\frac{dE}{dt}=\dot Q_\mathrm{in}-\dot Q_\mathrm{out}+\dot Q_\mathrm{source}+\text{其他能量交换项}.
\]

只看最高温度不能判断能量是否守恒。对于给定热流壁面，面积单位错误会直接改变总功率；对于给定功率的体热源，还要确认它是总功率、体积功率密度还是按质量归一化的源项。

### 逐步建立难度

先验证一维固体导热，再加入一个对流流体区，最后考虑复杂材料或辐射。每增加一种模型，都保留一个极限情况检查，例如关闭热源后系统是否趋向预期温度，改变导热系数后温差趋势是否符合热阻模型。

练习报告应包含区域列表、界面对应关系、物性单位、界面两侧温度与热流、整体热量收支。官方案例命令与区域名称见 [v2512 多区域加热器](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater)。
''','物理模型','heat','v2512 chtMultiRegionFoam/multiRegionHeater；Wolf module8 热传导与共轭传热','diffusion-gradients-laplacian',85)

add('compressibility-and-thermodynamics','24 · 可压缩流动与热物性模型','理解 Mach 数、状态方程和能量变量，避免将不可压缩压力文件直接用于可压缩求解器。',r'''
可压缩模型允许密度随压力、温度及成分变化。声速 $a$ 与局部速度给出 Mach 数 $Ma=|\mathbf{u}|/a$，但低 Mach 数也不必然意味着密度恒定：明显温差或不同组分同样可能造成密度变化。

![模型假设应与输入和验证同时检查](/assets/diagrams/core-uncertainty.svg)

理想气体的基本关系为

\[
p=\rho R T.
\]

这里 $p$ 为绝对物理压力，温度采用 Kelvin，$R$ 为与所选质量基准一致的气体常数。把不可压缩算例中任意参考的运动学压力直接填入热物性模型，会改变密度甚至导致不合理状态。

### thermophysicalProperties 是一组关联选择

v2512 的热物性配置通过热力学类型、混合物、输运模型、热容模型、状态方程与能量变量共同构造模型。以下展示一种常见层次，完整可运行值应从目标求解器的官方案例复制：

```foam
thermoType
{
    type hePsiThermo;
    mixture pureMixture;
    transport const;
    thermo hConst;
    equationOfState perfectGas;
    specie specie;
    energy sensibleEnthalpy;
}
```

这段不包含必需的 `mixture` 物性系数，因此不是完整文件。`sensibleEnthalpy` 与 `sensibleInternalEnergy` 不是随意可交换的标签，需要与实际方程和边界条件一致。

声学或压力波问题还要关注声传播的时间与空间分辨率。仅看流速定义的 Co 可能不足以刻画波的数值传播误差。若有激波，应额外关注激波捕捉、振荡与守恒；不能用平滑低速问题的格式选择代替。

**入门练习：**阅读 v2512 `rhoPimpleFoam/laminar/helmholtzResonance`，先列出其压力、温度、密度、能量变量之间的关系。运行前用一个均匀状态手算理想气体密度并与输入模型核对；运行后比较压力波频率和幅值对时间步的敏感性。

参考：[官方 Helmholtz 共振算例](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance)。本页不将该扩展案例标记为本站已完整验证。
''','物理模型','uncertainty','v2512 thermophysicalModels、rhoPimpleFoam/laminar/helmholtzResonance；Wolf module8','heat-and-multiregion',75)

add('moving-mesh-and-ami','25 · 动网格、旋转参考系与 AMI','区分真实网格运动和参考系建模，理解运动边界、相对通量与网格质量随时间变化。',r'''
转动机械可以采用不同层次的模型。MRF 在选定区域使用旋转参考系描述效应，常用于某些稳态近似；真实滑移网格随时间转动，区域间通过接口交换；Overset 使用重叠网格和插值连接。它们的假设、守恒处理和代价不同。

![运动与耦合仍需保持单元收支一致](/assets/diagrams/core-finite-volume.svg)

网格运动后，对流相对于运动面发生。离散时既要追踪流体速度，又要处理网格面运动对体积和通量的影响。几何守恒不满足时，即使均匀场也可能产生非物理变化。

动网格通常涉及 `constant/dynamicMeshDict`、相应动态网格库、运动求解器与点位移或刚体参数。不同案例使用的网格类型差别很大，因此以完整官方算例建立第一步，比组合不同来源片段可靠。

```bash
# 先定位 v2512 的完整运动案例，再阅读它的 Allrun 和字典
ls "$FOAM_TUTORIALS/incompressible/pimpleFoam/laminar/movingCone"
find "$FOAM_TUTORIALS/incompressible/pimpleFoam/laminar/movingCone" \
  -name dynamicMeshDict -o -name pointDisplacement
```

这些命令只定位文件，不会执行计算。具体类型和库必须以该案例实际内容为准。

### AMI 接口需要检查什么

接口两侧的几何覆盖、面法向、区域连通性及插值权重都影响结果。网格运动过程中还要观察最差单元质量是否逐渐恶化。起始时刻 `checkMesh` 通过，不代表整个运动周期都有效。

建议按三个层次验收：先只检查运动轨迹和几何，确认位移、角速度和周期正确；再用尽可能简单的场检查运动与通量；最后加入真实流动，并比较质量收支和周期统计。对滑移网格，还需研究角步长与接口分辨率。

用 v2512 `mixerVesselAMI2D` 阅读区域、运动和接口文件，回答“哪里在运动、哪里保持静止、哪两个面交换数据”。不要仅凭渲染中转子在旋转就认为流固运动耦合正确。

参考：[v2512 pimpleFoam 运动案例](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar)。
''','物理模型','fvm','v2512 pimpleFoam/laminar/movingCone、mixerVesselAMI2D；Wolf 动网格资料仅作主题参考','simple-piso-pimple',80)

add('parallel-decompose-reconstruct','26 · 并行计算：分区、MPI、重构与效率','完成 decomposePar 到 reconstructPar 的闭环，理解小算例并行变慢、分区负载和浮点次序差异。',r'''
并行计算将网格分给多个进程，每个进程计算局部单元，并与邻接分区交换面数据。增加进程数减少了单个进程的单元数，也增加通信、同步和 I/O 开销，所以速度不会无限线性提升。

![四个进程的域分解示意](/assets/diagrams/core-parallel.svg)

在已经有有效网格的算例中，新建或修改 `system/decomposeParDict`。以下为使用 Scotch 的完整基础字典：

```foam
FoamFile
{
    format ascii;
    class dictionary;
    object decomposeParDict;
}
numberOfSubdomains 4;
method scotch;
```

确认安装含所需分解库，然后在算例副本中执行：

```bash
decomposePar > log.decomposePar 2>&1
mpirun -np 4 icoFoam -parallel > log.icoFoam.parallel 2>&1
reconstructPar -latestTime > log.reconstructPar 2>&1
```

MPI 进程数应与分区数一致。这里的 `icoFoam` 只用于方腔示例，其他案例要用自身求解器。若使用集群，应遵守调度器分配的核数和启动方式，不要在登录节点运行大规模任务。

### 并行验证先于性能宣传

比较同一网格、同一设置在串行与并行的中心线数据及积分量。浮点求和次序和分区路径变化可能产生小差异，严格逐位相同并非普遍要求；但显著差异必须排查分区、边界和处理流程。

速度比和效率定义为

\[
S_p=\frac{T_1}{T_p},\qquad E_p=\frac{S_p}{p}.
\]

记录计时范围：是否包含网格生成、分区、写盘和重构。400 单元方腔主要用来学习流程，通常不适合证明并行效率。对有意义的性能测试，固定问题规模并比较 1、2、4 个进程，说明硬件、MPI 和文件系统。

重构只处理指定时间的数据，不会自动替你判断结果是否完整。重新分区或清理旧 `processor*` 前，应确认哪些时间目录是唯一副本，并先归档需要的结果。
''','计算与数据分析','parallel','v2512 decomposePar、reconstructPar、decomposeParDict；Wolf module4 parallel','first-cavity-result',70)

add('sampling-functions-and-observables','27 · 采样、监测与 function objects','配置点探针、中心线采样、截面积分和时间平均，明确变量、数据位置、单位与统计窗口。',r'''
后处理的第一步是定义观测量。中心线速度用于比较流动剖面，面通量用于质量收支，压降与力用于工程目标。不同观测量需要不同几何区域与平均方式，不能把彩色图上的一个像素当作定量采样。

![线采样与截面采样的位置](/assets/diagrams/core-sampling.svg)

下面的点探针设置可加入 `controlDict` 的 `functions` 子字典，位置对应基础方腔内部：

```foam
functions
{
    cavityProbes
    {
        type probes;
        libs (sampling);
        writeControl timeStep;
        writeInterval 1;
        fields (p U);
        probeLocations
        (
            (0.05 0.05 0.005)
            (0.025 0.05 0.005)
        );
    }
}
```

如果已有 `functions`，应合并子对象，不要重复建立互相覆盖的同名键。探针位于流体域内，坐标以米为单位。运行后检查 `postProcessing/cavityProbes` 中的文件头、探针位置与时间列。

### 线采样要明确插值规则

`sets` 适合线与点集，`surfaces` 适合截面。使用 `cell` 或其他插值方式可能改变局部曲线，尤其在粗网格与强梯度区。比较不同网格时保持相同物理位置、坐标轴、分量与归一化方式，并记录插值选择。

### 时间平均的窗口有物理含义

瞬态计算开始后的启动阶段不应随意混入统计稳定阶段。时间平均速度定义为

\[
\overline{\mathbf{u}}=\frac{1}{T}\int_{t_0}^{t_0+T}\mathbf{u}(t)\,dt.
\]

`fieldAverage` 可以在运行时进行场平均。采用变时间步时，要区分按时间加权与按迭代次数平均；二者通常不相同。重启平均时还要明确是否延续已有累计信息。

每个 function object 对所需模型对象、运行模式和输出位置都有要求。不要假定所有对象均可通过通用 `postProcess` 独立重算；部分对象需要对应求解器的 `-postProcess` 或求解过程中执行。

**验收：**为方腔保留两个探针历史和两条中心线曲线，标出分量、单位与采样时刻。对入口出口案例，再给出通量平衡，解释质量通量与体积通量的区别。
''','计算与数据分析','sampling','v2512 src/sampling/probes、functionObjects/field/fieldAverage；Wolf module5 与 supplement3','parallel-decompose-reconstruct',75)

add('verification-validation-uncertainty','28 · 数值验证、物理确认与不确定性','区分代码与数值解验证、物理模型确认及不确定性来源，说明各类结论所需的证据和适用条件。',r'''
程序正常结束、线性残差降低、彩色图平滑，分别说明了某一层面的情况，却都不能独立证明预测可信。研究报告应将数值实现、数值解和物理模型的证据分开。

![离散、模型、输入和实验的不确定性来源](/assets/diagrams/core-uncertainty.svg)

代码验证关注实现是否正确，例如解析解、制造解或严格单元问题；解的数值验证关注当前计算中的网格、时间步和迭代误差；物理确认关注模型预测与相应实验或观测是否一致。不同中文资料对 verification/validation 的译名可能不同，因此报告中应明确你使用的定义。

### 三个层次的实例

一维常系数导热能检验离散与边界处理。方腔网格细化能检验数值解对分辨率的敏感性。实验管路压降对比则还涉及入口发展、壁面粗糙度、传感器精度和物性温度依赖。不能用第一个测试通过来替代后两项。

计算和实验都可能有不确定性。若将彼此独立、同一覆盖含义下的标准不确定度作近似组合，常见形式为

\[
u_c=\sqrt{u_1^2+u_2^2+\cdots+u_n^2}.
\]

相关输入需考虑协方差；系统偏差不能不加说明地塞入独立随机误差。离散误差估计也未必服从相同的统计解释，应清楚写出处理方法和限制。

### 面向初学者的最小证据表

| 证据 | 最少记录 | 主要排除的问题 |
| --- | --- | --- |
| 版本与输入 | 分支、构建、物性、边界、几何 | 用错程序或物理问题 |
| 网格与时间 | 质量、细化序列、时间步比较 | 分辨率不足 |
| 数值迭代 | 残差、守恒、目标量历史 | 解算未充分收敛 |
| 物理参照 | 解析、实验或可信基准及条件 | 模型假设不适用 |
| 后处理 | 位置、变量、单位、平均窗口 | 比较口径不一致 |

**练习：**审阅一张 CFD 图片，只依据附带资料判断哪些结论有证据、哪些需要补充。用精确表达替代“效果很好”：例如“在当前三组网格上，平均压降相对变化为某值；尚未检验入口扰动敏感性”。
''','验证与研究方法','uncertainty','Wolf module6 / supplement8；有限体积数值验证与误差分析基础','grid-time-verification',70)

add('reproducible-case-and-sharing','29 · 可复现算例的组织与共享','组织算例输入、运行脚本、环境记录、数据和图，注明执行顺序、检查方法及实际验证范围。',r'''
共享一个巨大结果文件夹，未必能让别人复现。高质量资料首先需要明确物理问题、软件版本、运行入口与检查方法；结果图是证据的一部分，而不是唯一交付物。

![可复现计算的输入、运行与证据](/assets/diagrams/core-reproducibility.svg)

推荐在算例外层保留一个简洁结构：

```text
case/             # 0、constant、system 与必要网格输入
scripts/          # 有明确工作目录和错误处理的运行脚本
results/          # 用于报告的 CSV、PNG 与后处理脚本
README.md         # 物理问题、版本、执行顺序、预期检查
environment.txt   # 系统、构建、编译器、MPI、后处理版本
```

把重建成本高的大网格或大量时间目录作为单独资源，并标注体积与是否必需。CAD、第三方脚本和原始资料应保留来源及许可证。公开分享前清除密码、令牌和私人绝对路径。

### 一个明确失败语义的运行脚本

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../case"
: "${WM_PROJECT_VERSION:?请先加载 OpenFOAM 环境}"
printf 'OpenFOAM=%s\n' "$WM_PROJECT_VERSION"
blockMesh 2>&1 | tee log.blockMesh
checkMesh 2>&1 | tee log.checkMesh
if grep -Eq 'Failed [1-9][0-9]* mesh checks' log.checkMesh; then
    printf '%s\n' '网格质量检查有失败项，请查看 log.checkMesh。' >&2
    exit 1
fi
icoFoam 2>&1 | tee log.icoFoam
```

这个脚本针对基础方腔，不适用于所有求解器。它遇到命令失败会停止，同时保存日志；另外识别 `checkMesh` 的明确失败汇总，因为质量失败未必通过非零退出码传递。日志格式变更时应核对这一判据，并继续人工检查网格警告和目标量。退出码是必要证据，但不是物理验证结论。

**README 至少写清楚：**算例做什么；采用哪些假设；需要哪个版本；从哪一目录执行哪些命令；结果存在哪里；什么数值或趋势说明流程合理；哪些功能仅经过启动检查、哪些完成了全时段计算、哪些经过网格研究。

上传到本站时，将课程讲解、可下载资源和讨论关联起来。问题帖优先附最小可复現输入、完整版本横幅、出错命令及最早异常日志。不要仅贴最后一行报错或没有色标的截图。

练习：请另一位同学仅阅读你的 README 运行方腔。如果需要口头补充路径、环境或缺失文件，就把这些信息写回资料中。可复现性通过实际复跑检验。
''','验证与研究方法','repro','本站资料组织规范；v2512 官方案例运行方式；Wolf 教学实践','sampling-functions-and-observables',55)

add('tool-paraview','ParaView · 场数据可视化与结果检查','介绍 OpenFOAM Reader、Slice、Plot Over Line 与固定色标，保存状态文件和批量出图脚本。',r'''
ParaView 是科学数据可视化工具。它读取已有结果，再通过过滤器生成截面、等值面、流线和曲线；本身不会替你判断输入算例是否物理正确。本站真实方腔图使用虚拟机中 ParaView 6.1.1 的 `pvpython` 生成。

![本站实际方腔速度大小结果](/assets/science/cavity-velocity.png)

在算例目录建立空标记文件 `cavity.foam`，在 ParaView 中用 OpenFOAM Reader 打开。选择需要的网格区域与字段后点 Apply，再选择目标时间。若看到初始静止状态，先检查时间而不是立即怀疑求解失败。

### 最值得掌握的四种操作

`Slice` 创建几何截面，适合观察内部结构；`Plot Over Line` 沿给定线段生成数据曲线；`Calculator` 从现有字段构造表达式；`Stream Tracer` 基于指定向量场生成流线。瞬时流线不是粒子在随时间变化流场中的完整轨迹。

OpenFOAM 体场通常是单元数据。`Cell Data to Point Data` 会产生插值后的点场，图可能更平滑，但不会增加实际网格分辨率。报告中应说明是 cell 还是 point 数据。见 [ParaView 数据模型](https://docs.paraview.org/en/latest/UsersGuide/understandingData.html)。

### 用脚本固定截图条件

以下脚本从当前算例生成最后时间的速度图，是可修改示例；在自己的 ParaView 版本中用 Trace 核对具体属性。

```python
from pathlib import Path
from paraview.simple import *

r = OpenFOAMReader(FileName=str(Path('cavity.foam').resolve()))
r.MeshRegions = ['internalMesh']
r.CellArrays = ['U', 'p']
scene = GetAnimationScene()
scene.UpdateAnimationUsingDataTimeSteps()
scene.GoToLast()
view = GetActiveViewOrCreate('RenderView')
display = Show(r, view)
ColorBy(display, ('CELLS', 'U', 'Magnitude'))
display.RescaleTransferFunctionToDataRange(True, False)
display.SetScalarBarVisibility(view, True)
ResetCamera(view)
SaveScreenshot('velocity.png', view, ImageResolution=[1600, 1100])
```

通过 `pvpython render.py` 运行；无图形会话时，还需与系统图形后端匹配的离屏设置。本站已经完成自己的离屏渲染流程，但这不证明每一种显卡与远程服务器配置都能无修改使用同一命令。

比较多张图时固定相机、色标范围、时间和数据分量。自动重标色标可能让两张差异很大的结果看起来相近。保存 `.pvsm` 状态或 Python 脚本，同时保留原始数据。截图、状态和数据的作用不同，见 [ParaView 保存结果说明](https://docs.paraview.org/en/latest/UsersGuide/savingResults.html)。

**小任务：**为方腔导出一张速度图、一条中心线 CSV 和一份状态文件；用另一时间重新打开状态，说明哪些设置保持一致。
''','扩展工具','/assets/science/cavity-velocity.png','ParaView 官方 Users Guide；Wolf supplement5；本站 ParaView 6.1.1 方腔渲染','first-cavity-result',65,kind='tool',verification='本站 ParaView 6.1.1 已生成 v2512 方腔图；本页通用脚本需按安装环境检查',series='OpenFOAM 扩展工具')

add('tool-gmsh','Gmsh · 参数化几何、物理分组与网格转换','用一个可追踪的三维盒子解释 Physical Groups、MSH 格式和 gmshToFoam 的边界映射。',r'''
Gmsh 将几何、网格及物理分组组织在同一套模型中，适合参数化几何和可重复生成的网格。对接 OpenFOAM 时，关键问题不是“能否显示网格”，而是体单元、边界名称、单位和法向是否完整传递。

![几何网格工具到 OpenFOAM 的接口位置](/assets/diagrams/core-ecosystem.svg)

Gmsh 的几何实体与 Physical Groups 是两个层次。前者描述点、曲线、面、体，后者把实体赋予求解意义。定义了物理组时，输出中哪些元素被保留受组和保存选项影响。因此只给入口和出口分组、却遗漏体区域，可能导出不完整的求解网格。见 [Gmsh 官方参考手册](https://gmsh.info/doc/texinfo/)。

### 一个最小盒子实验

下面是 `.geo` 教学示例。它只把所有外表面合成 `walls`，用于检查转换；尚未定义入口出口，不是完整管流算例。

```cpp
SetFactory("OpenCASCADE");
Box(1) = {0, 0, 0, 0.1, 0.02, 0.02};
Physical Volume("fluid") = {1};
b[] = Boundary{ Volume{1}; };
Physical Surface("walls") = {b[]};
Mesh.MeshSizeMin = 0.002;
Mesh.MeshSizeMax = 0.004;
Mesh.MshFileVersion = 2.2;
```

```bash
gmsh box.geo -3 -format msh2 -o box.msh
# 在已有 system/controlDict 的独立 OpenFOAM 算例目录运行
gmshToFoam box.msh > log.gmshToFoam 2>&1
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
```

选用 MSH 2.2 是便于建立明确的初始转换实验，不代表所有新格式都不受支持。实际接受的单元与版本应查安装的 v2512 `gmshToFoam -help-full`、源码和转换日志。

转换成功后查看 `constant/polyMesh/boundary`，检查 `walls` 是否存在、类型是否符合后续物理边界，体网格包围盒是否仍为 $0.1\times0.02\times0.02\,\mathrm{m}$。不能直接把原场文件的 patch 名称沿用到名称已变化的网格。

**扩展任务：**将左右端面分别建立为 `inlet`、`outlet`，其余面为 `walls`。先通过可视化和面积检查证明分组正确，再建立流场边界。Gmsh 在本站提供的是官方文档核对后的教学流程，尚未完成本机版本组合的端到端运行验证。
''','扩展工具','tools','Gmsh 官方 Reference Manual；v2512 applications/utilities/mesh/conversion/gmshToFoam','surface-geometry-preparation',70,kind='tool',verification='官方文档与 v2512 转换器源码核对；Gmsh 生成转换流程未在本站运行',series='OpenFOAM 扩展工具')

add('tool-salome','SALOME · 几何分组、体网格与 UNV 交换','面向图形化前处理建立命名明确的几何和网格组，并在转换后核对边界与体单元。',r'''
SALOME 提供几何建模和网格模块，适合通过图形界面建立局部网格控制、子网格与边界分组，也能保存 Python 操作脚本。选择它的理由应是当前几何和网格流程需要，而不是把图形界面视为自动保证网格质量。

![SALOME 在几何到求解的流程中的位置](/assets/diagrams/core-ecosystem.svg)

一个推荐的入门对象是长方体流道：先建立具有明确单位的实体，再分别创建入口面、出口面和壁面组。网格生成后，确认这些几何组对应所需网格面组，同时具有填充整个流体域的体单元。

### 通过 UNV 与 OpenFOAM 交换

SALOME SMESH 提供 UNV 导出接口。官方 API 列出的 `Mesh.ExportUNV` 属于网格导出，而不是 CAD 几何导出，见 [SMESH 官方文档](https://docs.salome-platform.org/latest/gui/SMESH/modules.html)。GUI 菜单位置可能随版本变化，应以安装版本为准。

```bash
# 在独立算例副本中，先查看安装版本的帮助
ideasUnvToFoam -help-full
ideasUnvToFoam channel.unv > log.ideasUnvToFoam 2>&1
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
```

算例仍需要 `system/controlDict` 等运行环境。转换后不应跳过检查直接求解。重点检查边界名、面数、面方向、长度单位、单元类型和是否存在意外内部面。

### 为什么几何组和网格组都需要看

几何分组建立在 CAD 实体上，后续布尔操作或重新分割可能改变实体标识；网格组则关联离散实体。修改几何后，旧分组未必仍表示原来的物理面。需要重新检查命名是否与实际位置一致。

不同网格算法和插件适合的几何不同，也可能具有不同的许可证和可用性。对接 v2512 时，先用小盒子确认一整条生成、导出、转换、检查流程，再扩大到复杂形状。这能把软件安装问题与几何问题分开。

**练习：**导出前后分别记录入口面积、总容积和包围盒，建立同一张比较表。若三项不能相互对应，即使转换日志没有报错，也不能认为前处理完成。本页未把该第三方软件组合标记为本站已运行验证。
''','扩展工具','tools','SALOME 官方 SMESH modules、UNV 导出；v2512 ideasUnvToFoam','checkmesh-and-quality',65,kind='tool',verification='SALOME 官方文档与 v2512 转换器核对；本机 SALOME 端到端流程未运行',series='OpenFOAM 扩展工具')

add('tool-pyvista','PyVista · Python 截面提取与数据分析','读取 .foam、多块网格与时间步，保留单元和点数据关联，编写用于批量比较的后处理脚本。',r'''
PyVista 为 VTK 数据结构与可视化提供 Python 接口。它适合在批处理中读取结果、生成截面、提取数据和制作一致风格的图片。它读取 OpenFOAM 文件，并不调用 OpenFOAM 离散方程求解器。

![从数据区域中提取一致的截面和采样线](/assets/diagrams/core-sampling.svg)

`OpenFOAMReader` 包装 VTK OpenFOAM Reader，可选择时间、网格 patch 和是否创建点数据。其默认 patch 选择与底层 VTK 默认行为并非完全相同，因此脚本应明确检查输出结构。见 [PyVista 官方 Reader 接口](https://docs.pyvista.org/api/readers/_autosummary/pyvista.openfoamreader)。

下面给出方腔脚本起点，假定当前目录已有 `cavity.foam` 和结果时间目录。本页代码是 API 核对后的示例，未在本站虚拟机执行。

```python
from pathlib import Path
import pyvista as pv

reader = pv.OpenFOAMReader(str(Path('cavity.foam').resolve()))
print('times:', reader.time_values)
reader.set_active_time_value(reader.time_values[-1])
data = reader.read()
print('blocks:', data.keys())
mesh = data['internalMesh']
print('cell fields:', mesh.cell_data.keys())
print('point fields:', mesh.point_data.keys())

section = mesh.slice(normal='z', origin=(0.05, 0.05, 0.005))
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(section, scalars='U', preference='cell', cmap='viridis')
plotter.view_xy()
plotter.show(screenshot='cavity-section.png')
```

向量字段可按模或分量显示；需要检查所用版本的显示选项，不能凭颜色猜测。输出为多块数据时，不要未经检查就把所有边界与内部场合并：这可能使积分区域或采样口径发生变化。

### 脚本比手动截图多承担哪些责任

必须显式选择时间和区域，记录读取器设置，处理缺失字段与空截面，并保存用于比较的数值，而不仅保存图片。离屏渲染仍依赖本地 VTK 构建与图形后端；`off_screen=True` 并不保证所有服务器无需额外环境。

采样曲线比较时，优先固定一条物理线和共同采样坐标，再比较各网格插值得到的值。将插值曲线与原始单元值区分，有助于发现“图更平滑但误差未减少”的情形。

**小任务：**把脚本改为读取指定时间，输出中心线数据到 CSV；遇到时间不存在、字段不存在时给出明确错误。另存软件版本记录，避免日后 API 变化造成不可复现。
''','扩展工具','sampling','PyVista 官方 OpenFOAMReader、set_active_time_value 与 Plotter API','sampling-functions-and-observables',65,kind='tool',verification='PyVista 官方 API 核对；此脚本未在本站安装环境执行',series='OpenFOAM 扩展工具')

add('tool-pyfoam','PyFoam · 运行管理、日志分析与参数实验','认识 PyFoam 的外部自动化定位，先建立版本隔离和最小运行，再扩展到参数扫描。',r'''
PyFoam 通过读取字典、启动程序和分析日志辅助 OpenFOAM 工作流，不需要把自己的 Python 代码链接进 OpenFOAM 求解器。它适合重复运行、监控和参数组织，但不会自动替你选择正确的物理模型。

![自动化工具管理输入、运行和输出](/assets/diagrams/core-reproducibility.svg)

本页指 Bernhard Gschaider 维护的 **PyFoam**，来源为 [项目 PyPI 页面](https://pypi.org/project/pyfoam/)。网上存在历史名称相似的其他项目，安装前应核对维护者与来源。本次查证的发布版本为 2026.6；这不代表它的每一项命令都已与本站 v2512 环境测试兼容。

### 在独立 Python 环境中试用

```bash
python3 -m venv "$HOME/venvs/foamlab-pyfoam"
source "$HOME/venvs/foamlab-pyfoam/bin/activate"
python -m pip install 'PyFoam==2026.6'
python -c "from importlib.metadata import version; print(version('PyFoam'))"
pyFoamPlotRunner.py --help
```

先加载正确 OpenFOAM 环境，再使用该 Python 环境。某些图形输出功能可能另有绘图库或外部程序依赖；在无桌面服务器上，先选择不依赖图形窗口的日志分析路径。

### 参数扫描要保存实验身份

设希望比较三个入口速度。为每个速度复制独立算例，保存“参数值、派生量 Re、输入文件哈希、程序版本、运行状态、目标量”的一行记录。一个目录应对应一个清晰的实验身份，避免在同一目录反复覆盖旧输入。

自动修改字典后先解析并检查，不要立即提交数百个长任务。先运行最小网格和短时间，确认参数确实进入目标条目、输出文件互不覆盖，再执行完整计算。使用相同日志解析器时，也要确认 v2512 的日志格式与解析规则匹配。

可以先用一份成功的 `log.icoFoam` 做离线分析，对照原始日志核查时间和残差列，再使用运行包装器。解析出漂亮曲线并不说明物理上收敛；残差、守恒与目标量仍需联合判断。

**小任务：**设计包含三组参数的 CSV 任务表，不必先上复杂自动化框架。把其中一组手动流程完整复现，再让自动化执行完全相同的步骤。本文提供接入路线，未声称 PyFoam/v2512 组合已在本站完成端到端测试。
''','扩展工具','repro','PyFoam 维护者发布的 PyPI 页面（2026.6）；v2512 运行日志结构','reproducible-case-and-sharing',60,kind='tool',verification='官方项目页核对；PyFoam 2026.6 与本机 v2512 组合尚未运行验证',series='OpenFOAM 扩展工具')

add('tool-freecad-geometry','FreeCAD 与几何工具 · 实体建模与 CFD 表面导出','保留 CAD 源文件，控制单位和三角化误差，记录几何简化、表面导出与网格检查过程。',r'''
FreeCAD 等 CAD 工具适合建立尺寸可编辑的实体；STL/OBJ 则适合把外表面传给某些网格流程。原生 CAD、STEP 和 STL 应保留各自角色：源几何用于修改，交换几何用于协作，三角表面用于特定离散步骤。

![CAD 与三角化表面的区别](/assets/diagrams/core-cad-tessellation.svg)

FreeCAD 的官方 STL/OBJ 导出说明强调了网格文件的单位问题，并说明直接导出与先建立 Mesh 对象的两条路径，见 [官方 FreeCAD 文档仓库](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Export_to_STL_or_OBJ.md)。具体界面名称和网格选项以安装版本为准。

### 一个小管道模型的前处理实验

先建立内径、长度和壁厚可追踪的管道实体，明确 CFD 需要的是**流体域**还是固体材料。若研究内流，只导出外部金属表面往往无法表达预期流体空间；应建立流体体积或具有适当开口与区域的边界表面。

对弯管，比较两组三角化容差。较粗表面可能把圆截面变成明显多边形，影响最小间隙和局部曲率；过细表面则增加处理成本。判断标准应是目标几何误差和网格需求，而不是 STL 文件越大越好。

```bash
surfaceCheck bend.stl > log.surfaceCheck 2>&1
surfaceTransformPoints -help-full
```

记录 CAD 单位与 OpenFOAM 包围盒，检查封闭性、退化面及法向一致性。经过尺度转换后再次检查。几何修补不能只以“工具不再报错”为目标，应保证修补没有封住原本的入口或改变关键流道尺寸。

### 常见工具怎样分工

CAD 工具处理参数化尺寸与布尔运算；表面处理工具检查和修复三角面；Gmsh、SALOME 或 snappyHexMesh 构造体网格；ParaView 检查最终网格和场。某些软件同时覆盖多个阶段，但交付物的数据类型仍需要明确。

**验收：**提交源 CAD、一个表面文件、三角化参数、单位转换记录以及最终网格包围盒。绘制入口与出口的命名示意，说明它们如何映射到 OpenFOAM patch。第三方 GUI 操作路线尚未在本站环境逐项运行，几何单位与转换器检查按 v2512 主线解释。
''','扩展工具','cad','FreeCAD 官方文档 Export to STL or OBJ；v2512 surfaceCheck / surfaceTransformPoints；Wolf module2','surface-geometry-preparation',60,kind='tool',verification='官方导出文档和 v2512 表面工具核对；FreeCAD GUI 流程未在本站运行',series='OpenFOAM 扩展工具')

add('foamlab-build-log-2026-10','建设日志 · 以 v2512 为基线重新组织学习资料','说明课程来源、版本适配、图片证据和内容维护原则，公开区分已运行、已核对与待验证的内容。',r'''
本次重整把学习路径从固定讲次数量改为可扩展的课程与专题：先认识环境和算例，再学习网格与数值方法，随后进入物理模型、计算分析、编程和扩展工具。命令与配置索引承担查询功能，课程负责解释为什么使用这些条目以及如何检查结果。

![学习资料需要能追溯到输入和证据](/assets/diagrams/core-reproducibility.svg)

### 资料来源与版本处理

Wolf Dynamics 的基础培训为教学顺序、算例组织和有限体积概念提供参考。用户提供的基础资料采用 Foundation 9；本站运行基线是 OpenCFD v2512，所以保留概念关联，同时根据 v2512 官方教程和源码核对文件、命令与设置。这里是重新编写的中文课程，不是把旧幻灯片原样改一个版本号。

`BasicOFProgramming` 纳入编程路径；`OF_material` 中已适配的代码优先作为示例来源。适配记录中的字典解析、Shell 语法检查、网格检查和短时求解，分别提供不同层次的证据。它们不能自动等同于所有案例已完成长时间计算或网格无关性研究。

### 图片的三类证据

原创 SVG 图用于解释控制体积、网格、耦合和工作流，属于示意图。本站生成的方腔速度图来自实际 v2512 运行，参数和时间写在课程图注中。首页视觉封面是 CFD 概念插画，不应被引用为真实求解结果。阅读、下载和再次分享时，请保留这个区别。

首次方腔使用官方基础设置：$20\times20\times1$ 网格、$Re=10$、结束时间 $0.5\,\mathrm{s}$。这次运行用于验证求解与出图流程，没有被描述为网格独立验证。以后扩展结果应附输入、日志、脚本和必要的数值数据。

### 下一步如何增加内容

一篇可发布的课程至少需要清楚的问题、版本、具体示例、必要图解、可检查的结果及来源。新命令条目要区分主仓库程序、Shell 工具、可选模块和第三方软件；新配置示例要注明它适用的求解器与模型。改名、迁移或删除内容时，优先保留读者能追踪的修订记录。

欢迎通过讨论中心提交可复现问题，也欢迎补充运行记录和纠错。提问时附版本横幅、命令、最早异常日志与最小输入；回答时说明结论依据和适用条件。维护者会优先合并能够重现、能够核对的改进。

来源：[Wolf Dynamics 培训资料入口](https://www.wolfdynamics.com/tutorials.html?id=181&layout=edit)、[OpenCFD v2512 源码标签](https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512)。
''','作者专栏','repro','FoamLab 建设记录；用户提供材料；OpenCFD v2512 官方源码','无',10,kind='log',verification='建设过程与证据边界说明；具体功能是否上线以网站实际状态为准',series='FoamLab 建设与维护')

if __name__ == '__main__':
    output=Path(__file__).with_name('core-content.json')
    output.write_text(json.dumps(ITEMS,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'items':len(ITEMS),'lessons':sum(x['kind']=='lesson' for x in ITEMS),'tools':sum(x['kind']=='tool' for x in ITEMS),'logs':sum(x['kind']=='log' for x in ITEMS),'svg':len(list(OUT.glob('core-*.svg'))),'body_characters':sum(len(x['body']) for x in ITEMS),'output':str(output)},ensure_ascii=False))
