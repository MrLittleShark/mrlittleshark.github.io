---
title: "phaseChangeProperties"
layout: reference
description: "interCondensatingEvaporatingFoam 的凝结与蒸发模型配置。"
dictionary: true
cms_slug: "dictionary-phasechangeproperties"
---

<p>interCondensatingEvaporatingFoam 的凝结与蒸发模型配置。</p><p>位置：<code>constant/phaseChangeProperties</code></p><h2>配置实例</h2><p>multiphase/interCondensatingEvaporatingFoam/condensatingVessel 中的 phaseChangeProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      phaseChangeProperties;
}

phaseChangeTwoPhaseModel constant;

constantCoeffs
{
    coeffC          150;
    coeffE          150;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>phaseChangeTwoPhaseModel</td><td>相变模型名称，本页凝结教程选择 constant。</td></tr><tr><td>constantCoeffs</td><td>与 constant 模型对应的系数字典。</td></tr><tr><td>coeffC</td><td>凝结方向的模型系数，含义由该相变模型实现确定。</td></tr><tr><td>coeffE</td><td>蒸发方向的模型系数，不能假定与 coeffC 总应相等。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interCondensatingEvaporatingFoam/condensatingVessel</summary><p><code>condensatingVessel</code> 用温度偏离饱和值的程度驱动液汽相变。<code>constant</code> 表示相变速率系数为常数，局部速率仍随温度和相分数变化。</p>
<ul>
<li><code>coeffC 150</code> 控制凝结，<code>coeffE 150</code> 控制蒸发；本模型中的量纲均为 \(\mathrm{s^{-1}K^{-1}}\)。</li>
<li>温度低于饱和温度时，凝结项与 \(\alpha_v\rho_v(T_{sat}-T)\) 成正比；高于饱和温度时，蒸发项与 \(\alpha_l\rho_l(T-T_{sat})\) 成正比。</li>
<li>两个数值相同给出对称的温差系数，但两相密度与相分数不同，实际质量变化率会随流场变化。</li>
<li>饱和温度和两相热物性来自热物性模型；本文件只指定相变模型与系数。</li>
</ul>
<p>例如保持过冷度和局部汽相状态不变，把 <code>coeffC</code> 从 150 改为 300，会使该凝结源项加倍。参数增大后，相分数和能量交换更快，需结合时间步及潜热收支观察收敛情况。</p>
<p><a href="/assets/examples/v2512/phasechangeproperties/1-phaseChangeProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel/constant/phaseChangeProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interCondensatingEvaporatingFoam/condensatingVessel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseChangeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phaseChangeTwoPhaseModel constant;

constantCoeffs
{
    coeffC          150;
    coeffE          150;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam</summary><p>Stefan 问题通过界面移动与解析解比较相变计算。本例选择 <code>interfaceHeatResistance</code>，利用重建的界面面积与温差计算质量交换。</p>
<ul>
<li><code>R 1e6</code> 在该实现中的量纲是 \(\mathrm{W/(m^2K)}\)，作为界面换热系数乘以温差。相变质量率按“界面面积密度 × <code>R</code> × 温差 ÷ 潜热”计算。</li>
<li><code>spread 3</code> 控制源项向邻近单元的平滑扩展，源码据此构造与局部网格尺度有关的扩散系数。</li>
<li>界面几何从液相分数的 0.5 等值面重建；网格加密会改变界面面积的离散表示。</li>
<li>文件还保留了 <code>maxAlphaRate 1</code>、<code>coeffC 0</code>、<code>coeffE 500</code>。当前 <code>interfaceHeatResistance</code> 实现读取的模型参数是 <code>R</code> 与 <code>spread</code>，调参应集中在这两项及温度、潜热和网格上。</li>
</ul>
<p>可固定网格分别改变 <code>R</code>、<code>spread</code>，比较界面位置曲线；再固定参数进行网格与时间步细化。这样可以区分界面换热强度、源项分布与离散误差。</p>
<p><a href="/assets/examples/v2512/phasechangeproperties/2-phaseChangeProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/constant/phaseChangeProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      phaseChangeProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

phaseChangeTwoPhaseModel interfaceHeatResistance;//constant;


R               1e6;
maxAlphaRate    1;
spread          3;


coeffC          0;
coeffE          500;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/intercondensatingevaporatingfoam/">interCondensatingEvaporatingFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
