---
title: "omega"
layout: reference
description: "比耗散率场，常用于 k–omega 和 SST 模型，单位为 1/s。"
dictionary: true
cms_slug: "dictionary-omega"
---

<p>比耗散率场，常用于 k–omega 和 SST 模型，单位为 1/s。</p><p>位置：<code>0/omega</code></p><p><code>omega</code> 是比耗散率，单位 s⁻¹，可理解为湍流时间尺度倒数的模型量。k–ω 和 SST 模型使用 <code>k</code>、<code>omega</code> 共同计算湍流黏度，并通过模型中的限制和混合关系处理不同流动区域。</p>
<h3>示例：SST 的入口与壁面</h3>
<p>使用 \(\omega=\sqrt{k}/(C_\mu^{1/4}\ell)\)，当 \(k=0.375\ \mathrm{m^2/s^2}\)、\(\ell=0.01\ \mathrm m\)、\(C_\mu=0.09\) 时，入口 \(\omega\approx112\ \mathrm{s^{-1}}\)。在 <code>0/omega</code> 的 <code>boundaryField</code> 中设置：</p>
<pre><code class="language-foam">inlet
{
    type  fixedValue;
    value uniform 112;
}
wall
{
    type  omegaWallFunction;
    value uniform 112;
}
</code></pre>
<p>场量纲为 <code>[0 0 -1 0 0 0 0]</code>。入口采用给定值，壁面由 <code>omegaWallFunction</code> 根据近壁信息更新。配套检查 <code>0/k</code>、<code>0/nut</code>、模型选择以及 <code>fvSolution</code> 中的 <code>omega</code> 求解器设置。</p>
<p><code>omegaWallFunction</code> 具有可配置的近壁混合方式，选择时结合 y⁺ 和模型要求。将入口尺度增大，会减小由上式估算的 <code>omega</code>，并影响湍流在入口下游的衰减。</p>
<p>切换模型后出现 <code>cannot find file omega</code>，说明初始字段尚未补齐；提示找不到 <code>div(phi,omega)</code> 或相应求解器时，继续补充离散和线性求解器配置。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pisoFoam/RAS/cavity</summary><p>湍流方腔使用 omega 描述比耗散率，壁面条件与相应 k–omega 类模型配合。</p>
<ul>
<li><code>dimensions [0 0 -1 0 0 0 0]</code> 表示 s⁻¹。</li>
<li>内部初值为 <code>22.4</code>，移动与固定壁面共用 <code>omegaWallFunction</code>。</li>
<li><code>frontAndBack/empty</code> 保持二维计算。</li>
</ul>
<p>增大盖板速度或更换湍流初值时，同时检查 k、omega、nut 和近壁网格的对应关系。</p>
<p><a href="/assets/examples/v2512/omega/1-omega.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/RAS/cavity/0.orig/omega">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/RAS/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      omega;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 -1 0 0 0 0];

internalField   uniform 22.4;

boundaryField
{
    &quot;(movingWall|fixedWalls)&quot;
    {
        type            omegaWallFunction;
        value           uniform 22.4;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interFoam/RAS/electrostaticDeposition</summary><p>electrostaticDeposition 给壁面和开放侧边分别设置 omega 条件。</p>
<ul>
<li>初值 <code>0.22</code> 的单位为 s⁻¹。</li>
<li><code>metalSheet/omegaWallFunction</code> 对金属板应用近壁处理。</li>
<li><code>"side-.*"/inletOutlet</code> 在流入时使用 <code>inletValue $internalField</code>，流出时采用相应外推。</li>
<li><code>value $internalField</code> 为边界提供启动值。</li>
</ul>
<p>侧边回流明显时应给定与进入流体相符的湍流尺度，而不是只调求解器容差。</p>
<p><a href="/assets/examples/v2512/omega/2-omega.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/electrostaticDeposition/0.orig/omega">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/electrostaticDeposition">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      omega;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 -1 0 0 0 0];

internalField   uniform 0.22;

boundaryField
{
    metalSheet
    {
        type            omegaWallFunction;
        value           $internalField;
    }

    &quot;side-.*&quot;
    {
        type            inletOutlet;
        inletValue      $internalField;
        value           $internalField;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/damBreakWithObstacle</summary><p>带障碍物溃坝目录中的 omega 文件提供可供相应湍流设置使用的字段模板，实际是否求解它由 turbulenceProperties 决定。</p>
<ul>
<li>初值 <code>2</code> 的单位为 s⁻¹。</li>
<li><code>atmosphere/inletOutlet</code> 在回流时使用同一初值，流出时外推。</li>
<li>障碍物与墙面共用 <code>omegaWallFunction</code>。</li>
</ul>
<p>启用 k–omega 类模型时同步准备 k 和 nut，保持所有墙面条件相容。</p>
<p><a href="/assets/examples/v2512/omega/3-omega.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreakWithObstacle/0.orig/omega">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreakWithObstacle">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      omega;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 -1 0 0 0 0];

internalField   uniform 2;

boundaryField
{
    atmosphere
    {
        type            inletOutlet;
        inletValue      $internalField;
        value           $internalField;
    }

    &quot;(obstacle|walls)&quot;
    {
        type            omegaWallFunction;
        value           $internalField;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
