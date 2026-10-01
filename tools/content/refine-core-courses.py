"""Refine the 29 core lessons and build complete, versioned course case downloads.

This is a post-processor, not a replacement for build-core.py. Rebuild order:
  python tools/content/build-core.py
  python tools/content/refine-core-courses.py --base tools/content/core-content.json
For this revision the preserved, pre-refinement input is also available at
.openfoam-work/course-refinement/core-content.json. The default uses that backup
when present, otherwise the current unrefined core-content.json. Re-running with
the same baseline/source archive is deterministic. No database writes occur.
Official files are copied byte for byte; symlinks are resolved into equivalent
regular files for portable ZIP extraction and recorded in SYMLINKS.txt.
New FoamLab exercises are separately identified. Packaging checks are not CFD
validation; any actual run evidence must be explicitly added to the README.
"""
from __future__ import annotations
import argparse, hashlib, json, math, posixpath, re, tarfile, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARCHIVE=ROOT/'.openfoam-work/replan/openfoam-v2512.tar.gz'
TARGET=ROOT/'tools/content/core-content.json'
BACKUP=ROOT/'.openfoam-work/course-refinement/core-content.json'
DEST=ROOT/'source-openfoam/downloads/courses'
UPSTREAM='openfoam-OpenFOAM-v2512/'
SOURCE='https://gitlab.com/openfoam/core/openfoam/-/archive/OpenFOAM-v2512/openfoam-OpenFOAM-v2512.tar.gz'
REVISION='core-readability-cases-2026-10-02-v1'
SHA=lambda b:hashlib.sha256(b).hexdigest()

PACKS={
 'v2512-cavity':dict(title='方腔与基础计算',cases=['incompressible/icoFoam/cavity'],resources=[],start='tutorials/incompressible/icoFoam/cavity/cavity',commands='blockMesh > log.blockMesh 2>&1\ncheckMesh > log.checkMesh 2>&1\nicoFoam > log.icoFoam 2>&1',notes='从 cavity/cavity 基础案例开始。外层 cavity/Allrun 会依次创建或处理 cavityFine、cavityGrade、cavityHighRe、cavityClipped，包含映射和雷诺数变化，不是单一网格细化实验。不要把这些不同物理条件的案例直接当成网格收敛序列。基础条件为 L=0.1 m、顶盖速度 1 m/s、nu=0.01 m²/s、Re=10，20×20×1 网格。本站已有该基础案例 t=0.5 s 的实际运行图；本次打包没有重跑整个案例组。'),
 'v2512-meshing-rans':dict(title='网格划分与 RANS',cases=['incompressible/simpleFoam/pitzDaily','incompressible/simpleFoam/motorBike'],resources=['motorBike.obj.gz'],start='tutorials/incompressible/simpleFoam/pitzDaily',commands='blockMesh > log.blockMesh 2>&1\ncheckMesh > log.checkMesh 2>&1\nsimpleFoam > log.simpleFoam 2>&1',notes='pitzDaily 使用 blockMesh，是学习稳态分离流、入口出口与湍流边界的较小起点。motorBike 使用完整 snappyHexMesh 流程，几何已附在 tutorials/resources/geometry/motorBike.obj.gz。先 source 包根目录 environment.sh，确保 Allrun 从本包复制几何；随后在 motorBike 内运行 ./Allrun。官方脚本采用 system/decomposeParDict.6，需要 MPI 与相应进程资源；不要直接用一条串行 snappyHexMesh 命令代替全部初始化。0.orig/include 已完整保留；0/ 和 processor*/0/ 由 restore0Dir 生成。motorBike 的 post-processing 包含多个对象，额外输出会消耗磁盘空间。本包没有本轮求解结果或性能保证。'),
 'v2512-scalar-diffusion':dict(title='标量输运与扩散',cases=['basic/scalarTransportFoam/pitzDaily','basic/laplacianFoam/flange'],resources=['flange.ans'],start='exercises/one-dimensional-diffusion',commands='bash Allrun',notes='exercises/ 中是 FoamLab 单独编写的两个最小教学输入，非官方已验证教程：one-dimensional-diffusion 对照一维线性温度解；one-dimensional-advection 对照紧支撑余弦平方脉冲的平移。它们的 README 说明参数、比较方法和运行状态。官方 scalarTransportFoam/pitzDaily 自带速度场，包含非零物理扩散，不能把其结果称作严格无扩散平移。其 Allrun 会额外创建兄弟目录 pitzDaily-stepFunction。官方 flange 的 Allrun 先恢复 0，再由 ansysToFoam 将已附 flange.ans 按 0.001 缩放导入；不要省略单位转换。运行这两个官方案例前均先在包根目录 source environment.sh。'),
 'v2512-vof-dambreak':dict(title='VOF 多相流与溃坝',cases=['multiphase/interFoam/laminar/damBreak'],resources=[],start='tutorials/multiphase/interFoam/laminar/damBreak/damBreak',commands='bash Allrun',notes='从内层 damBreak/Allrun 启动基础算例，它依次恢复 0.orig、生成网格、setFields 初始化和运行 interFoam。外层 Allrun 可创建 damBreakFine 并进行并行计算，需要额外资源。0.orig/alpha.water 不是最终初始水柱，setFields 后才建立本课指定水域；在运行前保存 alpha.water 截面。原始字典的 maxCo、maxAlphaCo、nAlphaSubCycles 应分别阅读，不能仅观察速度场 Co。本包只核验源码、路径与依赖，没有本轮溃坝计算结果。'),
 'v2512-conjugate-heat':dict(title='多区域共轭传热',cases=['heatTransfer/chtMultiRegionFoam/multiRegionHeater'],resources=[],start='tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater',commands='bash Allrun',notes='Allrun.pre 依次 blockMesh、topoSet、恢复场、splitMeshRegions，并为区域应用 changeDictionary。区域包括 bottomWater、topAir、heater、leftSolid、rightSolid；请以 constant/regionProperties 为准。官方 Allrun 默认分区并行求解、再重构全部区域，需要 MPI；每个区域的 decomposeParDict 均已包含。原始相对软链接已展开成同内容普通文件，避免 Windows 解压后丢失链接。对照 SYMLINKS.txt 可查原目标；未来修改 heater 物性时，展开后的 leftSolid/rightSolid 副本不会自动同步，需要分别核对。本包未运行多区域求解。'),
 'v2512-compressible-acoustics':dict(title='可压缩流动与声学共振',cases=['compressible/rhoPimpleFoam/laminar/helmholtzResonance'],resources=[],start='tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance',commands='bash Allrun -test',notes='Allrun 分别创建 resolved 与 modelled 两种腔室表示，先在 system/ 生成 blockMeshDict.caseBlocks 和 caseBoundary 的相对链接，再克隆并分区求解。请通过 Allrun 启动，不要在尚未生成链接时直接运行 blockMesh。-test 仅跳过脚本末尾可选的 gnuplot 作图分支，仍会进行这两种计算，并不是只做输入检查。必须有 MPI；如果另外运行不带 -test 的 Allrun，需安装 gnuplot。此案例实际采用 eConst + sensibleInternalEnergy，不能把课文中的焓形式示意原封不动替换进来。本包未运行声学求解。'),
 'v2512-moving-ami':dict(title='动网格与 AMI',cases=['incompressible/pimpleFoam/laminar/movingCone','incompressible/pimpleFoam/laminar/mixerVesselAMI2D'],resources=[],start='tutorials/incompressible/pimpleFoam/laminar/movingCone',commands='blockMesh > log.blockMesh 2>&1\ncheckMesh > log.checkMesh.initial 2>&1\npimpleFoam > log.pimpleFoam 2>&1',notes='movingCone 使用 velocityComponentLaplacian 和 pointMotionUx，先阅读真实字段，不要按名称猜成 pointDisplacement。两个 mixerVesselAMI2D 子案例各有 Allrun 和 Allrun.pre，后者使用 m4 生成 blockMeshDict 并运行 topoSet；前者恢复场、分区和并行 pimpleFoam，需 m4 与 MPI。普通子案例采用 reconstructPar，拓扑变化子案例使用 redistributePar -reconstruct；请保留各自脚本。观察全过程网格质量与接口覆盖，不能仅检查 t=0 的网格。本包未运行这些动网格计算。'),
}

def foam_header(name,cls='dictionary'):
 return f'// FoamLab teaching input for OpenCFD OpenFOAM v2512. GPL-3.0-or-later.\nFoamFile\n{{\n    format ascii;\n    class {cls};\n    object {name};\n}}\n'

