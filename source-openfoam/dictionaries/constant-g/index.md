---
title: "g"
layout: reference
description: "定义重力加速度的方向和大小，文件采用 uniformDimensionedVectorField 格式。"
dictionary: true
cms_slug: "dictionary-g"
---

<p>定义重力加速度的方向和大小，文件采用 uniformDimensionedVectorField 格式。</p><p>位置：<code>constant/g</code></p><p><code>constant/g</code> 保存重力加速度，是整个区域使用的均匀向量。自由液面、自然对流和浮体计算会使用它；方向需要与几何坐标一致。</p>
<h3>示例：y 轴竖直向上</h3>
<pre><code class="language-foam">FoamFile
{
    format ascii;
    class uniformDimensionedVectorField;
    object g;
}
dimensions [0 1 -2 0 0 0 0];
value (0 -9.81 0);
</code></pre>
<p><code>uniformDimensionedVectorField</code> 表示带量纲的均匀向量，量纲对应 m/s²。<code>(0 -9.81 0)</code> 使重力沿负 y 方向。若几何以 z 轴为竖直方向，改为 <code>(0 0 -9.81)</code>。</p>
<p>重力参与静压分解、浮力和界面运动。以静止水柱为例，水深增加 \(h\)，压力约增加 \(\rho gh\)；水深 0.1 m、密度 1000 kg/m³ 时，静压增加约 981 Pa。这可用于检查方向和量级。</p>
<p>将重力设为零可用于研究惯性或毛细主导过程，但会同时改变水面平衡与静压关系。改变重力或坐标方向后，检查 <code>p_rgh</code> 的高度参考、初始相分数和开口边界是否仍与新的物理方向一致。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · basic/chtMultiRegionFoam/2DImplicitCyclic</summary><p>2DImplicitCyclic 的多区域示例将重力设为零，便于在没有浮力驱动的条件下考察其他耦合。</p>
<ul>
<li><code>dimensions [0 1 -2 0 0 0 0]</code> 表示加速度量纲。</li>
<li><code>value (0 0 0)</code> 使各方向重力加速度均为零。</li>
<li>此项作用于使用重力的方程，压力和热边界仍需按原问题设置。</li>
</ul>
<p>要加入浮力，应给出实际重力方向，并检查压力变量与密度、温度模型的配合。</p>
<p><a href="/assets/examples/v2512/g/1-g.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/basic/chtMultiRegionFoam/2DImplicitCyclic/constant/g">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/chtMultiRegionFoam/2DImplicitCyclic">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       uniformDimensionedVectorField;
    object      g;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -2 0 0 0 0];
value           (0 0 0);

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/laminar/sloshing2D</summary><p>sloshing2D 使用沿负 y 方向的重力加速度。</p>
<ul>
<li><code>dimensions [0 1 -2 0 0 0 0]</code> 明确数值单位为 m/s²。</li>
<li><code>value (0 -1 0)</code> 的大小为 1 m/s²，采用的是该示例给定尺度。</li>
<li>重力方向应与初始液面和容器几何对应。</li>
</ul>
<p>改为地面常用重力时可设为 (0 -9.81 0)，同时重新估计晃荡时间尺度和时间步。</p>
<p><a href="/assets/examples/v2512/g/2-g.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/sloshing2D/constant/g">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/sloshing2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       uniformDimensionedVectorField;
    object      g;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -2 0 0 0 0];

value           (0 -1 0);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/capillaryRise</summary><p>capillaryRise 通过重力与表面张力竞争形成毛细上升。</p>
<ul>
<li><code>value (0 -10 0)</code> 设定沿负 y 的 10 m/s² 重力。</li>
<li>加速度量纲为 <code>[0 1 -2 0 0 0 0]</code>。</li>
<li>平衡高度还依赖两相密度、表面张力、接触角和几何尺寸，重力只是其中一个输入。</li>
</ul>
<p>改变重力或管径后，可比较最终液面高度及其随网格变化的趋势。</p>
<p><a href="/assets/examples/v2512/g/3-g.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/capillaryRise/constant/g">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/capillaryRise">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       uniformDimensionedVectorField;
    object      g;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -2 0 0 0 0];
value           (0 -10 0);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/interfoam/">interFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
