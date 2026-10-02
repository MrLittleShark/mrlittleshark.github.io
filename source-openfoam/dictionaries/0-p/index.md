---
title: "p"
layout: reference
description: "压力标量场。不可压缩求解器常使用运动学压力，可压缩求解器通常使用 Pa。"
dictionary: true
cms_slug: "dictionary-p"
---

<p>压力标量场。不可压缩求解器常使用运动学压力，可压缩求解器通常使用 Pa。</p><p>位置：<code>0/p</code></p><p><code>p</code> 保存压力。字段名相同，但单位由求解器决定：<code>simpleFoam</code>、<code>icoFoam</code> 等常密度不可压缩案例常使用运动学压力；可压缩热物性求解器通常使用 Pa。查看文件的 <code>dimensions</code> 可以区分。</p>
<h3>示例：不可压缩通道压力</h3>
<p>以下片段放在 <code>0/p</code> 的文件头之后，文件头使用 <code>class volScalarField</code> 和 <code>object p</code>。网格具有表中列出的四个 patch。</p>
<pre><code class="language-foam">dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type zeroGradient; }
    outlet { type fixedValue; value uniform 0; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}
</code></pre>
<p><code>[0 2 -2 0 0 0 0]</code> 对应 m²/s²，即物理压力除以恒定密度。出口固定为零，建立压力参考；入口与静止壁面使用此通道案例中的零梯度设置。与给定入口速度配合后，压力分布由动量与连续性求出。</p>
<p>两点压差换算为 Pa 时，使用 \(\Delta p_{\mathrm{Pa}}=\rho\Delta p\)。例如密度为 1000 kg/m³，字段压差 0.2 m²/s² 对应 200 Pa。</p>
<p>可压缩案例的量纲为 <code>[1 -1 -2 0 0 0 0]</code>，理想气体状态方程需要绝对压力，例如 <code>internalField uniform 100000</code>。封闭的不可压缩域如果压力边界全部为梯度型，还需要在相应的 PISO、SIMPLE 或 PIMPLE 设置中指定压力参考。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>不可压缩方腔的 p 是运动学压力，配合速度边界求解压力校正。</p>
<ul>
<li><code>dimensions [0 2 -2 0 0 0 0]</code> 表示 m²/s²，即物理压力除以恒定密度。</li>
<li><code>internalField uniform 0</code> 给出统一初值。</li>
<li>移动顶盖与固定侧壁均采用 <code>zeroGradient</code>；前后面采用 <code>empty</code>。</li>
<li>全域压力缺少固定值边界时，配套 fvSolution 中的 <code>pRefCell 0</code>、<code>pRefValue 0</code> 提供参考。</li>
</ul>
<p>比较物理压差时再乘流体密度；变更开口边界后重新安排压力参考与速度条件。</p>
<p><a href="/assets/examples/v2512/p/1-p.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/0/p">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    movingWall
    {
        type            zeroGradient;
    }

    fixedWalls
    {
        type            zeroGradient;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p>pitzDaily 在出口给定运动学压力参考，让入口速度决定通过流量。</p>
<ul>
<li>压力量纲 <code>[0 2 -2 0 0 0 0]</code>，初值为零。</li>
<li><code>outlet/fixedValue 0</code> 固定出口参考压力。</li>
<li>入口与上下壁面为 <code>zeroGradient</code>，与入口定速、壁面无滑移配合。</li>
<li><code>frontAndBack/empty</code> 保持二维约束。</li>
</ul>
<p>若改为压差驱动，应成组调整入口出口的 p 与 U 条件，并按目标物理问题设置压力值。</p>
<p><a href="/assets/examples/v2512/p/2-p.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/0/p">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    inlet
    {
        type            zeroGradient;
    }

    outlet
    {
        type            fixedValue;
        value           uniform 0;
    }

    upperWall
    {
        type            zeroGradient;
    }

    lowerWall
    {
        type            zeroGradient;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · compressible/rhoSimpleFoam/gasMixing/injectorPipe</summary><p>气体混合喷管使用可压缩求解器，这里的 p 是绝对物理压力。</p>
<ul>
<li>量纲 <code>[1 -1 -2 0 0 0 0]</code> 对应 Pa。</li>
<li><code>internalField uniform 1e5</code> 给出 100000 Pa 初始压力。</li>
<li>出口 <code>fixedValue</code> 通过 <code>$internalField</code> 复用同一个数值，形成给定背压。</li>
<li><code>".*"/zeroGradient</code> 给其他一般边界默认梯度条件，公共 include 处理几何约束类型。</li>
</ul>
<p>改变背压时结合入口总压、温度和气体状态方程检查流动，尤其关注是否发生阻塞或激波。</p>
<p><a href="/assets/examples/v2512/p/3-p.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/gasMixing/injectorPipe/0.orig/p">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/gasMixing/injectorPipe">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform 1e5;

boundaryField
{
    #includeEtc &quot;caseDicts/setConstraintTypes&quot;

    outlet
    {
        type            fixedValue;
        value           $internalField;
    }

    &quot;.*&quot;
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
