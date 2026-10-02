---
title: "U"
layout: reference
description: "速度矢量场，包含速度量纲、内部初值和各个边界的速度条件。"
dictionary: true
cms_slug: "dictionary-u"
---

<p>速度矢量场，包含速度量纲、内部初值和各个边界的速度条件。</p><p>位置：<code>0/U</code></p><p><code>U</code> 是速度向量场，通常保存在 <code>0/U</code>。三个分量按全局 x、y、z 方向排列，单位为 m/s。<code>internalField</code> 给出计算开始时域内的速度，<code>boundaryField</code> 规定各边界的速度。</p>
<h3>示例：通道入口速度为 1 m/s</h3>
<p>下面是一个具有 <code>inlet</code>、<code>outlet</code>、<code>walls</code>、<code>frontAndBack</code> 四个 patch 的二维通道字段。patch 名称需与自己的网格一致。</p>
<pre><code class="language-foam">FoamFile
{
    format ascii;
    class volVectorField;
    object U;
}
dimensions [0 1 -1 0 0 0 0];
internalField uniform (0 0 0);
boundaryField
{
    inlet { type fixedValue; value uniform (1 0 0); }
    outlet { type zeroGradient; }
    walls { type noSlip; }
    frontAndBack { type empty; }
}
</code></pre>
<p><code>volVectorField</code> 表示定义在单元中心的向量场。入口值 <code>(1 0 0)</code> 沿 x 方向；内部初值为零，求解开始后会由方程更新。<code>noSlip</code> 表示静止壁面无滑移，<code>zeroGradient</code> 从出口附近内部单元外推速度。二维前后面采用 <code>empty</code>，网格本身也应满足对应二维要求。</p>
<p>给定入口速度时，通常与入口压力零梯度、出口参考压力配合。已知流量时，可用 <code>flowRateInletVelocity</code>；压力驱动且允许回流的开口，可研究 <code>pressureInletOutletVelocity</code>。运动壁面使用与网格运动或参考系相符的速度条件。</p>
<p>修改入口速度会同时改变流量、雷诺数和 Courant 数。湍流计算保持入口湍流强度时，还需要据此更新 <code>k</code>、<code>epsilon</code> 或 <code>omega</code>。出现 patch 缺失报错时，先对照 <code>constant/polyMesh/boundary</code> 补齐各个边界名称。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>方腔的 U 文件给出静止初场和运动顶盖，流动由顶盖剪切驱动。</p>
<ul>
<li><code>dimensions [0 1 -1 0 0 0 0]</code> 表示速度单位 m/s。</li>
<li><code>internalField uniform (0 0 0)</code> 让腔内流体从静止开始。</li>
<li><code>movingWall/fixedValue (1 0 0)</code> 使顶盖沿 x 以 1 m/s 运动，<code>fixedWalls/noSlip</code> 令其余侧壁速度为零。</li>
<li><code>frontAndBack/empty</code> 对应网格的一层二维结构。</li>
</ul>
<p>顶盖速度改为 2 m/s 后，在相同黏度和尺寸下 Reynolds 数加倍，应同时检查时间步和剪切层分辨率。</p>
<p><a href="/assets/examples/v2512/u/1-U.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/0/U">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volVectorField;
    object      U;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (0 0 0);

boundaryField
{
    movingWall
    {
        type            fixedValue;
        value           uniform (1 0 0);
    }

    fixedWalls
    {
        type            noSlip;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p>后台阶流动由入口速度驱动，墙面形成边界层和台阶后的分离。</p>
<ul>
<li>速度量纲为 m/s，内部初值 <code>(0 0 0)</code> 供稳态迭代起步。</li>
<li><code>inlet/fixedValue (10 0 0)</code> 指定沿 x 的 10 m/s 入口。</li>
<li><code>outlet/zeroGradient</code> 使出口速度从内部外推；出口压力由 p 文件给定。</li>
<li>上下壁面为 <code>noSlip</code>，前后面为 <code>empty</code>。</li>
</ul>
<p>改变入口速度时同步更新湍流入口尺度，并比较回流长度和压降。</p>
<p><a href="/assets/examples/v2512/u/2-U.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/0/U">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volVectorField;
    object      U;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (0 0 0);

boundaryField
{
    inlet
    {
        type            fixedValue;
        value           uniform (10 0 0);
    }

    outlet
    {
        type            zeroGradient;
    }

    upperWall
    {
        type            noSlip;
    }

    lowerWall
    {
        type            noSlip;
    }

    frontAndBack
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common</summary><p>平面 Poiseuille 模板先规定静止流体和无滑移壁面，再由配套驱动力形成通道流动。</p>
<ul>
<li><code>internalField uniform (0 0 0)</code> 给出静止初值。</li>
<li><code>wall/fixedValue (0 0 0)</code> 约束壁面速度为零。</li>
<li><code>#includeEtc "caseDicts/setConstraintTypes"</code> 引入周期、empty 等几何约束边界的公共写法。</li>
<li>速度量纲为 <code>[0 1 -1 0 0 0 0]</code>。</li>
</ul>
<p>改变壁面运动或通道驱动时同时查看源项与压力设置；从零初场发展到目标剖面需要相应计算时间。</p>
<p><a href="/assets/examples/v2512/u/3-U.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common/0.orig/U">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volVectorField;
    object      U;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (0 0 0);

boundaryField
{
    wall
    {
        type            fixedValue;
        value           uniform (0 0 0);
    }

    #includeEtc &quot;caseDicts/setConstraintTypes&quot;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
