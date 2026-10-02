---
title: "foamyQuadMeshDict"
layout: reference
description: "foamyQuadMesh 的二维四边形网格构造与优化配置。"
dictionary: true
cms_slug: "dictionary-foamyquadmeshdict"
---

<p>foamyQuadMesh 的二维四边形网格构造与优化配置。</p><p>位置：<code>system/foamyQuadMeshDict</code></p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>minCellSize</td><td>允许的最小单元尺寸，过小可能显著增加单元数与内存需求。</td></tr><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · mesh/foamyQuadMesh/jaggedBoundary</summary><p>jaggedBoundary 用带折角的封闭表面演示 foamyQuadMesh 如何生成平面网格并贴合边界。</p>
<ul>
<li><code>locationInMesh (-0.6 0.3 0)</code> 选定内部区域，同时其 z 坐标给出网格所在平面。</li>
<li>扩展特征边文件保存边界折角，<code>maxQuadAngle 125</code> 为四边形几何控制提供角度阈值。</li>
<li><code>surfaceOffsetLinearDistance</code> 从壁面附近的尺寸向内部过渡，<code>surfaceCellSizeCoeff 0.1</code>、<code>totalDistanceCoeff 5</code> 等系数控制这一变化。</li>
<li><code>randomiseInitialGrid yes</code>、<code>randomPerturbation 0.1</code> 对初始点施加相当于局部尺寸 10% 的扰动，帮助避免过于规则的初始排列。</li>
<li><code>adaptiveLinear</code> 的松弛系数从 0.5 降到 0；shortEdgeFilterFactor 为 0.2，最后 <code>extrude off</code> 保留平面网格处理。</li>
</ul>
<p>折角附近网格不足时先调表面尺度与特征边，生成后查看短边过滤是否保留了所需几何细节。</p>
<p><a href="/assets/examples/v2512/foamyquadmeshdict/1-foamyQuadMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/jaggedBoundary/system/foamyQuadMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/jaggedBoundary">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      foamyQuadMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

geometry
{
    jaggedBoundary.stl
    {
        name jaggedBoundary;
        type closedTriSurfaceMesh;
    }
}

surfaceConformation
{
    // The z-coordinate of the plane is taken from here.
    locationInMesh                  (-0.6 0.3 0.0);

    pointPairDistanceCoeff          0.001;

    // If area of a dual cell is less than the square of this, do not refine.
    minEdgeLenCoeff                 0.001;

    // How much cells are allowed to stick out of the surfaces before
    // points are inserted onto the boundary
    maxNotchLenCoeff                1;

    minNearPointDistCoeff           0.001;

    maxQuadAngle                    125;

    // Insert near-boundary point mirror or point-pairs
    insertSurfaceNearestPointPairs  yes;

    // Mirror near-boundary points rather than insert point-pairs
    mirrorPoints                    no;

    // Insert point-pairs vor dual-cell vertices very near the surface
    insertSurfaceNearPointPairs     yes;

    // Maximum number of iterations used in boundaryConform.
    maxBoundaryConformingIter       5;

    geometryToConformTo
    {
        jaggedBoundary
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;jaggedBoundary.extendedFeatureEdgeMesh&quot;;
        }
    }

    additionalFeatures
    {
    }

    // Choose if to randomise the initial grid created by insertGrid.
    randomiseInitialGrid yes;

    // Perturbation fraction, 1 = cell-size.
    randomPerturbation   0.1;
}


motionControl
{
    // This is a tolerance for determining whether to deal with surface
    // protrusions or not.
    minCellSize         0.04;

    // Assign a priority to all requests for cell sizes, the highest overrules.
    defaultPriority     0;

    shapeControlFunctions
    {
        jaggedBoundary
        {
            type                    searchableSurfaceControl;
            priority                1;
            mode                    inside;

            cellSizeFunction        surfaceOffsetLinearDistance;
            surfaceOffsetLinearDistanceCoeffs
            {
                distanceCellSizeCoeff    1;
                totalDistanceCoeff       5;
                surfaceOffsetCoeff       1;
            }

            surfaceCellSizeFunction uniformValue;
            uniformValueCoeffs
            {
                surfaceCellSizeCoeff     0.1;
            }
        }
    }

    relaxationModel     adaptiveLinear;

    adaptiveLinearCoeffs
    {
        relaxationStart 0.5;
        relaxationEnd   0.0;
    }

    objOutput           no;

    meshedSurfaceOutput yes;

    // Near-wall region where cells are aligned with the wall specified as a
    // number of cell layers
    nearWallAlignedDist 3;
}