def exercise_files():
 """Generate two minimal cases; every file is distinguished from upstream."""
 out={}
 for name,n,length,solver in [('one-dimensional-diffusion',40,0.1,'laplacianFoam'),('one-dimensional-advection',200,1.0,'scalarTransportFoam')]:
  prefix='exercises/'+name+'/'
  def put(p,b):out[prefix+p]=b.encode('utf-8')
  adv=solver=='scalarTransportFoam'
  put('system/blockMeshDict',foam_header('blockMeshDict')+f'''scale 1;
vertices ((0 0 0) ({length} 0 0) ({length} 0.01 0) (0 0.01 0)
          (0 0 0.01) ({length} 0 0.01) ({length} 0.01 0.01) (0 0.01 0.01));
blocks (hex (0 1 2 3 4 5 6 7) ({n} 1 1) simpleGrading (1 1 1));
edges ();
boundary
(
    left  {{type patch; faces ((0 4 7 3));}}
    right {{type patch; faces ((1 2 6 5));}}
    sides {{type empty; faces ((0 1 5 4) (3 7 6 2) (0 3 2 1) (4 5 6 7));}}
);
mergePatchPairs ();
''')
  pulse=lambda x:math.cos(math.pi*(x-0.25)/(2*0.1))**2 if abs(x-0.25)<0.1 else 0.
  internal=('nonuniform List<scalar>\n'+str(n)+'\n(\n'+'\n'.join(f'{pulse((i+.5)*length/n):.12g}' for i in range(n))+'\n)') if adv else 'uniform 300'
  right='type zeroGradient;' if adv else 'type fixedValue; value uniform 300;'
  put('0/T',foam_header('T','volScalarField')+f'dimensions [0 0 0 1 0 0 0];\ninternalField {internal};\nboundaryField\n{{\n left {{type fixedValue; value uniform {0 if adv else 400};}}\n right {{{right}}}\n sides {{type empty;}}\n}}\n')
  if adv:put('0/U',foam_header('U','volVectorField')+'dimensions [0 1 -1 0 0 0 0];\ninternalField uniform (1 0 0);\nboundaryField\n{\n left {type fixedValue; value uniform (1 0 0);}\n right {type zeroGradient;}\n sides {type empty;}\n}\n')
  put('constant/transportProperties',foam_header('transportProperties')+f'DT [0 2 -1 0 0 0 0] {0 if adv else "1e-5"};\n')
  put('system/controlDict',foam_header('controlDict')+f'''application {solver};
startFrom startTime;
startTime 0;
stopAt endTime;
endTime {0.2 if adv else 1};
deltaT {0.001 if adv else 1};
writeControl timeStep;
writeInterval {50 if adv else 1};
purgeWrite 0;
writeFormat ascii;
writePrecision 12;
writeCompression off;
timeFormat general;
timePrecision 10;
runTimeModifiable false;
''')
  div='div(phi,T) Gauss upwind;' if adv else ''
  put('system/fvSchemes',foam_header('fvSchemes')+f'''ddtSchemes {{default {"Euler" if adv else "steadyState"};}}
gradSchemes {{default Gauss linear;}}
divSchemes {{default none; {div}}}
laplacianSchemes {{default Gauss linear orthogonal;}}
interpolationSchemes {{default linear;}}
snGradSchemes {{default orthogonal;}}
''')
  put('system/fvSolution',foam_header('fvSolution')+('''solvers
{
    T {solver SOLVER; preconditioner PRECONDITIONER; tolerance 1e-12; relTol 0;}
}
SIMPLE {nNonOrthogonalCorrectors 0;}
'''.replace('SOLVER','PBiCGStab' if adv else 'PCG').replace('PRECONDITIONER','DILU' if adv else 'DIC')))
  put('Allrun',f'''#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${{WM_PROJECT_VERSION:?Load OpenCFD OpenFOAM v2512 first}}"
blockMesh > log.blockMesh 2>&1
checkMesh -allGeometry -allTopology > log.checkMesh 2>&1
if grep -Eq 'Failed [1-9][0-9]* mesh checks' log.checkMesh; then
    echo 'Mesh checks failed: read log.checkMesh' >&2; exit 1
fi
{solver} > log.{solver} 2>&1
python3 compare.py
''')
  put('compare.py',f'''"""Compare the unmodified teaching case against its analytic reference.
Run after Allrun. Changes to mesh, length, velocity or endTime require updating
this explicit comparison as well. Source: FoamLab, GPL-3.0-or-later.
"""
import csv, math, re
from pathlib import Path
n, length, time = {n}, {length}, {0.2 if adv else 1}
file=Path(__file__).parent / str(time) / 'T'
text=file.read_text()
match=re.search(r'internalField\\s+nonuniform\\s+List<scalar>\\s+(\\d+)\\s*\\((.*?)\\)\\s*;',text,re.S)
if match:
 values=[float(x) for x in match.group(2).split()]
 assert int(match.group(1))==len(values)==n
else:
 match=re.search(r'internalField\\s+uniform\\s+([^;]+);',text)
 if not match: raise ValueError('ASCII internalField not found')
 values=[float(match.group(1))]*n
def expected(x):
 {'x=x-time; return math.cos(math.pi*(x-0.25)/0.2)**2 if abs(x-0.25)<0.1 else 0.0' if adv else 'return 400-100*x/length'}
rows=[((i+.5)*length/n,v,expected((i+.5)*length/n)) for i,v in enumerate(values)]
with (file.parent.parent/'comparison.csv').open('w',newline='') as f:
 writer=csv.writer(f); writer.writerow(['x_m','T_computed','T_reference']); writer.writerows(rows)
print('mean_absolute_error=',sum(abs(v-r) for _,v,r in rows)/n)
print('maximum_absolute_error=',max(abs(v-r) for _,v,r in rows))
print('computed_min_max=',min(values),max(values))
print('line_integral=',sum(values)*length/n)
''')
  explanation=('一维无物理扩散标量平移：长度 1 m，速度 1 m/s，200 个单元，deltaT=0.001 s，Co=0.2，结束时刻 0.2 s。初值是在 0.15–0.35 m 内的 cos² 脉冲，中心 0.25 m，峰值 1；解析参考在 0.2 s 时平移到中心 0.45 m。初值与入口均为零的域外部分相容，脉冲在测试时间内不经过出口。本例 T 可解释为幅值 1 K 的被动温差，不是绝对热力学温度，也不求完整能量耦合。基线采用 Euler + upwind，预计脉冲展宽，不能期待机器精度匹配。比较时分别修改 div(phi,T) 为 Gauss linear 或 Gauss limitedLinear 1，并保留独立副本。守恒核查要计入边界通量；原脉冲线积分为 0.1 K·m。' if adv else '一维稳态温度扩散：长度 0.1 m，40 个单元，左端 400 K，右端 300 K，DT=1e-5 m²/s。fvSchemes 使用 steadyState，所以目录 1 是稳态迭代标识，不是等待了 1 s 的瞬态解。解析解 T=400-100*x/0.1。在这一均匀正交网格与常系数设置下，线性温度解应能很好重现。DT 是热扩散率，不是导热系数；若要按课文算热流密度，另指定 k=10 W/(m K)，得到正 x 方向 10000 W/m²。该输入只含一种均匀材料，没有自动实现两材料交界练习。')
  put('README.zh-CN.md',f'# {name}\n\nFoamLab 针对 OpenCFD OpenFOAM v2512 编写的教学输入，GPL-3.0-or-later。\n\n{explanation}\n\n在已加载 v2512 的 Linux 终端，从本目录运行 `bash Allrun`。先看 log.blockMesh 与 log.checkMesh，再看求解器日志；compare.py 读取 ASCII 最终 T，写出 comparison.csv 并打印误差。脚本常量对应原始网格、速度与结束时刻，修改这些参数后必须同步修改对照脚本，不能沿用旧坐标或旧参考。\n\n运行状态：教学输入已按 v2512 源码读取项核对；实际核验记录若已附于包内 RUN-VERIFICATION.txt，以该文件记录的输入哈希、版本和范围为准。没有该记录时，仅表示已经生成和检查输入文件，不表示完成求解。\n')
 return out

def dependencies(files,all_members,tar):
 report=[];generated={
  'tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance/system/blockMeshDict.caseBlocks':'Allrun creates a symlink to blockMeshDict.resolvedBlocks or blockMeshDict.modelledBlocks',
  'tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance/system/blockMeshDict.caseBoundary':'Allrun creates a symlink to blockMeshDict.resolvedBoundary or blockMeshDict.modelledBoundary',
 }
 for p,b in files.items():
  if len(b)>100000 or p.endswith(('.gz','.ans')):continue
  txt=b.decode('utf-8',errors='replace')
  for kind,name in re.findall(r'#(includeEtc|include)\s+"([^"]+)"',txt):
   if kind=='includeEtc':
    assert UPSTREAM+'etc/'+name in all_members,(p,name)
    report.append(f'SYSTEM v2512 etc/{name} <- {p}')
   else:
    resolved=posixpath.normpath(posixpath.join(posixpath.dirname(p),name))
    if resolved in files:report.append(f'INCLUDED {resolved} <- {p}')
    elif resolved in generated:report.append(f'GENERATED {resolved}: {generated[resolved]}')
    else:raise ValueError(f'Missing include {name} in {p}')
  for func in re.findall(r'#includeFunc\s+(\w+)',txt):
   candidates=[n for n in all_members if '/etc/caseDicts/postProcessing/' in n and n.endswith('/'+func)]
   assert candidates,(p,func)
   report.append(f'SYSTEM function template {candidates[0].removeprefix(UPSTREAM)} <- {p}')
 for geom in ['motorBike.obj.gz','flange.ans']:
  users=[p for p,b in files.items() if p.endswith('Allrun') and geom.encode() in b]
  if users:
   assert 'tutorials/resources/geometry/'+geom in files
   report.append('BUNDLED geometry tutorials/resources/geometry/'+geom+' <- '+', '.join(users))
 for p,b in files.items():
  if p.endswith('Allrun') and b'./Allrun.pre' in b:assert posixpath.join(posixpath.dirname(p),'Allrun.pre') in files
  if p.endswith('Allrun.pre') and b'm4 system/blockMeshDict.m4' in b:assert posixpath.join(posixpath.dirname(p),'system/blockMeshDict.m4') in files
 report+=['SYSTEM OpenCFD v2512 binaries/libraries and $WM_PROJECT_DIR/bin/tools/RunFunctions are required, not bundled.',
 'SYSTEM #includeEtc templates were checked against this same v2512 archive; runtime uses the installed version.',
 'GENERATED 0 from 0.orig, polyMesh, processor directories, cloned cases and mesh-selection links are outputs of the documented Allrun steps, not missing input.',
 'The original Allrun/Allclean scripts are unchanged. Run Allrun only in an extracted working copy. Allclean removes results; it is not a setup step.']
 return '\n'.join(report)+'\n'

