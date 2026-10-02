---
title: "surfaceFeatureExtractDict"
layout: reference
description: "从三角化表面提取棱边，生成 snappyHexMesh 使用的 eMesh 特征线文件。"
dictionary: true
cms_slug: "dictionary-surfacefeatureextractdict"
---

<p>从三角化表面提取棱边，生成 snappyHexMesh 使用的 eMesh 特征线文件。</p><p>位置：<code>system/surfaceFeatureExtractDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object surfaceFeatureExtractDict;
}
body.stl
{
    extractionMethod extractFromSurface;
    extractFromSurfaceCoeffs { includedAngle 150; }
    writeObj yes;
}</code></pre>
<p>输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMesh 文件名用于后续特征线配置。</p>
<h2>17.7 surfaceFeatureExtractDict</h2><pre><code class="language-openfoam">body.stl
{
    extractionMethod    extractFromSurface;
    includedAngle       150;          // 夹角超过它的棱视为特征边
    subsetFeatures      { nonManifoldEdges no; openEdges yes; }
    writeObj            yes;          // 输出 obj 方便在 ParaView 里检查
}</code></pre>
<p>includedAngle 越大，提取的边越多。150 是常用起点：太小会漏掉圆角过渡处的特征，太大会把曲面上的三角片棱也当成特征。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/windAroundBuildings</summary><p>建筑绕流先提取 buildings.obj 的尖锐特征边，供后续网格贴合使用。</p>
<ul>
<li>外层键 <code>buildings.obj</code> 指定处理的表面文件。</li>
<li><code>#includeEtc "caseDicts/surface/surfaceFeatureExtractDict.cfg"</code> 引入安装目录中的默认提取设置，当前文件没有另行覆盖夹角等参数。</li>
<li>产生的特征文件需要在 snappyHexMesh 的 <code>features</code> 中对应引用。</li>
</ul>
<p>更换建筑几何后重新提取；要调整识别敏感度，可在该子字典中覆盖 includedAngle，并查看提取出的边。</p>
<p><a href="/assets/examples/v2512/surfacefeatureextractdict/1-surfaceFeatureExtractDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/windAroundBuildings/system/surfaceFeatureExtractDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/windAroundBuildings">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

buildings.obj
{
    #includeEtc &quot;caseDicts/surface/surfaceFeatureExtractDict.cfg&quot;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/overInterDyMFoam/rigidBodyHull/overset-1</summary><p>船体重叠网格中的 HULL.obj 需要保留棱边特征，避免贴合时抹平重要几何。</p>
<ul>
<li><code>extractionMethod extractFromSurface</code> 直接从三角表面提取特征。</li>
<li><code>includedAngle 150</code> 设置特征边夹角阈值，控制哪些几何折转进入特征集合。</li>
<li><code>writeObj yes</code> 额外输出可视化文件，便于检查提取结果。</li>
</ul>
<p>改变船体离散精度或夹角阈值后，在几何查看器中检查关键棱边是否连续，再更新网格。</p>
<p><a href="/assets/examples/v2512/surfacefeatureextractdict/2-surfaceFeatureExtractDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/overset-1/system/surfaceFeatureExtractDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/rigidBodyHull/overset-1">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

HULL.obj
{
    extractionMethod extractFromSurface;
    writeObj        yes;

    extractFromSurfaceCoeffs
    {
        includedAngle   150;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</summary><p>cpuCabinet 的 MRF_region.obj 定义需要保留几何特征的区域表面，提取结果用于相关网格生成步骤。</p>
<ul>
<li><code>extractFromSurface</code> 从已有表面得到特征边。</li>
<li><code>includedAngle 150</code> 用几何夹角区分平滑连接和特征。</li>
<li><code>writeObj yes</code> 输出可视化数据，方便对照原表面检查。</li>
</ul>
<p>更改风扇区域尺寸或位置后重新生成特征，确保 snappyHexMesh 引用的文件与几何一致。</p>
<p><a href="/assets/examples/v2512/surfacefeatureextractdict/3-surfaceFeatureExtractDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/system/surfaceFeatureExtractDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      surfaceFeatureExtractDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF_region.obj
{
    extractionMethod extractFromSurface;
    writeObj        yes;

    extractFromSurfaceCoeffs
    {
        includedAngle   150;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/surfacefeatureextract/">surfaceFeatureExtract</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
