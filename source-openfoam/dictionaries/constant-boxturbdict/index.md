---
title: "boxTurbDict"
layout: reference
description: "各向同性湍流盒初始速度的谱参数。"
dictionary: true
cms_slug: "dictionary-boxturbdict"
---

<p>各向同性湍流盒初始速度的谱参数。</p><p>位置：<code>constant/boxTurbDict</code></p><h2>配置实例</h2><p>DNS/dnsFoam/boxTurb16 中的 boxTurbDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      boxTurbDict;
}

Ea              10;

k0              5;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · DNS/dnsFoam/boxTurb16</summary><p>boxTurb16 在规则盒状网格上生成随机湍流速度场，供 dnsFoam 计算使用。boxTurbDict 用两个参数控制初始化能谱。</p>
<ul>
<li><code>Ea 10</code> 是生成能谱的幅值参数，增大后初始速度脉动能量随之增大。</li>
<li><code>k0 5</code> 控制能谱的特征波数尺度，从而改变初始能量主要分布的空间尺度。</li>
<li>生成工具会使用已有网格构造波数空间，盒子尺寸与网格分辨率共同限制能表达的波长。</li>
</ul>
<p>比较不同初场时保持网格、盒子尺寸和后续黏性参数一致，先查看生成的速度能谱，再分析能量随时间衰减。</p>
<p><a href="/assets/examples/v2512/boxturbdict/1-boxTurbDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16/constant/boxTurbDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

Ea              10;

k0              5;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · etc/caseDicts/annotated</summary><p>这个注释模板为 boxTurb 提供简洁的谱参数输入。它适用于已有规则盒状网格上的随机速度场初始化。</p>
<ul>
<li><code>Ea 10</code> 控制谱幅值；修改它主要用于改变初始脉动强度。</li>
<li><code>k0 5</code> 控制谱的波数尺度；修改它会改变初始涡结构的典型尺寸。</li>
<li>参数由 boxTurb 从 constant/boxTurbDict 读取，生成的 U 随后作为流动求解的初场。</li>
</ul>
<p>采用更高特征波数时应增加网格分辨率，使新增的小尺度结构有足够单元表达。</p>
<p><a href="/assets/examples/v2512/boxturbdict/2-boxTurbDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/boxTurbDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

Ea              10;

k0              5;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/boxturb/">boxTurb</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