def build_packages():
 DEST.mkdir(parents=True,exist_ok=True);manifest={};archive_sha=SHA(ARCHIVE.read_bytes())
 with tarfile.open(ARCHIVE) as tar:
  members={m.name:m for m in tar.getmembers()};copyright_bytes=tar.extractfile(UPSTREAM+'COPYING').read()
  for key,cfg in PACKS.items():
   files={};modes={};links=[];upstream_hashes=[]
   prefixes=[UPSTREAM+'tutorials/'+p+'/' for p in cfg['cases']]
   extras={UPSTREAM+'tutorials/resources/geometry/'+p for p in cfg['resources']}
   for name,m in members.items():
    if not (any(name.startswith(p) for p in prefixes) or name in extras) or m.isdir():continue
    p=name.removeprefix(UPSTREAM)
    if m.issym() or m.islnk():
     target=posixpath.normpath(posixpath.join(posixpath.dirname(name),m.linkname)) if m.issym() else m.linkname
     assert target in members and any(target.startswith(pref) for pref in prefixes),(name,target)
     links.append(f'{p} -> {m.linkname} [materialized regular file]')
    b=tar.extractfile(m).read();files[p]=b;modes[p]=0o644 if m.issym() or m.islnk() else m.mode;upstream_hashes.append(f'{SHA(b)}  {p}')
   if key=='v2512-scalar-diffusion':files.update(exercise_files())
   report=dependencies(files,members,tar)
   files['COPYING']=copyright_bytes
   files['SOURCE.txt']=(f'OpenCFD OpenFOAM v2512 official source archive\n{SOURCE}\nArchive SHA-256: {archive_sha}\n\nSelected tutorial source files remain byte-for-byte unchanged. Copyright headers are retained. Original relative symlinks are materialized as regular files containing the resolved upstream bytes; see SYMLINKS.txt. No compiled OpenFOAM binary is redistributed. The upstream OpenFOAM source is GPL version 3 or later; see COPYING and individual file notices. FoamLab README, environment helper and exercises: GPL-3.0-or-later. No endorsement by OpenCFD is implied.\n').encode()
   files['UPSTREAM.sha256']=('\n'.join(sorted(upstream_hashes))+'\n').encode()
   files['SYMLINKS.txt']=('\n'.join(links) if links else 'No upstream symlinks in this selection.').encode()
   files['DEPENDENCIES.txt']=report.encode()
   files['environment.sh']=b'''# Source from Bash after loading the installed OpenCFD v2512 environment.
# This points tutorial resources at this package, not at the software install.
: "${WM_PROJECT_DIR:?Load OpenCFD OpenFOAM v2512 before sourcing this file}"
case "$WM_PROJECT_VERSION" in v2512|2512) ;; *) echo "Expected v2512, found $WM_PROJECT_VERSION" >&2; return 1 ;; esac
export FOAM_TUTORIALS="$(cd "$(dirname "${BASH_SOURCE[0]}")/tutorials" && pwd)"
printf 'Using packaged tutorial resources: %s\n' "$FOAM_TUTORIALS"
'''
   selected='\n'.join('- `tutorials/'+p+'`' for p in cfg['cases'])
   files['README.zh-CN.md']=(f'''# {cfg['title']} · OpenCFD OpenFOAM v2512

## 先找对运行目录

本包用于配套课程，包含原始输入，不是软件安装包，也不把打包检查称作物理验证。先解压到自己可写的 Linux 工作目录，再进入 `{key}`；保留一个未改动副本用于对照。

官方案例目录：
{selected}

建议起点：`{cfg['start']}`。

```bash
# 在新终端中先加载已安装 v2512 的环境；路径以你的安装为准
source /usr/lib/openfoam/openfoam2512/etc/bashrc
echo "$WM_PROJECT_VERSION"
blockMesh -help
# 以下命令从本包根目录执行
source ./environment.sh
cd {cfg['start']}
{cfg['commands']}
```

每一步都检查退出码和日志；前一步失败时停止，不要继续执行。`checkMesh` 还应检查失败项汇总，不能只看 Shell 退出码。脚本需要 Linux Shell，不能在 Windows PowerShell 中直接执行 OpenFOAM 命令。MPI、m4、Python 3、gnuplot 等额外工具按具体案例说明准备。

## 这个合集怎样用于练习

{cfg['notes']}

官方 Allrun 使用 `$WM_PROJECT_DIR/bin/tools/RunFunctions`，`#includeEtc` 使用已安装 v2512 的模板，因此必须安装完整、同分支同版本的 OpenFOAM。environment.sh 只将 FOAM_TUTORIALS 指向本包 tutorials，并不替换 WM_PROJECT_DIR；请在专用终端中使用。它使几何资源从本包读取，不依赖另一套教程的位置。部分字典宏里的 `${{../name}}` 是字典作用域引用，并不是缺失的父目录文件。

## 对照与运行证据

包内原始教程文件、资源、包含文件及相对链接已经逐项核对；不等于已完成这些案例的 CFD 计算。除方腔课程明确引用的既有基础运行外，本轮官方合集没有新增完整求解证据。FoamLab 新教学案例如有 RUN-VERIFICATION.txt，应按其版本、输入哈希和运行范围阅读，不能外推到整个合集。

计算结果通常写到案例时间目录；监测对象写入 postProcessing/。先核对单位、边界与日志，再看图。比较不同设置时建立独立副本，记录改动；不要将一个案例的结果图作为另一个参数组合的证据。

## 来源、许可与完整性

来源与版本见 SOURCE.txt，完整 GPL 文本见 COPYING；原始版权头和字典代码保留。UPSTREAM.sha256 记录原始文件内容哈希，SYMLINKS.txt 记录为跨平台解压展开的链接，DEPENDENCIES.txt 记录包含关系、系统依赖和生成步骤。MANIFEST.sha256 可用于检查下载后文件完整性。

本包由 `tools/content/refine-core-courses.py` 生成；课程文字在旧 `build-core.py` 生成后由该脚本后处理。无需重新编辑官方源文件即可重新生成同一下载包。
''').encode()
   evidence=ROOT/'.openfoam-work/course-refinement/RUN-VERIFICATION.txt'
   if key=='v2512-scalar-diffusion' and evidence.exists():
    files['RUN-VERIFICATION.txt']=evidence.read_bytes()
    proof=ROOT/'.openfoam-work/course-refinement/evidence'
    # Never label changed teaching inputs as verified by an older run.
    for name in ['one-dimensional-diffusion','one-dimensional-advection']:
     for line in (proof/name/'inputs.sha256').read_text().splitlines():
      digest,input_path=line.split(None,1)
      assert SHA(files['exercises/'+name+'/'+input_path.strip()])==digest,(name,input_path,'stale run evidence')
     assert 'Mesh OK.' in (proof/name/'log.checkMesh').read_text()
    for p in sorted(proof.rglob('*')):
     if p.is_file():
      rel=p.relative_to(proof).as_posix();b=p.read_bytes()
      if p.suffix!='.png':b=b.replace(b'/home/shark/foamlab-website-20261002/course-refinement-r2/v2512-scalar-diffusion',b'<verification-workdir>')
      files['verification/'+rel]=b
   files['MANIFEST.sha256']=('\n'.join(f'{SHA(b)}  {p}' for p,b in sorted(files.items()))+'\n').encode()
   target=DEST/(key+'.zip')
   with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,b in sorted(files.items()):
     info=zipfile.ZipInfo(key+'/'+p,(2026,10,2,0,0,0));info.create_system=3;info.compress_type=zipfile.ZIP_DEFLATED
     mode=modes.get(p,0o755 if p.endswith(('Allrun','Allrun.pre','.sh')) else 0o644)
     info.external_attr=(0o100000|mode)<<16;z.writestr(info,b)
   with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    for p,b in files.items():assert z.read(key+'/'+p)==b
   verification='已核对 v2512 源文件、包含依赖与 ZIP 完整性；官方案例本轮未重新求解。'
   if key=='v2512-scalar-diffusion' and evidence.exists():verification='两个 FoamLab 一维案例已在 v2512 完成 blockMesh、完整 checkMesh 和指定终点求解，包内含日志与解析比较；官方 pitzDaily/flange 本轮未运行。'
   manifest[key]=dict(label=cfg['title']+'案例包',url='/downloads/courses/'+target.name,size_bytes=target.stat().st_size,sha256=SHA(target.read_bytes()),kind='case',verification=verification)
   print(f'PACK {key}: {len(files)} files, {target.stat().st_size} bytes, links={len(links)}')
 return manifest

