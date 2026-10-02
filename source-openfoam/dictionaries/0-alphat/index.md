---
title: "alphat"
layout: reference
description: "湍流热扩散相关系数字段。常见可压缩热物性模型采用 kg/(m·s) 量纲，按求解器的热输运定义配置。"
dictionary: true
cms_slug: "dictionary-alphat"
---

<p>湍流热扩散相关系数字段。常见可压缩热物性模型采用 kg/(m·s) 量纲，按求解器的热输运定义配置。</p><p>位置：<code>0/alphat</code></p><p><code>alphat</code> 描述湍流引起的能量扩散。在常见可压缩能量模型中，其定义为 \(\alpha_t=\mu_t/Pr_t\)，量纲与动力黏度相同，为 kg/(m·s)。<code>Prt</code> 是湍流 Prandtl 数，用于联系动量与热量的湍流输运。</p>
<h3>示例：可压缩传热壁面</h3>
<p>在使用该热物性接口的 <code>0/alphat</code> 中，字段量纲为 <code>[1 -1 -1 0 0 0 0]</code>。下列块放入其 <code>boundaryField</code>，将 <code>heatedWall</code> 换成实际壁面名称：</p>
<pre><code class="language-foam">heatedWall
{
    type  compressible::alphatWallFunction;
    Prt   0.85;
    value uniform 0;
}
</code></pre>
<p>该条件根据湍流黏度和 <code>Prt</code> 计算壁面热扩散。<code>value</code> 为初始读取值；<code>Prt=0.85</code> 是这一壁面函数的常见默认设置。保持其他量不变时，减小 <code>Prt</code> 会增大湍流能量扩散，进而影响温度梯度和换热。</p>
<p>内部 <code>alphat</code> 由模型更新，入口和出口通常采用与该模型匹配的 <code>calculated</code> 等条件。热壁面处理还可采用具有更详细近壁温度规律的条件，需与 y⁺、温度边界和湍流模型配套。</p>
<p>不同能量接口可能使用不同定义，读取实际文件量纲后再解释数值。分析换热系数时，还需要明确参考温度和热流方向；仅修改 <code>alphat</code> 的初始值通常不会永久改变模型计算出的湍流热扩散。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area</summary><p>热房间的 alphat 表示能量方程使用的湍流热扩散系数。</p>
<ul>
<li>量纲 <code>[1 -1 -1 0 0 0 0]</code> 对应 kg/(m·s)，采用包含密度的形式。</li>
<li>内部初值为 <code>0</code>。</li>
<li><code>compressible::alphatWallFunction</code> 使壁面热扩散与相应湍流壁面处理一致。</li>
</ul>
<p>更改热壁面或湍流 Prandtl 数时，同时检查温度边界与模型参数对壁面热流的影响。</p>
<p><a href="/assets/examples/v2512/alphat/1-alphat.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area/0/alphat">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantPimpleFoam/hotRoomWithThermalShell.multi-area">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alphat;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    &quot;.*&quot;
    {
        type            compressible::alphatWallFunction;
        value           uniform 0;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · lagrangian/sprayFoam/aachenBomb</summary><p>aachenBomb 用 alphat 壁面函数连接湍流动量输运与热量输运。</p>
<ul>
<li><code>internalField uniform 0</code> 给出启动值。</li>
<li>量纲为 kg/(m·s)，与该可压缩能量方程的热扩散形式一致。</li>
<li><code>walls/compressible::alphatWallFunction</code> 提供壁面热扩散处理。</li>
</ul>
<p>更换传热或湍流模型时检查 alphat、nut 和温度边界是否成套匹配。</p>
<p><a href="/assets/examples/v2512/alphat/2-alphat.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/alphat">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alphat;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    walls
    {
        type            compressible::alphatWallFunction;
        value           uniform 0;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/chtMultiRegionFoam/snappyMultiRegionHeaterImplicit</summary><p>snappyMultiRegionHeaterImplicit 的 alphat 是多区域初始场模板。</p>
<ul>
<li>内部初值为 <code>0</code>，量纲为 kg/(m·s)。</li>
<li>公共 <code>setConstraintTypes</code> 先设置几何约束边界。</li>
<li>其他匹配边界采用 <code>calculated</code>，初值由 <code>$internalField</code> 引用，后续由模型或区域准备流程确定。</li>
</ul>
<p>查看实际生成区域的字段，确认流固界面、壁面与开口已采用合适的最终条件。</p>
<p><a href="/assets/examples/v2512/alphat/3-alphat.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/snappyMultiRegionHeaterImplicit/0.orig/alphat">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/snappyMultiRegionHeaterImplicit">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alphat;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -1 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    #includeEtc &quot;caseDicts/setConstraintTypes&quot;

    &quot;.*&quot;
    {
        type    calculated;
        value   $internalField;
    }
}

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/buoyantsimplefoam/">buoyantSimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界条件未识别，或与网格边界类型不匹配：<code>Unknown patchField / patch type mismatch</code></td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
