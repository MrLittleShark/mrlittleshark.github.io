---
title: "dynamicMeshDict"
layout: reference
description: "选择动态网格类型、运动求解器及其系数，控制网格随时间的移动或拓扑变化。"
dictionary: true
cms_slug: "dictionary-dynamicmeshdict"
---

<p>选择动态网格类型、运动求解器及其系数，控制网格随时间的移动或拓扑变化。</p><p>位置：<code>constant/dynamicMeshDict</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-mesh-modes.png" alt="预设运动、液面晃荡与网格变形" loading="lazy"><figcaption><strong>预设运动、液面晃荡与网格变形</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 146</small></figcaption></figure><h2>dynamicMeshDict 规定网格怎样运动</h2>
<p><code>constant/dynamicMeshDict</code> 选择动态网格类型、运动求解器及运动参数。它适用于移动边界、旋转网格和相应动态细化等计算，具体字段由选择的模型读取。</p>
<h3>一个区域做刚体旋转</h3>
<p>下面是 v2512 <code>pimpleFoam/laminar/mixerVesselAMI2D</code> 的旋转配置主体，放在 <code>FoamFile</code> 文件头之后：</p>
<pre><code class="language-foam">dynamicFvMesh dynamicMotionSolverFvMesh;
motionSolver solidBody;
cellZone rotor;
solidBodyMotionFunction rotatingMotion;
origin (0 0 0);
axis (0 0 1);
omega 6.2832;
</code></pre>
<table>
<thead>
<tr>
<th>条目</th>
<th>作用</th>
</tr>
</thead>
<tbody><tr>
<td><code>dynamicFvMesh</code></td>
<td>选择通过运动求解器更新网格的类型</td>
</tr>
<tr>
<td><code>motionSolver solidBody</code></td>
<td>所选区域按刚体运动</td>
</tr>
<tr>
<td><code>cellZone rotor</code></td>
<td>运动的单元区域</td>
</tr>
<tr>
<td><code>rotatingMotion</code></td>
<td>选择转动形式</td>
</tr>
<tr>
<td><code>origin</code>、<code>axis</code></td>
<td>转轴位置和方向</td>
</tr>
<tr>
<td><code>omega</code></td>
<td>角速度，单位 rad/s</td>
</tr>
</tbody></table>
<p>本例角速度约为 \(2\pi\,\mathrm{rad/s}\)，即每秒转一圈。一个时间步内转角为 \(\Delta\theta=\omega\Delta t\)。取 \(\Delta t=0.001\,\mathrm s\)，每步约转 \(0.36^\circ\)。转速加倍时，同一步长内的相对运动也加倍。</p>
<h3>运动区与静止区怎样连接</h3>
<p>刚体旋转时，内部网格形状随区域一起旋转，区域边界与静止外区存在相对滑动。AMI 接口允许两侧网格面不一一对应，通过几何重叠构造插值。</p>
<p>完整算例还需配置相应 <code>cyclicAMI</code> 网格 patch、字段边界和速度条件。转动导致的壁面速度应与网格运动一致。接口覆盖范围及运动后的网格质量会影响通量传递，特别是狭缝和局部高速区域。</p>
<h3>刚体运动与网格变形</h3>
<p>刚体模型适合形状保持的平移或旋转。若物体在外边界固定的域中往复运动，可使用位移类运动求解器，将边界位移传播到内部节点；常见输入还包括 <code>pointDisplacement</code>。这时单元形状随时间改变，需要检查运动全过程中的体积、非正交和偏斜。</p>
<h3>实际运动与 MRF</h3>
<p>本字典更新网格坐标，流场与几何相对位置随时间变化。MRF 则在静止网格中使用旋转参考系项，两者对叶片通过和转静干涉的描述方式不同。研究瞬态力矩或叶片经过固定位置的影响时，实际运动通常更直接。</p>
<p>在 ParaView 中载入多个输出时刻，显示网格边线并播放动画，可以检查旋转方向、转轴和运动区域。若物体绕错误位置旋转，先检查 <code>origin</code>；方向相反则检查轴向和角速度符号。</p>
<p>运行前还可用完整教程的网格运动检查流程预览运动。实际运行选择具有动态网格更新流程的求解器，例如 <code>pimpleFoam</code>。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D</summary><p>mixerVesselAMI2D 让搅拌器周围的 rotor 网格区刚体旋转，并通过 AMI 连接静止区。</p>
<ul>
<li><code>dynamicMotionSolverFvMesh</code> 使用运动求解器更新网格点，<code>motionSolver solidBody</code> 指定刚体运动。</li>
<li><code>cellZone rotor</code> 把运动限制在命名区域，需与网格中的 cellZone 一致。</li>
<li><code>rotatingMotion</code>、<code>origin (0 0 0)</code>、<code>axis (0 0 1)</code> 定义绕 z 轴旋转。</li>
<li><code>omega 6.2832</code> 使用弧度每秒，约为每秒一周。</li>
</ul>
<p>改变转轴时同时检查几何与 AMI 接口；改变转速后检查运动 Courant 数和时间步。</p>
<p><a href="/assets/examples/v2512/dynamicmeshdict/authored-mixerVesselAMI2D-dynamicMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D/constant/dynamicMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

