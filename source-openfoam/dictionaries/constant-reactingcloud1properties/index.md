---
title: "reactingCloud1Properties"
layout: reference
description: "配置名为 reactingCloud1 的反应颗粒云，包括注入、颗粒物性、传热、挥发或表面反应与边界碰撞。"
dictionary: true
cms_slug: "dictionary-reactingcloud1properties"
---

<p>配置名为 reactingCloud1 的反应颗粒云，包括注入、颗粒物性、传热、挥发或表面反应与边界碰撞。</p><p>位置：<code>constant/reactingCloud1Properties</code></p><h2>配置实例</h2><p>lagrangian/reactingParcelFoam/rivuletPanel 中的 reactingCloud1Properties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      reactingCloud1Properties;
}

solution
{
    active          no;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>solution</td><td>颗粒云的求解控制，包含稳态/瞬态、载体耦合、源项与时间积分等。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>constantProperties</td><td>单个颗粒或材料的基本属性，例如密度、温度和热容；具体键由云类型决定。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingParcelFoam/rivuletPanel</summary><p><code>rivuletPanel</code> 的这个文件把名为 <code>reactingCloud1</code> 的颗粒云关闭。计算重点可放在壁面液膜形成的细流上。</p>
<ul>
<li><code>solution/active no</code> 是本文件唯一的有效设置，求解过程中不推进该颗粒云。</li>
<li>算例目录中即使保留注入数据，也要由启用的注入模型读取后才会形成计算粒子。这个云目前没有提供这样的完整模型配置。</li>
<li>液膜模型与膜内初始场由 <code>surfaceFilmProperties</code> 及相应区域文件单独控制，修改云开关与修改液膜流量是两种不同操作。</li>
</ul>
<p>若要研究喷滴补给细流，可从完整的颗粒云教程复制 <code>solution</code>、<code>constantProperties</code> 与 <code>subModels</code>，配置注入器和膜碰撞模型后再启用。比较新增液滴质量与膜内质量增长，可以检查交换过程。</p>
<p><a href="/assets/examples/v2512/reactingcloud1properties/1-reactingCloud1Properties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel/constant/reactingCloud1Properties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      reactingCloud1Properties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          no;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/fireFoam/LES/compartmentFire</summary><p><code>compartmentFire</code> 研究室内火灾流动。此文件使用 <code>solution/active false</code>，关闭额外的反应颗粒云。</p>
<ul>
<li><code>active false</code> 表示不推进 <code>reactingCloud1</code> 的位置、温度或质量。</li>
<li>火灾的气相燃烧、浮力与辐射由各自模型文件承担，因此这里无需列出颗粒的阻力、注入和蒸发参数。</li>
<li>若扩展为喷雾灭火，应同时提供水滴注入、传热、蒸发及耦合设置；云的开关是这些设置完整后的启用步骤。</li>
</ul>
<p>扩展时可以固定火源与通风条件，先加入少量液滴观察轨迹，再逐步增加流量。分别记录液滴蒸发量、气相降温和水汽增加量，能更清楚地分析冷却机制。</p>
<p><a href="/assets/examples/v2512/reactingcloud1properties/2-reactingCloud1Properties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire/constant/reactingCloud1Properties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/compartmentFire">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      reactingCloud1Properties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          false;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/counterFlowFlame2DLTS</summary><p><code>counterFlowFlame2DLTS</code> 当前求解气相对向流火焰，<code>reactingCloud1</code> 被关闭，便于先建立气相火焰基准。</p>
<ul>
<li><code>solution/active no</code> 关闭该颗粒云，当前不发生颗粒注入或跟踪。</li>
<li><code>constantProperties/volumeUpdateMethod constantRho</code> 保留了启用后采用恒密度方式更新颗粒体积的选择；质量改变时，颗粒体积相应变化。</li>
<li>气相反应由配套 <code>combustionModel laminar</code> 和开启的化学模型推进，颗粒开关与气相燃烧分别配置。</li>
</ul>
<p>要扩展为液滴对向流火焰，需要补齐注入、液体成分、相变和传热模型。先复用已得到的气相状态，再逐步增加液滴质量流量，比较火焰位置与蒸发冷却的变化。</p>
<p><a href="/assets/examples/v2512/reactingcloud1properties/3-reactingCloud1Properties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/counterFlowFlame2DLTS/constant/reactingCloud1Properties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/counterFlowFlame2DLTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      reactingCloud1Properties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solution
{
    active          no;
}

constantProperties
{
    volumeUpdateMethod  constantRho;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/reactingparcelfoam/">reactingParcelFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
