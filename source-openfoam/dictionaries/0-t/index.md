---
title: "T"
layout: reference
description: "温度场，以 K 为单位，包含内部初始温度和温度边界条件。"
dictionary: true
cms_slug: "dictionary-t"
---

<p>温度场，以 K 为单位，包含内部初始温度和温度边界条件。</p><p>位置：<code>0/T</code></p><p><code>T</code> 是温度标量场，单位为 K。它常由能量方程与热物性关系共同确定；在共轭传热中，各 region 分别保存自己的温度，例如 <code>0/fluid/T</code> 和 <code>0/solid/T</code>。</p>
<h3>示例：热流体入口与绝热壁面</h3>
<p>在已有 <code>0/T</code> 中保留标准场文件头，设置以下内容。网格包含 <code>inlet</code>、<code>outlet</code> 和 <code>walls</code> 三个 patch。</p>
<pre><code class="language-foam">dimensions [0 0 0 1 0 0 0];
internalField uniform 300;
boundaryField
{
    inlet
    {
        type fixedValue;
        value uniform 350;
    }
    outlet
    {
        type inletOutlet;
        inletValue uniform 300;
        value uniform 300;
    }
    walls
    {
        type zeroGradient;
    }
}
</code></pre>
<p>入口固定 350 K，内部初始为 300 K；出口正常流出时外推内部温度，回流时带入 300 K 的外界流体。对于此处的普通导热边界，<code>zeroGradient</code> 表示法向温度梯度为零，对应绝热壁面。</p>
<p>固定壁温可将壁面改为 <code>fixedValue</code>；给定功率、热流或外部换热时，可以研究 <code>externalWallHeatFluxTemperature</code>。流固界面则使用温度耦合条件，并从两侧热物性读取导热系数。</p>
<p>温度输入采用 K，摄氏度转换为 \(T_K=T_{\mathrm C}+273.15\)。若温度异常，除了边界值，还需检查能量变量、比热容、导热系数和发热源单位。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common</summary><p>这是大气边界层入口 boundaryData 中的温度采样表，数据与同目录体系中的采样点一一对应。</p>
<ul>
<li>表中温度值全部为 <code>300</code>，给定 300 K 的均匀入口温度分布。</li>
<li>外层括号保存标量列表；位置由配套 points 文件提供，而不是由列表本身给出。</li>
<li>路径中的时间目录 <code>0</code> 表示这一组边界采样数据的时刻，后续可增加其他时刻供时间插值。</li>
</ul>
<p>引入温度廓线时保持点数和顺序相容，并按采样点高度填写对应温度。</p>
<p><a href="/assets/examples/v2512/t/1-T.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common/constant/boundaryData/p1/0/T">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common">案例目录</a></p><pre><code class="language-foam">(
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
300
)</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection</summary><p>VOF 转拉格朗日液滴示例提供 293 K 的温度字段，供相关相或颗粒热量设置使用。</p>
<ul>
<li><code>dimensions [0 0 0 1 0 0 0]</code> 表示 K。</li>
<li><code>internalField uniform 293</code> 给全域统一初温。</li>
<li><code>walls/zeroGradient</code> 使用零法向温度梯度。</li>
<li>具体温度如何参与计算还由所选连续相与云热模型决定。</li>
</ul>
<p>需要冷热液滴交换时同步设置连续相初温、注入温度和传热模型。</p>
<p><a href="/assets/examples/v2512/t/2-T.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection/0.orig/T">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/vofToLagrangian/lagrangianDistributionInjection">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      T;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 1 0 0 0];

internalField   uniform 293;

boundaryField
{
    walls
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · lagrangian/sprayFoam/aachenBomb</summary><p>aachenBomb 模拟向高温环境喷雾，初始气体温度在这里给定。</p>
<ul>
<li><code>internalField uniform 800</code> 表示环境温度 800 K。</li>
<li>温度量纲为 K；壁面采用 <code>zeroGradient</code>。</li>
<li>这组温度与箱内压力、气体组分共同决定环境密度和液滴蒸发条件。</li>
</ul>
<p>改变环境温度时同步检查热物性有效范围，并比较液滴蒸发、穿透和温度变化。</p>
<p><a href="/assets/examples/v2512/t/3-T.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb/0.orig/T">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/sprayFoam/aachenBomb">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      T;
}
// ************************************************************************* //

dimensions          [0 0 0 1 0 0 0];

internalField       uniform 800;

boundaryField
{
    walls
    {
        type                zeroGradient;
    }
}

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/laplacianfoam/">laplacianFoam</a> · <a href="/commands/chtmultiregionfoam/">chtMultiRegionFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown patchField / patch type mismatch</td><td>同时检查网格 patch 类型与场边界类型，例如 empty 网格面应使用相容的场条件。</td></tr><tr><td>速度与压力约束不相容</td><td>在入口、出口和封闭壁面共同考虑通量约束与压力参考。</td></tr><tr><td>湍流场出现非法值</td><td>检查 k、epsilon、omega 等场的正性及壁面函数适用范围，不能以截断代替模型诊断。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