dynamicFvMesh   dynamicMotionSolverFvMesh;

motionSolver    solidBody;

cellZone        rotor;

solidBodyMotionFunction  rotatingMotion;

origin        (0 0 0);
axis          (0 0 1);
omega         6.2832; // rad/s


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interIsoFoam/damBreak</summary><p>这个 interIsoFoam 溃坝配置明确使用静止网格，界面运动由相分数输运描述。</p>
<ul>
<li><code>dynamicFvMesh staticFvMesh</code> 创建静态有限体积网格。</li>
<li>文件没有运动求解器或移动区域，水面变化不会自动移动网格点。</li>
<li>计算初期的网格由其他网格字典生成。</li>
</ul>
<p>若增加运动壁面或自适应网格，需要换用相应网格类型并补齐运动或细化配置。</p>
<p><a href="/assets/examples/v2512/dynamicmeshdict/1-dynamicMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak/constant/dynamicMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint</summary><p>NACA0012 形状优化通过拉普拉斯型网格运动把边界形变传入内部网格。</p>
<ul>
<li><code>solver laplacianMotionSolver</code> 指定本例的网格运动算法。</li>
<li><code>diffusivity uniform</code> 使用均匀扩散权重传递位移。</li>
<li><code>iters 1000</code>、<code>tolerance 1.e-06</code> 控制该运动求解过程的迭代上限与容差。</li>
</ul>
<p>形状变化较大时检查近壁单元质量；必要时调整位移传播方式或分多次更新几何。</p>
<p><a href="/assets/examples/v2512/dynamicmeshdict/2-dynamicMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint/constant/dynamicMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/naca0012/laminar/drag/primalAdjoint">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 4 · compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground</summary><p>hotCylinder 的 cylinderAndBackground 采用重叠网格，把圆柱附近网格与背景网格连接。</p>
<ul>
<li><code>dynamicFvMesh dynamicOversetFvMesh</code> 启用重叠网格处理。</li>
<li><code>motionSolverLibs (fvMotionSolvers)</code> 加载运动求解器库，<code>solver displacementLaplacian</code> 根据位移求解网格运动。</li>
<li><code>diffusivity uniform 1</code> 使用均匀运动扩散系数。</li>
</ul>
<p>改变物体移动方式时修改位移边界或运动输入，并检查重叠区覆盖、插值单元和网格质量。</p>
<p><a href="/assets/examples/v2512/dynamicmeshdict/3-dynamicMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground/constant/dynamicMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/overRhoSimpleFoam/hotCylinder/cylinderAndBackground">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/interfoam/">interFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
