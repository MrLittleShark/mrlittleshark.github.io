---
title: "system/snappyHexMeshDict"
layout: "reference"
description: "snappyHexMesh 包括切割细化、表面贴合和边界层生成三个阶段。运行 foamGetDict snappyHexMeshDict 获取带注释模板，在已建立的背景网格上配置几何和各阶段参数。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/snappyHexMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>castellatedMesh</code> · <code>snap</code> · <code>addLayers</code> · <code>geometry</code> · <code>refinementSurfaces</code> · <code>refinementRegions</code> · <code>locationInMesh</code> · <code>nCellsBetweenLevels</code></p><h2>关联命令</h2><p><a href="/commands/?q=snappyHexMesh">snappyHexMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/snappyHexMeshDict -keywords
snappyHexMesh -help</code></pre><h2>7.2 system/snappyHexMeshDict</h2><p>snappyHexMesh 包括切割细化、表面贴合和边界层生成三个阶段。运行 foamGetDict snappyHexMeshDict 获取带注释模板，在已建立的背景网格上配置几何和各阶段参数。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>设置方法</th></tr>
<tr><td>castellatedMesh、snap、addLayers</td><td>分别控制切割细化、贴体和边界层生成</td><td>先检查切割细化和贴体，再配置边界层</td></tr>
<tr><td>geometry</td><td>表面及可搜索几何体</td><td>body.stl { type triSurfaceMesh; name body; }</td></tr>
<tr><td>maxLocalCells、maxGlobalCells</td><td>局部及全局细化控制限额</td><td>根据可用内存设置单元数量上限</td></tr>
<tr><td>minRefinementCells</td><td>停止继续细化的候选单元阈值</td><td>设为 0 时继续处理剩余细化单元，计算量相应增加</td></tr>
<tr><td>nCellsBetweenLevels</td><td>相邻细化级别间的过渡层数</td><td>例如 3</td></tr>
<tr><td>features</td><td>显式特征文件和细化等级</td><td>({ file &quot;body.eMesh&quot;; level 2; })</td></tr>
<tr><td>refinementSurfaces</td><td>表面的最小最大细化等级</td><td>body { level (2 3); patchInfo { type wall; } }</td></tr>
<tr><td>resolveFeatureAngle</td><td>区分尖锐表面特征的角度</td><td>示例为 30，按表面几何特征确定</td></tr>
<tr><td>refinementRegions</td><td>体积或距离带细化</td><td>mode inside、outside 或 distance；levels 定义等级</td></tr>
<tr><td>locationInMesh</td><td>标记需要保留的连通流体区域</td><td>取目标流体区域内部点，避开边界面</td></tr>
<tr><td>allowFreeStandingZoneFaces</td><td>是否允许独立区域面</td><td>与 zone 生成方式匹配</td></tr>
<tr><td>snapControls</td><td>贴体松弛和迭代</td><td>nSmoothPatch、tolerance、nSolveIter、nRelaxIter</td></tr>
<tr><td>显式特征贴合</td><td>explicitFeatureSnap 与 nFeatureSnapIter</td><td>与 features 中的 eMesh 配合</td></tr>
<tr><td>layers</td><td>各 patch 的层数</td><td>&quot;body.*&quot; { nSurfaceLayers 3; }</td></tr>
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
<pre><code>// 片段：放入对应的 snappyHexMeshDict
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
    features ({ file &quot;body.eMesh&quot;; level 2; });
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
<pre><code>castellatedMesh true;
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
    #includeEtc &quot;caseDicts/meshQualityDict&quot;
}
mergeTolerance 1e-6;</code></pre>
<h2>第 16 章　system/snappyHexMeshDict</h2>
{% endraw %}