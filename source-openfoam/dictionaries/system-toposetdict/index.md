---
title: "system/topoSetDict"
layout: "reference"
description: "常用 source 一览"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/topoSetDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>actions</code> · <code>name</code> · <code>type</code> · <code>action</code> · <code>source</code> · <code>sourceInfo</code> · <code>cellSet</code> · <code>faceSet</code> · <code>cellZoneSet</code></p><h2>关联命令</h2><p><a href="/commands/?q=topoSet">topoSet</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/topoSetDict -keywords
topoSet -help</code></pre><h2>7.7 system/topoSetDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object topoSetDict;
}
actions
(
    {
        name heaterCells;
        type cellSet;
        action new;
        source boxToCell;
        box (0.2 0 0) (0.4 0.1 0.01);
    }
    {
        name heater;
        type cellZoneSet;
        action new;
        source setToCellZone;
        set heaterCells;
    }
);</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置方法与取值</th></tr>
<tr><td>name</td><td>输出集合或区域名称</td><td>与源项中的 cellZone 匹配</td></tr>
<tr><td>type</td><td>对象类别</td><td>cellSet、faceSet、pointSet、cellZoneSet、faceZoneSet</td></tr>
<tr><td>action</td><td>集合操作</td><td>new、add、subtract、subset、invert、clear、remove</td></tr>
<tr><td>source</td><td>选择算法</td><td>boxToCell、sphereToCell、cylinderToCell、patchToFace、fieldToCell 等</td></tr>
<tr><td>sourceInfo</td><td>选择源参数子字典</td><td>多数选择源可将参数直接写入动作字典；名称冲突时采用 sourceInfo</td></tr>
</table></div>
<h2>17.3 topoSetDict（选择集合）</h2><pre><code>actions
(
    {
        name    c0;
        type    cellSet;        // cellSet / faceSet / pointSet / cellZoneSet / faceZoneSet
        action  new;            // new / add / subtract / subset / invert / clear / remove
        source  boxToCell;
        box     (0 0 0) (1 1 1);
    }
    {
        name    porous;
        type    cellZoneSet;
        action  new;
        source  setToCellZone;
        set     c0;
    }
);</code></pre>
<p>常用 source 一览</p>
<div class="table-scroll"><table>
<tr><th>类别</th><th>source</th><th>关键参数</th></tr>
<tr><td>几何选单元</td><td>boxToCell</td><td>box (min) (max) 或 boxes ((..)(..))</td></tr>
<tr><td></td><td>rotatedBoxToCell</td><td>origin, i, j, k</td></tr>
<tr><td></td><td>sphereToCell</td><td>origin, radius</td></tr>
<tr><td></td><td>cylinderToCell</td><td>p1, p2, radius</td></tr>
<tr><td></td><td>surfaceToCell</td><td>file &quot;x.stl&quot;, outsidePoints, includeCut</td></tr>
<tr><td>拓扑选单元</td><td>zoneToCell / setToCell / labelToCell</td><td>zone/set/value</td></tr>
<tr><td></td><td>cellToCell</td><td>set</td></tr>
<tr><td>选面</td><td>boxToFace、patchToFace、normalToFace、cellToFace</td><td></td></tr>
<tr><td></td><td>boundaryToFace</td><td>全部边界面</td></tr>
<tr><td>选点</td><td>boxToPoint、labelToPoint、surfaceToPoint</td><td></td></tr>
<tr><td>转 zone</td><td>setToCellZone、setsToFaceZone、setToPointZone</td><td></td></tr>
</table></div>
<p>Set 与 Zone 的区别（重要）：Set 是临时选择结果，写在 constant/polyMesh/sets/；Zone 是网格的正式组成部分，写进 cellZones/faceZones。求解器里的多孔介质、MRF、fvOptions、动网格全都认 Zone 不认 Set，所以典型流程是”先 xxxToCell 造 Set，再 setToCellZone 转 Zone”。</p>
{% endraw %}