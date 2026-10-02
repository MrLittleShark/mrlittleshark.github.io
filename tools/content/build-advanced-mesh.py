"""Package the pinned OpenFOAM v2512 tutorials used by the mesh lessons."""
from pathlib import Path
import tarfile, re, json, zipfile, hashlib

ROOT = Path(__file__).resolve().parents[2]
WORK = Path('F:/UbuntuShareFolder/.foamlab-build/advanced-mesh')
CASES = WORK / 'source' / 'foamLabAdvancedMesh'
ARCHIVE = ROOT / '.openfoam-work/replan/openfoam-v2512.tar.gz'
SPECS = {
 '01-deforming': ('incompressible/pimpleFoam/laminar/movingCone', 'pimpleFoam', 0.003, 'U p'),
 '02-overset': ('incompressible/overPimpleDyMFoam/rotatingSquare', 'overPimpleDyMFoam', 0.28, 'U p zoneID'),
 '03-refinement': ('multiphase/interFoam/laminar/damBreakWithObstacle', 'interFoam', 0.3, 'U p_rgh alpha.water cellLevel'),
 '04-ami': ('incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D', 'pimpleFoam', 0.5, 'U p'),
 '05-mrf': ('incompressible/simpleFoam/mixerVessel2D', 'simpleFoam', 500, 'U p k epsilon'),
 '06-srf': ('incompressible/SRFSimpleFoam/mixer', 'SRFSimpleFoam', 1000, 'U Urel p'),
}

def put(path, text):
 path.parent.mkdir(parents=True, exist_ok=True)
 path.write_text(text.strip()+'\n', encoding='utf-8', newline='\n')

def entry(path, name, value):
 s=path.read_text(encoding='utf-8')
 s,n=re.subn(r'(?m)^(\s*'+re.escape(name)+r'\s+)[^;]+;',lambda m:m[1]+str(value)+';',s)
 assert n==1,(path,name,n)
 put(path,s)

