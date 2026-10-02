---
title: "alpha.water"
layout: reference
description: "水相体积分数场：0 表示无水，1 表示充满水，介于两者之间的值表示部分占据。"
dictionary: true
cms_slug: "dictionary-alpha-water"
---

<p>水相体积分数场：0 表示无水，1 表示充满水，介于两者之间的值表示部分占据。</p><p>位置：<code>0/alpha.water</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-vof-volume-fraction.png" alt="相分数如何表示网格内的界面" loading="lazy"><figcaption><strong>相分数如何表示网格内的界面</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 78 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><p><code>alpha.water</code> 是水相体积分数场。它没有单位：0 表示单元中没有水，1 表示全是水，0 到 1 之间表示水与另一相共存。字段后缀 <code>water</code> 来自相模型中的相名。</p>
<h3>示例：设置初始水区</h3>
<p>先在 <code>0/alpha.water</code> 中准备完整场和边界，再把以下主体写入具有标准字典文件头的 <code>system/setFieldsDict</code>：</p>
<pre><code class="language-foam">defaultFieldValues
(
    volScalarFieldValue alpha.water 0
);
regions
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues
        (
            volScalarFieldValue alpha.water 1
        );
    }
);
</code></pre>
<p>全部单元先设为空气，再把单元中心位于盒内的区域设为水。盒子的两个坐标是对角点，按当前几何单位填写。<code>blockMesh</code> 生成网格后运行 <code>setFields</code>，工具才有可选择的单元。</p>
<p>顶部与空气相通的边界通常需要回流值，例如 <code>inletOutlet</code> 的 <code>inletValue uniform 0</code> 表示外部空气进入。壁面若研究润湿和毛细现象，还需选取适用的接触角条件。</p>
<p>初始化后查看水柱位置，求解中检查相分数范围。域内水体积由 \(V_w=\sum_i\alpha_iV_i\) 得到，可用 <code>volFieldValue</code> 的 <code>volIntegrate</code> 输出。水从开口离开时，体积变化还应与水相边界通量配合解释。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/interFoam/laminar/sloshingTank3D</summary><p>晃荡水箱的这份 alpha.water 是相分数字段模板，水域几何还需由初始化步骤设置。</p>
<ul>
<li>量纲全为零，水体积分数是无量纲量。</li>
<li><code>internalField uniform 0</code> 先把整个域设为非水相，配套 setFields 等步骤再填入水区。</li>
<li>壁面 <code>zeroGradient</code> 让相分数沿法向从内部外推。</li>
</ul>
<p>调整初始液位时修改初始化区域，并在启动前查看 alpha.water 的实际分布及水体积。</p>
<p><a href="/assets/examples/v2512/alpha-water/1-alpha.water.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D/0.orig/alpha.water">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/sloshingTank3D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    walls
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interIsoFoam/sphereInReversedVortexFlow</summary><p>球形界面输运测试先给背景相，再由几何初始化生成球体。</p>
<ul>
<li><code>internalField uniform 0</code> 表示背景中水体积分数为零。</li>
<li><code>sides/fixedValue 0</code> 使外边界保持非水相，与域内球形水相对应。</li>
<li>字段量纲全为零；球心和半径在 setAlphaFieldDict 中给出。</li>
</ul>
<p>放大球体或移动位置时检查它与外边界的距离，以及变形过程是否仍在计算域内。</p>
<p><a href="/assets/examples/v2512/alpha-water/2-alpha.water.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/0.orig/alpha.water">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    sides
    {
        type    fixedValue;
        value   uniform 0;
    }
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/compressibleInterFoam/laminar/waterCooler/fluid</summary><p>waterCooler 的 fluid 区采用二维相分数字段模板。</p>
<ul>
<li><code>internalField uniform 0</code> 给出背景相初值。</li>
<li><code>wall/zeroGradient</code> 按内部相分数延伸到壁面。</li>
<li><code>defaultFaces/empty</code> 与二维网格的前后约束配合。</li>
<li>文件属于 fluid 区，因此初始化与求解应使用对应区域的网格。</li>
</ul>
<p>改变装液高度时修改该区域的初始化设置，并确认没有把其他区域的字段覆盖到 fluid。</p>
<p><a href="/assets/examples/v2512/alpha-water/3-alpha.water.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/waterCooler/fluid/0.orig/alpha.water">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterFoam/laminar/waterCooler/fluid">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      alpha.water;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    wall
    {
        type            zeroGradient;
    }

    defaultFaces
    {
        type            empty;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/interfoam/">interFoam</a> · <a href="/commands/interisofoam/">interIsoFoam</a> · <a href="/commands/setfields/">setFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
