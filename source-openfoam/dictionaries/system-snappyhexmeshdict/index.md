---
title: "snappyHexMeshDict"
layout: reference
description: "设置表面几何、局部细化、表面贴合和边界层，供 snappyHexMesh 生成贴体网格。"
dictionary: true
cms_slug: "dictionary-snappyhexmeshdict"
---

<p>设置表面几何、局部细化、表面贴合和边界层，供 snappyHexMesh 生成贴体网格。</p><p>位置：<code>system/snappyHexMeshDict</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-snappy-workflow.png" alt="snappyHexMesh 的几何与背景网格输入" loading="lazy"><figcaption><strong>snappyHexMesh 的几何与背景网格输入</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module3.pdf，p. 71 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><h2>配置实例</h2><p>snappyHexMesh 包括切割细化、表面贴合和边界层生成三个阶段。运行 foamGetDict snappyHexMeshDict 获取带注释模板，在已建立的背景网格上配置几何和各阶段参数。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>设置方法</th></tr>
<tr><td>castellatedMesh、snap、addLayers</td><td>分别控制切割细化、贴体和边界层生成</td><td>先检查切割细化和贴体，再配置边界层</td></tr>
<tr><td>geometry</td><td>表面及可搜索几何体</td><td>body.stl { type triSurfaceMesh; name body; }</td></tr>
<tr><td>maxLocalCells、maxGlobalCells</td><td>局部及全局细化控制限额</td><td>根据可用内存设置单元数量上限</td></tr>
<tr><td>minRefinementCells</td><td>停止继续细化的候选单元阈值</td><td>设为 0 时继续处理剩余细化单元，计算量相应增加</td></tr>
<tr><td>nCellsBetweenLevels</td><td>相邻细化级别间的过渡层数</td><td>例如 3</td></tr>
<tr><td>features</td><td>显式特征文件和细化等级</td><td>({ file "body.eMesh"; level 2; })</td></tr>
<tr><td>refinementSurfaces</td><td>表面的最小最大细化等级</td><td>body { level (2 3); patchInfo { type wall; } }</td></tr>
<tr><td>resolveFeatureAngle</td><td>区分尖锐表面特征的角度</td><td>示例为 30，按表面几何特征确定</td></tr>
<tr><td>refinementRegions</td><td>体积或距离带细化</td><td>mode inside、outside 或 distance；levels 定义等级</td></tr>
<tr><td>locationInMesh</td><td>标记需要保留的连通流体区域</td><td>取目标流体区域内部点，避开边界面</td></tr>
<tr><td>allowFreeStandingZoneFaces</td><td>是否允许独立区域面</td><td>与 zone 生成方式匹配</td></tr>
<tr><td>snapControls</td><td>贴体松弛和迭代</td><td>nSmoothPatch、tolerance、nSolveIter、nRelaxIter</td></tr>
<tr><td>显式特征贴合</td><td>explicitFeatureSnap 与 nFeatureSnapIter</td><td>与 features 中的 eMesh 配合</td></tr>
<tr><td>layers</td><td>各 patch 的层数</td><td>"body.*" { nSurfaceLayers 3; }</td></tr>
<tr><td>relativeSizes</td><td>层厚是否相对外层网格尺寸</td><td>true 相对尺寸；false 绝对长度</td></tr>
<tr><td>expansionRatio</td><td>层间厚度增长比</td><td>例如 1.2</td></tr>
<tr><td>finalLayerThickness、firstLayerThickness、thickness</td><td>不同的层厚约束</td><td>按层厚参数关系选取相容组合</td></tr>
<tr><td>minThickness</td><td>允许保留的最小总层厚指标</td><td>阈值过大时，局部边界层将被取消</td></tr>
<tr><td>nGrow、nBufferCellsNoExtrude</td><td>尖角附近的非挤出区域及过渡缓冲</td><td>控制未生成边界层区域的过渡</td></tr>
<tr><td>featureAngle、slipFeatureAngle</td><td>层网格遇尖角时的行为</td><td>按几何特征及边界层覆盖率调整</td></tr>
<tr><td>nLayerIter、nRelaxedIter</td><td>边界层生成迭代及质量阈值放宽迭代</td><td>几何有效性满足要求后设置迭代上限</td></tr>
<tr><td>meshQualityControls</td><td>质量约束</td><td>通常包含系统 meshQualityDict</td></tr>
<tr><td>mergeTolerance</td><td>点合并相对容差</td><td>常用 1e-6，以几何包围盒尺度为基准</td></tr>
</table></div>
<pre><code class="language-openfoam">// 片段：放入对应的 snappyHexMeshDict
geometry
{
    body.stl { type triSurfaceMesh; name body; }
    refineBox
    {
        type searchableBox;
        min (-0.2 -0.2 -0.2);
        max (1.2 0.2 0.2);
    }
}
castellatedMeshControls
{
    maxLocalCells 1000000;
    maxGlobalCells 3000000;
    minRefinementCells 0;
    nCellsBetweenLevels 3;
    features ({ file "body.eMesh"; level 2; });
    refinementSurfaces
    {
        body { level (2 3); patchInfo { type wall; } }
    }
    resolveFeatureAngle 30;
    refinementRegions
    {
        refineBox { mode inside; levels ((1e15 2)); }
    }
    locationInMesh (2 0 0);
    allowFreeStandingZoneFaces true;
}
snapControls
{
    nSmoothPatch 3; tolerance 2.0;
    nSolveIter 30; nRelaxIter 5;
    nFeatureSnapIter 10;
    implicitFeatureSnap false;
    explicitFeatureSnap true;
    multiRegionFeatureSnap false;
}</code></pre>
<p>locationInMesh 中的 (2 0 0) 表示待保留流体区域内的一点，该点须位于背景网格范围内及物体外部。网格生成前应消除 STL 自相交，统一长度单位，并检查背景网格。</p>
<p>边界层生成配置如下。snapControls 和质量控制参数保留模板中的完整设置。将 addLayers 设为 false，可单独检查切割细化和表面贴合结果。</p>
<pre><code class="language-openfoam">castellatedMesh true;
snap true;
addLayers true;
addLayersControls
{
    relativeSizes true;
    layers { body { nSurfaceLayers 3; } }
    expansionRatio 1.2;
    finalLayerThickness 0.3;
    minThickness 0.1;
    nGrow 0;
    featureAngle 60;
    nRelaxIter 5;
    nSmoothSurfaceNormals 1;
    nSmoothNormals 3;
    nSmoothThickness 10;
    maxFaceThicknessRatio 0.5;
    maxThicknessToMedialRatio 0.3;
    minMedialAxisAngle 90;
    nBufferCellsNoExtrude 0;
    nLayerIter 50;
}
meshQualityControls
{
    #includeEtc "caseDicts/meshQualityDict"
}
mergeTolerance 1e-6;</code></pre>
<h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>expansionRatio</td><td>相邻挤出层的厚度增长比例。</td></tr><tr><td>regions</td><td>几何选择区域或多区域列表；在不同字典中结构不同，不能只复制键名。</td></tr><tr><td>cellZone</td><td>源项、运动或材料区域所引用的单元区名称。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/motorBike</summary><p>motorBike 用 snappyHexMesh 把背景网格贴合摩托车表面，并在尾迹与近壁区域增加分辨率。</p>
<ul>
<li><code>castellatedMesh true</code>、<code>snap true</code>、<code>addLayers true</code> 分别启用切割加密、表面贴合和层网格。</li>
<li><code>motorBike.obj</code> 提供表面；表面 <code>level (5 6)</code> 与 <code>motorBike.eMesh</code> 的 <code>level 6</code> 加密几何和特征边。</li>
<li><code>refinementBox</code> 从 (−1,−0.7,0) 到 (8,0.7,2.5)，其内部使用 level 4，使尾迹附近保持较细网格。</li>
<li><code>locationInMesh (3.0001 3.0001 0.43)</code> 标记要保留的流体连通域。</li>
<li><code>nSurfaceLayers 1</code>、<code>relativeSizes true</code>、<code>finalLayerThickness 0.3</code> 给指定壁面加一层相对厚度网格。</li>
</ul>
<p>目标 y⁺ 变化时，应联动背景分辨率与层厚；修改几何后重新检查保留点、层覆盖率和质量。</p>
<p><a href="/assets/examples/v2512/snappyhexmeshdict/1-snappyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/motorBike/system/snappyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/motorBike">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      snappyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Which of the steps to run
castellatedMesh true;
snap            true;
addLayers       true;


