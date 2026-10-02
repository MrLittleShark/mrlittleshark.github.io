---
title: "physicalProperties"
layout: reference
description: "v2512 的 electrostaticFoam/chargedWire 教程使用此文件定义 epsilon0 和电荷输运参数 k。"
dictionary: true
cms_slug: "dictionary-physicalproperties"
---

<p>v2512 的 electrostaticFoam/chargedWire 教程使用此文件定义 epsilon0 和电荷输运参数 k。</p><p>位置：<code>constant/physicalProperties</code></p><h2>配置实例</h2><p>electromagnetics/electrostaticFoam/chargedWire 中的 physicalProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      physicalProperties;
}

epsilon0        8.85419e-12;

k               0.00016;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>epsilon0</td><td>真空介电常数，用于 electrostaticFoam 静电 Poisson 方程。</td></tr><tr><td>k</td><td>此处是电荷输运相关系数，不是湍动能场，也不是热导率；应结合 electrostaticFoam 方程及量纲理解。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · electromagnetics/electrostaticFoam/chargedWire</summary><p>chargedWire 求解电势与空间电荷的输运。physicalProperties 给出介电常数和电荷迁移率。</p>
<ul>
<li><code>epsilon0 8.85419e-12</code> 是真空介电常数，单位 F/m；它把电荷密度与电势 Poisson 方程联系起来。</li>
<li><code>k 0.00016</code> 是迁移率，单位 m²/(V·s)，电场驱动的漂移速度与 k 成正比。</li>
<li>求解器从电势梯度得到电场，并通过 <code>rhoFlux = -k*magSf*snGrad(phi)</code> 构造输运通量。</li>
</ul>
<p>改变迁移率后比较相同边界电压下的电荷分布与迁移时间，电势 phi 的单位为 V。</p>
<p><a href="/assets/examples/v2512/physicalproperties/1-physicalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/electromagnetics/electrostaticFoam/chargedWire/constant/physicalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/electromagnetics/electrostaticFoam/chargedWire">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      physicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

epsilon0        8.85419e-12;

k               0.00016;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/electrostaticfoam/">electrostaticFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