def build():
 with tarfile.open(ARCHIVE) as tar:
  for member in tar:
   if not member.isfile():continue
   if member.name.endswith('/COPYING') and member.name.count('/')==1:
    license_text=tar.extractfile(member).read().decode()
   for name,(source,*_) in SPECS.items():
    marker='/tutorials/'+source+'/'
    if marker not in member.name:continue
    rel=member.name.split(marker,1)[1]
    if rel.split('/')[0] not in ('0','0.orig','constant','system'):continue
    dst=(CASES/name/rel).resolve()
    assert dst.is_relative_to(CASES.resolve())
    put(dst,tar.extractfile(member).read().decode('utf-8'))
 for name,(source,solver,end,fields) in SPECS.items():
  case=CASES/name
  put(case/'COPYING',license_text)
  control=case/'system/controlDict'
  entry(control,'endTime',end);entry(control,'writeFormat','ascii');entry(control,'writePrecision',10)
  if name=='01-deforming':
   s=control.read_text();s=re.sub(r'functions\s*\{.*?\}', 'functions {}', s, flags=re.S);put(control,s)
   entry(control,'writeInterval',100)
  if name=='02-overset':
   entry(control,'writeInterval',0.04)
   # Keep the rotating component inside the background domain throughout a revolution.
   mesh=case/'system/blockMeshDict'
   put(mesh,mesh.read_text().replace('//- 0 degrees shifted down','//- Centred rotating component').replace('-0.20','0.20').replace('0.40','0.80'))
   motion=case/'constant/dynamicMeshDict';put(motion,motion.read_text().replace('(0.005 0 0.005)','(0.005 0.005 0.005)'))
   topo=case/'system/topoSetDict';put(topo,topo.read_text().replace('(0.004 -0.001 -100)(0.006 0.003 100)','(0.004 0.003 -100)(0.006 0.007 100)'))
   schemes=case/'system/fvSchemes';put(schemes,schemes.read_text().replace('(0.00 -0.0021 -0.0001)(0.00701 0.00401 0.0101)','(-0.0001 -0.0001 -0.0001)(0.0101 0.0101 0.0101)'))
   options=case/'constant/fvOptions';put(options,options.read_text().split('\nlimitU')[0])
  if name=='03-refinement':
   entry(control,'writeInterval',0.05)
   mesh=case/'system/blockMeshDict';put(mesh,mesh.read_text().replace('(32 32 32)','(16 16 16)'))
   entry(case/'constant/dynamicMeshDict','maxRefinement',1)
   entry(case/'constant/dynamicMeshDict','maxCells',50000)
  if name=='04-ami':entry(control,'writeInterval',0.1)
  # Include only the commands actually run in the virtual machine.
  pre=[]
  if (case/'0.orig').exists() and name!='02-overset':pre.append('cp -r 0.orig 0')
  if (case/'system/blockMeshDict.m4').exists():pre.append('m4 system/blockMeshDict.m4 > system/blockMeshDict')
  pre+=['blockMesh > log.blockMesh 2>&1']
  if name=='02-overset':pre+=['topoSet > log.topoSet.first 2>&1','subsetMesh box -patch hole -overwrite > log.subsetMesh 2>&1','topoSet > log.topoSet 2>&1','cp -r 0.orig 0','setFields > log.setFields 2>&1']
  if name=='03-refinement':pre+=['topoSet > log.topoSet 2>&1','subsetMesh -overwrite c0 -patch walls > log.subsetMesh 2>&1','setFields > log.setFields 2>&1']
  if name=='04-ami':pre+=['topoSet > log.topoSet 2>&1']
  pre+=['checkMesh -allGeometry -allTopology > log.checkMesh.initial 2>&1',
         f'{solver} > log.{solver} 2>&1',
         'checkMesh -allGeometry -allTopology -latestTime > log.checkMesh.final 2>&1',
         'checkMesh -latestTime > log.checkMesh.standard 2>&1',
         f"foamToVTK -ascii -legacy -no-boundary {'-noZero ' if name=='02-overset' else ''}-fields '({fields})' > log.foamToVTK 2>&1",
         'touch case.foam']
  put(case/'Allrun', '#!/usr/bin/env bash\nset -e\ncd "$(dirname "$0")"\n: "${WM_PROJECT_DIR:?请先加载 OpenFOAM v2512 环境}"\n'+ '\n'.join(pre))
  put(case/'README.md',f'''# {name} / OpenFOAM v2512

来源：OpenFOAM v2512 官方教程 `tutorials/{source}`。
本站修改：短程教学运行、ASCII 输出与结果导出；02-overset 将旋转区域移入背景域中央、同步调整挖孔与搜索范围，移除域外速度阻尼；03-refinement 使用 16×16×16 背景网格和一级加密。
原始文件版权声明保留，许可证见 COPYING。

将算例解压到 Linux 工作目录，加载 v2512 环境，在算例目录运行 `bash Allrun`。
脚本依次生成网格、设置场、计算、检查网格并导出 VTK。
日志保存在 log.* 文件；用 ParaView 打开 case.foam 或 VTK 文件夹。
再次计算时使用一份新解压的算例目录。

求解器：{solver}；结束时间/迭代步：{end}。
课程：https://foamlabshark.github.io/read/?slug=advanced-mesh-{name[:2]}
''')
 package()

def package():
 out=ROOT/'source-openfoam/downloads/meshes';out.mkdir(parents=True,exist_ok=True)
 manifest={}
 for name,(source,solver,end,fields) in SPECS.items():
  target=out/f'v2512-{name}.zip'
  with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
   for p in sorted((CASES/name).rglob('*')):
    if p.is_file():z.write(p,Path('foamLabAdvancedMesh')/name/p.relative_to(CASES/name))
  manifest[name[:2]]=dict(url='/downloads/meshes/'+target.name,bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest(),source='tutorials/'+source,solver=solver,end=end)
 put(out/'advanced-mesh-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 print(json.dumps(manifest,ensure_ascii=False))

if __name__=='__main__':build()
