"""Build original v2512 dictionary-code teaching cases (no supplied files modified)."""
from pathlib import Path
import json, textwrap, zipfile, hashlib

ROOT = Path(__file__).resolve().parents[2]
WORK = Path('F:/UbuntuShareFolder/.foamlab-build/coded-fields')
CASES = WORK / 'source' / 'foamLabCodedFields'
OUT = ROOT / 'source-openfoam/downloads/programming'

def put(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).strip()+'\n', encoding='utf-8', newline='\n')

def header(name, cls='dictionary'):
    return f'// FoamLab / OpenFOAM v2512 / SPDX-License-Identifier: GPL-3.0-or-later\nFoamFile\n{{\n    version 2.0;\n    format ascii;\n    class {cls};\n    object {name};\n}}\n\n'

INCLUDE = '''codeInclude
    #{
        #include "fvCFD.H"
    #};
    codeOptions
    #{
        -I$(LIB_SRC)/finiteVolume/lnInclude -I$(LIB_SRC)/meshTools/lnInclude
    #};
    codeLibs
    #{
        -lfiniteVolume -lmeshTools
    #};'''

def stream(code):
    return '#codeStream\n{\n    '+INCLUDE+'\n    code\n    #{\n'+textwrap.indent(code.strip(),'        ')+'\n    #};\n};'

MESH = '''const IOdictionary& fieldDict = static_cast<const IOdictionary&>(dict);
const fvMesh& mesh = refCast<const fvMesh>(fieldDict.db());'''
TEMP_CODES = {
 '01-uniform': MESH+'''
scalarField temperature(mesh.nCells(), 300.0);
temperature.writeEntry("", os);''',
 '02-linear': MESH+'''
scalarField temperature(mesh.nCells(), 300.0);
const scalar length = 0.1;
forAll(temperature, cellI)
{
    const scalar x = mesh.C()[cellI].x();
    temperature[cellI] = 300.0 + 20.0*x/length;
}
temperature.writeEntry("", os);''',
 '03-gaussian': MESH+'''
scalarField temperature(mesh.nCells(), 300.0);
const scalar xc = 0.05, yc = 0.01;
const scalar sigmaX = 0.01, sigmaY = 0.003;
forAll(temperature, cellI)
{
    const vector& centre = mesh.C()[cellI];
    const scalar r2 = sqr((centre.x()-xc)/sigmaX)
                    + sqr((centre.y()-yc)/sigmaY);
    temperature[cellI] = 300.0 + 50.0*Foam::exp(-0.5*r2);
}
temperature.writeEntry("", os);''',
 '04-ellipse': MESH+'''
scalarField temperature(mesh.nCells(), 300.0);
const scalar xc = 0.05, yc = 0.01;
const scalar a = 0.02, b = 0.005;
forAll(temperature, cellI)
{
    const vector& centre = mesh.C()[cellI];
    const scalar q = sqr((centre.x()-xc)/a)
                   + sqr((centre.y()-yc)/b);
    if (q <= 1.0)
    {
        temperature[cellI] = 350.0;
    }
}
temperature.writeEntry("", os);'''
}

PROFILE_INIT = MESH+'''
vectorField velocity(mesh.nCells(), vector::zero);
const scalar height = 0.01, maxSpeed = 0.15;
forAll(velocity, cellI)
{
    const scalar eta = mesh.C()[cellI].y()/height;
    velocity[cellI] = vector(4.0*maxSpeed*eta*(1.0-eta), 0, 0);
}
velocity.writeEntry("", os);'''

PROFILE_FIXED = '''const IOdictionary& fieldDict = static_cast<const IOdictionary&>
(
    dict.parent().parent()
);
const fvMesh& mesh = refCast<const fvMesh>(fieldDict.db());
const label patchID = mesh.boundaryMesh().findPatchID("inlet");
if (patchID < 0)
{
    FatalErrorInFunction << "Patch inlet was not found" << exit(FatalError);
}
const fvPatch& inletPatch = mesh.boundary()[patchID];
vectorField velocity(inletPatch.size(), vector::zero);
const scalar height = 0.01, maxSpeed = 0.15;
forAll(velocity, faceI)
{
    const scalar eta = inletPatch.Cf()[faceI].y()/height;
    velocity[faceI] = vector(4.0*maxSpeed*eta*(1.0-eta), 0, 0);
}
velocity.writeEntry("", os);'''