// Geometry. Definition of all surfaces. All surfaces are of class
// searchableSurface.
// Surfaces are used
// - to specify refinement for any mesh cell intersecting it
// - to specify refinement for any mesh cell inside/outside/near
// - to &#x27;snap&#x27; the mesh boundary to the surface
geometry
{
    motorBike.obj
    {
        type triSurfaceMesh;
        name motorBike;
    }

    refinementBox
    {
        type box;
        min  (-1.0 -0.7 0.0);
        max  ( 8.0  0.7 2.5);
    }
}


// Settings for the castellatedMesh generation.
castellatedMeshControls
{

    // Refinement parameters
    // ~~~~~~~~~~~~~~~~~~~~~

    // If local number of cells is &gt;= maxLocalCells on any processor
    // switches from from refinement followed by balancing
    // (current method) to (weighted) balancing before refinement.
    maxLocalCells 100000;

    // Overall cell limit (approximately). Refinement will stop immediately
    // upon reaching this number so a refinement level might not complete.
    // Note that this is the number of cells before removing the part which
    // is not &#x27;visible&#x27; from the keepPoint. The final number of cells might
    // actually be a lot less.
    maxGlobalCells 2000000;

    // The surface refinement loop might spend lots of iterations refining just a
    // few cells. This setting will cause refinement to stop if &lt;= minimumRefine
    // are selected for refinement. Note: it will at least do one iteration
    // (unless the number of cells to refine is 0)
    minRefinementCells 10;

    // Allow a certain level of imbalance during refining
    // (since balancing is quite expensive)
    // Expressed as fraction of perfect balance (= overall number of cells /
    // nProcs). 0=balance always.
    maxLoadUnbalance 0.10;


    // Number of buffer layers between different levels.
    // 1 means normal 2:1 refinement restriction, larger means slower
    // refinement.
    nCellsBetweenLevels 3;


    // Explicit feature edge refinement
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    // Specifies a level for any cell intersected by its edges.
    // This is a featureEdgeMesh, read from constant/triSurface for now.
    features
    (
        {
            file &quot;motorBike.eMesh&quot;;
            level 6;
        }
    );


    // Surface based refinement
    // ~~~~~~~~~~~~~~~~~~~~~~~~

    // Specifies two levels for every surface. The first is the minimum level,
    // every cell intersecting a surface gets refined up to the minimum level.
    // The second level is the maximum level. Cells that &#x27;see&#x27; multiple
    // intersections where the intersections make an
    // angle &gt; resolveFeatureAngle get refined up to the maximum level.

    refinementSurfaces
    {
        motorBike
        {
            // Surface-wise min and max refinement level
            level (5 6);

            // Optional specification of patch type (default is wall). No
            // constraint types (cyclic, symmetry) etc. are allowed.
            patchInfo
            {
                type wall;
                inGroups (motorBikeGroup);
            }
        }
    }

    // Resolve sharp angles
    resolveFeatureAngle 30;


    // Region-wise refinement
    // ~~~~~~~~~~~~~~~~~~~~~~

    // Specifies refinement level for cells in relation to a surface. One of
    // three modes
    // - distance. &#x27;levels&#x27; specifies per distance to the surface the
    //   wanted refinement level. The distances need to be specified in
    //   descending order.
    // - inside. &#x27;levels&#x27; is only one entry and only the level is used. All
    //   cells inside the surface get refined up to the level. The surface
    //   needs to be closed for this to be possible.
    // - outside. Same but cells outside.

    refinementRegions
    {
        refinementBox
        {
            mode inside;
            levels ((1E15 4));
        }
    }


    // Mesh selection
    // ~~~~~~~~~~~~~~

    // After refinement patches get added for all refinementSurfaces and
    // all cells intersecting the surfaces get put into these patches. The
    // section reachable from the locationInMesh is kept.
    // NOTE: This point should never be on a face, always inside a cell, even
    // after refinement.
    locationInMesh (3.0001 3.0001 0.43);


    // Whether any faceZones (as specified in the refinementSurfaces)
    // are only on the boundary of corresponding cellZones or also allow
    // free-standing zone faces. Not used if there are no faceZones.
    allowFreeStandingZoneFaces true;
}