# Lesson-specific prose and entry-file mapping follow. These are deliberately
# concrete transitions within each chapter, not a uniform appended summary.
CAV='tutorials/incompressible/icoFoam/cavity/cavity'
PITZ='tutorials/incompressible/simpleFoam/pitzDaily'
BIKE='tutorials/incompressible/simpleFoam/motorBike'
DAM='tutorials/multiphase/interFoam/laminar/damBreak/damBreak'
HEAT='tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater'
ACOUSTIC='tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance'
MOTION='tutorials/incompressible/pimpleFoam/laminar/movingCone'
AMI='tutorials/incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D'
REFINEMENTS={
 1:dict(lead='学习 OpenFOAM，可以先把一个计算过程拆成四件事：描述物理问题，准备输入文件，运行计算程序，检查输出是否合理。OpenFOAM 提供完成这些任务的求解器、网格与后处理工具，以及供开发者使用的 C++ 库。它并非一个必须从图形界面操作的单一程序。本课先建立可识别、可检查的运行环境；下一课再把环境与一个具体算例连接起来。',bridges=[
 ('### 本站版本边界','这里统一学习 OpenCFD OpenFOAM v2512。先确认正在使用的程序，再阅读它自带的帮助和教程：帮助说明命令如何调用，完整算例说明文件如何配合，源码则用于核对程序实际读取了什么。遇到陌生条目时，沿这条线追踪，会比根据文件名猜测其功能更可靠。'),
 ('### 从软件安装到第一个可用环境','可以把环境脚本理解为向当前终端说明“程序和库在哪里”。它不会替你生成网格，也不会改变一个案例的物理模型。检查时按顺序看：版本变量是否正确、项目根目录是否存在、command -v 指向哪一个程序、程序自己的帮助与横幅是否一致。四项相互印证，才能排除终端仍在调用另一套安装的情况。')],cases=[('v2512-cavity',CAV,'本课只定位并阅读 system/controlDict 中的 application，确认它需要 icoFoam；暂不修改物理参数。先把软件环境检查记录保存下来。')],topics=[]),
 2:dict(lead='接下来把“终端能找到程序”推进到“程序能找到正确输入”。OpenFOAM 的许多工具默认把当前目录当作算例目录，因此同一条 blockMesh 命令，在不同目录运行会读取不同文件。遇到找不到 controlDict 的错误，先检查工作目录和 -case 选项，再检查软件安装。这样可以把路径问题与模型问题分开。',bridges=[
 ('### 将命令输出变成可检查的记录','先用 pwd 回答“我在哪里”，再用 ls 回答“这里有没有 0、constant、system”。复制后应进入新副本，而不是仍停在它的父目录。本课的 cavity-first 是你可以修改的工作副本；官方目录则作为原始输入对照。若重复练习，请选新的目录名，避免把新文件混进已经有计算结果的旧目录。'),
 ('### 命令、源码和库的位置','日志阅读也有顺序：开头确认程序、版本和案例路径，中间寻找最早的异常，结尾检查是否正常结束。重定向后屏幕没有文字并不表示程序未运行；反过来，有一个 log 文件也不表示运行成功。先建立这一习惯，后面处理网格、边界和求解失败时才有可追踪的证据。')],cases=[('v2512-cavity',CAV,'复制该目录为 cavity-first。重点操作 system/controlDict、system/blockMeshDict 与新生成的 log.blockMesh；不要修改软件安装目录。')],topics=[]),
 3:dict(lead='一个算例可以看作三组互相配合的输入：0 目录描述起始场及其边界，constant 描述不随常规时间步改变的网格与模型信息，system 描述怎样计算和写出结果。先理解这些职责，再逐个阅读字典，比背诵文件名更有效。实际需要哪些文件由求解器决定，不能要求所有求解器都使用同一套 Properties 文件。',bridges=[
 ('`class` 表示文件存储的场类型；`object` 应与读取对象相符。分号结束一个普通条目，花括号围成子字典，圆括号用于列表或向量，方括号用于量纲指数。`//` 与 `/* ... */` 分别表示行注释和块注释。','读一份新字典时，可以先找“对象是什么、数值是什么、作用在哪些边界”三条线。以 U 为例，volVectorField 表明每个体单元存的是一个三分量向量，uniform (0 0 0) 表明所有单元初值相同；它不负责指定壁面运动。壁面的约束写在后面的 boundaryField 中，下一课会把这两部分放在一起检查。'),
 ('`icoFoam` 中的 `p` 是以密度归一化的压力，量纲为 $L^2T^{-2}$；它不能直接当作 Pa 读出。','量纲检查是物理检查的一部分。两个数字都写成 0.01，可能分别表示长度、黏度或时间，不能只比较数值大小。对于本课的不可压缩压力，若已知且假设密度恒定，压力差可以按密度换算成物理压力差；任意选定的参考压力常数则不能直接拿去和绝对压力测量比较。')],cases=[('v2512-cavity',CAV,'依次阅读 0/U、0/p、constant/transportProperties 和 system 下的四个主要字典。用 foamDictionary 读取条目，再和原文核对语法与量纲。')],topics=[]),
 4:dict(lead='现在用一个尺寸和边界都容易说明的问题串起完整流程。方形腔体没有入口和出口：上壁向右运动，通过黏性剪切带动内部流体，其余壁面保持静止。我们关心的第一个结果不是“生成一张漂亮的图”，而是网格、边界与计算出的速度场是否描述了同一个物理问题。',bridges=[
 ('这里的基础算例**不是**常见文献中 $Re=100$、$1000$ 的方腔设置。比较基准数据之前，必须先匹配几何、雷诺数、边界定义与采样位置。','这个雷诺数告诉我们，本课研究的是黏性影响很明显的流动。顶盖向右带动上部流体，流体受到封闭壁面限制后回流，形成主环流；这给看图提供了方向上的预期。预测只是一项合理性检查，并不预先决定涡心位置或速度剖面，那些量仍需从计算中提取和验证。'),
 ('### 看图时要回答的问题','先分清数据与显示方式。速度大小是一个非负标量，速度的水平和竖直分量则可以为负；把颜色变量从 U 的大小换成 U 的 x 分量，物理问题没有改变，但颜色含义变了。建议先显示网格边线，再查看速度大小，最后沿两条中心线提取分量。这样可以避免把绘图插值造成的平滑当成真实分辨率。')],cases=[('v2512-cavity',CAV,'直接使用 0/U、0/p 与原始 system 字典运行基础方腔。20×20×1、Re=10、t=0.5 s 对应本站既有计算图；顶盖速度减半的副本需要重新计算。')],topics=[]),
 5:dict(lead='初始条件回答“计算刚开始时，域内是什么状态”，边界条件回答“计算过程中，边界怎样约束流体”。方腔的内部速度从零开始，顶盖持续向内部传递动量，所以零初值不会把整个流场永久固定为零。阅读场文件时，应先看 internalField，再逐个对照 boundaryField；两部分共同定义问题。',bridges=[
 ('`movingWall` 等名称必须对应 `constant/polyMesh/boundary` 中的 patch 名称。网格 patch 的类型与场边界类型处于不同层次：网格上 `wall` 表示几何边界类别，速度场上 `noSlip` 表示物理约束。','这里的 movingWall 是边界名称，不是启动动网格的命令。基础方腔的网格形状保持不变，只给顶盖流体一个切向速度，等价于理想化的移动带壁面。若你需要几何本身变形或转动，还要用相应动网格模型；不能仅通过改 patch 名称实现。另一个常见错误是改了网格 patch 名，却没有同步更新 U 和 p 的同名边界。'),
 ('### 为什么压力不能随意全部设为零','先做一个简单区分：给某面 fixedValue 0，约束的是该面变量的数值；给 zeroGradient，约束的是沿法向的变化率。这两件事通常不等价。对于封闭不可压缩方腔，应让压力承担满足连续性的任务，而不是为了看起来“约束完整”就把所有边界压力都钉死。随后再处理压力整体常数的不唯一性。')],cases=[('v2512-cavity',CAV,'对照 0/U、0/p、system/blockMeshDict 与 system/fvSolution。生成网格后再检查 constant/polyMesh/boundary，完成每个 patch 的物理条件对照表。')],topics=[]),
 6:dict(lead='一次瞬态计算有两套“时钟”：求解器每步更新的物理时间，以及结果文件实际写到磁盘的时刻。把这两者分清，才能解释为什么日志显示完成了很多步，目录中却只有少数结果。本课用方腔学习输出频率和续算；它们影响数据是否够用，也影响以后能否从中间状态继续计算。',bridges=[
 ('当 `writeControl timeStep` 时，`writeInterval` 是步数；改成基于运行物理时间的控制方式后，含义随之改变。不要只改一个数字而忽略控制模式。`purgeWrite 0` 保留输出；非零会使旧时间目录按规定清理，所以保留策略需要在长计算前确定。','把当前数值代入就容易检查：每步 0.005 s、每 20 步写一次，两个常规输出时刻相隔 0.1 s。若将 deltaT 减半而保持 writeInterval 不变，输出间隔也会减半。比较两次瞬态结果时，应该对齐物理时间；比较文件夹序号或第几个文件，可能比较到不同的流动状态。'),
 ('### 续算需要保留完整状态','续算前先列出已有时间目录，并查看最新目录中需要的场是否齐全。把 endTime 从 0.5 改成 1.0，只指定了新的终点；startFrom latestTime 才要求从已有最新状态读入。应在新日志开头确认实际起点，避免把从零重新计算误认为续算，或把一份旧算例残留的更晚时间误当成本次起点。')],cases=[('v2512-cavity',CAV,'修改 system/controlDict，保留首次计算写出的时间目录。用两个独立副本对比一次算到 1 s 和从 0.5 s 续算，检查相同物理时刻的字段。')],topics=[]),
 7:dict(lead='生成网格前，先在纸上画出一个六面体，并给八个顶点编号。blockMesh 读取的就是几何顶点、顶点之间的连接、各方向单元数和边界面归属。只要这些定义能与你的草图一一对应，字典就不再是一串难以解释的坐标。本课先生成均匀方腔网格，再做保持几何不变的细化。',bridges=[
 ('非单位 expansion ratio 表示该局部方向末端与起始端的单元尺寸比，方向取决于块顶点顺序，不能凭屏幕上的左右判断。','块的局部方向由 hex 后面的编号确定。例如，第一方向的细化数属于这一块的第一局部边，不一定始终是全局 x 方向。初学时保持 simpleGrading 为 1，先确认顶点顺序、尺度和边界；再单独改变一个方向的 grading，并用网格边线观察较小单元实际出现在何处。这样能把连接错误和加密方向错误分开。'),
 ('这是 `boundary (...)` 内的片段。一个外表面不应被重复分配给两个 patch，内部共享面也不应误放到外边界。前后两面采用 `empty`，与所有场中的二维边界定义保持一致。','面上的四个编号描述一个有方向的面。若漏掉顶点、重复顶点或反转了块的有效朝向，问题可能在网格生成阶段就出现。生成后先看包围盒和 400 个单元是否符合预期，再看顶盖 patch 是否位于真正的上表面。只有这些基础检查通过，讨论分辨率是否足够才有意义。')],cases=[('v2512-cavity',CAV,'主要编辑 system/blockMeshDict；40×40×1 练习请从基础 cavity 另建副本。外层 Allrun 的 cavityFine 还涉及映射和时间设置，不要混用为纯网格细化。')],topics=['meshing']),
 8:dict(lead='有了网格，还需要回答两个不同问题：这些单元是否组成合法计算域，它们的几何形状是否适合准确离散。checkMesh 会从多个角度给出信息，并没有一个能代表所有问题的“质量总分”。本课先用正交方腔建立对照，再学习怎样根据异常位置判断哪些结果可能受到影响。',bridges=[
 ('两者都会影响面值与法向梯度重建。它们可能同时存在，但不是同一个指标。','可以用两个动作区分它们：先看相邻单元中心的连线有没有对准公共面的法向，再看插值位置与真实面中心有没有偏离。前者解释非正交修正为什么出现，后者解释即使角度不大，面值插值仍可能不准确。示意图帮助理解几何关系，日志提供数值，局部网格图则把这些数值对应回具体位置。'),
 ('### 为什么只看最大值不够','例如，同样少量的扭曲单元，位于远离物体的均匀来流区，和位于预测壁面剪切的第一层，可能对阻力造成不同影响。先定位失败单元，再问附近有什么强梯度、这里是否参与目标量积分。正交方腔可以作为“本应简单”的参照：若它出现负体积或意外三维单元，优先检查你对顶点与边界的修改。')],cases=[('v2512-cavity',CAV,'用原始 system/blockMeshDict 生成质量基线，保留 log.checkMesh。对照自己的网格副本逐项比较，说明非正交或偏斜变化出现在哪些位置，以及影响哪些观测量。')],topics=['meshing']),
 9:dict(lead='从 CAD 到计算网格，中间至少经过一次表达方式变化：CAD 用曲面与拓扑描述物体，STL 或 OBJ 用离散面表示表面，而求解器需要的是填满流体区域的体网格。表面看起来完整，不代表单位正确，也不代表已经有了可求解的流体域。本课把几何尺度、封闭性和计算域选择放在网格生成之前处理。',bridges=[
 ('实际输入和输出文件名要与自己的目录对应。检查包围盒、边界边、重复面、退化三角形及表面区域数量。内流问题要明确入口、出口和壁面组成哪个封闭域；外流问题则还需要背景计算域。一个有意保留的入口开口，与意外裂缝，不应使用同一种修补逻辑。','下载包采用 motorBike.obj.gz 作为实际可读取表面，课文中的 pipe-mm.stl 则用于解释毫米到米的换算。不要对 motorBike 也机械执行 0.001 缩放；应先检查它本来的包围盒，并与 system/blockMeshDict 的背景域比较。物体应以预期尺度位于背景域内，入口、出口和外边界则通常来自背景网格，而不是物体表面。'),
 ('### 几何精度应服务于计算目标','判断一个细节是否保留，先说明它会通过什么机制影响结果。例如，控制分离的尖角可能必须保留，而远离关注区、尺寸极小的装饰倒角未必值得极端细化。简化不是为了让网格“看起来规则”，而是基于问题尺度降低无关复杂度；简化后仍要重新检查封闭性、区域名称和预期流体连通关系。')],cases=[('v2512-meshing-rans',BIKE,'表面文件在包内 tutorials/resources/geometry/motorBike.obj.gz；Allrun 会复制到本例 constant/triSurface。结合 system/blockMeshDict 与 system/snappyHexMeshDict 检查包围盒和流体区域。')],topics=['meshing']),
 10:dict(lead='复杂表面网格可以分成三个逐步检查的阶段：先用背景网格分辨物体与局部特征，再让边界贴合几何，最后增加近壁层。snappyHexMesh 将这些阶段组织在同一工具中，但这不意味着应一次打开所有功能。每一步保留网格和日志，才能判断问题来自域选择、贴合还是层网格。',bridges=[
 ('`surfaceFeatureExtract` 需要对应的 `surfaceFeatureExtractDict`。某些案例使用特征捕捉的其他配置方式，不能无条件套用这一步。`-overwrite` 会更新当前网格，应在独立工作副本运行。','motorBike 下载例给出了可用的完整字典和几何。先阅读它的 Allrun，理解为何复制表面、提取特征、分区、网格生成、恢复初值要按该顺序进行；再在独立副本中研究阶段开关。原始脚本采用并行流程，不能在没有 0 场、没有必要特征文件的目录中，照抄上面四条概念命令就期待全部设置自动完成。'),
 ('### 每一阶段检查一个明确问题','第一阶段尤其要核实 locationInMesh：它给算法一个应保留区域的内部点，不是物体中心坐标的固定写法。点若位于固体内、表面上或错误的连通区域，后续即使得到大量单元，也可能保留了错误的计算域。第二、第三阶段再分别检查表面贴合和壁面层，避免把物理域选择错误误诊为迭代次数不足。'),
 ('字典是否使用相对厚度，要看 `relativeSizes` 设置；不能把以背景单元尺寸为基准的数值直接当成米。验收时保存三个阶段的网格截面、单元数、质量统计和层覆盖情况。','总层数写成某个值，并不保证每个壁面位置都生成了同样多的层。层添加可能因间隙、曲率或质量限制而局部停止，所以应在关键壁面显示截面并统计覆盖。若目标是壁面剪切或换热，首层中心距和实际层覆盖比一个全域总单元数更能解释结果差异。')],cases=[('v2512-meshing-rans',BIKE,'从 system/snappyHexMeshDict、surfaceFeatureExtractDict、meshQualityDict 和完整 Allrun 开始。官方几何与 0.orig/include 全部包含；运行需要 MPI，默认六分区。')],topics=['meshing','turbulence']),
 11:dict(lead='前几课用字典告诉程序“怎样算”，这一课解释程序为何会形成一组代数方程。有限体积方法不从单个数学点开始，而是对每个小体积建立收支：内部储存了多少，边界流进流出多少，有没有源项。把每个单元的收支连接起来，就得到整个计算域的离散问题。',bridges=[
 ('### 内部面为什么特别重要','以两个相邻单元为例，同一份流体穿过公共面，对左侧是流出，对右侧就是流入。如果两边使用互不一致的数值通量，全域求和时会凭空出现增量或损失。因此，理解“内部面通量以相反符号进入两边方程”，比先记某个矩阵求解器名字更接近守恒方法的核心。'),
 ('`fvSchemes` 决定如何构造系数，`fvSolution` 决定如何解组装后的代数系统。练习时在三单元一维网格上标出每个面的方向，写出中间单元的收支式，再验证左右内部面在全域求和中消失。','本课的下载练习把流动耦合暂时去掉：一维标量案例给定速度，只求被输运量 T；一维扩散案例则只保留扩散与边界温度。这样可以把数值结果中的变化对应到某个算子。待这两种收支都能解释后，再回到方腔，把速度、压力与面通量的相互作用加入理解框架。')],cases=[('v2512-scalar-diffusion','exercises/one-dimensional-advection','阅读 0/T、0/U 和 system/fvSchemes，识别被输运量与面通量；相邻 one-dimensional-diffusion 目录用于去掉对流后的收支对照。'),('v2512-cavity',CAV,'对照 system/fvSchemes 中的 div(phi,U) 与 laplacianSchemes，说明完整方腔相比单一标量方程多了哪些未知量。')],topics=[]),
 12:dict(lead='判断对流格式，先选一个能明确知道答案的测试：让一团标量随均匀速度移动，保持没有物理扩散和源项。理想结果应保持原来的形状并向前平移。数值结果如果变宽、峰值降低，或出现不该有的负值与新极值，就可以据此分析格式，而不必从复杂流场中猜测原因。',bridges=[
 ('### 从方腔设置开始识别语法','同一个“迎风”思想可以用于不同变量，但字典键必须对准具体方程。方腔解速度，所以这里先展示 div(phi,U)；下载的一维被动标量案例解 T，对应条目是 div(phi,T)。要比较标量对流格式，应修改后者；修改一个求解器没有读取的键，计算结果不变并不能说明格式完全等价。'),
 ('### 设计一个有意义的比较','配套一维案例给出了紧支撑的余弦平方脉冲：初始中心在 0.25 m，流速为 1 m/s，计算至 0.2 s 时解析中心在 0.45 m。脉冲尚未碰到出口，且 DT 为零，因此更容易把形状变化归因于数值处理。基线采用 Euler 与 upwind；在副本中只改变 div(phi,T)，保持网格和时间步不变，再运行 compare.py 比较同一时刻的剖面。'),
 ('**验收：**提交同一坐标轴上的三条剖面，列出极值、积分误差、时间步与单元数。解释你选择的格式对当前问题为什么合适，而不是简单写“二阶比一阶好”。','下载包还保留了官方 scalarTransportFoam/pitzDaily，供你把方法移到更复杂的速度场。它的 DT 非零，包含真实扩散，所以不能把全部平滑都归因于迎风格式。先用最小案例区分物理扩散与数值扩散，再分析工程几何，比较会更有解释力。')],cases=[('v2512-scalar-diffusion','exercises/one-dimensional-advection','运行 Allrun 后查看 comparison.csv；修改 system/fvSchemes 的 div(phi,T)，比较 upwind、linear 与 limitedLinear。compare.py 的坐标与参考对应原始参数，改网格或时刻时也要同步调整。')],topics=[]),
 13:dict(lead='扩散项描述由空间梯度驱动的输运。最容易核对的例子是一根均匀材料杆：两端温度固定、内部没有热源时，稳态温度应沿长度线性变化。先用这个答案明确的案例检查离散与边界，再增加非正交网格或材料交界；否则很难判断误差来自哪一环。',bridges=[
 ('### 两种误差应分开处理','先看我们需要什么：求热流必须知道面上的温度梯度，而未知温度通常存储在单元中心。从中心到面，要进行插值；从三维梯度到穿过面的通量，要取法向分量。网格几何不理想时，这两步都会引入误差。因此不能只改一个 laplacianSchemes 条目，而完全忽略梯度重建和面法向修正。'),
 ('### 材料交界不能只比较温度图是否平滑','下载的一维最小案例采用 steadyState 时间格式，目的是直接求线性稳态解；输出目录名 1 在这里不是已经真实演化了 1 s。先将 comparison.csv 中的单元中心温度与解析直线对照，检查两端边界和斜率，再用给定导热系数计算热流方向。包内这份最小输入只有一种材料；下面两材料问题是后续扩展，不能把单材料的通过结果作为界面处理已经验证的证据。')],cases=[('v2512-scalar-diffusion','exercises/one-dimensional-diffusion','40 个单元、左 400 K、右 300 K、长度 0.1 m。运行 Allrun 并读取 comparison.csv，逐点对照线性解；官方 flange 示例另在 tutorials/basic/laplacianFoam/flange。')],topics=['meshing']),
 14:dict(lead='选择时间步前，可以先问：在这一步内，流动信息大约走过多少个单元？Courant 数把速度、单元尺度和时间步联系起来，帮助识别那些变化太快而未被充分分辨的位置。它是一项局部数值尺度检查，不是所有物理过程精度的通用证明。',bridges=[
 ('OpenFOAM 的 `Euler` 表示其对应的一阶隐式时间离散，不能与所有教科书里的显式 Forward Euler 混为一谈。`backward` 使用多时间层的后向差分形式；`CrankNicolson` 的具体偏心参数和历史层处理应查 v2512 实现与教程。','时间离散回答的是“怎样由已有时刻估计新的状态”。时间步回答的是“相邻状态隔多远”。把一阶方法换成高阶方法，并不能补回从未解析到的快速变化；同样，减小步长也不会修复一个错误的边界或物理模型。比较方法时，应把时间格式和时间步分别记录，避免把两个因素同时改变。'),
 ('### 隐式不等于可以任意放大时间步','以一个周期过程为例，若一个周期只保留四个计算状态，即使算法不发散，也很难准确确定峰值位置和相位。方腔启动过程没有必须预先给定的涡脱落周期，但仍可比较相同物理时刻的探针速度和中心线剖面。若改变步长后这些量还明显变化，就不能仅凭日志中 Co 不大而结束时间分辨率研究。')],cases=[('v2512-cavity',CAV,'分别修改 system/controlDict 的 deltaT，在 system/fvSchemes 中记录 ddtSchemes。输出比较时对齐真实物理时间；icoFoam 不应被假定自动读取所有步长控制键。')],topics=[]),
 15:dict(lead='速度决定质量怎样穿过单元面，压力又通过梯度影响速度。计算时若只更新其中一项，两者通常还不协调。SIMPLE、PISO 与 PIMPLE 的目的都是组织这种耦合，使离散动量关系和连续性逐步一致；它们的区别主要体现在什么时候重组方程、做多少层校正以及是否推进真实时间。',bridges=[
 ('`nCorrectors` 控制该算法中的压力校正；`nNonOrthogonalCorrectors` 对应非正交压力修正循环。正交网格上写零不代表忽略连续性，而是无需额外非正交校正。','可以沿日志读一次时间步：先找到时间标记，再找速度求解与后续压力求解记录。压力出现多次，不意味着生成了多个独立压力场，而是在同一步里做校正。增加 nCorrectors 主要改变耦合工作量；是否值得增加，要看连续性、目标量与耗时的变化，而不是以日志行数更多作为精度提高的证据。'),
 ('### 怎样判断校正是否足够','用两个完整官方案例建立对照最直接：方腔 controlDict 选择 icoFoam，fvSolution 中读取 PISO；pitzDaily 选择 simpleFoam，读取 SIMPLE。先确认求解器实际支持的算法，再改对应子字典。下面的 PIMPLE 片段用于解释外层与内层的关系；若要实际运行它，应选择 pimpleFoam 的完整输入，而不是把方腔字典的标题换个名字。')],cases=[('v2512-cavity',CAV,'阅读 system/fvSolution 的 PISO，结合 log.icoFoam 标出每步的速度、压力校正。'),('v2512-meshing-rans',PITZ,'对照 system/controlDict 与 system/fvSolution 中的稳态 SIMPLE 设置。目录中的迭代标记不能直接解释为瞬态流动秒数。')],topics=['turbulence']),
 16:dict(lead='一次流场计算通常包含许多次线性方程组求解。日志里的 Initial residual 和 Final residual 描述的是其中一次代数求解前后的残差，不直接给出整幅流场距离真实物理解还有多远。先分清“这次方程组解得怎样”和“整个模拟是否可信”，再选择容差与监测量。',bridges=[
 ('`pFinal` 仅在程序选择最终求解设置时使用，不是一个新的压力场。','例如，某次压力求解的初始残差若为 0.01，relTol 为 0.05，则相对条件对应降到 0.0005；它与 tolerance=0.000001 是不同的停止门槛。普通校正可能先满足相对条件，而最终校正使用 relTol 0 后继续追求绝对条件。这个例子解释配置含义，并不表示这些数值能普遍保证某个速度误差。'),
 ('### 在运行时保存解算信息','先决定以后要画什么，再启动计算。如果要观察求解过程的残差与迭代数，需要运行时监测或完整日志；如果只留下最终一个时间目录，就只留下了那个状态的场数据。两种数据回答的问题不同。将 solverInfo 与一个物理探针同时记录，可以观察残差降低时，真正关心的速度或压差是否也趋于稳定。')],cases=[('v2512-cavity',CAV,'修改 system/fvSolution 的 p/pFinal 容差，并把课文 solverHistory 合并进 system/controlDict 的 functions。保存 solverInfo.dat、完整日志与目标量，不能从最终场补出历史残差。')],topics=[]),
 17:dict(lead='面对发散，最容易做的事是把所有松弛因子调小，但这常常没有回答问题为什么发生。松弛控制的是迭代更新幅度：它可以帮助某些非线性迭代平稳推进，却不能纠正几何单位、相互矛盾的边界或错误物性。本课把松弛放在诊断流程中理解，而不是把一组系数当成通用修复方案。',bridges=[
 ('这组数字只是教学起点，不是任何问题的推荐最优值。正则键必须匹配真实场名。实际求解器还要在相应位置调用松弛，字典才能发挥作用。','本课下载的 pitzDaily 默认采用 kEpsilon，而示意正则键包含 k 和 omega。若你在这个例子里研究湍流方程松弛，应按原始 fvSolution 的 k、epsilon 等真实字段设置，不能期待 omega 的系数影响一个并不存在的方程。先查模型与场名，再读日志确认迭代变化，这比只看字典保存成功更可靠。'),
 ('### 发散时先寻找第一个异常','把日志按时间顺序保留，寻找变化开始的那一步：是网格生成就失败，初始密度已不合理，还是某个局部 Co 先急剧升高？最终的浮点异常可能只是后续运算遇到非法值。为一个怀疑建立检验，例如只改时间步、只修一个边界或只替换异常网格，并观察最早的异常是否消失。一次改很多参数会破坏这条因果线索。')],cases=[('v2512-meshing-rans',PITZ,'使用完整稳态 RANS 算例研究 system/fvSolution 中已有的 relaxationFactors。记录默认模型的真实场名，逐次只改一个设置；方腔仅作为前面日志阅读流程的参照。')],topics=['turbulence']),
 18:dict(lead='做网格研究之前，先说清楚你要收敛的量是什么。中心线速度、壁面力和平均压降对网格的要求并不相同；两幅颜色相似的图，可能仍给出不同的梯度和积分量。本课把“网格更细”转化为可比较的实验序列，再说明什么时候可以讨论误差阶与外推。',bridges=[
 ('建立至少三组有规则关联的网格，保持几何、物性、边界、离散格式与相同物理时刻一致。时间步和迭代误差需要控制在不会掩盖空间差别的水平。每组至少记录：单元数、代表尺度、质量指标、目标量、运行时间。','方腔可以从同一基础目录复制出 20、40、80 三组平面网格，保持 0.1 m 的边长与相同雷诺数。细化只应改变空间分辨率；若同时改黏度、顶盖速度或停止时间，就在比较不同实验。包内外层 Allrun 还演示映射和高雷诺数变化，因此不能把它自动生成的所有子案例直接排成一组细化序列。'),
 ('### 方腔练习的合格报告','对于相同物理位置，不同网格未必恰好都有一个中心点落在那里。因此必须统一采样坐标与插值规则，而不是取各自“差不多在中间”的单元编号。若目标量非常接近零，相对误差还可能因分母很小而夸大，应同时报告绝对差或采用明确的参考尺度。先把比较定义清楚，外推公式才有可解释的输入。')],cases=[('v2512-cavity',CAV,'从基础 cavity 手动建立独立 20×20×1、40×40×1、80×80×1 副本，分别保存网格、时间步、采样与日志。不要使用改变了雷诺数的 cavityHighRe 作为细网格点。')],topics=['meshing']),
 19:dict(lead='边界条件可以理解为计算实验的操作方式。若给定入口流量，压降通常是需要求出的响应；若给定两端压差，流量就可能成为响应。把两种实验中的已知量全部同时强制指定，可能过度约束问题。本课先借助有解析关系的管流理解这一点，再用实际入口出口案例检查字典和结果。',bridges=[
 ('### 常见入口出口组合的含义','先画出计算域与真实装置的对应关系：入口代表泵后的哪一个截面，出口离回流区多远，侧面是实体壁面还是人为截断的边界。条件类型的选择要服务于这些物理含义。pitzDaily 是带分离与再附着的通道例子，适合检查入口、出口和壁面配合；它并不是充分发展圆管，不能用上面的圆管公式直接计算其压降误差。'),
 ('`inletValue` 指定回流时进入域内的值；`value` 还承担初始化等作用。不同变量不应机械地使用同一类型。','为什么出口需要考虑回流值？因为局部速度一旦指向域内，这个面就在向计算域带入标量，单纯“让它流出去”的解释已不成立。回流温度、湍流量或组分应代表域外环境，而不是随便填一个数来消除报错。若大范围回流源于出口截断了关键涡结构，还需要调整计算域，不能只依赖边界条件补救。')],cases=[('v2512-meshing-rans',PITZ,'阅读 0/U、0/p、0/k、0/epsilon 与 system/blockMeshDict，核对入口、出口及壁面名称。这里用于边界组合与域长影响练习，不作为圆管解析解案例。')],topics=['turbulence']),
 20:dict(lead='选择湍流模型前，先把“想得到什么”写成一个可测量的量。平均压降、瞬态升力和混合时间依赖的流动细节不同，也未必需要同样的计算代价。模型选择不是从菜单中找一个最复杂的名字，而是让物理假设、输入信息、网格与目标量相互匹配。',bridges=[
 ('RANS 将速度分解为平均和脉动，产生 Reynolds 应力等未闭合项；LES 解析较大的涡尺度、建模未解析尺度；DNS 则要求直接解析相关小尺度。**把网格加密一点并不会自动把 RANS 变成 LES，也不会把 LES 变成 DNS。**','这里的“未闭合”指的是平均以后出现了新的未知统计量，需要额外模型表达。RANS 给出的平均速度场即使很平滑，也不意味着真实流动没有脉动；LES 的瞬态结构很多，也不意味着所有尺度都已充分解析。先分清模型试图描述的量，再决定什么观测能支持或反驳它。'),
 ('### 模型选择必须带着网格计划','下载包提供两个 RANS 起点：pitzDaily 默认 kEpsilon，motorBike 默认 kOmegaSST。比较时先列出它们各自需要的场，尤其注意 epsilon 与 omega 不是同一个变量。若要在同一几何比较模型，应在独立副本中同时调整模型、必需字段、边界和近壁策略；只改 RASModel 这一行往往会得到缺字段错误或不一致输入。')],cases=[('v2512-meshing-rans',PITZ,'先检查 constant/turbulenceProperties 与 0/k、0/epsilon；再对照同包 motorBike 的 kOmegaSST、0.orig/k、0.orig/omega 和 nut。两者不同几何不能直接归因为模型差异。')],topics=['turbulence']),
 21:dict(lead='如果关注阻力或换热，最靠近壁面的几个单元往往比远场的大量单元更关键。因为壁面剪切和热流由近壁梯度决定，而这些梯度变化很快。本课把第一层单元位置、湍流模型与壁面条件联系起来，说明为什么“总单元数很多”仍可能不足以解析目标壁面。',bridges=[
 ('这里 $y$ 是壁面到第一层单元中心的距离，不是整个边界层厚度。粗略估算首层高度后，还需要使用初步计算得到的壁面剪切反算实际 $y^+$ 分布。','对近似平直、均匀的第一层单元，中心通常位于层厚的约一半处，因此“首层厚度”和公式中的 y 也不应直接混为一谈。壁面剪切本身又是解的一部分，所以设计阶段得到的是估算值。实际计算后需要回到壁面逐点检查，特别是分离、再附着或局部加速使剪切明显变化的位置。'),
 ('### 字典是成套设置','这里用 kOmegaSST 说明成套配置的原则，下面 k 的片段则取自默认 kEpsilon 的 pitzDaily，不能据此认为该官方算例已经使用 SST。学习时先保持每个完整教程的原始模型和字段，再检查 k、epsilon 或 omega、nut 的壁面含义。之后再做模型更换，才容易判断变化来自哪里。'),
 ('### 验收不只写一个平均数','后处理的 yPlus 数值要结合所选近壁处理解释。将整个壁面画成分布图，标出你要积分阻力或热流的区域；再查看极值出现在哪里。如果层网格在关键位置中断，即使全壁面平均 yPlus 接近设计值，也可能掩盖局部不足。目标不是追求一个漂亮的平均数，而是让重要区域落在方法适用范围。')],cases=[('v2512-meshing-rans',PITZ,'先求解完整 pitzDaily，再用相同模型环境执行 yPlus 后处理。网格层构造可对照同包 motorBike 的 addLayersControls；后者使用不同模型，应分别解释。')],topics=['turbulence','meshing']),
 22:dict(lead='水和空气共存时，固定网格中的一个单元可能被水填满、完全没有水，或被界面切过。VOF 用水占该单元体积的比例来描述这三种状态，而不是另外建立一张实体薄膜网格。溃坝案例让我们从一个明确的水柱初值开始，观察界面运动，同时检查体积分数与总体积是否合理。',bridges=[
 ('必须先生成体网格，再初始化场。阅读该教程 `Allrun`，确认是否需要先从 `0.orig` 恢复 `0`；不要缺少初始字段就直接运行 `setFields`。','在这个案例里，0.orig 提供字段结构，setFields 再按网格单元与区域的关系设置水柱。检查时应在求解前就打开初始化后的 alpha.water：水是否位于左下角，尺寸是否与 box 一致，边界是否仍存在？如果初值已经错误，后续看到异常界面时就不应首先修改压缩系数或压力容差。'),
 ('### 需要同时控制三类行为','还要分清速度、压力和重力的配合。interFoam 中的 p_rgh 与常规压力扣除静水贡献有关，不应把方腔 0/p 原文直接搬过来。先在下载例中阅读 g、相物性、0.orig/p_rgh、U 与 alpha.water，再读控制字典。这样能区分“初始水量不对”“受力不对”和“界面输运误差过大”这三类不同原因。'),
 ('界面压缩是数值处理，不是额外的真实物理吸引力。过强压缩与不合适的网格、时间步可能造成锯齿或寄生流。接触角、壁面润湿和表面张力的设置也要与具体物理场景一致。','总水体积应从 alpha 与单元体积求和，而不是数一数被等值面包住的像素。若水会通过开放边界离开域，还必须计入该边界的水相通量，体积减少本身不一定是守恒错误。对每次比较统一采用相同的等值面阈值、时间与前沿提取规则，否则“前沿更快”可能只是后处理定义不同。')],cases=[('v2512-vof-dambreak',DAM,'从内层 Allrun 启动。重点阅读 system/setFieldsDict、controlDict、fvSolution，及 0.orig/alpha.water、p_rgh、constant/transportProperties、g；外层脚本另含细网格并行扩展。')],topics=['multiphase']),
 23:dict(lead='讨论传热时，先说清楚温度由哪些机制改变。一个静止均匀固体可以只研究导热；流体中还可能有能量对流、压缩作用和模型源项。共轭传热进一步把流体与固体连接起来：不同区域解各自的方程，通过共同界面交换热量。区域文件夹只是组织输入，真正的耦合由接口设置与求解器完成。',bridges=[
 ('这是结构示意，`fluid` 和 `solid` 应替换成案例真正的区域名称。v2512 官方 `chtMultiRegionFoam/multiRegionHeater` 提供完整示例；不要只新建两个同名文件夹，就认为耦合关系自动成立。','配套 multiRegionHeater 中的真实区域有 bottomWater、topAir、heater、leftSolid 和 rightSolid。先从 regionProperties 列表开始，再追到各区域物性和字段。Allrun.pre 用 cellZones 划分网格并应用区域字典，所以“案例最初没有每个区域的完整时间目录”可能是正常的生成流程；跳过预处理才会使这些输入缺失。'),
 ('### 用热量收支检查结果','比较界面两侧热流前，先统一法向约定：从流体向固体流出的热量，对固体就是流入，两侧使用各自外法向时符号通常相反。温度相近只是界面检查的一部分，还应看传递的热量是否匹配。整体稳态收支则把所有外边界与源项放在一起，避免只盯一个最高温度而遗漏额外热源或输出面积错误。')],cases=[('v2512-conjugate-heat',HEAT,'按 Allrun.pre/Allrun 的顺序建立与计算全部区域。先核对 constant/regionProperties、各区域 thermophysicalProperties 与 system/*/changeDictionaryDict；Windows 可读副本已展开原始相对软链接。')],topics=[]),
 24:dict(lead='有些流动不能把密度当成常数：压力波会引起压缩与膨胀，明显温差或成分变化也会改变密度。因此，是否使用可压缩模型不能只凭“速度看起来很低”判断。本课先把压力、温度、密度和能量变量的关系理清，再用共振腔案例认识声传播对时间与空间分辨率的要求。',bridges=[
 ('### thermophysicalProperties 是一组关联选择','字典中的几项选择共同定义“怎样由状态求密度、热容和输运性质”。例如，同样写 perfectGas，求解的能量可能是焓，也可能是内能；相应热容模型和输入系数必须一致。可以先把每个选择翻译成一个问题：用什么状态方程、使用哪个能量变量、系数是否随温度变化，然后再核对具体数值与单位。'),
 ('这段不包含必需的 `mixture` 物性系数，因此不是完整文件。`sensibleEnthalpy` 与 `sensibleInternalEnergy` 不是随意可交换的标签，需要与实际方程和边界条件一致。','下载的 helmholtzResonance 实际采用 eConst 和 sensibleInternalEnergy，提供 Cv；上面的 hConst 与 sensibleEnthalpy 是另一种常见结构示意。进入实际练习时应保留官方完整热物性输入，不要用这个片段覆盖它。用 molWeight 对应的质量气体常数、输入的绝对压力与 Kelvin 温度手算密度，能很快暴露把运动学压力或摄氏温度误填进去的问题。'),
 ('声学或压力波问题还要关注声传播的时间与空间分辨率。仅看流速定义的 Co 可能不足以刻画波的数值传播误差。若有激波，应额外关注激波捕捉、振荡与守恒；不能用平滑低速问题的格式选择代替。','这个共振案例分别用完整几何和边界模型表示腔室，因此 Allrun 会创建 resolved、modelled 两个子案例。两者对照的是腔室表示方法；做时间步研究时，还应在每一种表示内部单独细化时间步。读取颈部压力探针时，绝对压力减去参考环境压力得到的波动，与原始绝对压力不是同一个绘图变量。')],cases=[('v2512-compressible-acoustics',ACOUSTIC,'通过 Allrun -test 建立两种几何表示与相对链接，再读取 resolved/modelled 的压力探针。此参数仍执行计算，只跳过 gnuplot；需要 MPI。')],topics=[]),
 25:dict(lead='描述旋转或移动问题时，先区分“改变参考系”和“让网格真的运动”。MRF 常用于某些稳态旋转近似；滑移网格随时间运动，通过接口交换信息；Overset 用重叠区域和插值连接不同网格。这些方法回答的物理问题与数值代价不同，不能仅凭画面里是否出现转动来判断模型是否合适。',bridges=[
 ('动网格通常涉及 `constant/dynamicMeshDict`、相应动态网格库、运动求解器与点位移或刚体参数。不同案例使用的网格类型差别很大，因此以完整官方算例建立第一步，比组合不同来源片段可靠。','先用 movingCone 分清运动输入与流动输入。它实际使用 velocityComponentLaplacian，点运动字段是 pointMotionUx；并不是每个运动案例都包含 pointDisplacement。dynamicMeshDict 选择怎样移动内部网格点，点场边界给出相应运动约束，U 的边界则描述流体与运动边界的速度关系。这几个文件需要一起读。'),
 ('### AMI 接口需要检查什么','AMI 用于连接两侧不必逐面匹配的接口。mixerVesselAMI2D 中可以沿着 topoSet 定义的区域、dynamicMeshDict 中的运动设置和网格边界的 cyclicAMI 配对，回答“谁转动、谁静止、信息通过哪里交换”。几何上有两个圆面并不代表配对已经成立；还要检查邻接关系、方向和有效覆盖。'),
 ('建议按三个层次验收：先只检查运动轨迹和几何，确认位移、角速度和周期正确；再用尽可能简单的场检查运动与通量；最后加入真实流动，并比较质量收支和周期统计。对滑移网格，还需研究角步长与接口分辨率。','网格运动还会改变单元体积和面的位置，因此质量通量应与网格运动一致。观察某一时刻的漂亮网格只能说明那个瞬间的外观；至少应在一个有代表性的运动周期内检查最小体积、质量指标、接口覆盖和目标量历史。增加外循环或降低线性容差，不能自动修复运动导致的局部网格塌陷。')],cases=[('v2512-moving-ami',MOTION,'从 constant/dynamicMeshDict、0/pointMotionUx、0/U 追踪移动边界；blockMesh 后使用 pimpleFoam。'),('v2512-moving-ami',AMI,'同一下载包中的 AMI 练习位置。先读 Allrun.pre 的 m4 与 topoSet，再读 motion 和 cyclicAMI 配置；运行 Allrun 需要 m4、MPI。')],topics=['dynamic-mesh','meshing']),
 26:dict(lead='并行计算把同一张网格拆成几部分，交给多个进程各自计算；分区边界上的信息仍需相互传递。它改变的是计算任务的分配方式，不应该改变你要解的物理问题。因此，本课先练习分区、启动和重构，再比较串行与并行结果，最后才讨论速度提升。',bridges=[
 ('MPI 进程数应与分区数一致。这里的 `icoFoam` 只用于方腔示例，其他案例要用自身求解器。若使用集群，应遵守调度器分配的核数和启动方式，不要在登录节点运行大规模任务。','decomposePar 把网格与初始字段写进 processor0 等目录，求解器的 -parallel 模式从这些分区读入并交换数据。reconstructPar 再把指定时间的结果组合成便于整体查看的形式。如果求解失败，先看每个处理步骤及并行日志中的最早异常；没有成功求解的分区，不能靠重构命令补出结果。'),
 ('### 并行验证先于性能宣传','比较时用一份原始输入分别创建串行副本和并行副本，防止第二次计算从第一次残留的时间目录开始。两者应使用同一网格、边界、结束时间与采样规则。方腔只有 400 个单元，通信开销可能超过节省的计算量；即便并行更慢，也不意味着分区流程必然有错，它可能只是问题规模太小。')],cases=[('v2512-cavity',CAV,'在副本 system/ 中保存本课给出的 decomposeParDict，再按分区—MPI 求解—重构顺序运行。与另一独立副本的串行结果比较。'),('v2512-meshing-rans',BIKE,'较大问题的并行流程参照：Allrun 使用 decomposeParDict.6，并区分网格生成与求解步骤；本包不提供本轮并行性能结论。')],topics=['meshing']),
 27:dict(lead='计算之前就应决定以后用什么量回答问题。一个点的速度历史能反映局部随时间的变化，一条中心线能比较空间剖面，一个截面的积分则可能用于流量收支。三者不是同一种信息。先定义观测量、位置、单位和采样频率，再选择 function object，才能避免算完后才发现缺少关键数据。',bridges=[
 ('如果已有 `functions`，应合并子对象，不要重复建立互相覆盖的同名键。探针位于流体域内，坐标以米为单位。运行后检查 `postProcessing/cavityProbes` 中的文件头、探针位置与时间列。','文件头中记录了探针编号与坐标，速度每个采样点包含三个分量，而压力是标量。整理数据时不要把一个向量括号误读成一个数，也不要忽略时间列。固定探针位置后，先检查它确实在域内；若换了几何尺度而沿用旧坐标，数据缺失可能来自点在域外，而不是求解器没有输出。'),
 ('### 时间平均的窗口有物理含义','平均之前先画原始历史，判断仍处于启动阶段、已趋于稳定，还是存在持续周期或统计波动。对后一类问题，平均窗口应覆盖足够多的代表性变化，且应报告窗口长度。只因为曲线看起来“抖动”，就把全部初始数据一起平均，可能把启动偏差混入想比较的统计量。')],cases=[('v2512-cavity',CAV,'把 cavityProbes 合并到 system/controlDict/functions。求解后读取 postProcessing/cavityProbes，并保持与中心线采样一致的时刻、分量和单位。'),('v2512-meshing-rans',PITZ,'官方 system/streamlines 展示一个完整后处理对象及 includeEtc 模板；有入口出口的流动还应另外定义明确的通量收支。')],topics=[]),
 28:dict(lead='一项可信的 CFD 结论，需要知道它的证据能支持到哪里。程序正常结束说明执行流程完成，残差下降说明某一层迭代改善，图像平滑说明数据经过了某种显示；这些都不能独自证明物理预测准确。本课把实现、分辨率、模型和比较口径逐层分开，帮助你写出可被检查的结论。',bridges=[
 ('### 三个层次的实例','下载的一维导热案例具有明确解析解，适合检查简单离散与边界是否实现正确。方腔则可在没有实验数据时开展网格和时间敏感性研究。要进一步判断某个工程湍流模型能否预测真实压降，还需要条件匹配的实验或基准；前两个测试提供的是基础证据，不能自动覆盖这个更复杂问题。'),
 ('### 面向初学者的最小证据表','读者应能从记录中重建你的比较，而不是只接受“验证通过”四个字。比如，哪一条中心线、哪个速度分量、什么时间、哪种归一化和插值规则，都应明确。若引用文献，也要核实它的几何、雷诺数和边界定义；同名 cavity 或同名湍流模型并不足以保证在比较同一个问题。')],cases=[('v2512-scalar-diffusion','exercises/one-dimensional-diffusion','用 comparison.csv 检查解析线性温度解，明确这项检查只覆盖常系数正交单材料问题。'),('v2512-cavity',CAV,'结合第 18 课建立独立网格与时间步序列。既有 400 单元单次结果不能充当完整网格独立性或物理确认。')],topics=[]),
 29:dict(lead='共享算例的目标，是让另一位读者不依赖你的口头说明，也能知道输入是什么、从哪里运行、怎样判断结果。一个很大的结果文件夹未必做到这一点；一份完整输入、清楚的运行入口与可核查日志往往更重要。本课把前面的版本、网格、数值与证据记录组织成可以交给别人的资料。',bridges=[
 ('### 一个明确失败语义的运行脚本','脚本首先固定工作目录，随后检查环境，再逐步执行网格和求解。这样做是为了减少“在错误目录运行却没注意到”的情况，并保留每一步输出。管道配合 pipefail 使前面的命令失败不会被 tee 掩盖；网格质量失败则还需要阅读 checkMesh 的检查汇总。自动化减少重复操作，但不能替代结果判断。'),
 ('**README 至少写清楚：**算例做什么；采用哪些假设；需要哪个版本；从哪一目录执行哪些命令；结果存在哪里；什么数值或趋势说明流程合理；哪些功能仅经过启动检查、哪些完成了全时段计算、哪些经过网格研究。','本站下载包也遵循这一区分：原始文件哈希用于核查输入完整性，DEPENDENCIES.txt 说明包含文件和系统依赖，运行日志用于证明实际执行范围。哈希一致并不意味着解正确，完整求解也不意味着已有实验确认。写分享文章时，把这些证据分别说明，能使后来者更容易复跑、定位差异并继续改进。'),
 ('上传到本站时，将课程讲解、可下载资源和讨论关联起来。问题帖优先附最小可复現输入、完整版本横幅、出错命令及最早异常日志。不要仅贴最后一行报错或没有色标的截图。','“最小”不等于只剩一个 fvSolution 文件。若它通过 include 读取其他文件，依赖也必须一并提供；几何、初始字段和必要脚本同样不能遗漏。可以先把自己准备发布的 ZIP 解压到一个新目录，只按 README 运行一遍，再请别人复跑。这个过程常能发现自己电脑上存在、压缩包里却没有的隐含依赖。')],cases=[('v2512-cavity',CAV,'以基础方腔组织自己的共享目录与运行脚本。参考本包 README.zh-CN.md、SOURCE.txt、COPYING、MANIFEST.sha256 和 DEPENDENCIES.txt，完整说明输入、许可与验证范围。')],topics=[]),
}