STEADY = '''const vectorField& centres = patch().Cf();
vectorField velocity(patch().size(), vector::zero);
const scalar height = 0.01, maxSpeed = 0.15;
forAll(velocity, faceI)
{
    const scalar eta = centres[faceI].y()/height;
    velocity[faceI] = vector(4.0*maxSpeed*eta*(1.0-eta), 0, 0);
}
operator==(velocity);'''

RAMP = '''const scalar t = this->db().time().value();
const scalar start = 0.0, rampTime = 0.2, targetSpeed = 0.1;
const scalar fraction = min(max((t-start)/rampTime, scalar(0)), scalar(1));
operator==(vector(targetSpeed*fraction, 0, 0));'''

SINE = '''const scalar t = this->db().time().value();
const scalar meanSpeed = 0.1, amplitude = 0.5, frequency = 1.0;
const scalar pi = constant::mathematical::pi;
const scalar speed = meanSpeed*(1.0 + amplitude*Foam::sin(2.0*pi*frequency*t));
operator==(vector(speed, 0, 0));'''

PULSED = '''const dictionary& parameters = this->dict();
const scalar height = parameters.get<scalar>("height");
const scalar meanSpeed = parameters.get<scalar>("meanSpeed");
const scalar amplitude = parameters.get<scalar>("amplitude");
const scalar frequency = parameters.get<scalar>("frequency");
const scalar phase = parameters.get<scalar>("phase");
if (height <= SMALL || meanSpeed < 0 || amplitude < 0 || amplitude > 1 || frequency < 0)
{
    FatalErrorInFunction
        << "Require height>0, meanSpeed>=0, 0<=amplitude<=1, frequency>=0"
        << exit(FatalError);
}
const vectorField& centres = patch().Cf();
const scalarField& areas = patch().magSf();
scalarField shape(patch().size(), 0.0);
forAll(shape, faceI)
{
    const scalar eta = centres[faceI].y()/height;
    shape[faceI] = max(4.0*eta*(1.0-eta), scalar(0));
}
const scalar totalArea = gSum(areas);
const scalar weightedShape = gSum(shape*areas);
if (totalArea <= VSMALL || weightedShape <= VSMALL)
{
    FatalErrorInFunction << "Check inlet geometry and height" << exit(FatalError);
}
const scalar t = this->db().time().value();
const scalar pi = constant::mathematical::pi;
const scalar speed = meanSpeed*(1.0 + amplitude*Foam::sin(2.0*pi*frequency*t + phase));
vectorField velocity(patch().size(), vector::zero);
forAll(velocity, faceI)
{
    velocity[faceI] = vector(speed*shape[faceI]*totalArea/weightedShape, 0, 0);
}
operator==(velocity);'''

def coded(name, code, context=''):
    return 'type codedFixedValue;\nvalue uniform (0 0 0);\nname '+name+';\n'+context+'\n'+INCLUDE+'\ncode\n#{\n'+textwrap.indent(code,'    ')+'\n#};'

def mesh(height):
    return header('blockMeshDict')+f'''scale 1;
vertices
(
    (0 0 0) (0.1 0 0) (0.1 {height} 0) (0 {height} 0)
    (0 0 0.001) (0.1 0 0.001) (0.1 {height} 0.001) (0 {height} 0.001)
);
blocks (hex (0 1 2 3 4 5 6 7) (80 20 1) simpleGrading (1 1 1));
edges ();
boundary
(
    inlet {{ type patch; faces ((0 4 7 3)); }}
    outlet {{ type patch; faces ((1 2 6 5)); }}
    walls {{ type wall; faces ((0 1 5 4) (3 7 6 2)); }}
    frontAndBack {{ type empty; faces ((0 3 2 1) (4 5 6 7)); }}
);
mergePatchPairs ();
'''

def controls(heat):
    app='laplacianFoam' if heat else 'icoFoam'
    result=header('controlDict')+f'''application {app};
startFrom startTime;
startTime 0;
stopAt endTime;
endTime {0.2 if heat else 1};
deltaT {0.002 if heat else 0.001};
writeControl runTime;
writeInterval 0.05;
purgeWrite 0;
writeFormat ascii;
writePrecision 12;
writeCompression off;
timeFormat general;
timePrecision 8;
runTimeModifiable true;
functions
{{
'''
    if heat:
        result+='''    meanTemperature
    {
        type volFieldValue;
        libs (fieldFunctionObjects);
        operation volAverage;
        fields (T);
        writeFields false;
        writeControl timeStep;
        writeInterval 1;
    }
'''
    else:
        for name,patch,op,field in [('inletMean','inlet','areaAverage','U'),('inletFlux','inlet','sum','phi'),('outletFlux','outlet','sum','phi')]:
            result+=f'''    {name}
    {{
        type surfaceFieldValue;
        libs (fieldFunctionObjects);
        regionType patch;
        name {patch};
        operation {op};
        fields ({field});
        writeFields false;
        writeControl timeStep;
        writeInterval 1;
    }}
'''
    return result+'}\n'