// Settings for the snapping.
snapControls
{
    //- Number of patch smoothing iterations before finding correspondence
    //  to surface
    nSmoothPatch 3;

    //- Relative distance for points to be attracted by surface feature point
    //  or edge. True distance is this factor times local
    //  maximum edge length.
    tolerance 2.0;

    //- Number of mesh displacement relaxation iterations.
    nSolveIter 30;

    //- Maximum number of snapping relaxation iterations. Should stop
    //  before upon reaching a correct mesh.
    nRelaxIter 5;

    // Feature snapping

        //- Number of feature edge snapping iterations.
        //  Leave out altogether to disable.
        nFeatureSnapIter 10;

        //- Detect (geometric only) features by sampling the surface
        //  (default=false).
        implicitFeatureSnap false;

        //- Use castellatedMeshControls::features (default = true)
        explicitFeatureSnap true;

        //- Detect points on multiple surfaces (only for explicitFeatureSnap)
        multiRegionFeatureSnap false;
}


// Settings for the layer addition.
addLayersControls
{
    // Are the thickness parameters below relative to the undistorted
    // size of the refined cell outside layer (true) or absolute sizes (false).
    relativeSizes true;

    // Per final patch (so not geometry!) the layer information
    layers
    {
        &quot;(lowerWall|motorBike).*&quot;
        {
            nSurfaceLayers 1;
        }
    }

    // Expansion factor for layer mesh
    expansionRatio 1.0;

    // Wanted thickness of final added cell layer. If multiple layers
    // is the thickness of the layer furthest away from the wall.
    // Relative to undistorted size of cell outside layer.
    // See relativeSizes parameter.
    finalLayerThickness 0.3;

    // Minimum thickness of cell layer. If for any reason layer
    // cannot be above minThickness do not add layer.
    // Relative to undistorted size of cell outside layer.
    minThickness 0.1;

    // If points get not extruded do nGrow layers of connected faces that are
    // also not grown. This helps convergence of the layer addition process
    // close to features.
    // Note: changed(corrected) w.r.t 1.7.x! (didn&#x27;t do anything in 1.7.x)
    nGrow 0;

    // Advanced settings

    // When not to extrude surface. 0 is flat surface, 90 is when two faces
    // are perpendicular
    featureAngle 60;

    // At non-patched sides allow mesh to slip if extrusion direction makes
    // angle larger than slipFeatureAngle.
    slipFeatureAngle 30;

    // Maximum number of snapping relaxation iterations. Should stop
    // before upon reaching a correct mesh.
    nRelaxIter 3;

    // Number of smoothing iterations of surface normals
    nSmoothSurfaceNormals 1;

    // Number of smoothing iterations of interior mesh movement direction
    nSmoothNormals 3;

    // Smooth layer thickness over surface patches
    nSmoothThickness 10;

    // Stop layer growth on highly warped cells
    maxFaceThicknessRatio 0.5;

    // Reduce layer growth where ratio thickness to medial
    // distance is large
    maxThicknessToMedialRatio 0.3;

    // Angle used to pick up medial axis points
    // Note: changed(corrected) w.r.t 1.7.x! 90 degrees corresponds to 130
    // in 1.7.x.
    minMedialAxisAngle 90;


    // Create buffer region for new layer terminations
    nBufferCellsNoExtrude 0;


    // Overall max number of layer addition iterations. The mesher will exit
    // if it reaches this number of iterations; possibly with an illegal
    // mesh.
    nLayerIter 50;
}


