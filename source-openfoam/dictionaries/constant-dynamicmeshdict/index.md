---
title: "constant/dynamicMeshDict · dynamicMeshDict"
layout: reference
description: "下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/dynamicMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dynamicFvMesh</code> · <code>dynamicRefineFvMesh</code> · <code>dynamicMotionSolverFvMesh</code> · <code>motionSolver</code> · <code>field</code> · <code>lowerRefineLevel</code> · <code>upperRefineLevel</code> · <code>refineInterval</code> · <code>maxRefinement</code> · <code>maxCells</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/dynamicMeshDict -keywords
interFoam -help</code></pre><h2>9.11 constant/dynamicMeshDict</h2><p>下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。</p>
<pre><code class="language-openfoam">dynamicFvMesh dynamicMotionSolverFvMesh;
motionSolverLibs (&quot;libfvMotionSolvers.so&quot;);
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
<h2>18.5 dynamicMeshDict（动网格）</h2><p>刚体运动（最简单）</p>
<pre><code class="language-openfoam">dynamicFvMesh   dynamicMotionSolverFvMesh;
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
<pre><code class="language-openfoam">motionSolver    sixDoFRigidBodyMotion;
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
<pre><code class="language-openfoam">dynamicFvMesh   dynamicRefineFvMesh;
refineInterval  10;
field           alpha.water;      // 按哪个场判断
lowerRefineLevel 0.001;
upperRefineLevel 0.999;
maxRefinement   2;
maxCells        2000000;
nBufferLayers   1;</code></pre>
<p>用途：VOF 里只在界面附近加密，单元数可以省一个量级。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>dynamicFvMesh</td><td>运行时网格类型；它决定运动、拓扑变化或重叠插值等处理的入口。</td></tr><tr><td>motionSolverLibs</td><td>加载运动求解器所在的动态库。使用当前教程提供的库名并核对安装。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>solver</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interIsoFoam/damBreak</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/damBreak/constant/dynamicMeshDict</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak/constant/dynamicMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/dynamicmeshdict/1-dynamicMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    &quot;constant&quot;;
    object      dynamicMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dynamicFvMesh   staticFvMesh;


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint/constant/dynamicMeshDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint/constant/dynamicMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/dynamicmeshdict/2-dynamicMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      dynamicMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solver laplacianMotionSolver;

laplacianMotionSolverCoeffs
{
    diffusivity uniform;
    iters       1000;
    tolerance   1.e-06;
}


// ************************************************************************* //</code></pre><h3>示例 3 · compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground</h3><p>原始路径：<code>tutorials/compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground/constant/dynamicMeshDict</code>；求解器：<code>overRhoSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground/constant/dynamicMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/dynamicmeshdict/3-dynamicMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      dynamicMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dynamicFvMesh   dynamicOversetFvMesh;

motionSolverLibs (fvMotionSolvers);

solver          displacementLaplacian;

displacementLaplacianCoeffs
{
    diffusivity     uniform 1;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/interfoam/">interFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/dynamicMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/dynamicMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
