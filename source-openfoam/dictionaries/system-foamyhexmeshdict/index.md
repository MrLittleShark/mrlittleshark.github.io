---
title: "system/foamyHexMeshDict · foamyHexMeshDict"
layout: reference
description: "foamyHexMesh 的体网格、尺寸控制与网格优化参数。这个网格生成器与 snappyHexMesh 采用不同构造过程，并依赖相应构建支持；示例只证明 v2512 源码包含配置，不表示当前安装已编译该程序。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>foamyHexMesh 的体网格、尺寸控制与网格优化参数。这个网格生成器与 snappyHexMesh 采用不同构造过程，并依赖相应构建支持；示例只证明 v2512 源码包含配置，不表示当前安装已编译该程序。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>initialPointsMethod</td><td>initialPointsMethod         pointFile;</td></tr><tr><td>autoDensityCoeffs</td><td>initialPointsMethod     pointFile;</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/porousSimpleFoam/straightDuctImplicit</h3><p>原始路径：<code>tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/foamyHexMeshDict</code>；求解器：<code>porousSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/foamyHexMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyhexmeshdict/1-foamyHexMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/foamyHexMeshDict&quot;；&quot;meshDict.geometry&quot;；&quot;meshDict.conformationSurfaces&quot;；&quot;meshDict.shapeControlFunctions&quot;；&quot;meshQualityDict&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · mesh/foamyHexMesh/mixerVessel</h3><p>原始路径：<code>tutorials/mesh/foamyHexMesh/mixerVessel/system/foamyHexMeshDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/foamyHexMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyhexmeshdict/2-foamyHexMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/foamyHexMeshDict&quot;；&quot;meshDict.geometry&quot;；&quot;meshDict.conformationSurfaces&quot;；&quot;meshDict.cellShapeControl&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · mesh/foamyHexMesh/blob</h3><p>原始路径：<code>tutorials/mesh/foamyHexMesh/blob/system/foamyHexMeshDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/blob/system/foamyHexMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyhexmeshdict/3-foamyHexMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/blob">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/foamyHexMeshDict&quot;；&quot;meshQualityDict&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/foamyhexmesh/">foamyHexMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/foamyHexMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/foamyHexMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
