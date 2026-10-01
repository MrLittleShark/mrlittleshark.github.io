---
title: "system/mapFieldsDict"
layout: "reference"
description: "mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/mapFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>patchMap</code> · <code>cuttingPatches</code></p><h2>关联命令</h2><p><a href="/commands/?q=mapFields">mapFields</a> · <a href="/commands/?q=mapFieldsPar">mapFieldsPar</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/mapFieldsDict -keywords
mapFields -help</code></pre><h2>7.12 system/mapFieldsDict</h2><p>mapFieldsDict 用于源算例与目标算例边界不一致时的场映射。patchMap 中每组名称依次为目标边界和源边界。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object mapFieldsDict;
}
patchMap
(
    inlet sourceInlet
    outlet sourceOutlet
);
cuttingPatches (newCutBoundary);</code></pre>
<p>在目标算例中执行 mapFields ../sourceCase -sourceTime latestTime。cuttingPatches 指定切穿源计算域的目标边界，其数值由源域内部插值得到。-consistent 适用于边界拓扑匹配的算例。映射体积分数等守恒量后，应检查有界性及积分守恒。</p>
<h2>17.9 mapFieldsDict</h2><pre><code>patchMap        ( inlet1 inlet );   // 源算例 patch → 目标算例 patch
cuttingPatches  ( outlet );         // 被切开的 patch（源网格不覆盖的部分）</code></pre>
<p>网格边界一致时可以完全不用这个文件，直接 mapFields ../src -consistent。</p>
{% endraw %}