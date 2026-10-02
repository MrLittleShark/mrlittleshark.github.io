---
title: "regionProperties"
layout: reference
description: "列出多区域计算中的流体区和固体区，用于组织各区域的网格、物性和场。"
dictionary: true
cms_slug: "dictionary-regionproperties"
---

<p>列出多区域计算中的流体区和固体区，用于组织各区域的网格、物性和场。</p><p>位置：<code>constant/regionProperties</code></p><h2>regionProperties 列出多区域计算的区域</h2>
<p><code>constant/regionProperties</code> 用于多区域求解器，指定哪些网格区域属于流体，哪些属于固体。共轭传热中，流体求解流动和能量，固体求解导热，再通过界面交换热量。</p>
<p>以下主体来自多区域加热教程，放在标准文件头之后：</p>
<pre><code class="language-foam">regions
(
    fluid (bottomWater topAir)
    solid (heater leftSolid rightSolid)
);
</code></pre>
<p><code>bottomWater</code> 和 <code>topAir</code> 是两个流体区域，<code>heater</code>、<code>leftSolid</code>、<code>rightSolid</code> 是三个固体区域。括号中保存区域名列表，名称应与实际网格及文件夹一致。</p>
<h3>每个区域对应哪些文件</h3>
<p>以 <code>topAir</code> 为例，常见目录为：</p>
<pre><code class="language-text">constant/topAir/polyMesh/
constant/topAir/thermophysicalProperties
constant/topAir/turbulenceProperties
0/topAir/U
0/topAir/p_rgh
0/topAir/T
system/topAir/fvSchemes
system/topAir/fvSolution
</code></pre>
<p>固体区域通常有温度和热物性，流动及湍流字段由区域物理决定。各区域可以有不同的网格尺度和材料，但共同参与一次多区域计算。</p>
<p><code>regionProperties</code> 负责登记区域，网格由前处理步骤建立。例如已经划分好 <code>cellZone</code> 时，可在对应完整流程中使用 <code>splitMeshRegions</code> 将各区拆分为独立区域网格。命令参数和初场映射应与原始区域划分方式配合。</p>
<h3>区域之间怎样交换热量</h3>
<p>流固界面需要成对的 patch 和耦合温度边界。理想接触界面满足温度连续和法向热流平衡；具有接触热阻时则按相应边界模型允许温度跳变。</p>
<p>因此，添加一个新固体区域时需要准备三部分：区域网格，材料及初场，界面耦合关系。随后把名称加入 <code>solid (...)</code>，将完整的新区域交给求解器处理。</p>
<h3>检查某个区域</h3>
<pre><code class="language-bash">checkMesh -region topAir
foamDictionary constant/topAir/thermophysicalProperties -entry thermoType
</code></pre>
<p>第一条检查指定区域网格，第二条查看该区域采用的物性组合。逐区检查能区分全局配置错误和局部材料或边界问题。后处理可选择各区域分别查看温度，也可同时显示界面两侧，比较热流和温度连续性。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid</summary><p>jouleHeatingSolid 虽使用多区域框架，这份区域清单只包含一个固体区。</p>
<ul>
<li><code>fluid ()</code> 表示没有列出的流体区域。</li>
<li><code>solid (solid)</code> 指定名为 solid 的固体区域，网格、场和物性目录需使用同名。</li>
<li>电势、导热及焦耳热源相关设置应在该固体区域中对应。</li>
</ul>
<p>增加流体冷却域时，把新区域列入 fluid 并补齐其网格、物性和耦合边界。</p>
<p><a href="/assets/examples/v2512/regionproperties/1-regionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid/constant/regionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      regionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

regions
(
    fluid   ()
    solid   (solid)
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/heatExchanger</summary><p>heatExchanger 在此把 air 和 porous 两个区域都列为流体处理。</p>
<ul>
<li><code>fluid (air porous)</code> 决定要创建和求解的流体区。</li>
<li><code>solid ()</code> 没有列出独立固体区域；名称 porous 本身不会把区域变成固体导热模型。</li>
<li>各区还需要分别给出物性、阻力或其他模型设置。</li>
</ul>
<p>增加实际金属固体时建立对应网格和温度耦合，再把区域列到 solid 列表。</p>
<p><a href="/assets/examples/v2512/regionproperties/2-regionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/heatExchanger/constant/regionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/heatExchanger">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      regionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

regions
(
    fluid   (air porous)
    solid   ()
);


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/chtMultiRegionFoam/reverseBurner</summary><p>reverseBurner 将气体与固体分开求解，并通过界面交换热量。</p>
<ul>
<li><code>fluid (gas)</code> 指定气体流动区。</li>
<li><code>solid (solid)</code> 指定固体导热区。</li>
<li>两类区域名决定 constant、system 和时间目录中相关子目录的对应关系。</li>
</ul>
<p>新增区域时同时补齐区域清单、网格、各场边界与热物性，尤其要核对界面双方名称。</p>
<p><a href="/assets/examples/v2512/regionproperties/3-regionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/reverseBurner/constant/regionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/reverseBurner">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      regionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

regions
(
    fluid       (gas)
    solid       (solid)
);


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/chtmultiregionfoam/">chtMultiRegionFoam</a> · <a href="/commands/splitmeshregions/">splitMeshRegions</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
