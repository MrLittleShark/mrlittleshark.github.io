---
title: "system/refineMeshDict"
layout: "reference"
description: "set 指定待细化的单元集合，directions 指定细化方向。二维网格仅沿面内方向细化，厚度方向保持 empty 边界要求的单层结构。运行 refineMesh -overwrite 后，检查场、区域和边界与新网格的对应关系。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/refineMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>set</code> · <code>coordinateSystem</code> · <code>globalCoeffs</code> · <code>directions</code> · <code>useHexTopology</code> · <code>geometricCut</code></p><h2>关联命令</h2><p><a href="/commands/?q=refineMesh">refineMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/refineMeshDict -keywords
refineMesh -help</code></pre><h2>7.10 system/refineMeshDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object refineMeshDict;
}
set heaterCells;
coordinateSystem global;
globalCoeffs
{
    tan1 (1 0 0);
    tan2 (0 1 0);
}
directions (tan1 tan2);
useHexTopology true;
geometricCut false;
writeMesh false;</code></pre>
<p>set 指定待细化的单元集合，directions 指定细化方向。二维网格仅沿面内方向细化，厚度方向保持 empty 边界要求的单层结构。运行 refineMesh -overwrite 后，检查场、区域和边界与新网格的对应关系。</p>
<h2>17.8 refineMeshDict</h2><pre><code>set             c0;                 // 对哪个 cellSet 加密
coordinateSystem global;
globalCoeffs    { tan1 (1 0 0); tan2 (0 1 0); }
directions      ( tan1 tan2 );      // 只在这两个方向加密（各向异性）
useHexTopology  yes;
geometricCut    no;
writeMesh       no;
$ topoSet &amp;&amp; refineMesh -overwrite -dict system/refineMeshDict</code></pre>
{% endraw %}