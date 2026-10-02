---
title: "09 场文件与物理模型配置"
layout: reference
description: "场文件与物理模型配置：用法与配置实例。"
cms_slug: "reference-manual-09"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>9.1 速度场与压力场</h3>
<p>下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class volVectorField; object U;
}
dimensions [0 1 -1 0 0 0 0];
internalField uniform (1 0 0);
boundaryField
{
    inlet { type fixedValue; value uniform (1 0 0); }
    outlet { type zeroGradient; }
    walls { type noSlip; }
    frontAndBack { type empty; }
}
FoamFile
{
    version 2.0; format ascii;
    class volScalarField; object p;
}
dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type zeroGradient; }
    outlet { type fixedValue; value uniform 0; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}</code></pre>
<p>本例 p 为运动学压力，适用于相应的不可压缩求解器。采用绝对压力的可压缩求解器时，dimensions 设为 [1 -1 -2 0 0 0 0]，压力值按状态方程设置，如 101325 Pa。</p>
<h3>9.2 常用边界条件</h3>
<div class="table-scroll"><table>
<tr><th>类型</th><th>含义</th><th>配置要点</th></tr>
<tr><td>fixedValue</td><td>固定值</td><td>value uniform 300; 或向量值</td></tr>
<tr><td>zeroGradient</td><td>法向梯度为零</td><td>无需 value；按出口物理条件选用</td></tr>
<tr><td>fixedGradient</td><td>固定法向梯度</td><td>gradient uniform 0;</td></tr>
<tr><td>noSlip</td><td>速度为零的壁面</td><td>用于 U，网格对应 wall</td></tr>
<tr><td>slip</td><td>无穿透、切向滑移</td><td>适用于相应速度边界</td></tr>
<tr><td>movingWallVelocity</td><td>随移动壁面的速度</td><td>通常通过 value uniform (0 0 0) 初始化</td></tr>
<tr><td>inletOutlet</td><td>流出零梯度，回流指定值</td><td>inletValue uniform 0; value uniform 0;</td></tr>
<tr><td>outletInlet</td><td>与 inletOutlet 的切换方向相反</td><td>出口指定值按该类型的字段要求设置</td></tr>
<tr><td>pressureInletOutletVelocity</td><td>根据压力入口出口条件确定速度</td><td>配套压力边界，value 为初始值</td></tr>
<tr><td>flowRateInletVelocity</td><td>以体积或质量流量规定入口速度</td><td>volumetricFlowRate constant 0.01; 或 massFlowRate 并提供密度信息</td></tr>
<tr><td>totalPressure</td><td>总压条件</td><td>p0 uniform 101325;，U、phi、rho、psi 和 gamma 按流动类型设置</td></tr>
<tr><td>totalTemperature</td><td>总温条件</td><td>T0、gamma、U、phi、psi 等按模型配置</td></tr>
<tr><td>fixedFluxPressure</td><td>按通量约束调节压力梯度</td><td>常用于带重力或特定速度条件的压力场</td></tr>
<tr><td>waveTransmissive</td><td>波传出型边界</td><td>配置声速、psi 和 gamma 等参数，反射特性受波入射条件影响</td></tr>
<tr><td>advective</td><td>对流传出型边界</td><td>速度、参考值和远场长度参数依类型要求</td></tr>
<tr><td>empty</td><td>二维模型未求解方向</td><td>体网格仅一个单元层，场和网格均须 empty</td></tr>
<tr><td>symmetryPlane</td><td>平面对称</td><td>几何 patch 必须平面且网格类型匹配</td></tr>
<tr><td>symmetry</td><td>一般对称约束</td><td>按相应几何使用</td></tr>
<tr><td>wedge</td><td>小角度轴对称扇形</td><td>两个楔面须符合轴对称几何约束</td></tr>
<tr><td>cyclic</td><td>周期耦合</td><td>网格定义 neighbourPatch、变换等；场写 cyclic</td></tr>
<tr><td>cyclicAMI</td><td>非匹配网格周期或滑动接口</td><td>接口需具备几何重叠，计算后检查通量误差</td></tr>
<tr><td>overset</td><td>重叠网格插值边界</td><td>还需要 zoneID、孔切割与重叠插值配置</td></tr>
<tr><td>calculated</td><td>值由其他模型计算</td><td>value 用于初始化，边界值由关联模型更新</td></tr>
<tr><td>codedFixedValue</td><td>运行时编译的固定值边界</td><td>见 9.13</td></tr>
<tr><td>compressible::turbulentTemperatureCoupledBaffleMixed</td><td>多区域共轭传热温度耦合</td><td>配套 mappedWall、相邻区域、导热率获取方式</td></tr>
</table></div>
<h3>9.3 温度场与多相流场</h3>
<p>温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。</p>
<p>p_rgh 表示扣除静水压项后的压力，常见定义为 \(p_{\mathrm{rgh}}=p-\rho gh\)。参考高度和量纲由求解器确定，不可压缩 Boussinesq 模型可采用归一化形式。恢复实际压力时，应按该求解器的定义还原静水压项。</p>
<p>alpha.water 表示水相体积分数，为无量纲量，取值范围为 [0,1]；多相体系中各相体积分数之和为 1。入口可指定相分数，开放边界可采用 inletOutlet，壁面可采用 zeroGradient 或接触角条件。字段后缀 water 与 phases 中的相名对应。</p>
<h3>9.4 湍流场与热扩散场</h3>
<div class="table-scroll"><table>
<tr><th>字段</th><th>量纲</th><th>常见边界与设置</th></tr>
<tr><td>k</td><td>[0 2 -2 0 0 0 0]</td><td>入口固定湍动能；壁面可配 kqRWallFunction</td></tr>
<tr><td>epsilon</td><td>[0 2 -3 0 0 0 0]</td><td>k epsilon 模型使用；壁面 epsilonWallFunction</td></tr>
<tr><td>omega</td><td>[0 0 -1 0 0 0 0]</td><td>k omega 模型使用；壁面 omegaWallFunction</td></tr>
<tr><td>nut</td><td>[0 2 -1 0 0 0 0]</td><td>湍动黏度，由模型给定；壁面可用 nutkWallFunction 等</td></tr>
<tr><td>alphat</td><td>由热模型定义，常见可压缩形式为 [1 -1 -1 0 0 0 0]</td><td>量纲按所用热模型确定</td></tr>
</table></div>
<p>入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：\(k=1.5(IU)^2\)，\(\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{L}\)，\(\omega=\frac{\sqrt{k}}{C_\mu^{0.25}L}\)。常用 \(C_\mu = 0.09\)，湍流强度 5% 对应 \(I = 0.05\)。</p>
<p>近壁处理方式应与网格设计一致。采用壁面函数或直接解析近壁区域时，分别据其要求确定第一层网格厚度及目标 y+。</p>
<h3>9.5 constant/transportProperties</h3>
<p>不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object transportProperties;
}
transportModel Newtonian;
nu [0 2 -1 0 0 0 0] 1e-6;</code></pre>
<p>nu 为运动黏度，mu 为动力黏度，两者满足 \(\mu = \rho*\nu\)。powerLaw、BirdCarreau 等非牛顿模型采用各自的系数字典，参数定义见对应模型源码和教程。</p>
<p>不可压缩 VOF 的两相物性配置如下。</p>
<pre><code class="language-plaintext">phases (water air);
water { transportModel Newtonian; nu 1e-6; rho 1000; }
air   { transportModel Newtonian; nu 1.5e-5; rho 1.2; }
sigma 0.072;</code></pre>
<p>rho 表示相密度，sigma 表示表面张力系数。示例数值为常温条件下的近似示例。可压缩多相模型通常分别设置各相热物性。</p>
<h3>9.6 constant/turbulenceProperties</h3>
<p>v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object turbulenceProperties;
}
simulationType RAS;
RAS
{
    RASModel kOmegaSST;
    turbulence on;
    printCoeffs on;
}</code></pre>
<p>层流采用 simulationType laminar;。LES 可采用 simulationType LES; LES { LESModel WALE; turbulence on; printCoeffs on; delta cubeRootVol; }。</p>
<p>LES 配置还需确定滤波宽度、近壁处理、入口脉动和时间分辨率，并与网格及边界条件配合。</p>
<h3>9.7 constant/thermophysicalProperties</h3>
<p>下例采用单相理想气体、常热容和常输运系数，能量变量为显焓。热物性类型和能量形式应与求解器接口对应。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object thermophysicalProperties;
}
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
mixture
{
    specie { molWeight 28.96; }
    thermodynamics { Cp 1005; Hf 0; }
    transport { mu 1.8e-5; Pr 0.7; }
}</code></pre>
<div class="table-scroll"><table>
<tr><th>参数</th><th>作用</th><th>设置方法</th></tr>
<tr><td>type</td><td>热物性基类</td><td>hePsiThermo、heRhoThermo 等；须与求解器匹配</td></tr>
<tr><td>mixture</td><td>混合物模型</td><td>pureMixture 单组分；反应流使用相应多组分模型</td></tr>
<tr><td>transport</td><td>输运模型</td><td>const、sutherland 等</td></tr>
<tr><td>thermo</td><td>热容模型</td><td>hConst 常热容；janaf 温度相关多项式</td></tr>
<tr><td>equationOfState</td><td>状态方程</td><td>perfectGas、rhoConst 等，按介质状态关系选择</td></tr>
<tr><td>energy</td><td>能量变量</td><td>sensibleEnthalpy 或 sensibleInternalEnergy 等</td></tr>
<tr><td>molWeight</td><td>摩尔质量</td><td>单位为 kg/kmol，空气示例为 28.96</td></tr>
<tr><td>Cp、Hf</td><td>定压比热、生成焓</td><td>按模型定义及参考态赋值</td></tr>
<tr><td>mu、Pr</td><td>动力黏度和 Prandtl 数</td><td>采用一致的单位与适用温度范围</td></tr>
<tr><td>As、Ts</td><td>Sutherland 输运系数</td><td>选择 sutherland 后按该模型填写</td></tr>
<tr><td>Tlow、Thigh、Tcommon、lowCpCoeffs、highCpCoeffs</td><td>JANAF 温度区间及系数</td><td>从可靠物性数据或机理文件提取</td></tr>
</table></div>
<p>rhoCentralFoam 等采用相应的热物性基类和能量变量。使用显内能的求解器应配置 sensibleInternalEnergy，并保留配套教程中的热物性组合。</p>
<h3>9.8 重力与压力参考值</h3>
<pre><code class="language-openfoam">// constant/g 完整示例
FoamFile
{
    version 2.0; format ascii;
    class uniformDimensionedVectorField; object g;
}
dimensions [0 1 -2 0 0 0 0];
value (0 -9.81 0);</code></pre>
<p>g 定义重力矢量，其方向与几何坐标系对应。hRef 定义静水压参考高度，通常采用 uniformDimensionedScalarField 和长度量纲；pRef 按求解器接口设置。fvSolution 中的 pRefCell/pRefValue 用于压力方程参考值，作用不同。</p>
<h3>9.9 constant/fvOptions</h3>
<p>fvOptions 用于配置源项和约束，文件位置由求解器的读取路径确定，常见于 constant 或 system。下例在指定 cellZone 内施加速度方程源项，采用 sources 条目。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvOptions;
}
drive
{
    type vectorSemiImplicitSource;
    active true;
    selectionMode cellZone;
    cellZone heater;
    volumeMode specific;
    sources
    {
        U ((0.1 0 0) 0);
    }
}</code></pre>
<p>半隐式源项写为 Su + Sp*字段，括号内依次给出显式项和隐式系数。specific 按单位体积定义，absolute 按所选体积的总量定义。源项量纲取决于控制方程；速度、动量以及以 h、e 或 T 为变量的能量方程应分别确定量纲和密度因子。</p>
<p>selectionMode 指定作用范围，可选 all、cellZone、cellSet 等；timeStart 和 duration 指定作用时间。常用类型包括 scalarSemiImplicitSource、vectorSemiImplicitSource、meanVelocityForce、explicitPorositySource、scalarFixedValueConstraint、limitTemperature 和 codedSource，其参数按对应模型设置。</p>
<h3>9.10 constant/MRFProperties 与 SRFProperties</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object MRFProperties;
}
rotorZone
{
    active yes;
    cellZone rotor;
    nonRotatingPatches (stator);
    origin (0 0 0);
    axis (0 0 1);
    omega constant 100;
}</code></pre>
<p>rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。</p>
<p>SRFProperties 配置单参考系模型，常用 SRFModel rpm 和 rpmCoeffs/rpm，以 rpm 表示转速。使用两种模型时应分别采用对应的角速度单位。</p>
<h3>9.11 constant/dynamicMeshDict</h3>
<p>下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。</p>
<pre><code class="language-openfoam">dynamicFvMesh dynamicMotionSolverFvMesh;
motionSolverLibs ("libfvMotionSolvers.so");
solver displacementLaplacian;
displacementLaplacianCoeffs
{
    diffusivity uniform;
}</code></pre>
<p>pointDisplacement 为 pointVectorField，采用长度量纲。运动壁面指定相应位移，固定壁面指定零位移。motionSolver 或兼容键 solver 按 v2512 对应模型的接口设置。</p>
<div class="table-scroll"><table>
<tr><th>模型或功能</th><th>配置项</th><th>相关参数</th></tr>
<tr><td>规定刚体运动</td><td>solidBodyMotionFvMesh、solidBodyMotionFunction 及相应系数</td><td>旋转中心、轴、速度或时间函数</td></tr>
<tr><td>六自由度</td><td>sixDoFRigidBodyMotion 运动求解器</td><td>mass、momentOfInertia、centreOfMass、力矩参考与约束</td></tr>
<tr><td>自适应细化</td><td>dynamicRefineFvMesh</td><td>field、refineInterval、lowerRefineLevel、upperRefineLevel、unrefineLevel</td></tr>
<tr><td>细化限制</td><td>maxRefinement、maxCells、nBufferLayers</td><td>内存估计和细化一致性</td></tr>
<tr><td>拓扑改变通量修正</td><td>correctFluxes</td><td>通量和关联速度字段的配对，依求解器设置</td></tr>
<tr><td>重叠网格</td><td>dynamicOversetFvMesh 等、oversetInterpolation</td><td>zoneID、overset patch、孔切割和插值层</td></tr>
</table></div>
<p>先运行 moveDynamicMesh 检查网格运动，重点检查运动过程中质量最差的时刻，再进行流场求解。运动和拓扑变化类型应处于求解器的支持范围内。</p>
<h3>9.12 多区域传热及专用模型配置</h3>
<pre><code class="language-plaintext">// constant/regionProperties 片段
regions
(
    fluid (air)
    solid (solidBlock)
);</code></pre>
<p>air 和 solidBlock 分别配置 constant/区域名/polyMesh、热物性文件以及 system/区域名 下的 fvSchemes 和 fvSolution。初始场位于 0/区域名/。流固界面通常采用 mappedWall 网格边界，并设置相邻区域映射和温度耦合条件。</p>
<div class="table-scroll"><table>
<tr><th>文件</th><th>用途</th><th>主要参数</th></tr>
<tr><td>constant/radiationProperties</td><td>辐射模型</td><td>radiation on/off、radiationModel（P1、fvDOM、viewFactor 等）、solverFreq 及模型专用系数</td></tr>
<tr><td>constant/viewFactorsDict</td><td>视角因子设置</td><td>指定参与边界，按生成工具配置积分或射线参数</td></tr>
<tr><td>constant/chemistryProperties</td><td>化学积分</td><td>chemistry、chemistryType 中的 solver/method、initialChemicalTimeStep、ODE 系数</td></tr>
<tr><td>constant/combustionProperties</td><td>燃烧闭合模型</td><td>combustionModel 及 PaSR、EDC、laminar 等模型的专用系数</td></tr>
<tr><td>constant/reactions</td><td>反应机理</td><td>物种名称、反应式、速率系数；可由 chemkinToFoam 转换</td></tr>
<tr><td>constant/thermophysicalProperties.相名</td><td>多相分相热物性</td><td>各相 thermoType、状态方程、热容与输运</td></tr>
<tr><td>constant/phaseProperties</td><td>Euler 多相体系或特定多相模型</td><td>phases、直径模型、阻力、升力、传热等分相和相间模型</td></tr>
<tr><td>constant/kinematicCloudProperties 等</td><td>拉格朗日粒子云</td><td>solution、constantProperties、subModels、injectionModels、forces、patchInteractionModel</td></tr>
<tr><td>constant/sprayCloudProperties</td><td>喷雾云</td><td>在粒子设置基础上加入 atomization、breakup、phaseChange 等模型</td></tr>
<tr><td>constant/porosityProperties</td><td>部分求解器的多孔阻力入口</td><td>zone、Darcy–Forchheimer 系数及局部坐标；也可通过 fvOptions 配置</td></tr>
<tr><td>constant/solidProperties 或 mechanicalProperties</td><td>固体材料</td><td>按固体求解器设置 rho、E、nu 和 planeStress；此处 nu 表示泊松比</td></tr>
<tr><td>system/faSchemes、faSolution 的有限面积位置</td><td>面上离散与求解</td><td>v2512 常位于 system/finite-area/；使用 faMesh 对应的字段和算子</td></tr>
<tr><td>system/finite-area/faMeshDefinition</td><td>有限面积网格生成</td><td>polyMeshPatches、boundary、面选取和边界命名</td></tr>
<tr><td>system/optimisationDict</td><td>伴随优化</td><td>优化类型、设计变量、目标函数、约束和更新算法</td></tr>
</table></div>
<p>专用模型的配置项随物种机理、粒子模型、燃烧模型和优化算法变化。可通过 find "$FOAM_TUTORIALS" -name 文件名 查找对应求解器算例，并据模型源码确定条目层级及参数。</p>
<h3>9.13 运行时编译与字典扩展</h3>
<p>下例在温度场 T 的 inlet 边界中定义随时间变化的温度。codedFixedValue 在运行时编译代码，需配置编译器和动态库搜索路径。</p>
<pre><code class="language-cpp">inlet
{
    type codedFixedValue;
    value uniform 300;
    name rampedTemperature;
    code
    #{
        const scalar t = this-&gt;db().time().value();
        operator==(300.0 + 10.0*t);
    #};
}</code></pre>
<p>name 指定生成的类型名称，code 定义边界值计算过程；codeInclude、codeOptions、codeLibs 和 localCode 分别补充头文件、编译选项、链接库和局部代码。#codeStream 属于字典函数，通过 C++ 输出流生成字典内容。</p>
<h3>9.14 Make/files 与 Make/options</h3>
<pre><code class="language-makefile"># Make/files
myScalarFoam.C

EXE = $(FOAM_USER_APPBIN)/myScalarFoam
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude

EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 <code>LIB = $(FOAM_USER_LIBBIN)/libMyModel</code>，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。</p>
