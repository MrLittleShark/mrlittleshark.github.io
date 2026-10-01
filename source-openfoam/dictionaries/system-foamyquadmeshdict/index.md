---
title: "system/foamyQuadMeshDict · foamyQuadMeshDict"
layout: reference
description: "foamyQuadMesh 的二维四边形网格构造与优化配置。使用前应确认安装包含该工具及依赖；输出需检查边界贴合、非正交性与单元质量。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>foamyQuadMesh 的二维四边形网格构造与优化配置。使用前应确认安装包含该工具及依赖；输出需检查边界贴合、非正交性与单元质量。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>minCellSize</td><td>允许的最小单元尺寸，过小可能显著增加单元数与内存需求。</td></tr><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>geometry</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>locationInMesh</td><td>The z-coordinate of the plane is taken from here.</td></tr><tr><td>minEdgeLenCoeff</td><td>If area of a dual cell is less than the square of this, do not refine.</td></tr><tr><td>maxNotchLenCoeff</td><td>How much cells are allowed to stick out of the surfaces before points are inserted onto the boundary</td></tr><tr><td>insertSurfaceNearestPointPairs</td><td>Insert near-boundary point mirror or point-pairs</td></tr><tr><td>mirrorPoints</td><td>Mirror near-boundary points rather than insert point-pairs</td></tr><tr><td>insertSurfaceNearPointPairs</td><td>Insert point-pairs vor dual-cell vertices very near the surface</td></tr><tr><td>maxBoundaryConformingIter</td><td>Maximum number of iterations used in boundaryConform.</td></tr><tr><td>randomiseInitialGrid</td><td>Choose if to randomise the initial grid created by insertGrid.</td></tr><tr><td>randomPerturbation</td><td>Perturbation fraction, 1 = cell-size.</td></tr><tr><td>defaultPriority</td><td>Assign a priority to all requests for cell sizes, the highest overrules.</td></tr><tr><td>nearWallAlignedDist</td><td>Near-wall region where cells are aligned with the wall specified as a number of cell layers</td></tr><tr><td>shortEdgeFilterFactor</td><td>Factor to multiply the average of a face&#x27;s edge lengths by. If an edge of that face is smaller than that value then delete it.</td></tr><tr><td>edgeAttachedToBoundaryFactor</td><td>Weighting for the lengths of edges that are attached to the boundaries. Used when calculating the length of an edge. Default 2.0.</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · mesh/foamyQuadMesh/jaggedBoundary</h3><p>原始路径：<code>tutorials/mesh/foamyQuadMesh/jaggedBoundary/system/foamyQuadMeshDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/jaggedBoundary/system/foamyQuadMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyquadmeshdict/1-foamyQuadMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/jaggedBoundary">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;extrude2DMeshDict&quot;;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · mesh/foamyQuadMesh/square</h3><p>原始路径：<code>tutorials/mesh/foamyQuadMesh/square/system/foamyQuadMeshDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square/system/foamyQuadMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyquadmeshdict/2-foamyQuadMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/square">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;extrude2DMeshDict&quot;;。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · mesh/foamyQuadMesh/OpenCFD</h3><p>原始路径：<code>tutorials/mesh/foamyQuadMesh/OpenCFD/system/foamyQuadMeshDict</code>；求解器：<code>foamyQuadMesh</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD/system/foamyQuadMeshDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/foamyquadmeshdict/3-foamyQuadMeshDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;extrude2DMeshDict&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/foamyquadmesh/">foamyQuadMesh</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/foamyQuadMeshDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/foamyQuadMeshDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
