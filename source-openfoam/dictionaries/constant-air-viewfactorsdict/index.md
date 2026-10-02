---
title: "viewFactorsDict"
layout: reference
description: "辐射视角因子预处理的配置，用于表面间辐射交换。"
dictionary: true
cms_slug: "dictionary-viewfactorsdict"
---

<p>辐射视角因子预处理的配置，用于表面间辐射交换。</p><p>位置：<code>constant/air/viewFactorsDict</code></p><h2>配置实例</h2><p>heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation 中的 viewFactorsDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      viewFactorsDict;
}

writeViewFactorMatrix     true;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation</summary><p>multiRegionHeaterRadiation 的 topAir 区域通过视角系数描述表面间的辐射交换，本文件控制预处理结果的输出。</p>
<ul>
<li><code>writeViewFactorMatrix true</code> 保存视角系数矩阵，矩阵元素表示某个表面发出的辐射到达另一表面的几何比例。</li>
<li>实际参加交换的表面由辐射模型、边界配置及面聚合结果共同确定。</li>
</ul>
<p>改变遮挡关系或网格表面后应重新生成视角系数；可检查封闭系统的行和与面积互易关系判断几何计算是否合理。</p>
<p><a href="/assets/examples/v2512/viewfactorsdict/1-viewFactorsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation/constant/topAir/viewFactorsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/multiRegionHeaterRadiation">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      viewFactorsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

writeViewFactorMatrix     true;

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionFoam/externalSolarLoad</summary><p>externalSolarLoad 在 air 区域生成视角系数，并把辐射壁面聚合成较少的面组以降低几何求交成本。</p>
<ul>
<li><code>patchAgglomeration/viewFactorWall</code> 选择辐射壁面，<code>nFacesInCoarsestLevel 10</code> 指定最粗聚合层的目标面数。</li>
<li><code>featureAngle 45</code> 限制跨越明显几何折角的聚合，有助于保留表面朝向变化。</li>
<li><code>writeFacesAgglomeration true</code> 保存聚合分区，<code>writeViewFactorMatrix true</code> 保存视角系数矩阵。</li>
<li><code>writePatchViewFactors false</code> 关闭 patch 级结果输出，<code>maxDynListLength 200000</code> 设置相关动态列表的容量上限。</li>
</ul>
<p>先显示聚合面组确认遮挡边缘和折角仍有足够分辨率，再比较更细聚合下的辐射热流。</p>
<p><a href="/assets/examples/v2512/viewfactorsdict/2-viewFactorsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalSolarLoad/constant/air/viewFactorsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/externalSolarLoad">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      viewFactorsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


writeViewFactorMatrix       true;
writePatchViewFactors       false;

// Write rays as lines to .obj file
//dumpRays                    true;


// Switch on debug for faceAgglomerate
//debug                       1;
writeFacesAgglomeration     true;
patchAgglomeration
{
    // Do all of the view-factor patches
    viewFactorWall
    {
        nFacesInCoarsestLevel   10;
        featureAngle            45;
    }
}

maxDynListLength          200000;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/annotated</summary><p>这个注释模板控制辐射面的聚合及射线调试输出，示例边界为 bottomAir_to_heater。</p>
<ul>
<li><code>nFacesInCoarsestLevel 30</code> 设置该边界在最粗层的目标面数，<code>featureAngle 10</code> 对折角采用较严格的聚合条件。</li>
<li><code>writeFacesAgglomeration true</code> 输出各面所属聚合组，便于在可视化中检查。</li>
<li><code>debug 0</code>、<code>dumpRays false</code> 保持常规输出规模；分析遮挡或射线问题时可按工具支持的选项开启调试。</li>
</ul>
<p>迁移到其他加热器时替换边界名，并根据曲率、遮挡物尺寸和表面温度变化选择聚合尺度。</p>
<p><a href="/assets/examples/v2512/viewfactorsdict/3-viewFactorsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/viewFactorsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      viewFactorsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Write agglomeration as a volScalarField with calculated boundary values
writeFacesAgglomeration   true;

//Debug option
debug                     0;

//Dump connectivity rays
dumpRays                  false;

// Per patch (wildcard possible) the coarsening level
bottomAir_to_heater
{
    nFacesInCoarsestLevel     30;
    featureAngle              10;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/viewfactorsgen/">viewFactorsGen</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
