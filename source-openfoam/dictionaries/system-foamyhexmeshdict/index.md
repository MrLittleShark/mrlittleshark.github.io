---
title: "foamyHexMeshDict"
layout: reference
description: "foamyHexMesh 的体网格、尺寸控制与网格优化参数。"
dictionary: true
cms_slug: "dictionary-foamyhexmeshdict"
---

<p>foamyHexMesh 的体网格、尺寸控制与网格优化参数。</p><p>位置：<code>system/foamyHexMeshDict</code></p><h2>配置实例</h2><p>incompressible/porousSimpleFoam/straightDuctImplicit 中的 foamyHexMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      foamyHexMeshDict;
}

#includeEtc &quot;caseDicts/foamyHexMeshDict&quot;

geometry
{
    #include &quot;meshDict.geometry&quot;
}

surfaceConformation
{
    locationInMesh (-0.078 0.02 0.0);

    featurePointControls
    {
        specialiseFeaturePoints         on;
        edgeAiming                      on;
        guardFeaturePoints              off;
        snapFeaturePoints               off;
        circulateEdges                  off;
    }

    geometryToConformTo
    {
        #include &quot;meshDict.conformationSurfaces&quot;
    }

    additionalFeatures
    {
        boundaryAndFaceZones
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;boundaryAndFaceZones.extendedFeatureEdgeMesh&quot;;
        }
    }
}

motionControl
{
    defaultCellSize         0.0035;

    minimumCellSizeCoeff    0;

    maxRefinementIterations 0;

    maxSmoothingIterations  100;

    shapeControlFunctions
    {
        #include &quot;meshDict.shapeControlFunctions&quot;
    }

    objOutput                   off;

    timeChecks                  off;

    printVertexInfo             off;
}

polyMeshFiltering
{
    filterEdges                         false;
    filterFaces                         off;
    writeTetDualMesh                    true;
    writeCellShapeControlMesh           false;
    writeBackgroundMeshDecomposition    false;
}

meshQualityControls
{
    #include &quot;meshQualityDict&quot;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/porousSimpleFoam/straightDuctImplicit</summary><p>straightDuctImplicit 使用 foamyHexMesh 在管道几何周围生成多面体网格，公共配置与本算例几何分别通过 include 读入。</p>
<ul>
<li><code>locationInMesh (-0.078 0.02 0)</code> 选择保留的内部区域，该点应位于管道流体域。</li>
<li><code>defaultCellSize 0.0035</code> 给出默认单元尺度 3.5 mm，局部尺度由 shapeControlFunctions 补充。</li>
<li>特征边来自 boundaryAndFaceZones.extendedFeatureEdgeMesh，edgeAiming 等选项使生成网格适应几何棱边。</li>
<li><code>maxRefinementIterations 0</code>、<code>maxSmoothingIterations 100</code> 配置细化与平滑阶段；公共 include 中仍提供其他控制项。</li>
<li><code>filterEdges false</code>、<code>filterFaces off</code> 关闭最后的边、面过滤，<code>writeTetDualMesh true</code> 输出相应中间网格。</li>
</ul>
<p>更换管道尺寸时同步修改内部点与单元尺度，并检查入口、出口和壁面是否被正确识别。</p>
<p><a href="/assets/examples/v2512/foamyhexmeshdict/1-foamyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/foamyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      foamyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#includeEtc &quot;caseDicts/foamyHexMeshDict&quot;

geometry
{
    #include &quot;meshDict.geometry&quot;
}


surfaceConformation
{
    locationInMesh (-0.078 0.02 0.0);

    featurePointControls
    {
        specialiseFeaturePoints         on;
        edgeAiming                      on;
        guardFeaturePoints              off;
        snapFeaturePoints               off;
        circulateEdges                  off;
    }


    geometryToConformTo
    {
        #include &quot;meshDict.conformationSurfaces&quot;
    }

    additionalFeatures
    {
        boundaryAndFaceZones
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;boundaryAndFaceZones.extendedFeatureEdgeMesh&quot;;
        }
    }
}


motionControl
{
    defaultCellSize         0.0035;

    minimumCellSizeCoeff    0;

    maxRefinementIterations 0;

    maxSmoothingIterations  100;

    shapeControlFunctions
    {
        #include &quot;meshDict.shapeControlFunctions&quot;
    }

    objOutput                   off;

    timeChecks                  off;

    printVertexInfo             off;
}


polyMeshFiltering
{
    filterEdges                         false;
    filterFaces                         off;
    writeTetDualMesh                    true;
    writeCellShapeControlMesh           false;
    writeBackgroundMeshDecomposition    false;
}


