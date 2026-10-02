---
title: "financialProperties"
layout: reference
description: "Black–Scholes 模型的利率、波动率等金融参数。"
dictionary: true
cms_slug: "dictionary-financialproperties"
---

<p>Black–Scholes 模型的利率、波动率等金融参数。</p><p>位置：<code>constant/financialProperties</code></p><h2>配置实例</h2><p>financial/financialFoam/europeanCall 中的 financialProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      financialProperties;
}

strike          40;

r               0.1;

sigma           0.2;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · financial/financialFoam/europeanCall</summary><p>europeanCall 展示有限体积离散在 Black–Scholes 方程中的应用，financialProperties 提供欧式看涨期权模型的三个常数。</p>
<ul>
<li><code>strike 40</code> 设置执行价格，与计算域中标的价格使用相同单位。</li>
<li><code>r 0.1</code> 是模型使用的无风险利率。</li>
<li><code>sigma 0.2</code> 是波动率参数，决定方程中的扩散强度；利率与波动率的时间尺度应与到期时间一致。</li>
</ul>
<p>改变 sigma 后可比较相同标的价格和剩余期限下的数值解，并用解析解检查离散误差。</p>
<p><a href="/assets/examples/v2512/financialproperties/1-financialProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/financial/financialFoam/europeanCall/constant/financialProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/financial/financialFoam/europeanCall">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      financialProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

strike          40;

r               0.1;

sigma           0.2;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/financialfoam/">financialFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