// Generic mesh quality settings. At any undoable phase these determine
// where to undo.
meshQualityControls
{
    #include &quot;meshQualityDict&quot;


    // Advanced

    //- Number of error distribution iterations
    nSmoothScale 4;
    //- Amount to scale back displacement at error points
    errorReduction 0.75;
}


// Advanced

// Write flags
writeFlags
(
    scalarLevels
    layerSets
    layerFields     // write volScalarField for layer coverage
);


// Merge tolerance. Is fraction of overall bounding box of initial mesh.
// Note: the write tolerance needs to be higher than this.
mergeTolerance 1e-6;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/snappyHexMesh/faceZoneRegions</summary><p>这个网格示例演示表面区域命名与 faceZone/cellZone 的生成，便于后续把旋转区与固定区分开。</p>
<ul>
<li>开头 <code>#includeEtc</code> 引入 snappyHexMesh 的公共默认配置，本地条目作具体覆盖。</li>
<li><code>castellatedMesh on</code>、<code>snap on</code>、<code>addLayers off</code> 表示生成并贴合网格，本次不长层。</li>
<li><code>fixed.obj/regions</code> 将原始区域映射为 <code>slipWall</code>、<code>outlet</code>、<code>inlet</code>，同时可以指定各区加密级别。</li>
<li><code>rotatingZone</code> 的 <code>cellZoneInside inside</code> 选取内部单元，<code>faceZoneNaming region</code> 按区域命名相关面区。</li>
<li><code>strictRegionSnap true</code> 强调贴合时的区域对应，<code>locationInMesh</code> 决定保留连通域。</li>
</ul>
<p>更换表面文件时逐项对应 region 名称；区域正确后再设置旋转或耦合边界。</p>
<p><a href="/assets/examples/v2512/snappyhexmeshdict/2-snappyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/faceZoneRegions/system/snappyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/faceZoneRegions">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      snappyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#includeEtc &quot;caseDicts/mesh/generation/snappyHexMeshDict.cfg&quot;

