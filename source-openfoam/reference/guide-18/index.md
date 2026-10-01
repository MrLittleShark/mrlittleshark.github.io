---
title: "第 18 章　constant/ 目录下的文件"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>18.1 transportProperties（物性）</h4>
<p>单相不可压</p>
<pre><code>transportModel  Newtonian;
nu              [0 2 -1 0 0 0 0] 1e-05;      // 运动粘度 m²/s
// 新版也可以简写（量纲由程序推断）：nu 1e-05;</code></pre>
<p>非牛顿流体可选 CrossPowerLaw、BirdCarreau、HerschelBulkley、powerLaw，各自再跟一个系数子字典。</p>
<p>两相（interFoam）</p>
<pre><code>phases (water air);

water { transportModel Newtonian; nu 1e-06; rho 1000; }
air   { transportModel Newtonian; nu 1.48e-05; rho 1; }

sigma  0.07;          // 表面张力系数 N/m</code></pre>
<p>laplacianFoam</p>
<pre><code>DT              [0 2 -1 0 0 0 0] 4e-05;      // 扩散系数</code></pre>
<h4>18.2 turbulenceProperties（湍流模型）</h4>
<pre><code>simulationType  RAS;          // laminar / RAS / LES

RAS
{
    RASModel        kOmegaSST;
    turbulence      on;
    printCoeffs     on;        // 启动时把模型系数打印到日志，便于确认
}
simulationType  LES;

LES
{
    LESModel        WALE;              // 或 Smagorinsky / kEqn / dynamicKEqn
    delta           cubeRootVol;       // 滤波尺度：cubeRootVol / vanDriest / smooth
    turbulence      on;
    printCoeffs     on;

    cubeRootVolCoeffs { deltaCoeff 1; }
}</code></pre>
<p>常用 RANS 模型怎么挑</p>
<div class="table-scroll"><table>
<tr><th>模型</th><th>特点</th><th>场合</th></tr>
<tr><td>kEpsilon</td><td>最经典，壁面靠壁函数</td><td>内流、自由剪切流</td></tr>
<tr><td>realizableKE</td><td>对旋转/分离更好</td><td>旋流</td></tr>
<tr><td>kOmegaSST</td><td>近壁用 \(k-\omega\)、远场用 \(k-\varepsilon\)，逆压梯度和分离预测好</td><td>外流绕流、翼型，最常用</td></tr>
<tr><td>SpalartAllmaras</td><td>单方程，便宜</td><td>航空外流</td></tr>
<tr><td>LaunderSharmaKE</td><td>低雷诺数版本，需要 \(y^{+}\approx 1\)</td><td>不用壁函数时</td></tr>
</table></div>
<p>v2512 的 kEpsilon 新增 twoLayerTreatment 开关，可以在近壁内层用代数关系式，降低对第一层网格的要求：</p>
<pre><code>RAS
{
    RASModel        kEpsilon;
    turbulence      on;
    kEpsilonCoeffs  { twoLayerTreatment true; }
}</code></pre>
<p>层流就写 simulationType laminar;，此时 0/ 里不需要 k、epsilon、nut 等文件。</p>
<h4>18.3 thermophysicalProperties（可压/传热必需）</h4>
<pre><code>thermoType
{
    type            hePsiThermo;          // hePsiThermo(可压理想气体) / heRhoThermo(液体)
    mixture         pureMixture;          // 单组分
    transport       sutherland;           // const / sutherland / polynomial
    thermo          janaf;                // hConst / eConst / janaf
    equationOfState perfectGas;           // perfectGas / rhoConst / Boussinesq / PengRobinson
    specie          specie;
    energy          sensibleInternalEnergy;   // sensibleEnthalpy / sensibleInternalEnergy
}

