---
title: "moleculeProperties"
layout: reference
description: "分子动力学系统的分子种类与分子属性。"
dictionary: true
cms_slug: "dictionary-moleculeproperties"
---

<p>分子动力学系统的分子种类与分子属性。</p><p>位置：<code>constant/moleculeProperties</code></p><h2>配置实例</h2><p>discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon 中的 moleculeProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      moleculeProperties;
}

Ar
{
    siteIds                     (Ar);
    pairPotentialSiteIds        (Ar);
    siteReferencePositions
    (
        (0 0 0)
    );
    siteMasses
    (
        6.63352033e-26
    );
    siteCharges
    (
        0
    );
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</summary><p><code>periodicCubeArgon</code> 把每个氩原子表示为一个无电荷的作用位点。该文件定义分子结构，原子间作用强度由相互作用势配置提供。</p>
<ul>
<li><code>siteIds (Ar)</code> 定义唯一位点；<code>siteReferencePositions ((0 0 0))</code> 把它放在分子参考原点。</li>
<li><code>siteMasses (6.63352033e-26)</code> 给出单原子质量，单位 kg。初始化时它与目标质量密度共同决定原子间距。</li>
<li><code>siteCharges (0)</code> 表示电荷为零。</li>
<li><code>pairPotentialSiteIds (Ar)</code> 指定参与短程成对相互作用的位点类型，相互作用势字典需为该类型提供配套模型与参数。</li>
</ul>
<p>研究不同惰性气体时，应一起替换原子质量和势函数参数。改变数值精度时则保持这些材料参数不变，通过时间步细化观察能量漂移。</p>
<p><a href="/assets/examples/v2512/moleculeproperties/1-moleculeProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/constant/moleculeProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

Ar
{
    siteIds                     (Ar);
    pairPotentialSiteIds        (Ar);
    siteReferencePositions
    (
        (0 0 0)
    );
    siteMasses
    (
        6.63352033e-26
    );
    siteCharges
    (
        0
    );
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/molecularDynamics/mdFoam/nanoNozzle</summary><p><code>nanoNozzle</code> 采用四位点水分子：两个氢位点、一个氧位点，以及一个承载负电荷的虚拟位点 <code>M</code>。</p>
<ul>
<li><code>siteIds (H H O M)</code> 与位置、质量、电荷列表按顺序一一对应。</li>
<li>两个氢位点相对氧对称，坐标的单位为 m；由这些数值可得到约 0.09572 nm 的 O–H 距离。<code>M</code> 位于 <code>(0 1.5e-11 0)</code>。</li>
<li>两个氢的质量各为 <code>1.67353255e-27</code> kg，氧为 <code>2.6560176e-26</code> kg，<code>M</code> 的质量为零。</li>
<li>两个氢各带 <code>8.3313177324e-20</code> C，<code>M</code> 带相反的两倍电荷，总电荷为零；氧位点本身的电荷为零。</li>
<li><code>pairPotentialSiteIds (O)</code> 指定短程成对势采用氧位点；带电位点通过配套静电作用参与分子间相互作用。</li>
</ul>
<p>更换水模型时，需要成套修改位点几何、质量、电荷和势参数。只改变流动初态时，保持此文件不变，在初始化文件中调整密度、温度与整体速度。</p>
<p><a href="/assets/examples/v2512/moleculeproperties/2-moleculeProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/constant/moleculeProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

water
{
    siteIds                     (H H O M);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</summary><p><code>periodicCubeWater</code> 定义 <code>water</code> 与 <code>water2</code> 两种分子标识，供初始化晶格交替放置。</p>
<ul>
<li><code>water</code> 使用 <code>(H H O M)</code>，<code>water2</code> 使用 <code>(H2 H2 O M2)</code>；两者的位点坐标、质量和电荷数值完全相同。</li>
<li>这里 <code>H2</code> 是第二套位点名称。其质量仍是 <code>1.67353255e-27</code> kg，解释模型时应按照质量与电荷数据识别物理意义。</li>
<li>两种分子都用 <code>pairPotentialSiteIds (O)</code> 选择氧的短程成对势；带电位点名称需与相互作用势配置中的类型对应。</li>
<li>每种分子均含两个正电荷氢位点与一个等量负电荷虚拟位点，电荷和为零；虚拟位点质量为零。</li>
<li><code>mdInitialiseDict</code> 的 <code>latticeIds</code> 按顺序引用这两个分子名称，从而控制每个晶格位置放置的类型。</li>
</ul>
<p>若将两套定义合并为一种名称，应同步修改初始化的 <code>latticeIds</code> 和相关势类型列表。若希望比较两种水模型，则需明确改变的几何、电荷或势参数，并分别统计各类分子的数量。</p>
<p><a href="/assets/examples/v2512/moleculeproperties/3-moleculeProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/constant/moleculeProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      moleculeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

water
{
    siteIds                     (H H O M);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}

water2
{
    siteIds                     (H2 H2 O M2);
    pairPotentialSiteIds        (O);
    siteReferencePositions
    (
        (7.56950327263661e-11 5.85882276618295e-11 0)
        (-7.56950327263661e-11 5.85882276618295e-11 0)
        (0 0 0)
        (0 1.5e-11 0)
    );
    siteMasses
    (
        1.67353255e-27
        1.67353255e-27
        2.6560176e-26
        0
    );
    siteCharges
    (
        8.3313177324e-20
        8.3313177324e-20
        0
        -1.66626354648e-19
    );
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mdfoam/">mdFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
