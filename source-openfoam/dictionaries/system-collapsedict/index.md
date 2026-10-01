---
title: "system/collapseDict · collapseDict"
layout: reference
description: "网格边或面塌缩操作的控制参数。此类操作会改变拓扑并可能损失几何特征，应在算例副本上执行，并比较操作前后的单元数、非正交性和边界完整性。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>网格边或面塌缩操作的控制参数。此类操作会改变拓扑并可能损失几何特征，应在算例副本上执行，并比较操作前后的单元数、非正交性和边界完整性。</p><figure><img src="/assets/diagrams/reference-0.svg" alt="网格配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>collapseEdgesCoeffs</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>minimumEdgeLength</td><td>Edges shorter than this absolute value will be merged</td></tr><tr><td>maximumMergeAngle</td><td>The maximum angle between two edges that share a point attached to no other edges</td></tr><tr><td>controlMeshQuality</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // If on, after collapsing check the quality of the mesh. If bad faces are generated then redo the collapsing with stricter filtering.</td></tr><tr><td>initialFaceLengthFactor</td><td>The initial face length factor</td></tr><tr><td>maxCollapseFaceToPointSideLengthCoeff</td><td>If the face can&#x27;t be collapsed to an edge, and it has a span less than the target face length multiplied by this coefficient, collapse it to a point.</td></tr><tr><td>allowEarlyCollapseToPoint</td><td>Allow early collapse of edges to a point</td></tr><tr><td>allowEarlyCollapseCoeff</td><td>Fraction to premultiply maxCollapseFaceToPointSideLengthCoeff by if allowEarlyCollapseToPoint is enabled</td></tr><tr><td>guardFraction</td><td>Only allow a collapse if all projected vertices are outwith guardFraction (g) of the distance form the face centre to the furthest vertex in the considered direction</td></tr><tr><td>edgeReductionFactor</td><td>The amount that minimumEdgeLength will be reduced by for each edge if that edge&#x27;s collapse generates a poor quality face</td></tr><tr><td>faceReductionFactor</td><td>The amount that initialFaceLengthFactor will be reduced by for each face if its collapse generates a poor quality face</td></tr><tr><td>maximumIterations</td><td>Maximum number of outer iterations is mesh quality checking is enabled</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · compressible/rhoCentralFoam/biconic25-55Run35</h3><p>原始路径：<code>tutorials/compressible/rhoCentralFoam/biconic25-55Run35/system/collapseDict</code>；求解器：<code>rhoCentralFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoCentralFoam/biconic25-55Run35/system/collapseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/collapsedict/1-collapseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoCentralFoam/biconic25-55Run35">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · mesh/foamyHexMesh/mixerVessel</h3><p>原始路径：<code>tutorials/mesh/foamyHexMesh/mixerVessel/system/collapseDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel/system/collapseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/collapsedict/2-collapseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyHexMesh/mixerVessel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;meshQualityDict&quot;;。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · incompressible/porousSimpleFoam/straightDuctImplicit</h3><p>原始路径：<code>tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/collapseDict</code>；求解器：<code>porousSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit/system/collapseDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/collapsedict/3-collapseDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/porousSimpleFoam/straightDuctImplicit">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;meshQualityDict&quot;;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/collapseedges/">collapseEdges</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/collapseDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/collapseDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