castellatedMesh on;
snap            on;
addLayers       off;

geometry
{
    dummy
    {
        type    box;
        min     (0 0 0);
        max     (1 1 1);
    }
    fixed.obj
    {
        // Rename some of the regions inside the obj file
        type triSurfaceMesh;
        name fixed;
        regions
        {
            patch0 { name slipWall; }
            patch1 { name outlet; }
            patch2 { name inlet; }
        }
    }

    box-randomAligned.stl
    {
        // Rename some of the regions inside the obj file
        type triSurfaceMesh;
        name rotatingZone;
        regions
        {
            front { name myFront; }
        }
    }
}

castellatedMeshControls
{
    features
    (
      { file &quot;fixed.eMesh&quot;; level 2; }
      { file &quot;rotatingZone.eMesh&quot;; level 4; }
    );

    refinementSurfaces
    {
        fixed
        {
            level       (2 2);
            patchInfo   { type wall; }
            inGroups    (fixed);

            // Override per-patch information
            regions
            {
                patch0
                {
                    level (3 3);
                    patchInfo { type patch; }
                }

                patch1
                {
                    level (2 2);
                    patchInfo { type patch; }
                }

                patch2
                {
                    level (2 2);
                    patchInfo { type patch; }
                }
            }
        }
        rotatingZone
        {
            level       (4 4);

            // How to handle faceZones
            //  a. no faceZone. No keyword &#x27;faceZone&#x27; or &#x27;faceZoneNaming&#x27;
            //  b. single user-specified faceZone:
            //      faceZone myZone;
            //  c. faceZones according to the surface/region:
            //      faceZoneNaming region;

            // c. faceZones according to the surface/region
            faceZoneNaming  region;

            cellZone    rotatingZone;
            cellZoneInside  inside;
        }

    }

    refinementRegions
    {
        fixed
        {
            mode inside;
            levels ((1e-5 1));
        }
        rotatingZone
        {
            mode inside;
            levels ((1e-5 4));
        }
    }

    locationInMesh (1e-5 -1e-2 1e-5);// Offset from (0 0 0) to avoid
                                     // coinciding with face or edge and keep
                                     // away from disk itself

    allowFreeStandingZoneFaces  false;

    // Optional: switch off topological test for cells to-be-squashed
    //           and use geometric test instead
    useTopologicalSnapDetection false;
}

snapControls
{
    tolerance 1.0;
    implicitFeatureSnap     true;
    strictRegionSnap        true;
}

addLayersControls
{
    layers
    {
    }

    relativeSizes       true; // false, usually with firstLayerThickness
    expansionRatio      1.2;
    finalLayerThickness 0.5;
    minThickness        1e-3;
}

meshQualityControls
{
//    minTetQuality -1e+30;
}