CASE_TITLES = ['均匀温度初值','沿 x 方向的线性温度初值','高斯热斑初值','椭圆热区初值','codeStream 固定入口剖面','codedFixedValue 固定入口剖面','逐渐启动的入口','周期变化的均匀入口','时空变化的脉动入口']
BCS = {
 '05-fixed-profile': 'type fixedValue;\nvalue '+stream(PROFILE_FIXED),
 '06-coded-steady': coded('foamLabSteadyProfile',STEADY),
 '07-ramp': coded('foamLabRamp',RAMP),
 '08-sine': coded('foamLabSine',SINE),
 '09-pulsed-profile': coded('foamLabPulsedProfile',PULSED,'''codeContext
{
    height 0.01;
    meanSpeed 0.1;
    amplitude 0.5;
    frequency 1.0;
    phase 0.0;
}''')
}

def main():
    for i, key in enumerate([*TEMP_CODES,*BCS]):
        p=CASES/key; heat=key in TEMP_CODES
        put(p/'system/blockMeshDict',mesh(0.02 if heat else 0.01))
        put(p/'system/controlDict',controls(heat))
        put(p/'system/decomposeParDict',header('decomposeParDict')+'''numberOfSubdomains 2;
method simple;
simpleCoeffs { n (1 2 1); delta 0.001; }
''')
        put(p/'system/fvSchemes',header('fvSchemes')+'''ddtSchemes { default Euler; }
gradSchemes { default Gauss linear; }
divSchemes { default none; div(phi,U) Gauss linear; }
laplacianSchemes { default Gauss linear corrected; }
interpolationSchemes { default linear; }
snGradSchemes { default corrected; }
fluxRequired { default no; p; }
''')
        if heat:
            put(p/'constant/transportProperties',header('transportProperties')+'DT [0 2 -1 0 0 0 0] 1e-4;')
            put(p/'system/fvSolution',header('fvSolution')+'''solvers
{
    T { solver PCG; preconditioner DIC; tolerance 1e-10; relTol 0; }
}
SIMPLE { nNonOrthogonalCorrectors 0; }
''')
            put(p/'0/T',header('T','volScalarField')+'dimensions [0 0 0 1 0 0 0];\n\ninternalField '+stream(TEMP_CODES[key])+'''

boundaryField
{
    inlet { type zeroGradient; }
    outlet { type zeroGradient; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}
''')
        else:
            put(p/'constant/transportProperties',header('transportProperties')+'nu [0 2 -1 0 0 0 0] 1e-3;')
            put(p/'system/fvSolution',header('fvSolution')+'''solvers
{
    p { solver PCG; preconditioner DIC; tolerance 1e-10; relTol 0; }
    pFinal { $p; relTol 0; }
    U { solver smoothSolver; smoother symGaussSeidel; tolerance 1e-9; relTol 0; }
}
PISO { nCorrectors 2; nNonOrthogonalCorrectors 0; }
''')
            initial=stream(PROFILE_INIT) if key in ('05-fixed-profile','06-coded-steady') else 'uniform (0 0 0);'
            put(p/'0/U',header('U','volVectorField')+'dimensions [0 1 -1 0 0 0 0];\n\ninternalField '+initial+'\n\nboundaryField\n{\n    inlet\n    {\n'+textwrap.indent(BCS[key],'        ')+'''
    }
    outlet { type zeroGradient; }
    walls { type noSlip; }
    frontAndBack { type empty; }
}
''')
            put(p/'0/p',header('p','volScalarField')+'''dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type zeroGradient; }
    outlet { type fixedValue; value uniform 0; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}
''')
        field='T' if heat else 'U'; app='laplacianFoam' if heat else 'icoFoam'
        put(p/'Allrun',f'''#!/bin/bash
set -eo pipefail
cd "$(dirname "$0")"
: "${{WM_PROJECT_DIR:?请先加载 OpenFOAM v2512 环境}}"
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
foamToVTK -ascii -legacy -time 0 -fields '({field})' > log.initialVTK 2>&1
{app} > log.{app} 2>&1
foamToVTK -ascii -legacy -latestTime -fields '({field})' > log.finalVTK 2>&1
touch case.foam
echo "完成：{key}"
''')
        put(p/'README.md',f'''# {CASE_TITLES[i]}

OpenFOAM v2512。加载环境后在本目录运行 `bash Allrun`。

程序依次生成网格、检查网格、导出初始场、运行 {app}、导出最终场。
`0/{field}` 是本例的主要代码文件，`system/controlDict` 控制计算时间与保存频率。
ParaView 可以打开 `case.foam`，也可以打开 `VTK` 目录中的初始和最终结果。
改变初值重新计算时，在另一个目录解压原始算例，保留两组输出便于比较。

本例目录：`{key}`。完整教程见 https://foamlabshark.github.io/programming/coded-fields/ 。
源码：FoamLab，GPL-3.0-or-later。
''')
    put(CASES/'Allrun','''#!/bin/bash
set -eo pipefail
cd "$(dirname "$0")"
for caseDir in 0[1-9]-*; do (cd "$caseDir" && bash Allrun); done
''')
    put(CASES/'README.md','''# 用代码设置初始与边界条件

OpenFOAM v2512 · FoamLab

01–04：codeStream 温度初值。05：codeStream 初始速度与固定入口。
06：codedFixedValue 固定入口。07–08：随时间变化的入口。09：脉动抛物线入口。

将本文件夹解压到 Linux 的个人工作目录，加载 OpenFOAM v2512 环境。
进入任一算例，运行 `bash Allrun`；在本层运行 `bash Allrun` 可以依次计算全部九例。
首次运行会自动编译字典内的 C++ 代码，需要 g++、make 与 OpenFOAM 开发文件。

本包提供生成网格所需的字典，不包含已生成网格、平台库或完整时间目录。
reference-results 目录（如有）是配套 v2512 计算导出的 CSV 与检查结果。

教程：https://foamlabshark.github.io/programming/coded-fields/
教学思路参考：Joel Guerrero / Wolf Dynamics，OpenFOAM Introductory Training，编程部分。
本包的几何、代码、脚本与中文说明由 FoamLab 编写。代码许可证 GPL-3.0-or-later。
''')
    # Keep the standard licence from the existing licensed programming material.
    license_path=Path('F:/UbuntuShareFolder/BasicOFProgramming/LICENSE')
    if license_path.exists(): (CASES/'LICENSE').write_bytes(license_path.read_bytes())
    print(f'Prepared {len(TEMP_CODES)+len(BCS)} cases at {CASES}')

