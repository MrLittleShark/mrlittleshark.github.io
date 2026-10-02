---
title: "PDRsetFieldsDict"
layout: reference
description: "PDR 专用预处理工具的输入，用于把障碍物几何等信息转换为模型所需场。"
dictionary: true
cms_slug: "dictionary-pdrsetfieldsdict"
---

<p>PDR 专用预处理工具的输入，用于把障碍物几何等信息转换为模型所需场。</p><p>位置：<code>system/PDRsetFieldsDict</code></p><h2>配置实例</h2><p>combustion/PDRFoam/pipeLattice 中的 PDRsetFieldsDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      PDRsetFieldsDict;
}

// Data dictionary for PDRsetFields

// Replace by the relevant names

obsFileDir      &quot;&lt;case&gt;/geometry&quot;;

obsFileNames    (obstaclesDict);

// ------------------
// PDRfitMesh
// ------------------

// Some parameters for PDRfitMesh are read from this file,
// including the following

// Mandatory (here or in PDRfitMeshDict)
cellWidth       0.22;

// Optional
cellWidthFactor 1.0;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/PDRFoam/pipeLattice</summary><p>PDRsetFields 根据管阵列的几何描述生成孔隙率、阻塞程度等 PDR 输入场。</p>
<ul>
<li><code>obsFileDir "&lt;case&gt;/geometry"</code> 将障碍物目录定位到当前算例的 geometry 文件夹。</li>
<li><code>obsFileNames (obstaclesDict)</code> 指定要读取的几何描述文件，多个文件可放在同一列表中。</li>
<li><code>cellWidth 0.22</code> 与 <code>cellWidthFactor 1</code> 给出该预处理使用的网格尺度参数，单位应与障碍物几何一致。</li>
</ul>
<p>改变管径、间距或网格后重新运行预处理，并查看生成的孔隙率与阻塞场，确认管阵列位置和尺寸与输入几何一致。</p>
<p><a href="/assets/examples/v2512/pdrsetfieldsdict/1-PDRsetFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice/system/PDRsetFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/PDRFoam/pipeLattice">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRsetFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Data dictionary for PDRsetFields

// Replace by the relevant names

obsFileDir      &quot;&lt;case&gt;/geometry&quot;;

obsFileNames    (obstaclesDict);


// ------------------
// PDRfitMesh
// ------------------

// Some parameters for PDRfitMesh are read from this file,
// including the following

// Mandatory (here or in PDRfitMeshDict)
cellWidth       0.22;

// Optional
cellWidthFactor 1.0;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · preProcessing/PDRsetFields/simplePipeCage</summary><p>simplePipeCage 用几何文件描述管架，再将其影响写入 PDR 场。这个字典还给出预处理时使用的外边界名称。</p>
<ul>
<li>障碍物从 <code>&lt;case&gt;/geometry/obstaclesDict</code> 读取；<code>&lt;case&gt;</code> 随当前算例位置展开，复制整个算例后仍能找到几何文件。</li>
<li><code>cellWidth 0.22</code>、<code>cellWidthFactor 1</code> 设置预处理的尺度参数。</li>
<li><code>patchNames</code> 中 <code>ground ground</code>、<code>outer outer</code> 把预处理的地面和外边界角色对应到实际网格边界。</li>
</ul>
<p>如果网格中地面改名为 floor，应同步修改这里的对应值；随后检查生成场在地面附近和管架内部的分布。</p>
<p><a href="/assets/examples/v2512/pdrsetfieldsdict/2-PDRsetFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage/system/PDRsetFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/PDRsetFields/simplePipeCage">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      PDRsetFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Data dictionary for PDRsetFields

// Replace by the relevant names

obsFileDir      &quot;&lt;case&gt;/geometry&quot;;

obsFileNames    (obstaclesDict);


// ------------------
// PDRfitMesh
// ------------------

// Some parameters for PDRfitMesh are read from this file,
// including the following

// Mandatory (here or in PDRfitMeshDict)
cellWidth       0.22;

// Optional
cellWidthFactor 1.0;


// ------------------
// Advanced
// ------------------

// Change some predefined patch names
patchNames
{
    ground      ground;
    outer       outer;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/pdrsetfields/">PDRsetFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