mixture
{
    specie          { molWeight  28.96; }
    thermodynamics  { Cp 1004.5; Hf 0; }
    transport       { mu 1.8e-05; Pr 0.7; }
}</code></pre>
<p>七个字段各自的意思：type 决定用 \(\psi (=1/RT)\) 还是 \(\rho\) 作为基本量；mixture 是单组分还是多组分；transport 是粘性/导热系数的模型；thermo 是比热模型（hConst 常数比热，janaf 用 JANAF 多项式）；equationOfState 是状态方程；energy 是用焓还是内能作为求解变量。修改时七个字段必须相互兼容，不兼容时报错信息会把所有合法组合列出来——照着报错里的列表挑就行，这是 OpenFOAM 少数几个报错比文档还好用的地方。</p>
<p>sensibleEnthalpy 还是 sensibleInternalEnergy：基于压力的求解器（rhoPimpleFoam）一般用焓；基于密度的（rhoCentralFoam）用内能。照抄对应教程即可。</p>
<h4>18.4 g（重力）</h4>
<pre><code>FoamFile { ... class uniformDimensionedVectorField; object g; }

dimensions      [0 1 -2 0 0 0 0];
value           (0 -9.81 0);</code></pre>
<p>浮力、多相流求解器必需。方向要和你的网格坐标系一致——把 z 当竖直方向的算例写成 (0 -9.81 0) 是常见低级错误。</p>
<h4>18.5 dynamicMeshDict（动网格）</h4>
<p>刚体运动（最简单）</p>
<pre><code>dynamicFvMesh   dynamicMotionSolverFvMesh;
motionSolver    solidBody;
solidBodyMotionFunction  rotatingMotion;
rotatingMotionCoeffs
{
    origin  (0 0 0);
    axis    (0 0 1);
    omega   6.28;                 // rad/s
}
cellZone        rotor;            // 只让这个 zone 动</code></pre>
<p>其他运动函数：oscillatingLinearMotion、linearMotion、SDA、tabulated6DoFMotion、multiMotion。</p>
<p>六自由度耦合（自由运动物体）</p>
<pre><code>motionSolver    sixDoFRigidBodyMotion;
sixDoFRigidBodyMotionCoeffs
{
    patches         (floatingObject);
    innerDistance   0.05;
    outerDistance   0.35;
    mass            9.6;
    centreOfMass    (0.5 0.45 0.4);
    momentOfInertia (0.08 0.08 0.06);
    accelerationRelaxation 0.7;
    solver          { type Newmark; }
    constraints     { zAxis { sixDoFRigidBodyMotionConstraint line; direction (0 0 1);} }
}</code></pre>
<p>动态加密（AMR）</p>
<pre><code>dynamicFvMesh   dynamicRefineFvMesh;
refineInterval  10;
field           alpha.water;      // 按哪个场判断
lowerRefineLevel 0.001;
upperRefineLevel 0.999;
maxRefinement   2;
maxCells        2000000;
nBufferLayers   1;</code></pre>
<p>用途：VOF 里只在界面附近加密，单元数可以省一个量级。</p>
<h4>18.6 radiationProperties</h4>
<pre><code>radiation       on;
radiationModel  P1;              // none / P1 / fvDOM / viewFactor / opaqueSolid
solverFreq      10;
absorptionEmissionModel constantAbsorptionEmission;
constantAbsorptionEmissionCoeffs { absorptivity 0.5; emissivity 0.5; E 0; }
scatterModel    none;</code></pre>
<h4>18.7 polyMesh/ 与 triSurface/</h4>
<p>constant/polyMesh/ 里是网格数据，只有 boundary 这个文件需要偶尔手动改：</p>
<pre><code>6
(
    movingWall
    {
        type            wall;         // ← 转换来的网格常常要在这里把 patch 改成 wall
        inGroups        1(wall);
        nFaces          20;
        startFace       760;
    }
    ...
)</code></pre>
<p>nFaces 和 startFace 是程序生成的，绝对不要手改；type 和 inGroups 可以改。</p>
<p>constant/triSurface/ 放 snappyHexMesh 用的 STL/OBJ 几何文件。</p>
{% endraw %}