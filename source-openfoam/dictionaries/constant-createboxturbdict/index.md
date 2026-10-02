---
title: "createBoxTurbDict"
layout: reference
description: "特定湍流盒教程用于生成初始谱场的配置。"
dictionary: true
cms_slug: "dictionary-createboxturbdict"
---

<p>特定湍流盒教程用于生成初始谱场的配置。</p><p>位置：<code>constant/createBoxTurbDict</code></p><h2>配置实例</h2><p>incompressible/pimpleFoam/LES/decayIsoTurb 中的 createBoxTurbDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      createBoxTurbDict;
}

N           (64 64 64);
//N           (128 128 128);
//N           (256 256 256);

// Suggested box size of 9*2*pi [cm]
L           (0.56548667765 0.56548667765 0.56548667765);

nModes      5000;

// Energy as a function of wave number
// Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)
Ek          table
(
    (15 0)
    (20 0.000129)
    (25 0.00023)
    (30 0.000322)
    (40 0.000435)
    (50 0.000457)
    (70 0.00038)
    (100 0.00027)
    (150 0.000168)
    (200 0.00012)
    (250 8.9e-05)
    (300 7.03e-05)
    (400 4.7e-05)
    (600 2.47e-05)
    (800 1.26e-05)
    (1000 7.42e-06)
    (1250 3.96e-06)
    (1500 2.33e-06)
    (1750 1.34e-06)
    (2000 8e-07)
);</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/LES/decayIsoTurb</summary><p>decayIsoTurb 需要一个具有给定能谱的初始速度场。createBoxTurb 使用实验谱表和随机模态在周期立方体内构造速度。</p>
<ul>
<li><code>N (64 64 64)</code> 设置三方向各 64 个离散点，<code>L</code> 的三个分量均约 0.56549 m，网格尺度约为 8.84 mm。</li>
<li><code>nModes 5000</code> 用 5000 个模态近似目标谱；增加模态数会增加生成成本。</li>
<li><code>Ek table</code> 给出“波数—谱能量”数据，例如波数 50 对应 0.000457，高波数端逐渐衰减。该表来自文件注释所列的 Comte-Bellot–Corrsin 实验时刻。</li>
<li>后续流动计算让初始湍流在黏性作用下衰减，可以比较各时刻能谱与总动能。</li>
</ul>
<p>把 N 改成 128³ 时同步检查网格生成设置与输出空间；保持盒子尺寸和初始谱一致，才能比较分辨率的影响。</p>
<p><a href="/assets/examples/v2512/createboxturbdict/1-createBoxTurbDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb/constant/createBoxTurbDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBoxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

N           (64 64 64);
//N           (128 128 128);
//N           (256 256 256);

// Suggested box size of 9*2*pi [cm]
L           (0.56548667765 0.56548667765 0.56548667765);

nModes      5000;

// Energy as a function of wave number
// Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)
Ek          table
(
    (15 0)
    (20 0.000129)
    (25 0.00023)
    (30 0.000322)
    (40 0.000435)
    (50 0.000457)
    (70 0.00038)
    (100 0.00027)
    (150 0.000168)
    (200 0.00012)
    (250 8.9e-05)
    (300 7.03e-05)
    (400 4.7e-05)
    (600 2.47e-05)
    (800 1.26e-05)
    (1000 7.42e-06)
    (1250 3.96e-06)
    (1500 2.33e-06)
    (1750 1.34e-06)
    (2000 8e-07)
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · etc/caseDicts/annotated</summary><p>这个模板展示如何向 createBoxTurb 提供盒子尺寸、离散分辨率和完整目标能谱。</p>
<ul>
<li><code>N (64 64 64)</code> 对应 262144 个离散位置，<code>L (0.56548667765 ...)</code> 给出约 0.56549 m 的立方体边长。</li>
<li><code>nModes 5000</code> 控制随机谱展开的模态数。</li>
<li><code>Ek table</code> 从波数 15 到 2000 提供采样数据，工具据此构造初始速度的谱分布。</li>
</ul>
<p>提高分辨率主要扩展可表达的小尺度范围；提高 nModes 主要改善目标谱的离散近似。两项可分别改变并对照生成后的谱曲线。</p>
<p><a href="/assets/examples/v2512/createboxturbdict/2-createBoxTurbDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/createBoxTurbDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBoxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

N           (64 64 64);

// Suggested box size of 9*2*pi [cm]
L           (0.56548667765 0.56548667765 0.56548667765);

nModes      5000;

// Energy as a function of wave number
// Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)
Ek          table
(
    (15 0)
    (20 0.000129)
    (25 0.00023)
    (30 0.000322)
    (40 0.000435)
    (50 0.000457)
    (70 0.00038)
    (100 0.00027)
    (150 0.000168)
    (200 0.00012)
    (250 8.9e-05)
    (300 7.03e-05)
    (400 4.7e-05)
    (600 2.47e-05)
    (800 1.26e-05)
    (1000 7.42e-06)
    (1250 3.96e-06)
    (1500 2.33e-06)
    (1750 1.34e-06)
    (2000 8e-07)
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/boxturb/">boxTurb</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
