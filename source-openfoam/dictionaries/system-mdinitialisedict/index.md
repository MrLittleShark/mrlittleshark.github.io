---
title: "mdInitialiseDict"
layout: reference
description: "分子初始排布、种类及速度分布的设置。"
dictionary: true
cms_slug: "dictionary-mdinitialisedict"
---

<p>分子初始排布、种类及速度分布的设置。</p><p>位置：<code>system/mdInitialiseDict</code></p><h2>配置实例</h2><p>discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon 中的 mdInitialiseDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      mdInitialiseDict;
}

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

liquid
{
    massDensity             1220;
    temperature             300;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds              (Ar);
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</summary><p><code>periodicCubeArgon</code> 为周期立方体中的氩体系生成初始分子位置与速度。<code>liquid</code> 是待填充的网格单元区域名称。</p>
<ul>
<li><code>massDensity 1220</code> kg/m³ 与 <code>moleculeProperties</code> 中的氩原子质量共同决定原子数密度和初始晶格间距。</li>
<li><code>latticeIds (Ar)</code>、<code>latticePositions ((0 0 0))</code> 表示每个重复晶格单元放一个氩原子。<code>latticeCellShape (1 1 1)</code> 给出三个方向相同的尺寸比例，实际长度按目标密度缩放。</li>
<li><code>temperature 300</code> K 设置初始随机热运动；<code>bulkVelocity (0 0 0)</code> 表示没有叠加整体平移速度。</li>
<li><code>anchor (0 0 0)</code> 和 <code>orientationAngles (0 0 0)</code> 确定晶格的原点与方向；角度按度读取。</li>
<li><code>tetherSiteIds ()</code> 为空，当前没有指定通过系缚势约束的位点。</li>
</ul>
<p>提高目标密度会缩短初始原子间距，随后平衡阶段需要消除初始排列带来的非平衡结构。比较不同密度时，可记录能量、压力与温度随时间的变化，并在稳定后采样。</p>
<p><a href="/assets/examples/v2512/mdinitialisedict/1-mdInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/mdInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

liquid
{
    massDensity             1220;
    temperature             300;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds              (Ar);
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</summary><p><code>periodicCubeWater</code> 用规则排列建立周期水分子体系，随后通过分子运动达到平衡状态。</p>
<ul>
<li><code>massDensity 980</code> kg/m³、<code>temperature 298</code> K 设置初始密度和温度，整体平移速度为零。</li>
<li><code>latticePositions</code> 的四个位点为立方体顶点及三个面心位置；<code>latticeIds</code> 按同一顺序放置 <code>water</code>、<code>water2</code>、<code>water</code>、<code>water2</code>。</li>
<li>四个位点共同构成重复单元，程序把其中分子的总质量与目标密度结合起来确定晶格尺度。</li>
<li><code>water</code> 与 <code>water2</code> 需要在 <code>moleculeProperties</code> 中分别定义。本例二者几何、质量和电荷相同，部分位点名称不同。</li>
<li><code>anchor</code>、<code>orientationAngles</code> 和 <code>latticeCellShape</code> 控制整体排列的原点、取向与长宽比例。</li>
</ul>
<p>可先保持分子模型不变，改变目标密度观察平衡压力；改变初始取向则可检查结果对初始化排列的依赖。每次比较都在相近的平衡程度和采样长度下进行。</p>
<p><a href="/assets/examples/v2512/mdinitialisedict/2-mdInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/mdInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

liquid
{
    massDensity             980;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
        water2
        water
        water2
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
        (0 0.5 0.5)
        (0.5 0 0.5)
        (0.5 0.5 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · discreteMethods/molecularDynamics/mdFoam/nanoNozzle</summary><p><code>nanoNozzle</code> 分别向 <code>sectionA</code>、<code>sectionB</code>、<code>sectionC</code> 三个网格单元区域填充水分子，适合为纳米喷嘴的不同几何段建立一致的初始状态。</p>
<ul>
<li>三个子字典名称对应已有区域名，区域的几何位置由网格分区决定。</li>
<li>每区均使用 <code>massDensity 1004</code> kg/m³、<code>temperature 298</code> K 和零整体速度，使初始区域之间具有相同的热力学输入。</li>
<li><code>latticeIds (water)</code> 与单一 <code>latticePositions (0 0 0)</code> 规定每个重复单元放一分子，晶格间距按该分子的质量与目标密度生成。</li>
<li>三个区域的原点和旋转角均为零，<code>latticeCellShape (1 1 1)</code> 为等比例晶格；<code>tetherSiteIds</code> 为空。</li>
</ul>
<p>给不同区域设置不同密度或整体速度，可以建立新的初始流动工况。先确认各区域相接处的分子间距与重叠情况，再观察启动阶段的压力波和喷嘴质量通量。</p>
<p><a href="/assets/examples/v2512/mdinitialisedict/3-mdInitialiseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle/system/mdInitialiseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdFoam/nanoNozzle">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mdInitialiseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Euler angles, expressed in degrees as phi, theta, psi, see
// http://mathworld.wolfram.com/EulerAngles.html

sectionA
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}

sectionB
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}

sectionC
{
    massDensity             1004;
    temperature             298;
    bulkVelocity            (0.0 0.0 0.0);
    latticeIds
    (
        water
    );
    tetherSiteIds           ();
    latticePositions
    (
        (0 0 0)
    );
    anchor                  (0 0 0);
    orientationAngles       (0 0 0);
    latticeCellShape        (1 1 1);
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mdinitialise/">mdInitialise</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