shortEdgeFilter
{
    // Factor to multiply the average of a face&#x27;s edge lengths by.
    // If an edge of that face is smaller than that value then delete it.
    shortEdgeFilterFactor        0.2;

    // Weighting for the lengths of edges that are attached to the boundaries.
    // Used when calculating the length of an edge. Default 2.0.
    edgeAttachedToBoundaryFactor 2.0;
}


extrusion
{
    extrude     off;
    #include    &quot;extrude2DMeshDict&quot;;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/foamyQuadMesh/square</summary><p>square 演示方形边界与内部盒状细化区域共同控制 foamyQuadMesh 的尺寸分布。</p>
<ul>
<li>cube.stl 定义外边界，refinementBox 在 x、y 的 0.25～0.75 区间提供局部控制，z 范围覆盖整个平面。</li>
<li><code>locationInMesh (0 0 0)</code> 决定保留区域与平面位置，扩展特征边文件提供方形角点信息。</li>
<li>两个 searchableSurfaceControl 都采用 <code>bothSides</code> 和 linearDistance，以 <code>distanceCellSizeCoeff 5</code> 控制离表面后的尺度变化。</li>
<li><code>surfaceCellSizeCoeff 0.05</code> 设定表面相对尺度；<code>adaptiveLinear</code> 从 0.5 松弛到 0，shortEdgeFilterFactor 为 0.25。</li>
</ul>
<p><code>extrude off</code> 使当前阶段先处理二维网格；需要实体单层网格时再使用 extrude2DMeshDict 的设置。</p>
<p><a href="/assets/examples/v2512/foamyquadmeshdict/2-foamyQuadMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square/system/foamyQuadMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      foamyQuadMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

geometry
{
    unit_cube.stl
    {
        name cube;
        type triSurfaceMesh;
    }

    refinementBox
    {
        type box;
        min  (0.25 0.25 -1000);
        max  (0.75 0.75 1000);
    }
}


surfaceConformation
{
    // The z-coordinate of the plane is taken from here.
    locationInMesh                  (0 0 0);

    pointPairDistanceCoeff          0.005;

    minEdgeLenCoeff                 0.005;

    maxNotchLenCoeff                0.003;

    minNearPointDistCoeff           0.0025;

    maxQuadAngle                    125;

    // Insert near-boundary point mirror or point-pairs
    insertSurfaceNearestPointPairs  yes;

    // Mirror near-boundary points rather than insert point-pairs
    mirrorPoints                    no;

    // Insert point-pairs vor dual-cell vertices very near the surface
    insertSurfaceNearPointPairs     yes;

    // Maximum number of iterations used in boundaryConform.
    maxBoundaryConformingIter       5;

    geometryToConformTo
    {
        cube
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;unit_cube.extendedFeatureEdgeMesh&quot;;
        }
    }

    additionalFeatures
    {}

    // Choose if to randomise the initial grid created by insertGrid.
    randomiseInitialGrid yes;

    // Perturbation fraction, 1 = cell-size.
    randomPerturbation   0.1;
}


motionControl
{
    minCellSize         0.04;

    // Assign a priority to all requests for cell sizes, the highest overrules.
    defaultPriority     0;

    shapeControlFunctions
    {
        cube
        {
            type                    searchableSurfaceControl;
            priority                1;
            mode                    bothSides;
            cellSizeFunction        linearDistance;
            linearDistanceCoeffs
            {
                distanceCellSizeCoeff    1;
                distanceCoeff            5;
            }
            surfaceCellSizeFunction uniformValue;
            uniformValueCoeffs
            {
                surfaceCellSizeCoeff     0.05;
            }
        }

        refinementBox
        {
            type                    searchableSurfaceControl;
            priority                1;
            mode                    bothSides;
            cellSizeFunction        linearDistance;
            linearDistanceCoeffs
            {
                distanceCellSizeCoeff    1;
                distanceCoeff            5;
            }
            surfaceCellSizeFunction uniformValue;
            uniformValueCoeffs
            {
                surfaceCellSizeCoeff     0.05;
            }
        }
    }

    relaxationModel             adaptiveLinear;

    adaptiveLinearCoeffs
    {
        relaxationStart         0.5;
        relaxationEnd           0.0;
    }

    objOutput                   no;

    meshedSurfaceOutput         yes;

    // Near-wall region where cells are aligned with the wall specified as a
    // number of cell layers
    nearWallAlignedDist         3;
}


shortEdgeFilter
{
    // Factor to multiply the average of a face&#x27;s edge lengths by.
    // If an edge of that face is smaller than that value then delete it.
    shortEdgeFilterFactor           0.25;

    // Weighting for the lengths of edges that are attached to the boundaries.
    // Used when calculating the length of an edge. Default 2.0.
    edgeAttachedToBoundaryFactor    2.0;
}