mergeTolerance 1e-6;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · mesh/snappyHexMesh/gap_detection</summary><p>gap_detection 主要检查窄间隙加密，配置只执行切割加密阶段。</p>
<ul>
<li><code>castellatedMesh true</code>、<code>snap false</code>、<code>addLayers false</code> 将测试集中在间隙识别。</li>
<li><code>mech_test.obj</code> 提供几何；普通表面级别 <code>(0 0)</code>，间隙细化另由 <code>gapLevel (4 0 10)</code> 控制。</li>
<li><code>gapMode outside</code> 指定间隙检测所考虑的一侧，<code>nCellsBetweenLevels 1</code> 使级别过渡较紧凑。</li>
<li><code>locationInMesh (-100 -5 -300)</code> 选择需要保留的流体连通区域；<code>maxGlobalCells 2000000</code> 限制规模。</li>
</ul>
<p>细小间隙可能迅速增加单元数，先检查间隙内实际网格层数，再调整 gapLevel 和总体单元上限。</p>
<p><a href="/assets/examples/v2512/snappyhexmeshdict/3-snappyHexMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/gap_detection/system/snappyHexMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/gap_detection">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      snappyHexMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Which of the steps to run
castellatedMesh true;
snap            false;
addLayers       false;


// Geometry. Definition of all surfaces. All surfaces are of class
// searchableSurface.
// Surfaces are used
// - to specify refinement for any mesh cell intersecting it
// - to specify refinement for any mesh cell inside/outside/near
// - to &#x27;snap&#x27; the mesh boundary to the surface
geometry
{
    mech_test.obj
    {
        type triSurfaceMesh;
    }
    all
    {
        type box;
        min  (-1000 -1000 -1000);
        max  (1000 1000 1000);
    }
}


// Settings for the castellatedMesh generation.
castellatedMeshControls
{

    // Refinement parameters
    // ~~~~~~~~~~~~~~~~~~~~~

    // If local number of cells is &gt;= maxLocalCells on any processor
    // switches from from refinement followed by balancing
    // (current method) to (weighted) balancing before refinement.
    maxLocalCells 100000;

    // Overall cell limit (approximately). Refinement will stop immediately
    // upon reaching this number so a refinement level might not complete.
    // Note that this is the number of cells before removing the part which
    // is not &#x27;visible&#x27; from the keepPoint. The final number of cells might
    // actually be a lot less.
    maxGlobalCells 2000000;

    // The surface refinement loop might spend lots of iterations refining just a
    // few cells. This setting will cause refinement to stop if &lt;= minimumRefine
    // are selected for refinement. Note: it will at least do one iteration
    // (unless the number of cells to refine is 0)
    minRefinementCells 0;

    // Number of buffer layers between different levels.
    // 1 means normal 2:1 refinement restriction, larger means slower
    // refinement.
    nCellsBetweenLevels 1;


    // Explicit feature edge refinement
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    // Specifies a level for any cell intersected by its edges.
    // This is a featureEdgeMesh, read from constant/triSurface for now.
    features
    (
    );


    // Surface based refinement
    // ~~~~~~~~~~~~~~~~~~~~~~~~

    // Specifies two levels for every surface. The first is the minimum level,
    // every cell intersecting a surface gets refined up to the minimum level.
    // The second level is the maximum level. Cells that &#x27;see&#x27; multiple
    // intersections where the intersections make an
    // angle &gt; resolveFeatureAngle get refined up to the maximum level.

    refinementSurfaces
    {
        mech_test.obj
        {
            // Surface-wise min and max refinement level
            level (0 0);
        }
    }

    // Resolve sharp angles
    resolveFeatureAngle 60;


    // Region-wise refinement
    // ~~~~~~~~~~~~~~~~~~~~~~

    // Specifies refinement level for cells in relation to a surface. One of
    // three modes
    // - distance. &#x27;levels&#x27; specifies per distance to the surface the
    //   wanted refinement level. The distances need to be specified in
    //   descending order.
    // - inside. &#x27;levels&#x27; is only one entry and only the level is used. All
    //   cells inside the surface get refined up to the level. The surface
    //   needs to be closed for this to be possible.
    // - outside. Same but cells outside.

    refinementRegions
    {
        all
        {
            mode        inside;

            // Dummy base level
            levels      ((10000 0));

            // If cells
            // - have level 0..9
            // - and are in a gap &lt; 3 cell sizes across
            // - with the gap on the inside (&#x27;inside&#x27;), outside (&#x27;outside&#x27;)
            //   or both (&#x27;mixed&#x27;) of the surface
            // refine them
            gapLevel    (4 0 10);
            gapMode     outside;
        }
    }


    // Mesh selection
    // ~~~~~~~~~~~~~~

    // After refinement patches get added for all refinementSurfaces and
    // all cells intersecting the surfaces get put into these patches. The
    // section reachable from the locationInMesh is kept.
    // NOTE: This point should never be on a face, always inside a cell, even
    // after refinement.
    locationInMesh (-100 -5 -300);


    // Whether any faceZones (as specified in the refinementSurfaces)
    // are only on the boundary of corresponding cellZones or also allow
    // free-standing zone faces. Not used if there are no faceZones.
    allowFreeStandingZoneFaces false;
}


