---
title: "p_rgh"
layout: reference
description: "扣除静水压项后的压力场，常用于浮力和多相流求解器。"
dictionary: true
cms_slug: "dictionary-p-rgh"
---

<p>扣除静水压项后的压力场，常用于浮力和多相流求解器。</p><p>位置：<code>0/p_rgh</code></p><p><code>p_rgh</code> 是扣除重力静压项后的压力变量，常见于自由液面和浮力传热案例：</p>
<p>\[
p_{rgh}=p-\rho gh.
\]</p>
<p><code>gh</code> 由重力与位置构成，并包含求解器所采用的高度参考。密度在水和空气间相差很大时，分离重力静压项有利于压力方程的处理。<code>p_rgh</code> 的单位随具体求解器约定，<code>interFoam</code> 的此字段以 Pa 表示。</p>
<h3>示例：interFoam 的壁面和大气开口</h3>
<p>在已有 <code>0/p_rgh</code> 的 <code>boundaryField</code> 内，为相应的 <code>wall</code> 和 <code>atmosphere</code> patch 设置：</p>
<pre><code class="language-foam">wall
{
    type  fixedFluxPressure;
    value uniform 0;
}
atmosphere
{
    type totalPressure;
    p0   uniform 0;
}
</code></pre>
<p><code>fixedFluxPressure</code> 通过压力梯度与速度边界要求的通量配合，适用于该溃坝案例的无穿透壁面。<code>totalPressure</code> 用于案例中的开口压力处理，<code>p0</code> 为所选压力基准下的总压值。与之配套，开口的 <code>U</code> 使用 <code>pressureInletOutletVelocity</code>，相分数使用允许空气回流的 <code>inletOutlet</code>。</p>
<p>查看真实压力时，应使用求解器输出的 <code>p</code>，或按相同密度与高度参考重建静压。将 <code>p_rgh</code> 直接当作传感器测得的静压，会遗漏高度项。自建浮力或自由液面出口时，还可以研究 <code>prghPressure</code>、<code>prghTotalPressure</code> 等条件，它们的参数与压力转换需按所选求解器配套。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interFoam/laminar/sloshingTank3D</summary><p>晃荡水箱求解扣除静水头后的压力 p_rgh，使重力与压力梯度更方便配合。</p>
<ul>
<li>量纲为 Pa，<code>internalField uniform 0</code> 设置初始 p_rgh。</li>
<li><code>walls/fixedFluxPressure</code> 根据壁面速度通量设置相应压力梯度。</li>
<li>重构实际压力还需要密度、重力方向与重力势参考，关系由求解器处理。</li>
</ul>
<p>改变水深或容器运动时，保持 p_rgh、相分数、重力与壁面速度条件相容。</p>
<p><a href="/assets/examples/v2512/p-rgh/1-p_rgh.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D/0.orig/p_rgh">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p_rgh;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    walls
    {
        type            fixedFluxPressure;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interIsoFoam/sphereInReversedVortexFlow</summary><p>反向涡流中的球形界面测试把外边界 p_rgh 设为统一参考值。</p>
<ul>
<li><code>dimensions [1 -1 -2 0 0 0 0]</code> 表示压力单位 Pa。</li>
<li>内部初值为 0，<code>sides/fixedValue</code> 同样固定为 0。</li>
<li>这与配套给定速度场、界面输运测试共同组成问题。</li>
</ul>
<p>更换为封闭容器时重新选择压力边界和参考设置，而球形相区的几何仍由初始化文件决定。</p>
<p><a href="/assets/examples/v2512/p-rgh/2-p_rgh.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/0.orig/p_rgh">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p_rgh;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    sides
    {
        type    fixedValue;
        value   uniform 0;
    }
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/reactingParcelFoam/movingInjectorBox</summary><p>movingInjectorBox 为颗粒注入的连续相建立 p_rgh 初值和封闭壁面条件。</p>
<ul>
<li><code>internalField uniform 100000</code> 给定 100000 Pa 的初始 p_rgh。</li>
<li>量纲为 Pa，实际物理压力还包含求解器的重力势与密度处理。</li>
<li><code>walls/fixedFluxPressure</code> 与壁面通量对应，保持压力梯度和速度约束一致。</li>
</ul>
<p>改变初始热力状态时同时调整温度与热物性，检查密度是否符合预期。</p>
<p><a href="/assets/examples/v2512/p-rgh/3-p_rgh.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox/0/p_rgh">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/movingInjectorBox">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;0&quot;;
    object      p_rgh;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 100000;

boundaryField
{
    walls
    {
        type            fixedFluxPressure;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/interfoam/">interFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
