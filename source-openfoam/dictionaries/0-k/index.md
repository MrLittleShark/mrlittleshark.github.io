---
title: "k"
layout: reference
description: "湍动能场，表示单位质量流体的速度脉动动能，单位为 m²/s²。"
dictionary: true
cms_slug: "dictionary-k"
---

<p>湍动能场，表示单位质量流体的速度脉动动能，单位为 m²/s²。</p><p>位置：<code>0/k</code></p><p><code>k</code> 是单位质量的湍动能，定义为 \(k=\tfrac12\overline{u_i'u_i'}\)，单位 m²/s²。k–ε 和 k–ω SST 等模型通过它描述速度脉动强度，并与第二个湍流变量共同决定湍流黏度。</p>
<h3>示例：给定入口湍流强度</h3>
<p>平均速度 \(U=10\ \mathrm{m/s}\)、湍流强度 \(I=5\%\)，采用各向同性估算得到 \(k=\tfrac32(UI)^2=0.375\ \mathrm{m^2/s^2}\)。已有 <code>0/k</code> 的入口和壁面可以设置为：</p>
<pre><code class="language-foam">inlet
{
    type  fixedValue;
    value uniform 0.375;
}
wall
{
    type  kqRWallFunction;
    value uniform 0.375;
}
</code></pre>
<p>将这两个块放入 <code>boundaryField</code>，并保留其他 patch 的条件。字段量纲为 <code>[0 2 -2 0 0 0 0]</code>。入口值代表进入计算域的湍流水平；该壁面函数用于相应的壁面处理，<code>value</code> 提供初始字段值。具体近壁策略需与 <code>epsilon</code> 或 <code>omega</code>、<code>nut</code> 以及网格层配合。</p>
<p>保持湍流强度不变而将入口速度减半时，入口 <code>k</code> 变为原来的四分之一。也可以采用 <code>turbulentIntensityKineticEnergyInlet</code>，使入口 <code>k</code> 根据速度和给定强度更新。</p>
<p>运行中反复出现很小的负值并被限制时，应定位异常区域，查看对流格式、初值、回流边界和网格质量。入口湍流参数以实验数据为优先，经验强度用于缺少数据时的估算与敏感性分析。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/pitzDailyExptInlet</summary><p>pitzDailyExptInlet 用实验型入口数据给定非均匀湍动能廓线。</p>
<ul>
<li>列表开头 <code>70</code> 表示 70 个采样值，顺序应与入口 boundaryData 的 points 对应。</li>
<li>k 的单位为 m²/s²，表中包含 <code>2.95219</code>、<code>0.0807476</code> 等不同位置的数值。</li>
<li>这些数据由相应映射入口条件读入，位置和插值方式在配套文件中确定。</li>
</ul>
<p>替换实验廓线时同时更新点坐标及 k、epsilon 等数据，保留采样顺序和单位。</p>
<p><a href="/assets/examples/v2512/k/1-k.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet/constant/boundaryData/inlet/0/k">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDailyExptInlet">案例目录</a></p><pre><code class="language-foam">// Data on points
70
(

//minz
2.95219
2.95219
2.03053
0.578138
0.578138
0.395494
0.395494
0.240375
0.240375
0.178115
0.147052
0.147052
0.134358
0.118537
0.0868366
0.0821937
0.0830451
0.0986349
0.0910976
0.0970347
0.0989484
0.100615
0.101638
0.101436
0.093114
0.0807476
0.091841
0.128637
0.195302
0.188586
0.278105
1.68477
2.52454
3.28528
2.20308

// maxz
2.95219
2.95219
2.03053
0.578138
0.578138
0.395494
0.395494
0.240375
0.240375
0.178115
0.147052
0.147052
0.134358
0.118537
0.0868366
0.0821937
0.0830451
0.0986349
0.0910976
0.0970347
0.0989484
0.100615
0.101638
0.101436
0.093114
0.0807476
0.091841
0.128637
0.195302
0.188586
0.278105
1.68477
2.52454
3.28528
2.20308
)

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/fireFoam/LES/simplePMMApanel</summary><p>simplePMMApanel 的 LES 火灾算例给湍动能字段一个很小的正初值。</p>
<ul>
<li><code>dimensions [0 2 -2 0 0 0 0]</code> 对应 m²/s²。</li>
<li><code>internalField uniform 1e-5</code> 提供启动值，后续变化由所选模型决定。</li>
<li><code>".*"/zeroGradient</code> 为匹配的边界使用零法向梯度。</li>
</ul>
<p>更换湍流模型时检查它是否求解 k，以及壁面和开口条件是否与新的模型相容。</p>
<p><a href="/assets/examples/v2512/k/2-k.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel/0.orig/k">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version         2.0;
    format          ascii;
    class           volScalarField;
    object          k;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 1e-5;

boundaryField
{
    &quot;.*&quot;
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/sprayFoam/aachenBomb</summary><p>aachenBomb 的湍流初场用 k 和 epsilon 共同确定初始湍流尺度。</p>
<ul>
<li><code>internalField uniform 1</code> 给定 k=1 m²/s²。</li>
<li><code>walls/kqRWallFunction</code> 提供相应的近壁处理。</li>
<li>边界 <code>value uniform 1</code> 是该条件所需的初始值。</li>
</ul>
<p>改变湍流强度时与 epsilon 成组调整，并检查喷雾环境的长度与时间尺度。</p>
<p><a href="/assets/examples/v2512/k/3-k.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/k">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      k;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 1;

boundaryField
{
    walls
    {
        type            kqRWallFunction;
        value           uniform 1;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