extrusion
{
    extrude     off;

    #include    &quot;extrude2DMeshDict&quot;;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · mesh/foamyQuadMesh/OpenCFD</summary><p>OpenCFD 字样网格包含文字轮廓与外部盒子，foamyQuadMesh 需要同时保留文字细节和外边界名称。</p>
<ul>
<li>opencfd_text.stl 定义 letters，opencfd_box.stl 的各区域命名为 back、front、bottom、top、inlet、outlet。</li>
<li>两个扩展特征边文件用于跟踪文字转角与盒子棱边。</li>
<li><code>minCellSize 0.02</code> 提供局部尺度控制参数，letters 的 <code>mode inside</code>、<code>cellSizeFunction uniform</code>、<code>surfaceCellSizeCoeff 1</code> 定义当前使用的文字内部尺寸。</li>
<li>同块中的 linearDistanceCoeffs 是备用参数；当前选定的 uniform 函数决定生效的尺寸关系。</li>
<li><code>maxQuadAngle 120</code>、shortEdgeFilterFactor 0.2 和逐步减小的松弛系数共同控制生成质量。</li>
</ul>
<p>缩小文字细节时同步提高特征边和表面分辨率，重点查看笔画间隙是否仍被网格分开。</p>
<p><a href="/assets/examples/v2512/foamyquadmeshdict/3-foamyQuadMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD/system/foamyQuadMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      foamyQuadMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

geometry
{
    opencfd_text.stl
    {
        name letters;
        type closedTriSurfaceMesh;
    }

    opencfd_box.stl
    {
        name box;
        type closedTriSurfaceMesh;

        regions
        {
            back
            {
                name back;
            }
            front
            {
                name front;
            }
            bottom
            {
                name bottom;
            }
            top
            {
                name top;
            }
            inlet
            {
                name inlet;
            }
            outlet
            {
                name outlet;
            }
        }
    }
}


surfaceConformation
{
    // The z-coordinate of the plane is taken from here.
    locationInMesh                  (0 0 0);

    pointPairDistanceCoeff          0.1;

    minEdgeLenCoeff                 0.1;

    maxNotchLenCoeff                1.0;

    minNearPointDistCoeff           0.1;

    maxQuadAngle                    120;

    // Insert near-boundary point mirror or point-pairs
    insertSurfaceNearestPointPairs  yes;

    // Mirror near-boundary points rather than insert point-pairs
    mirrorPoints                    no;

    // Insert point-pairs vor dual-cell vertices very near the surface
    insertSurfaceNearPointPairs     yes;

    // Maximum number of iterations used in boundaryConform.
    maxBoundaryConformingIter       5;

    geometryToConformTo
    {
        letters
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;opencfd_text.extendedFeatureEdgeMesh&quot;;
        }

        box
        {
            featureMethod           extendedFeatureEdgeMesh;
            extendedFeatureEdgeMesh &quot;opencfd_box.extendedFeatureEdgeMesh&quot;;
        }
    }

    additionalFeatures
    {}

    // Choose if to randomise the initial grid created by insertGrid.
    randomiseInitialGrid            yes;

    // Perturbation fraction, 1 = cell-size.
    randomPerturbation              0.1;
}


motionControl
{
    // This is a tolerance for determining whether to deal with surface
    // protrusions or not.
    minCellSize         0.02;

    // Assign a priority to all requests for cell sizes, the highest overrules.
    defaultPriority     0;

    shapeControlFunctions
    {
        letters
        {
            type                  searchableSurfaceControl;
            priority              1;
            mode                  inside;
            cellSizeFunction      uniform;

            linearDistanceCoeffs
            {
                distanceCellSizeCoeff  1;
                distanceCoeff          50;
            }
            uniformCoeffs
            {}

            surfaceCellSizeFunction uniformValue;
            uniformValueCoeffs
            {
                surfaceCellSizeCoeff   1;
            }
        }
    }

    relaxationModel     adaptiveLinear;

    adaptiveLinearCoeffs
    {
        relaxationStart 0.5;
        relaxationEnd   0.0;
    }

    objOutput           no;

    meshedSurfaceOutput yes;

    // Near-wall region where cells are aligned with the wall specified as a
    // number of cell layers
    nearWallAlignedDist 3;
}


shortEdgeFilter
{
    // Factor to multiply the average of a face&#x27;s edge lengths by.
    // If an edge of that face is smaller than that value then delete it.
    shortEdgeFilterFactor           0.2;

    // Weighting for the lengths of edges that are attached to the boundaries.
    // Used when calculating the length of an edge. Default 2.0.
    edgeAttachedToBoundaryFactor    2.0;
}


extrusion
{
    extrude  off;

    #include &quot;extrude2DMeshDict&quot;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamyquadmesh/">foamyQuadMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
