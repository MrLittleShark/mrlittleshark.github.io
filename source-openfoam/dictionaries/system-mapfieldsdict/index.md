---
title: "mapFieldsDict"
layout: reference
description: "配置两个算例之间的边界映射，用于将已有结果转移到另一套网格。"
dictionary: true
cms_slug: "dictionary-mapfieldsdict"
---

<p>配置两个算例之间的边界映射，用于将已有结果转移到另一套网格。</p><p>位置：<code>system/mapFieldsDict</code></p><h2>配置实例</h2><p>mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object mapFieldsDict;
}
patchMap
(
    inlet sourceInlet
    outlet sourceOutlet
);
cuttingPatches (newCutBoundary);</code></pre>
<p>在目标算例中执行 mapFields ../sourceCase -sourceTime latestTime。cuttingPatches 指定切穿源计算域的目标边界，其数值由源域内部插值得到。-consistent 适用于边界拓扑匹配的算例。映射体积分数等守恒量后，应检查有界性及积分守恒。</p>
<h2>17.9 mapFieldsDict</h2><pre><code class="language-openfoam">patchMap        ( inlet1 inlet );   // 源算例 patch → 目标算例 patch
cuttingPatches  ( outlet );         // 被切开的 patch（源网格不覆盖的部分）</code></pre>
<p>网格边界一致时可以完全不用这个文件，直接 mapFields ../src -consistent。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavityGrade</summary><p>cavityGrade 用较粗或不同分布的方腔结果初始化新网格。</p>
<ul>
<li><code>patchMap ()</code> 没有额外列出需要配对的边界名称。</li>
<li><code>cuttingPatches ()</code> 表示没有指定穿过源域内部的新切割边界。</li>
<li>此配置只补充映射规则，源算例路径、源时刻和映射方法由 mapFields 的调用确定。</li>
</ul>
<p>两份网格边界完全对应时可结合一致映射用法；若边界改名或目标域被裁切，需要补充相应列表。</p>
<p><a href="/assets/examples/v2512/mapfieldsdict/1-mapFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityGrade/system/mapFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityGrade">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       dictionary;
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap        ( );

cuttingPatches  ( );


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common</summary><p>大气边界层 successor 区从已有流场取得初值，同时处理 terrain 和 top 这两类切割边界。</p>
<ul>
<li><code>patchMap ()</code> 未建立额外名称映射。</li>
<li><code>cuttingPatches (terrain top)</code> 把这两个目标边界作为切割面处理，取值需要从源场内部插值。</li>
<li>坐标、地形位置和源场覆盖范围应与目标区域一致。</li>
</ul>
<p>更换 successor 范围后先检查源域能否覆盖目标网格，再调整切割边界清单。</p>
<p><a href="/assets/examples/v2512/mapfieldsdict/2-mapFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common/system/mapFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       dictionary;
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap ( );

cuttingPatches
(
    terrain top
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/icoFoam/cavity/cavityClipped</summary><p>cavityClipped 的目标边界名与源方腔不同，因此需要一项名称对应。</p>
<ul>
<li><code>patchMap (lid movingWall)</code> 将目标 lid 与源 movingWall 配对。</li>
<li><code>cuttingPatches ()</code> 没有另外列出切割边界。</li>
<li>映射时还需提供源算例和相应结果时刻，字典不会自动选择数据来源。</li>
</ul>
<p>目标边界继续改名时同步更新配对；执行后查看顶盖速度与其他边界是否仍符合目标问题。</p>
<p><a href="/assets/examples/v2512/mapfieldsdict/3-mapFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityClipped/system/mapFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavityClipped">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       dictionary;
    object      mapFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

patchMap        (lid movingWall);

cuttingPatches  ();


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mapfields/">mapFields</a> · <a href="/commands/mapfieldspar/">mapFieldsPar</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