meshQualityControls
{
    #include &quot;meshQualityDict&quot;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/foamyHexMesh/mixerVessel</summary><p>mixerVessel 的几何含有叶片和容器壁，需要空间变化的网格尺度与特征贴合。</p>
<ul>
<li><code>defaultCellSize 0.006</code> 设置默认尺度 6 mm，shapeControlFunctions 给出叶片等部位的局部要求。</li>
<li>初始 autoDensity 布点中 <code>minLevels 2</code>、<code>sampleResolution 5</code> 控制几何采样与密度估计。</li>
<li><code>locationInMesh (0 0.1 1)</code> 指定流体域内点，<code>maxIterations 15</code> 限制边界贴合迭代次数。</li>
<li><code>maxRefinementIterations 1</code>、<code>maxSmoothingIterations 100</code> 允许一次细化和较充分的平滑；<code>filterEdges on</code> 清理局部短边。</li>
<li>开启 writeBackgroundMeshDecomposition 与 writeCellShapeControlMesh 输出有助于查看网格尺寸如何从几何需求过渡到实际单元。</li>
</ul>
<p>叶片间隙分辨率不足时先修改局部尺度函数，再检查狭缝中的单元数和网格质量。</p>
<p><a href="/assets/examples/v2512/foamyhexmeshdict/2-foamyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/foamyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class           dictionary;
    object          foamyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#includeEtc &quot;caseDicts/foamyHexMeshDict&quot;

geometry
{
    #include &quot;meshDict.geometry&quot;
}


initialPoints
{
    //initialPointsMethod         pointFile;
    initialPointsMethod         autoDensity;

    autoDensityCoeffs
    {
        minLevels               2;
        maxSizeRatio            2.0;
        sampleResolution        5;
        surfaceSampleResolution 5;
    }

    pointFileCoeffs
    {
        insideOutsideCheck off;
        randomiseInitialGrid off;
        randomPerturbationCoeff 1e-3;
        pointFile &quot;0/internalDelaunayVertices&quot;;
    }
}


surfaceConformation
{
    locationInMesh                      (0 0.1 1.0);

    #include &quot;meshDict.conformationSurfaces&quot;

    featurePointExclusionDistanceCoeff  0.65;
    featureEdgeExclusionDistanceCoeff   0.5;
    maxSurfaceProtrusionCoeff           0.1;

    conformationControls
    {
        edgeSearchDistCoeff             5;
        surfacePtReplaceDistCoeff       0.5;
        surfacePtExclusionDistanceCoeff 0.5;
        maxIterations                   15;
        iterationToInitialHitRatioLimit 0.0001;
    }
}


motionControl
{
    defaultCellSize             6e-3;

    minimumCellSizeCoeff        0.1;

    maxRefinementIterations     1;

    maxSmoothingIterations      100;

    shapeControlFunctions
    {
        #include &quot;meshDict.cellShapeControl&quot;
    }

    objOutput                   no;

    timeChecks                  no;
}


backgroundMeshDecomposition
{
    minLevels           1;
    sampleResolution    4;
    spanScale           20;
    maxCellWeightCoeff  20;
}


polyMeshFiltering
{
    writeBackgroundMeshDecomposition    true;
    writeCellShapeControlMesh           true;
    writeTetDualMesh                    false;
    filterEdges                         on;
    filterFaces                         off;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · mesh/foamyHexMesh/blob</summary><p>blob 算例用 STL 表面定义几何，再通过 foamyHexMesh 生成贴合网格。</p>
<ul>
<li><code>blob.stl</code> 作为 triSurfaceMesh 读入，refinementBox 还定义了一个可用于局部控制的空间盒。</li>
<li><code>locationInMesh (0.1 0.1 0.2)</code> 指定要保留的区域。</li>
<li><code>defaultCellSize 0.1</code> 给出基准尺度，blob 的 searchableSurfaceControl 以 <code>priority 1</code>、<code>mode bothSides</code> 控制表面两侧。</li>
<li><code>cellSizeFunction uniform</code> 与 <code>surfaceCellSizeCoeff 1</code> 使用均匀的表面尺度关系；<code>featureMethod none</code> 适合这种平滑几何演示。</li>
<li><code>maxSmoothingIterations 100</code> 控制平滑上限，质量标准由 meshQualityDict 提供。</li>
</ul>
<p>几何缩放后同步调整默认尺度和内部点，再检查曲率较大位置的表面分辨率。</p>
<p><a href="/assets/examples/v2512/foamyhexmeshdict/3-foamyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/blob/system/foamyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/blob">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class           dictionary;
    object          foamyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Include defaults parameters from master dictionary
#includeEtc &quot;caseDicts/foamyHexMeshDict&quot;

geometry
{
    blob.stl
    {
        name blob;
        type triSurfaceMesh;
    }

    refinementBox
    {
        type box;
        min  (-0.2  -0.6 -0.2);
        max  ( 0.4   0.2  0.35);
    }
}


backgroundMeshDecomposition
{
    minLevels           0;
    sampleResolution    4;
    spanScale           20;
    maxCellWeightCoeff  20;
}


initialPoints
{
    initialPointsMethod         autoDensity;
    // initialPointsMethod     pointFile;

    autoDensityCoeffs
    {
        minLevels               0;
        maxSizeRatio            5.0;
        sampleResolution        5;
        surfaceSampleResolution 5;
    }

    pointFileCoeffs
    {
        pointFile               &quot;&lt;constant&gt;/internalDelaunayVertices&quot;;
    }
}


surfaceConformation
{
    locationInMesh              (0.1 0.1 0.2);

    featurePointControls
    {
        specialiseFeaturePoints off;
        edgeAiming              off;
        guardFeaturePoints      off;
        snapFeaturePoints       off;
        circulateEdges          off;
    }

    geometryToConformTo
    {
        blob
        {
            featureMethod       none;
        }
    }
}


motionControl
{
    defaultCellSize             0.1;

    minimumCellSizeCoeff        0;

    maxSmoothingIterations      100;

    maxRefinementIterations     0;

    shapeControlFunctions
    {
        blob
        {
            type                    searchableSurfaceControl;
            priority                1;
            mode                    bothSides;

            surfaceCellSizeFunction uniformValue;
            uniformValueCoeffs
            {
                surfaceCellSizeCoeff     1;
            }

            cellSizeFunction        uniform;
            uniformCoeffs
            {}
        }
    }

    objOutput                   no;

    timeChecks                  no;
}


meshQualityControls
{
    #include &quot;meshQualityDict&quot;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamyhexmesh/">foamyHexMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
