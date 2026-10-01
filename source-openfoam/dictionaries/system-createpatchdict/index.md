---
title: "system/createPatchDict"
layout: "reference"
description: "constructFrom patches 从已有边界选面；constructFrom set 从指定 faceSet 选面。pointSync 控制耦合点同步。执行 createPatch -overwrite 后，将 0/U、0/p 等场文件中的边界条目与新建 walls 对应。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/createPatchDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>pointSync</code> · <code>patches</code> · <code>name</code> · <code>patchInfo</code> · <code>constructFrom</code> · <code>set</code></p><h2>关联命令</h2><p><a href="/commands/?q=createPatch">createPatch</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/createPatchDict -keywords
createPatch -help</code></pre><h2>7.8 system/createPatchDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object createPatchDict;
}
pointSync false;
patches
(
    {
        name walls;
        patchInfo { type wall; }
        constructFrom patches;
        patches (wallA wallB);
    }
);</code></pre>
<p>constructFrom patches 从已有边界选面；constructFrom set 从指定 faceSet 选面。pointSync 控制耦合点同步。执行 createPatch -overwrite 后，将 0/U、0/p 等场文件中的边界条目与新建 walls 对应。</p>
<h2>17.5 createPatchDict</h2><pre><code>pointSync false;

patches
(
    {
        name            cyclicLeft;
        patchInfo       { type cyclic; neighbourPatch cyclicRight; }
        constructFrom   patches;
        patches         (left);
    }
);</code></pre>
<p>用途：把网格转换器生成的一堆零散 patch 合并；把两个面配成周期边界；改 patch 类型。</p>
{% endraw %}