---
title: "chemistryProperties"
layout: reference
description: "控制化学反应开关、化学 ODE 求解方法和化学时间步。"
dictionary: true
cms_slug: "dictionary-chemistryproperties"
---

<p>控制化学反应开关、化学 ODE 求解方法和化学时间步。</p><p>位置：<code>constant/chemistryProperties</code></p><h2>配置实例</h2><p>lagrangian/reactingParcelFoam/rectangularChannel 中的 chemistryProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      chemistryProperties;
}

chemistryType
{
    solver            noChemistrySolver;
}

chemistry       off;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>chemistryType</td><td>化学求解器、方法或化学热物性组合选择，决定后续化学系数的读取方式。</td></tr><tr><td>chemistry</td><td>化学反应积分开关。关闭它并不自动移除所有组分输运方程。</td></tr><tr><td>initialChemicalTimeStep</td><td>首次化学积分采用的时间步估计；后续步长由所选化学积分器调整。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingParcelFoam/rectangularChannel</summary><p><code>rectangularChannel</code> 用带颗粒的流动算例演示颗粒与连续相的耦合。这里把气相化学反应积分关闭，便于单独观察输运和颗粒过程。</p>
<ul>
<li><code>chemistryType/solver noChemistrySolver</code> 选择不推进化学反应方程的求解对象。</li>
<li><code>chemistry off</code> 关闭化学计算。颗粒受力、换热和相变分别由云文件中的模型控制，阅读本文件时可同时打开该算例的云属性文件。</li>
<li>这个配置没有化学子步长或 ODE 容差需要调节。排查气相组分变化时，应先区分对流扩散、颗粒释放与气相反应三个来源。</li>
</ul>
<p>要把此通道改成反应流，可参考 <code>counterFlowFlame2DLTS</code> 中的 <code>EulerImplicit</code> 与 <code>chemistry on</code>，同时提供反应机理、组分初值和燃烧模型。先保持颗粒设置不变，比较新增化学反应前后的温度和组分收支。</p>
<p><a href="/assets/examples/v2512/chemistryproperties/1-chemistryProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rectangularChannel/constant/chemistryProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rectangularChannel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      chemistryProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

chemistryType
{
    solver            noChemistrySolver;
}

chemistry       off;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/fireFoam/LES/smallPoolFire3D</summary><p><code>smallPoolFire3D</code> 计算小型池火。此处关闭的是详细化学方程积分；配套 <code>combustionProperties</code> 实际选择 <code>EDM</code>，由混合控制的燃烧模型提供反应源项。</p>
<ul>
<li><code>noChemistrySolver</code> 与 <code>chemistry off</code> 使本文件不承担化学动力学积分工作。</li>
<li><code>initialChemicalTimeStep 1e-07</code> 是保留的化学初始子步长条目。在当前关闭状态下，改变它不会改变 EDM 的混合时间尺度。</li>
<li>火焰反应强弱应结合 <code>combustionProperties/EDMCoeffs</code> 中实际的 <code>Cd 1</code>、<code>CEDC 1</code> 以及流动和湍流设置理解。</li>
</ul>
<p>研究化学动力学对点火或熄火的影响时，需要更换配套燃烧/化学模型并准备反应机理。保持入口供燃料方式一致，比较热释放率和温度，才能看清模型变化带来的影响。</p>
<p><a href="/assets/examples/v2512/chemistryproperties/2-chemistryProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D/constant/chemistryProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/smallPoolFire3D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      chemistryProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

chemistryType
{
    solver            noChemistrySolver;
}

chemistry       off;

initialChemicalTimeStep 1e-07;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/movingInjectorBox</summary><p><code>movingInjectorBox</code> 重点展示随时间移动的喷射位置与颗粒输运。气相化学在此被关闭，配套燃烧文件也使用 <code>combustionModel none</code>。</p>
<ul>
<li><code>solver noChemistrySolver</code> 指定当前不进行反应积分；<code>chemistry off</code> 是相应的计算开关。</li>
<li><code>initialChemicalTimeStep 1e-7</code> 保留了以后启用化学时可用的初始子步长。当前颗粒运动时间步由运行设置与云跟踪设置决定。</li>
<li>调整喷射轨迹、注入速度或颗粒温度，应进入该算例的云属性文件；这些过程与本文件的化学开关分开配置。</li>
</ul>
<p>可以先改变喷射轨迹观察液滴空间分布，再加入传热或蒸发，最后配置气相反应。每次扩展后分别比较颗粒总质量、气相组分与能量变化。</p>
<p><a href="/assets/examples/v2512/chemistryproperties/3-chemistryProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox/constant/chemistryProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      chemistryProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

chemistryType
{
    solver            noChemistrySolver;
}

chemistry       off;

initialChemicalTimeStep 1e-7;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/chemfoam/">chemFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
