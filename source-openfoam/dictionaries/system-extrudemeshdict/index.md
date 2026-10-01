---
title: "system/extrudeMeshDict"
layout: "reference"
description: "constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 m"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/extrudeMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>constructFrom</code> · <code>sourceCase</code> · <code>sourcePatches</code> · <code>exposedPatchName</code> · <code>extrudeModel</code> · <code>nLayers</code> · <code>expansionRatio</code> · <code>thickness</code></p><h2>关联命令</h2><p><a href="/commands/?q=extrudeMesh">extrudeMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/extrudeMeshDict -keywords
extrudeMesh -help</code></pre><h2>7.11 system/extrudeMeshDict</h2><p>constructFrom 指定挤出来源，sourceCase 和 sourcePatches 指定源算例及边界，exposedPatchName 定义新暴露边界。extrudeModel 选择挤出模型，nLayers 和 expansionRatio 控制层数及层厚比，mergeFaces 和 mergeTol 控制合并。linearNormal 通过 linearNormalCoeffs/thickness 设置总厚度；其他模型采用各自的系数字典。</p>
<pre><code>// 片段：沿已有 patch 外法向挤出
constructFrom patch;
sourceCase &quot;.&quot;;
sourcePatches (front);
exposedPatchName back;
extrudeModel linearNormal;
nLayers 5;
expansionRatio 1;
linearNormalCoeffs { thickness 0.01; }
mergeFaces false;
mergeTol 0;</code></pre>
<h2>17.6 extrudeMeshDict</h2><pre><code>constructFrom   patch;              // mesh / patch / surface
sourceCase      &quot;../base&quot;;
sourcePatches   (front);
exposedPatchName back;

extrudeModel    linearNormal;       // linearNormal/linearDirection/wedge/sector/plane
linearNormalCoeffs { thickness 0.01; }
sectorCoeffs   { axisPt (0 0 0); axis (0 0 1); angle 5; }

nLayers         1;
expansionRatio  1.0;
mergeFaces      false;</code></pre>
<p>典型用途：把一个二维面拉伸成一层网格做二维算例；用 sector 模型做轴对称（wedge）算例。</p>
{% endraw %}