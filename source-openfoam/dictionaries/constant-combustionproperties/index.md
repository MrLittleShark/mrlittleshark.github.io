---
title: "combustionProperties"
layout: reference
description: "选择燃烧闭合模型及其系数，例如有限速率化学与湍流混合时间尺度的耦合。"
dictionary: true
cms_slug: "dictionary-combustionproperties"
---

<p>选择燃烧闭合模型及其系数，例如有限速率化学与湍流混合时间尺度的耦合。</p><p>位置：<code>constant/combustionProperties</code></p><h2>配置实例</h2><p>lagrangian/reactingHeterogenousParcelFoam/rectangularDuct 中的 combustionProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      combustionProperties;
}

combustionModel none;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>combustionModel</td><td>燃烧闭合模型名称，决定化学反应与湍流混合的耦合方式。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · lagrangian/reactingHeterogenousParcelFoam/rectangularDuct</summary><p><code>rectangularDuct</code> 使用异相颗粒求解器。这里的 <code>combustionModel none</code> 关闭气相燃烧模型，颗粒表面反应仍由颗粒云自己的子模型组织。</p>
<ul>
<li><code>none</code> 使连续相燃烧对象返回零燃烧贡献，适合先研究颗粒在矩形通道内的运动、传热和异相反应。</li>
<li>配套 <code>chemistryProperties</code> 同时使用 <code>noChemistrySolver</code> 与 <code>chemistry off</code>，两处设置保持一致。</li>
<li>气体组分仍可受入口输运与颗粒释放影响；具体释放哪种组分，要读取云文件中的成分和表面反应设置。</li>
</ul>
<p>扩展为同时存在气相与表面反应的过程时，应分别设置两套模型，并检查组分名称能否对应到同一套热物性数据。比较入口、出口和颗粒交换的质量流率，可帮助检查耦合是否完整。</p>
<p><a href="/assets/examples/v2512/combustionproperties/1-combustionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingHeterogenousParcelFoam/rectangularDuct/constant/combustionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingHeterogenousParcelFoam/rectangularDuct">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      combustionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

combustionModel none;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/reactingParcelFoam/movingInjectorBox</summary><p><code>movingInjectorBox</code> 中只有一个有效选择：<code>combustionModel none</code>。这样可把计算重点放在移动喷射器和颗粒轨迹上。</p>
<ul>
<li><code>none</code> 关闭气相燃烧源项，本文件因此没有模型系数子字典。</li>
<li>配套化学文件同样设为 <code>chemistry off</code>。修改云的注入位置、速度或粒径后，可以直接观察输运变化。</li>
<li>若需要蒸发，应配置云文件中的相变模型和液体热物性；若还需要蒸气燃烧，再增加气相燃烧与化学设置。</li>
</ul>
<p>实际扩展可依次比较轨迹、蒸发质量和热释放。这样每个新增模型都对应一个可观察的结果量。</p>
<p><a href="/assets/examples/v2512/combustionproperties/2-combustionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox/constant/combustionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      combustionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

combustionModel  none;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/counterFlowFlame2DLTS</summary><p><code>counterFlowFlame2DLTS</code> 是对向流动火焰算例。两侧来流把燃料与氧化剂带入反应区，<code>laminar</code> 燃烧模型从化学模型获得反应速率。</p>
<ul>
<li><code>combustionModel laminar</code> 选择层流化学耦合模型；<code>active true</code> 启用该模型。</li>
<li><code>laminarCoeffs {}</code> 采用此模型的默认可选参数。反应机理与反应积分方法由化学和热物性配置继续提供。</li>
<li>本例 <code>chemistryProperties</code> 实际选用 <code>EulerImplicit</code>、<code>chemistry on</code>，初始化学子步长为 <code>1e-7</code> s。阅读时把这两个文件放在一起，便能对应“使用哪种燃烧模型”与“怎样积分反应”。</li>
<li>案例使用局部时间步推进时，迭代时间服务于收敛到流场；火焰位置与温度剖面是主要比较对象。</li>
</ul>
<p>可调整两侧来流速度研究应变对火焰的影响，或改变入口温度研究反应区移动。更换机理后，要同步更新组分场，并检查产物与元素质量收支。</p>
<p><a href="/assets/examples/v2512/combustionproperties/3-combustionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/counterFlowFlame2DLTS/constant/combustionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/counterFlowFlame2DLTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      combustionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

combustionModel  laminar;

active  true;

laminarCoeffs
{}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/reactingfoam/">reactingFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