// Settings for the snapping.
snapControls
{
    //- Number of patch smoothing iterations before finding correspondence
    //  to surface
    nSmoothPatch 3;

    //- Relative distance for points to be attracted by surface feature point
    //  or edge. True distance is this factor times local
    //  maximum edge length.
    tolerance 2.0;

    //- Number of mesh displacement relaxation iterations.
    nSolveIter 30;

    //- Maximum number of snapping relaxation iterations. Should stop
    //  before upon reaching a correct mesh.
    nRelaxIter 5;


    // Feature snapping

        //- Number of feature edge snapping iterations.
        //  Leave out altogether to disable.
        nFeatureSnapIter 10;

        //- Detect (geometric) features by sampling the surface (default=false)
        implicitFeatureSnap true;

        //- Use castellatedMeshControls::features (default = true)
        explicitFeatureSnap false;
}


// Settings for the layer addition.
addLayersControls
{
    // Are the thickness parameters below relative to the undistorted
    // size of the refined cell outside layer (true) or absolute sizes (false).
    relativeSizes true;

    // Per final patch (so not geometry!) the layer information
    layers
    {
    }

    // Expansion factor for layer mesh
    expansionRatio 1.0;

    // Wanted thickness of final added cell layer. If multiple layers
    // is the thickness of the layer furthest away from the wall.
    // Relative to undistorted size of cell outside layer.
    // is the thickness of the layer furthest away from the wall.
    // See relativeSizes parameter.
    finalLayerThickness 0.5;

    // Minimum thickness of cell layer. If for any reason layer
    // cannot be above minThickness do not add layer.
    // Relative to undistorted size of cell outside layer.
    // See relativeSizes parameter.
    minThickness 0.25;

    // If points get not extruded do nGrow layers of connected faces that are
    // also not grown. This helps convergence of the layer addition process
    // close to features.
    // Note: changed(corrected) w.r.t 1.7.x! (didn&#x27;t do anything in 1.7.x)
    nGrow 0;


    // Advanced settings

    // When not to extrude surface. 0 is flat surface, 90 is when two faces
    // are perpendicular
    featureAngle 60;

    // Maximum number of snapping relaxation iterations. Should stop
    // before upon reaching a correct mesh.
    nRelaxIter 5;

    // Number of smoothing iterations of surface normals
    nSmoothSurfaceNormals 1;

    // Number of smoothing iterations of interior mesh movement direction
    nSmoothNormals 3;

    // Smooth layer thickness over surface patches
    nSmoothThickness 10;

    // Stop layer growth on highly warped cells
    maxFaceThicknessRatio 0.5;

    // Reduce layer growth where ratio thickness to medial
    // distance is large
    maxThicknessToMedialRatio 0.3;

    // Angle used to pick up medial axis points
    // Note: changed(corrected) w.r.t 16x! 90 degrees corresponds to 130 in 16x.
    minMedialAxisAngle 90;

    // Create buffer region for new layer terminations
    nBufferCellsNoExtrude 0;


    // Overall max number of layer addition iterations. The mesher will exit
    // if it reaches this number of iterations; possibly with an illegal
    // mesh.
    nLayerIter 50;
}


// Generic mesh quality settings. At any undoable phase these determine
// where to undo.
meshQualityControls
{
    #include &quot;meshQualityDict&quot;

    // Advanced

    //- Number of error distribution iterations
    nSmoothScale 4;
    //- amount to scale back displacement at error points
    errorReduction 0.75;
}


// Advanced

// Merge tolerance. Is fraction of overall bounding box of initial mesh.
// Note: the write tolerance needs to be higher than this.
mergeTolerance 1e-6;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/snappyhexmesh/">snappyHexMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
