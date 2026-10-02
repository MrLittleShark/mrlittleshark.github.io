---
title: "collapseDict"
layout: reference
description: "网格边或面塌缩操作的控制参数。"
dictionary: true
cms_slug: "dictionary-collapsedict"
---

<p>网格边或面塌缩操作的控制参数。</p><p>位置：<code>system/collapseDict</code></p><h2>配置实例</h2><p>compressible/rhoCentralFoam/biconic25-55Run35 中的 collapseDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      collapseDict;
}

collapseEdgesCoeffs
{
    // Edges shorter than this absolute value will be merged
    minimumEdgeLength   2e-7;

    // The maximum angle between two edges that share a point attached to
    // no other edges
    maximumMergeAngle   5;
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · compressible/rhoCentralFoam/biconic25-55Run35</summary><p>双锥超声速外流网格可能在几何拼接处产生很短的边。collapseDict 为边合并操作提供尺度和角度条件。</p>
<ul>
<li><code>minEdgeLen 2e-7</code> 将 0.2 μm 作为短边处理尺度，适合这个细尺度几何网格。</li>
<li><code>maxMergeAngle 5</code> 限制可合并边之间的角度，使明显的几何折角得到保留。</li>
<li>这两个条件共同决定哪些局部细小边适合合并；它们应与模型的最小有效几何尺寸比较。</li>
</ul>
<p>修改后查看锥尖、两段锥面交界和近壁网格，确认短边减少，同时关键几何形状保持正确。</p>
<p><a href="/assets/examples/v2512/collapsedict/1-collapseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoCentralFoam/biconic25-55Run35/system/collapseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoCentralFoam/biconic25-55Run35">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      collapseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

collapseEdgesCoeffs
{
    // Edges shorter than this absolute value will be merged
    minimumEdgeLength   2e-7;

    // The maximum angle between two edges that share a point attached to
    // no other edges
    maximumMergeAngle   5;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · mesh/foamyHexMesh/mixerVessel</summary><p>mixerVessel 的 foamyHexMesh 网格在生成后通过边、面折叠改善局部单元形状。这个文件控制折叠强度及质量检查。</p>
<ul>
<li><code>controlMeshQuality on</code> 将 meshQualityDict 中的质量约束纳入折叠过程。</li>
<li><code>minEdgeLen 1e-6</code> 标记微小边，<code>maxMergeAngle 180</code> 放宽角度条件；最终是否接受仍受网格质量检查影响。</li>
<li><code>initialFaceLengthFactor 1</code>、<code>maxCollapseFaceToPointSideLengthCoeff 0.3</code> 控制面折叠尺度，earlyCollapse 配置允许提前处理部分小面。</li>
<li><code>edgeReductionFactor 0.5</code>、<code>faceReductionFactor 0.5</code> 在尝试过程中收紧尺度，<code>maxIterations 10</code> 限定最大处理轮数。</li>
</ul>
<p>若叶片附近细节被过度简化，先降低相关长度系数，并比较处理前后的最差单元位置与数量。</p>
<p><a href="/assets/examples/v2512/collapsedict/2-collapseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/collapseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object          collapseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// If on, after collapsing check the quality of the mesh. If bad faces are
// generated then redo the collapsing with stricter filtering.
controlMeshQuality      on;

collapseEdgesCoeffs
{
    // Edges shorter than this absolute value will be merged
    minimumEdgeLength   1e-6;

    // The maximum angle between two edges that share a point attached to
    // no other edges
    maximumMergeAngle   180;
}


collapseFacesCoeffs
{
    // The initial face length factor
    initialFaceLengthFactor                 1;

    // If the face can&#x27;t be collapsed to an edge, and it has a span less than
    // the target face length multiplied by this coefficient, collapse it
    // to a point.
    maxCollapseFaceToPointSideLengthCoeff   0.3;

    // Allow early collapse of edges to a point
    allowEarlyCollapseToPoint               on;

    // Fraction to premultiply maxCollapseFaceToPointSideLengthCoeff by if
    // allowEarlyCollapseToPoint is enabled
    allowEarlyCollapseCoeff                 0.2;

    // Defining how close to the midpoint (M) of the projected
    // vertices line a projected vertex (X) can be before making this
    // an invalid edge collapse
    //
    // X---X-g----------------M----X-----------g----X--X
    //
    // Only allow a collapse if all projected vertices are outwith
    // guardFraction (g) of the distance form the face centre to the
    // furthest vertex in the considered direction
    guardFraction                           0.1;
}


controlMeshQualityCoeffs
{
    // Name of the dictionary that has the mesh quality coefficients used
    // by motionSmoother::checkMesh
    #include                    &quot;meshQualityDict&quot;;

    // The amount that minimumEdgeLength will be reduced by for each
    // edge if that edge&#x27;s collapse generates a poor quality face
    edgeReductionFactor         0.5;

    // The amount that initialFaceLengthFactor will be reduced by for each
    // face if its collapse generates a poor quality face
    faceReductionFactor         0.5;

    // Maximum number of outer iterations is mesh quality checking is enabled
    maximumIterations           10;

    maximumSmoothingIterations  1;

    maxPointErrorCount          3;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/porousSimpleFoam/straightDuctImplicit</summary><p>straightDuctImplicit 用面折叠整理多面体管道网格，重点是消除局部小面并满足质量要求。</p>
<ul>
<li><code>controlMeshQuality on</code> 读取同目录 meshQualityDict，约束每次网格修改。</li>
<li><code>minEdgeLen 1e-6</code>、<code>maxMergeAngle 180</code> 设置短边处理条件。</li>
<li><code>initialFaceLengthFactor 0.35</code> 比系数 1 的配置使用更小的初始面折叠尺度，适合保留管道局部结构。</li>
<li>边与面尺度的 reductionFactor 均为 0.5，最多执行 10 轮；<code>maxSmoothingIterations 1</code> 限制每轮平滑次数。</li>
</ul>
<p>调整时同时查看管壁形状、网格非正交性和极小体积单元，依据具体缺陷选择长度参数。</p>
<p><a href="/assets/examples/v2512/collapsedict/3-collapseDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/collapseDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object          collapseDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// If on, after collapsing check the quality of the mesh. If bad faces are
// generated then redo the collapsing with stricter filtering.
controlMeshQuality      on;

collapseEdgesCoeffs
{
    // Edges shorter than this absolute value will be merged
    minimumEdgeLength   1e-6;

    // The maximum angle between two edges that share a point attached to
    // no other edges
    maximumMergeAngle   180;
}


collapseFacesCoeffs
{
    // The initial face length factor
    initialFaceLengthFactor                 0.35;

    // If the face can&#x27;t be collapsed to an edge, and it has a span less than
    // the target face length multiplied by this coefficient, collapse it
    // to a point.
    maxCollapseFaceToPointSideLengthCoeff   0.3;

    // Allow early collapse of edges to a point
    allowEarlyCollapseToPoint               on;

    // Fraction to premultiply maxCollapseFaceToPointSideLengthCoeff by if
    // allowEarlyCollapseToPoint is enabled
    allowEarlyCollapseCoeff                 0.2;

    // Defining how close to the midpoint (M) of the projected
    // vertices line a projected vertex (X) can be before making this
    // an invalid edge collapse
    //
    // X---X-g----------------M----X-----------g----X--X
    //
    // Only allow a collapse if all projected vertices are outwith
    // guardFraction (g) of the distance form the face centre to the
    // furthest vertex in the considered direction
    guardFraction                           0.1;
}


controlMeshQualityCoeffs
{
    // Name of the dictionary that has the mesh quality coefficients used
    // by motionSmoother::checkMesh
    #include                    &quot;meshQualityDict&quot;;

    // The amount that minimumEdgeLength will be reduced by for each
    // edge if that edge&#x27;s collapse generates a poor quality face
    edgeReductionFactor         0.5;

    // The amount that initialFaceLengthFactor will be reduced by for each
    // face if its collapse generates a poor quality face
    faceReductionFactor         0.5;

    // Maximum number of outer iterations is mesh quality checking is enabled
    maximumIterations           10;

    maximumSmoothingIterations  1;

    maxPointErrorCount          3;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/collapseedges/">collapseEdges</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
