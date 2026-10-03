"""Build the small OpenFOAM v2512 cases used by the functionObject topic."""
from pathlib import Path
import tarfile,re,json,zipfile,hashlib,shutil

ROOT=Path(__file__).resolve().parents[2]
WORK=Path('F:/UbuntuShareFolder/.foamlab-build/function-objects')
CASES=WORK/'source'/'foamLabFunctionObjects'
SPECS={
 '01-cavity':('incompressible/icoFoam/cavity/cavity','icoFoam',0.5,0.005,10),
 '02-pitzDaily':('incompressible/simpleFoam/pitzDaily','simpleFoam',100,1,20),
 '03-hotRoom':('heatTransfer/buoyantPimpleFoam/hotRoom','buoyantPimpleFoam',0.2,0.01,0.1),
 '04-damBreak':('multiphase/interFoam/laminar/damBreak/damBreak','interFoam',0.2,0.001,0.05),
}
def put(p,s):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n',encoding='utf-8',newline='\n')
def fo(name,typ,body='',lib='fieldFunctionObjects',control='timeStep',interval=10):
 return f'''{name}
{{
    type {typ};
    libs ({lib});
    errors strict;
    writeControl {control};
    writeInterval {interval};
{body}
}}
'''
def build():
 with tarfile.open(ROOT/'.openfoam-work/replan/openfoam-v2512.tar.gz') as t:
  for m in t:
   if not m.isfile():continue
   if m.name.endswith('/COPYING') and m.name.count('/')==1:license=t.extractfile(m).read().decode()
   for case,(path,*_) in SPECS.items():
    marker='/tutorials/'+path+'/'
    if marker not in m.name:continue
    rel=m.name.split(marker,1)[1]
    if rel.split('/')[0] not in ('0','0.orig','constant','system'):continue
    dst=(CASES/case/rel).resolve();assert dst.is_relative_to(CASES.resolve());put(dst,t.extractfile(m).read().decode())
 for case,(path,solver,end,dt,wi) in SPECS.items():
  c=CASES/case;control=(c/'system/controlDict').read_text()
  # Tutorials with #includeFunc lists get a standalone teaching controlDict.
  put(c/'system/controlDict',f'''FoamFile
{{ version 2.0; format ascii; class dictionary; object controlDict; }}
application {solver};
startFrom startTime;
startTime 0;
stopAt endTime;
endTime {end};
deltaT {dt};
writeControl {'adjustableRunTime' if case in ('03-hotRoom','04-damBreak') else 'timeStep'};
writeInterval {wi};
purgeWrite 0;
writeFormat ascii;
writePrecision 10;
writeCompression off;
timeFormat general;
timePrecision 8;
runTimeModifiable true;
adjustTimeStep {'yes' if case in ('03-hotRoom','04-damBreak') else 'no'};
maxCo 0.5;
maxAlphaCo 0.5;
maxDeltaT {dt};
functions
{{
    #include "functions"
}}
''')
  put(c/'COPYING',license)
  pre=['cp -r 0.orig 0'] if (c/'0.orig').exists() else []
  pre+=['blockMesh > log.blockMesh 2>&1','checkMesh > log.checkMesh 2>&1']
  if case=='04-damBreak':pre+=['setFields > log.setFields 2>&1']
  pre+=[f'{solver} > log.{solver} 2>&1','touch case.foam']
  put(c/'Allrun','#!/usr/bin/env bash\nset -e\ncd "$(dirname "$0")"\n: "${WM_PROJECT_DIR:?请先加载 OpenFOAM v2512 环境}"\n'+'\n'.join(pre))
  put(c/'README.md',f'''# {case} / OpenFOAM v2512

来源：v2512 官方教程 `tutorials/{path}`；原始许可证见 COPYING。
本站增加 system/functions 中的后处理配置，使用短程运行和 ASCII 输出。
加载环境后在此目录运行 `bash Allrun`。使用新解压的目录开始一次计算。
运行后用 ParaView 打开 case.foam，探针、积分和导出文件在 postProcessing 中。
求解器：{solver}；终止时间/迭代步：{end}。
''')
 # Cavity: 0.1 m cube with one cell in z, moving lid U=(1 0 0).
 f=[]
 f+=[fo('speed','mag','    field U;\n    result speed;'),fo('velocityGradient','grad','    field U;\n    result gradU;')]
 for name,typ in [('vorticity','vorticity'),('Qcriterion','Q'),('lambda2','Lambda2'),('flowType','flowType'),('velocityComponents','components')]:f.append(fo(name,typ,'    field U;'))
 f.append(fo('courant','CourantNo','    field phi;\n    result Co;'))
 f.append(fo('extrema','fieldMinMax','    fields (p U speed);\n    mode magnitude;\n    location true;'))
 f.append(fo('volumeMean','volFieldValue','    regionType all;\n    operation volAverage;\n    fields (U p speed);\n    writeFields false;'))
 f.append(fo('lidPressure','surfaceFieldValue','    regionType patch;\n    name movingWall;\n    operation areaAverage;\n    fields (p);\n    writeArea true;\n    writeFields false;'))
 f.append(fo('pointHistory','probes','    fields (U p);\n    probeLocations ((0.05 0.05 0.005) (0.05 0.075 0.005));\n    interpolationScheme cellPoint;\n    fixedLocations true;\n    includeOutOfBounds false;','sampling',interval=1))
 f.append(fo('lidProbes','patchProbes','    patches (movingWall);\n    fields (p U);\n    probeLocations ((0.025 0.1 0.005) (0.075 0.1 0.005));','sampling'))
 f.append(fo('centreLines','sets','''    fields (U p);
    interpolationScheme cellPoint;
    setFormat raw;
    sets
    {
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.0001 0.005);
            end (0.05 0.0999 0.005);
            nPoints 51;
        }
        horizontal
        {
            type uniform;
            axis x;
            start (0.0001 0.05 0.005);
            end (0.0999 0.05 0.005);
            nPoints 51;
        }
    }''','sampling',control='writeTime',interval=1))
 f.append(fo('midPlane','surfaces','''    fields (U p speed);
    surfaceFormat vtk;
    interpolationScheme cellPoint;
    surfaces
    {
        midZ
        {
            type cuttingPlane;
            planeType pointAndNormal;
            pointAndNormalDict { point (0 0 0.005); normal (0 0 1); }
            interpolate true;
        }
    }''','sampling',control='writeTime',interval=1))
 f.append(fo('averages','fieldAverage','''    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart false;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );''',control='writeTime',interval=1))
 f.append(fo('residuals','solverInfo','    fields (p U);\n    writeResidualFields false;','utilityFunctionObjects',interval=1))
 f.append(fo('continuity','continuityError','    phi phi;'))
 f.append(fo('exportVTK','vtkWrite','    fields (U p speed);\n    boundary true;\n    internal true;\n    format ascii;\n    interpolate false;','utilityFunctionObjects',control='writeTime',interval=1))
 f.append(fo('centres','writeCellCentres',''))
 f.append(fo('volumes','writeCellVolumes',''))
 f.append(fo('clock','timeInfo','', 'utilityFunctionObjects'))
 for name,typ,body in [
  ('speedSquared','magSqr','field U; result speedSquared;'),
  ('divFlux','div','field phi; result divPhi;'),
  ('doubleVelocity','add','fields (U U); result twoU;'),
  ('pressureDifference','subtract','fields (p p); result zeroPressure;'),
  ('pressureProduct','multiply','fields (p p); result pressureSquared;'),
  ('enstrophy','enstrophy','field U;'),('lambVector','LambVector','field U;'),
  ('partition','processorField',''),
  ('facePressure','surfaceInterpolate','fields ((p pFace));'),
  ('energy','exprField','field kineticEnergy; expression "0.5*magSqr(U)"; dimensions [0 2 -2 0 0 0 0];'),
  ('statistics','fieldStatistics','fields (p U); statistics (min max mean variance); mode component; mean volumetric; internal true; extrema true;'),
  ('speedHistogram','histogram','field speed; model equalBinWidth; nBins 10; min 0; max 1;')
 ]:f.append(fo(name,typ,'    '+body,control='writeTime',interval=1))
 f.append(fo('streamlines','streamLine','''    U U;
    fields (U p);
    setFormat vtk;
    direction bidirectional;
    lifeTime 200;
    nSubCycle 5;
    seedSampleSet
    {
        type uniform;
        axis y;
        start (0.05 0.01 0.005);
        end (0.05 0.09 0.005);
        nPoints 5;
    }''',control='writeTime',interval=1))
 f.append(fo('exportEnsight','ensightWrite','    fields (U p);\n    format ascii;','utilityFunctionObjects',control='writeTime',interval=1))
 put(CASES/'01-cavity/system/functions','\n'.join(f))
 post=fo('readSaved','readFields','    fields (U p);')+fo('savedSpeed','mag','    field U;\n    result postSpeed;')+fo('savedVorticity','vorticity','    field U;')
 put(CASES/'01-cavity/system/postProcess','FoamFile { version 2.0; format ascii; class dictionary; object postProcess; }\nfunctions\n{\n'+post+'}\n')
 run=CASES/'01-cavity/Allrun'
 put(run,run.read_text()+'''\npostProcess -func 'mag(U)' -latestTime > log.postProcess.mag 2>&1
postProcess -func 'grad(p)' -time 0.5 > log.postProcess.grad 2>&1
postProcess -func vorticity -latestTime > log.postProcess.vorticity 2>&1
postProcess -funcs '(Q Lambda2)' -latestTime > log.postProcess.vortex 2>&1
postProcess -dict system/postProcess -latestTime > log.postProcess.dictionary 2>&1
''')
 # Turbulent backward-facing step: model-dependent wall and force objects.
 f=[]
 for typ in ['yPlus','wallShearStress','turbulenceFields']:
  body='    fields (k epsilon nut R);' if typ=='turbulenceFields' else ''
  f.append(fo(typ,typ,body,control='writeTime',interval=1))
 f.append(fo('wallForces','forces','    patches (upperWall lowerWall);\n    rho rhoInf;\n    rhoInf 1;\n    CofR (0 0 0);\n    pRef 0;','forces'))
 f.append(fo('wallCoefficients','forceCoeffs','    patches (upperWall lowerWall);\n    rho rhoInf;\n    rhoInf 1;\n    CofR (0 0 0);\n    dragDir (1 0 0);\n    liftDir (0 1 0);\n    magUInf 10;\n    lRef 0.0254;\n    Aref 0.0000254;','forces'))
 for name,patch in [('inletFlux','inlet'),('outletFlux','outlet')]:f.append(fo(name,'surfaceFieldValue',f'    regionType patch;\n    name {patch};\n    operation sum;\n    fields (phi);\n    writeFields false;'))
 for name,patch in [('inletPressure','inlet'),('outletPressure','outlet')]:f.append(fo(name,'surfaceFieldValue',f'    regionType patch;\n    name {patch};\n    operation areaAverage;\n    fields (p);\n    writeFields false;'))
 f.append(fo('staticPressure','pressure','    mode static;\n    rho rhoInf;\n    rhoInf 1;\n    result pPa;',control='writeTime',interval=1))
 f.append(fo('residuals','solverInfo','    fields (p U k epsilon);','utilityFunctionObjects',interval=1))
 put(CASES/'02-pitzDaily/system/functions','\n'.join(f))
 dp=fo('pressureDrop','multiFieldValue','''    operation subtract;
    functions
    {
        inletMean
        {
            type surfaceFieldValue;
            regionType patch;
            name inlet;
            operation areaAverage;
            fields (p);
            writeFields false;
        }
        outletMean
        {
            type surfaceFieldValue;
            regionType patch;
            name outlet;
            operation areaAverage;
            fields (p);
            writeFields false;
        }
    }''')
 p=CASES/'02-pitzDaily/system/functions';put(p,p.read_text()+'\n'+dp)
 run=CASES/'02-pitzDaily/Allrun';put(run,run.read_text()+'''\nsimpleFoam -postProcess -func yPlus -latestTime > log.solverPostProcess 2>&1\n''')
 f=[fo('wallHeatFlux','wallHeatFlux','    model wall;',control='writeTime',interval=1),fo('temperatureRange','fieldMinMax','    fields (T);\n    location true;',interval=1),fo('meanTemperature','volFieldValue','    regionType all;\n    operation volAverage;\n    fields (T);\n    writeFields false;',interval=1)]
 f.append(fo('heatGauge','wallHeatFlux','    model gauge;\n    patch floor;\n    probeLocations ((2.5 0 5) (7.5 0 5));\n    Tgauge 300;\n    convective true;\n    radiative false;\n    writeFields true;',control='writeTime',interval=1))
 f.insert(0,fo('readRadiation','readFields','    fields (qin);\n    readOnStart true;'))
 put(CASES/'03-hotRoom/0.orig/qin','''FoamFile { version 2.0; format ascii; class volScalarField; object qin; }
dimensions [1 0 -3 0 0 0 0];
internalField uniform 0;
boundaryField { ".*" { type calculated; value uniform 0; } }
''')
 f.append(fo('heatTransfer','heatTransferCoeff','    field T;\n    patches (floor ceiling);\n    htcModel localReferenceTemperature;\n    result htc;',control='writeTime',interval=1))
 put(CASES/'03-hotRoom/system/functions','\n'.join(f))
 f=[fo('waterVolume','volFieldValue','    regionType all;\n    operation volIntegrate;\n    fields (alpha.water);\n    writeFields false;',interval=10),fo('level','interfaceHeight','    alpha alpha.water;\n    liquid true;\n    direction (0 -1 0);\n    locations ((0.1 0 0.0073) (0.3 0 0.0073));'),fo('waterRange','fieldMinMax','    fields (alpha.water);')]
 f.append(fo('freeSurface','surfaces','''    fields (U p_rgh);
    surfaceFormat vtk;
    surfaces
    {
        waterAir
        {
            type isoSurfaceCell;
            isoField alpha.water;
            isoValue 0.5;
            interpolate true;
        }
    }''','sampling',control='writeTime',interval=1))
 put(CASES/'04-damBreak/system/functions','\n'.join(f))
 # Separate automatic-stop case keeps the main cavity time range unchanged.
 extra=CASES/'05-autoStop';shutil.copytree(CASES/'01-cavity',extra,dirs_exist_ok=True)
 stop=fo('stopAfter','runTimeControl','    conditions { elapsed { type maxDuration; duration 0.2; } }\n    satisfiedAction end;\n    nWriteStep 0;','utilityFunctionObjects',interval=1)
 put(extra/'system/functions',fo('residuals','solverInfo','    fields (p U);','utilityFunctionObjects',interval=1)+stop)
 put(extra/'Allrun','#!/usr/bin/env bash\nset -e\ncd "$(dirname "$0")"\nblockMesh > log.blockMesh 2>&1\nicoFoam > log.icoFoam 2>&1\ntouch case.foam')
 put(extra/'README.md','# 05-autoStop\n\n运行 bash Allrun。runTimeControl 在模拟时间经过 0.2 s 后正常结束计算。对应教程：自动控制。')
 put(WORK/'run.sh','''#!/usr/bin/env bash
shared=/mnt/hgfs/UbuntuShareFolder/.foamlab-build/function-objects
exec > "$shared/run.log" 2>&1
source /usr/lib/openfoam/openfoam2512/etc/bashrc
set -e
work=$(mktemp -d /home/shark/foamlab-functionobjects-XXXXXX)
echo "WORK=$work"
cp -r "$shared/source/foamLabFunctionObjects" "$work/"
echo "OpenFOAM $WM_PROJECT_VERSION"
command -v icoFoam
for c in "$work/foamLabFunctionObjects"/*; do
 echo "RUN $(basename "$c")"
 if (cd "$c" && bash Allrun); then echo "PASS $(basename "$c")"; else echo "FAIL $(basename "$c")"; fi
done
tar -czf "$shared/results-linux.tar.gz" -C "$work" foamLabFunctionObjects
python3 - "$work/foamLabFunctionObjects" "$shared/results" <<'PY'
import shutil,sys
shutil.copytree(sys.argv[1],sys.argv[2],dirs_exist_ok=True,ignore=lambda p,n:[x for x in n if ':' in x])
PY
postProcess -list > "$shared/postProcess-list.txt" 2>&1
echo COMPLETE
''')
 print('Built',len(SPECS),'cases in',CASES)
if __name__=='__main__':build()
