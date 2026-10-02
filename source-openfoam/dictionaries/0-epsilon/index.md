---
title: "epsilon"
layout: reference
description: "湍动能耗散率场，常用于 k–epsilon 湍流模型，单位为 m²/s³。"
dictionary: true
cms_slug: "dictionary-epsilon"
---

<p>湍动能耗散率场，常用于 k–epsilon 湍流模型，单位为 m²/s³。</p><p>位置：<code>0/epsilon</code></p><p><code>epsilon</code> 是湍动能耗散率，单位 m²/s³，在 k–ε 模型中表示湍流动能向黏性耗散的转移速率。给定 <code>k</code> 后，耗散率越小通常对应更大的湍流时间尺度 \(k/\epsilon\)。</p>
<h3>示例：根据长度尺度设置入口</h3>
<p>采用 \(\epsilon=C_\mu^{3/4}k^{3/2}/\ell\)，令 \(C_\mu=0.09\)、\(k=0.375\ \mathrm{m^2/s^2}\)、\(\ell=0.01\ \mathrm m\)，得到约 3.77 m²/s³。在 <code>0/epsilon</code> 的 <code>boundaryField</code> 中可写：</p>
<pre><code class="language-foam">inlet
{
    type  fixedValue;
    value uniform 3.77;
}
wall
{
    type  epsilonWallFunction;
    value uniform 3.77;
}
</code></pre>
<p>字段的 <code>dimensions</code> 为 <code>[0 2 -3 0 0 0 0]</code>。入口值与 <code>k</code> 一起控制湍流状态，壁面函数则根据近壁模型更新耗散率；其他边界继续按流入、流出和几何类型设置。</p>
<p>长度尺度 \(\ell\) 描述入口含能涡的尺度，可以按测量或适合该装置的经验关系估计。它与第一层网格厚度不同。保持速度和强度不变时，长度尺度增大一倍，估算耗散率减半。</p>
<p>更换为 SST 时，需要创建对应的 <code>omega</code> 场、离散和求解器条目。耗散率与比耗散率采用不同定义与量纲，应依据同一入口湍流强度和尺度重新计算。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/pitzDailyExptInlet</summary><p>这是与实验型入口 k 廓线配套的 epsilon 数据表。</p>
<ul>
<li><code>70</code> 表示采样点数，应与同一入口的 points 和 k 数据一致。</li>
<li>epsilon 的单位为 m²/s³；例如表首为 <code>9813.84</code>，内部还有约 <code>2.24094</code> 的数值，体现显著空间变化。</li>
<li>数据按位置映射到入口，无法仅凭列表序号解释物理高度。</li>
</ul>
<p>替换廓线时同时检查坐标、耗散率单位和正值范围，以免产生异常湍流长度尺度。</p>
<p><a href="/assets/examples/v2512/epsilon/1-epsilon.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet/constant/boundaryData/inlet/0/epsilon">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet">案例目录</a></p><pre><code class="language-foam">// Data on points
70
(

//minz
9813.84
9813.84
7231.83
1260.68
1260.68
253.433
253.433
76.6694
76.6694
30.8982
16.0868
16.0868
10.4406
7.39238
4.6135
3.0542
2.39951
2.24094
2.3504
2.93787
3.6326
3.15933
2.71282
2.72062
3.09416
4.18748
7.30754
14.5872
29.1787
73.9208
490.641
3622.84
5549.75
6430.47
6327.27

// maxz
9813.84
9813.84
7231.83
1260.68
1260.68
253.433
253.433
76.6694
76.6694
30.8982
16.0868
16.0868
10.4406
7.39238
4.6135
3.0542
2.39951
2.24094
2.3504
2.93787
3.6326
3.15933
2.71282
2.72062
3.09416
4.18748
7.30754
14.5872
29.1787
73.9208
490.641
3622.84
5549.75
6430.47
6327.27
)

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionFoam/externalCoupledHeater</summary><p>externalCoupledHeater 的 epsilon 模板给出统一初值，并把边界值交给后续模型或配置处理。</p>
<ul>
<li>量纲 <code>[0 2 -3 0 0 0 0]</code> 表示 m²/s³。</li>
<li><code>internalField uniform 0.01</code> 是初始耗散率。</li>
<li><code>".*"/calculated</code> 声明边界值由相关计算获得，<code>value $internalField</code> 提供初始化值。</li>
</ul>
<p>用于具体湍流区域时，检查最终边界是否已换成该区域需要的入口和壁面处理。</p>
<p><a href="/assets/examples/v2512/epsilon/2-epsilon.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater/0.orig/epsilon">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalCoupledHeater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      epsilon;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -3 0 0 0 0];

internalField   uniform 0.01;

boundaryField
{
    &quot;.*&quot;
    {
        type            calculated;
        value           $internalField;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/sprayFoam/aachenBomb</summary><p>aachenBomb 的 epsilon 与 k=1 的初场配合，控制初始湍流耗散尺度。</p>
<ul>
<li><code>internalField uniform 90</code> 给出 90 m²/s³。</li>
<li>壁面采用 <code>epsilonWallFunction</code>，并提供 <code>value uniform 90</code> 作为初始化值。</li>
<li>近壁耗散率随后由壁面模型和流场共同确定。</li>
</ul>
<p>改变 k 或流动尺度时同步评估 epsilon，并用所需 y⁺ 范围检查壁面网格。</p>
<p><a href="/assets/examples/v2512/epsilon/3-epsilon.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/epsilon">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      epsilon;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -3 0 0 0 0];

internalField   uniform 90;

boundaryField
{
    walls
    {
        type            epsilonWallFunction;
        value           uniform 90;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