def package():
    OUT.mkdir(parents=True,exist_ok=True)
    groups={'all':list(TEMP_CODES)+list(BCS),'01':list(TEMP_CODES)[:3],'02':['04-ellipse'],'03':['05-fixed-profile'],'04':['06-coded-steady'],'05':['07-ramp','08-sine'],'06':['09-pulsed-profile']}
    manifest={}
    for key,names in groups.items():
        dest=OUT/f'coded-fields-{key}-v2512.zip'
        with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
            for f in sorted(CASES.rglob('*')):
                if not f.is_file(): continue
                rel=f.relative_to(CASES)
                if len(rel.parts)>1 and rel.parts[0] not in [*names,'reference-results']: continue
                if rel.name=='Allrun' and len(rel.parts)==1 and key!='all': continue
                if rel.parts[0]=='reference-results' and f.suffix=='.csv' and not any(f.name.startswith(n) or (n=='09-pulsed-profile' and f.name.startswith('09-profile-')) for n in names): continue
                info=zipfile.ZipInfo('foamLabCodedFields/'+rel.as_posix())
                info.external_attr=(0o100755 if f.name=='Allrun' else 0o100644)<<16
                info.compress_type=zipfile.ZIP_DEFLATED
                data=f.read_bytes()
                if rel.as_posix()=='README.md':
                    text=f.read_text(encoding='utf-8')
                    start=text.index('01–04：');end=text.index('将本文件夹',start)
                    text=text[:start]+'本包包含：\n\n'+'\n'.join('- '+n for n in names)+'\n\n'+text[end:]
                    if key!='all':text=text.replace('；在本层运行 `bash Allrun` 可以依次计算全部九例','')
                    data=text.encode('utf-8')
                z.writestr(info,data)
        manifest[key]={'url':'/downloads/programming/'+dest.name,'size_bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
    put(OUT/'coded-fields-manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    return manifest

if __name__=='__main__':
    main()
    print(json.dumps(package(),ensure_ascii=False,indent=2))