def focus_v2512(body):
 replacements={
  '### 本站版本边界':'### 先确认运行环境',
  '本站主线是 **OpenCFD OpenFOAM v2512**。Wolf Dynamics 培训采用的 Foundation 9 有助于理解有限体积、网格和算例结构，但版本号不是同一条发布序列。旧教程中的文件名、边界条件参数、库名和求解器调用方法需要逐项核对，不能仅把文件头的 `Version` 改成 v2512。':'本站使用 **OpenCFD OpenFOAM v2512**。Wolf Dynamics 培训用于参考有限体积原理、网格概念与算例教学思路；本课程的命令、字典和运行步骤按 v2512 官方教程与源码核对。读者可以沿统一版本完成从输入到结果检查的练习。',
  'OF9 源案例须迁移后再运行。':'使用 v2512 输入建立独立网格副本，改变网格几何时保持物理条件与比较位置一致。',
  '旧 Foundation 9 演示求解器应先按 v2512 编程课程迁移和编译；本页不声称该旧程序可直接运行。':'本课下载包提供使用 v2512 scalarTransportFoam 的最小平移案例，可先用它建立比较方法，再扩展到高斯与方波初值。',
  '同样，Foundation 教程的 `fvModels/fvConstraints` 不能靠改文件名就变成 OpenCFD 的 `fvOptions`。需要同时检查字典层次、C++ 基类与方程中的调用位置，详见[动量源迁移实例](/read/?slug=programming-12)。':'在 v2512 中配置 `fvOptions` 时，需要同时检查字典层次、源项作用的场和方程中的调用位置。可继续阅读[动量源实现实例](/read/?slug=programming-12)，将字典条目与实际代码联系起来。',
  '不应沿用其他分支或旧资料中未经核对的 `type residuals`。':'本课程使用已核对的 `solverInfo` 配置保存运行过程信息。',
  'Wolf Dynamics 的基础培训为教学顺序、算例组织和有限体积概念提供参考。用户提供的基础资料采用 Foundation 9；本站运行基线是 OpenCFD v2512，所以保留概念关联，同时根据 v2512 官方教程和源码核对文件、命令与设置。这里是重新编写的中文课程，不是把旧幻灯片原样改一个版本号。':'Wolf Dynamics 的基础培训为有限体积原理、网格解释和算例组织提供参考。课程操作统一使用 OpenCFD OpenFOAM v2512，相关命令、配置与案例按该版本官方教程和源码核对。教学图注明作者、材料与页码，运行示例另外说明输入、软件构建和核验范围，便于读者追溯依据。',
  '### 资料来源与版本处理':'### 资料来源与操作依据',
  '最小可复現输入':'最小可复现输入',
 }
 for before,after in replacements.items():body=body.replace(before,after)
 assert not re.search(r'Foundation\s*9|\bOF9\b|OpenFOAM\s*9',body)
 return body

