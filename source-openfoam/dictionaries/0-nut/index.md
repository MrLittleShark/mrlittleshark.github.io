---
title: "nut"
layout: reference
description: "湍流运动黏度场，由湍流模型和近壁处理计算，单位为 m²/s。"
dictionary: true
cms_slug: "dictionary-nut"
---

<p>湍流运动黏度场，由湍流模型和近壁处理计算，单位为 m²/s。</p><p>位置：<code>0/nut</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-wall-law.png" alt="无量纲壁面速度分布与近壁区域" loading="lazy"><figcaption><strong>无量纲壁面速度分布与近壁区域</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 21 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><p><code>nut</code> 是湍流运动黏度，单位 m²/s，用来表示湍流对动量输运的附加作用。它由湍流模型计算；分子运动黏度 <code>nu</code> 来自材料物性。采用涡黏性模型时，二者共同构成有效动量扩散。</p>
<h3>示例：k–ε 案例的 nut 边界</h3>
<p>在已有 <code>0/nut</code> 文件中，保留 <code>class volScalarField</code>、<code>object nut</code>，并设置：</p>
<pre><code class="language-foam">dimensions [0 2 -1 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type calculated; value uniform 0; }
    outlet { type calculated; value uniform 0; }
    walls { type nutkWallFunction; value uniform 0; }
    frontAndBack { type empty; }
}
</code></pre>
<p>这个例子适用于具有相应 patch 的二维通道。<code>calculated</code> 表示边界值由模型计算，<code>value</code> 用于初始读取；壁面通过 <code>nutkWallFunction</code> 得到与所选近壁处理相符的湍流黏度。初始化为零后，模型会依据湍流场更新内部 <code>nut</code>。</p>
<p>标准 k–ε 关系为 \(\nu_t=C_\mu k^2/\epsilon\)。SST 和 LES 使用各自的计算与限制关系。后处理 <code>nut/nu</code> 可查看湍流扩散相对于分子扩散的大小，较大的比值常见于强湍流区域。</p>
<p>低 y⁺ 解析、连续壁面律和粗糙壁面需要匹配的 <code>nut</code> 条件。修改壁面函数后，同时检查 <code>k</code>、第二个湍流变量和首层网格，才能解释阻力或壁面剪切的变化。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/LES/decayIsoTurb</summary><p>衰减各向同性湍流采用周期边界，nut 由 LES 亚格子模型随流场计算。</p>
<ul>
<li><code>dimensions [0 2 -1 0 0 0 0]</code> 表示运动黏度单位 m²/s。</li>
<li><code>internalField uniform 0</code> 给定亚格子黏度初值。</li>
<li><code>".*"/cyclic</code> 让对应周期面传递一致的场值。</li>
</ul>
<p>更换网格或滤波尺度后，比较能量衰减和 nut 分布，而初始零值只是计算起点。</p>
<p><a href="/assets/examples/v2512/nut/1-nut.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb/0.orig/nut">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      nut;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    &quot;.*&quot;
    {
        type        cyclic;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/fireFoam/LES/simplePMMApanel</summary><p>PMMA 面板火灾算例以零湍流运动黏度开始，再由选定模型更新。</p>
<ul>
<li>nut 的单位为 m²/s，内部初值为 <code>0</code>。</li>
<li>匹配的边界统一采用 <code>zeroGradient</code>。</li>
<li>模型类型、网格尺度和 k 等字段共同决定后续 nut。</li>
</ul>
<p>调整近壁模型时检查 nut 边界是否需要改为对应的壁面函数。</p>
<p><a href="/assets/examples/v2512/nut/2-nut.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel/0.orig/nut">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      nut;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    &quot;.*&quot;
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area</summary><p>带热壳层的热房间采用 nut 壁面函数处理近壁湍流黏度。</p>
<ul>
<li>内部初值为 <code>0</code>，量纲为 m²/s。</li>
<li><code>".*"/nutkWallFunction</code> 对匹配壁面根据 k 等量计算近壁 nut。</li>
<li><code>value uniform 0</code> 提供启动时的边界值。</li>
</ul>
<p>改变壁面分组时核对正则表达式覆盖范围，并结合目标 y⁺ 调整首层网格。</p>
<p><a href="/assets/examples/v2512/nut/3-nut.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area/0/nut">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      nut;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    &quot;.*&quot;
    {
        type            nutkWallFunction;
        value           uniform 0;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