def final_teaching_corrections(slug,body):
 """Idempotent, evidence-based corrections applied after source-block checks.

This deliberately leaves figure HTML byte-for-byte unchanged. In particular,
movingCone has pointMotionUx and no Allrun in the official v2512 archive.
"""
 if slug=='snappyhexmesh-workflow':
  body=body.replace('原始脚本采用并行流程，不能在没有 0 场、没有必要特征文件的目录中，照抄上面四条概念命令就期待全部设置自动完成。','上面四条命令概括的是串行网格生成与检查，不包含完整求解准备。motorBike 的原始脚本采用并行流程，还需按 Allrun 完成几何复制、特征提取和分区，并在求解前恢复初始场；不要把缺少 0 场误当作 snappyHexMesh 本身无法生成网格的原因。')
  body=body.replace('局部细化覆盖尾迹、缝隙或曲率变化处。其次启用 snap','局部细化覆盖尾迹、缝隙或曲率变化处。\n\n其次启用 snap')
  body=body.replace('增加迭代次数不能代替必要分辨率。最后增加 layers','增加迭代次数不能代替必要分辨率。\n\n最后增加 layers')
 elif slug=='moving-mesh-and-ami':
  body=body.replace('# 先定位 v2512 的完整运动案例，再阅读它的 Allrun 和字典','# 定位 v2512 的运动案例，阅读网格运动字典与点运动字段')
  body=body.replace('-name dynamicMeshDict -o -name pointDisplacement','-name dynamicMeshDict -o -name pointMotionUx')
 elif slug=='simple-piso-pimple':
  body=body.replace('下面的 PIMPLE 片段用于解释外层与内层的关系','上面的 PIMPLE 片段用于解释外层与内层的关系')
 elif slug=='advection-schemes-boundedness':
  paragraphs=body.split('\n\n')
  results=[i for i,p in enumerate(paragraphs) if p.startswith('本轮已在 v2512 实际运行该基线至 0.2 s：')]
  parameters=[i for i,p in enumerate(paragraphs) if p.startswith('配套一维案例给出了紧支撑的余弦平方脉冲：')]
  if results and parameters and results[0]<parameters[0]:
   result=paragraphs.pop(results[0])
   index=next(i for i,p in enumerate(paragraphs) if p.startswith('配套一维案例给出了紧支撑的余弦平方脉冲：'))
   paragraphs.insert(index+1,result);body='\n\n'.join(paragraphs)
 return body

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--base',type=Path);parser.add_argument('--packages-only',action='store_true');args=parser.parse_args()
 packages=build_packages()
 if args.packages_only:return
 base=args.base or (BACKUP if BACKUP.exists() else TARGET)
 baseline=json.loads(base.read_text(encoding='utf-8'));base_lessons={x['slug']:x for x in baseline if x['kind']=='lesson'}
 data=json.loads(TARGET.read_text(encoding='utf-8')) if TARGET.exists() else baseline
 lessons=[x for x in data if x['kind']=='lesson'];assert len(lessons)==len(base_lessons)==29
 assert not any(x.get('metadata',{}).get('editorial_revision')==REVISION for x in base_lessons.values()),'Use the preserved baseline or rerun build-core.py first.'
 assert set(REFINEMENTS)==set(range(1,30)),'Missing lesson refinement'
 for x in lessons:
  cfg=REFINEMENTS[x['sort_order']];old=base_lessons[x['slug']]['body'];body=old
  if cfg.get('lead'):
   first,rest=body.split('\n\n',1)
   body=cfg['lead']+'\n\n'+(first+'\n\n' if '$' in first or '\\[' in first else '')+rest
  for anchor,extra in cfg['bridges']:
   assert body.count(anchor)==1,(x['slug'],anchor)
   body=body.replace(anchor,anchor+'\n\n'+extra,1)
  downloads=[];instructions=[]
  for key,location,explanation in cfg['cases']:
   d=dict(packages[key]);d['description']='解压后进入 '+key+'/'+location+'。'+explanation
   existing=next((item for item in downloads if item['url']==d['url']),None)
   if existing:existing['description']+=' 同包另一入口：'+location+'。'+explanation
   else:downloads.append(d)
   instructions.append(f'- [{d["label"]}]({d["url"]})：包内 `{location}`。{explanation}')
  body+='\n\n### 对应案例与练习文件\n\n'+'\n\n'.join(instructions)+'\n\n下载后先读包根目录的 `README.zh-CN.md`，在副本中修改本课指定文件。包中保留官方原始输入；运行状态与系统依赖在说明中单独列出。'
  # First check baseline code/TeX preservation; only then apply the small,
  # explicitly verified corrections in final_teaching_corrections below.
  for code in re.findall(r'```[\s\S]*?```',old):assert code in body,(x['slug'],'code changed')
  for tex in re.findall(r'\\\[[\s\S]*?\\\]',old):assert tex in body,(x['slug'],'TeX changed')
  assert len(body)>len(old)+350,(x['slug'],'insufficient substantive explanation')
  body=focus_v2512(body)
  if x['sort_order']==12 and (ROOT/'.openfoam-work/course-refinement/RUN-VERIFICATION.txt').exists():
   anchor='### 设计一个有意义的比较'
   result='本轮已在 v2512 实际运行该基线至 0.2 s：峰值约为 0.776896 K，线积分约为 0.100000 K·m，与解析平移的平均绝对误差约为 0.0287741 K。这里 T 表示被动温差。峰值下降而积分保持，说明不能仅用守恒判断形状误差；Euler 与 upwind 的联合数值扩散使脉冲展宽。包内 verification 提供日志和 comparison.csv；这是一组基线结果，并非所有格式的优劣结论。'
   body=body.replace(anchor,anchor+'\n\n'+result)
  if x['sort_order']==13 and (ROOT/'.openfoam-work/course-refinement/RUN-VERIFICATION.txt').exists():
   anchor='### 材料交界不能只比较温度图是否平滑'
   result='本轮已用 v2512 完成该 40 单元稳态案例：blockMesh 与完整 checkMesh 通过，PCG+DIC 求解正常结束；在输出精度 12 位的 ASCII 数据上，40 个单元中心温度与解析直线的比较误差为零。这个结果只覆盖均匀正交、常系数和固定端温设置，不说明一般扩散问题没有离散误差。日志、输入哈希与 comparison.csv 已放入包内 verification。'
   body=body.replace(anchor,anchor+'\n\n'+result)
  body=final_teaching_corrections(x['slug'],body)
  x['body']=body;x['metadata']['downloads']=downloads;x['metadata']['topics']=cfg['topics'];x['metadata']['editorial_revision']=REVISION
  if isinstance(x['metadata'].get('source'),str):x['metadata']['source']=re.sub(r'[（(]Foundation\s*9[）)]','',x['metadata']['source']).replace('（概念参考，OF9 算例须适配）','（网格质量概念参考）')
  assert set(cfg['topics'])<={'turbulence','multiphase','meshing','dynamic-mesh'}
 for x in data:
  x['body']=re.sub(r'(\*\*[^*\n]+：\*\*)(?=\S)',r'\1 ',x['body'])
  if x['slug']=='foamlab-build-log-2026-10':
   x['body']=focus_v2512(x['body'])
   if isinstance(x['metadata'].get('source'),str):x['metadata']['source']=re.sub(r'[（(]Foundation\s*9[）)]','',x['metadata']['source'])
 TARGET.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('REFINED',len(lessons),'lessons;',sum(len(x['body']) for x in lessons),'body characters;',len(packages),'shared ZIP packages')

if __name__=='__main__':main()
