---
title: "system/changeDictionaryDict"
layout: "reference"
description: "dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/changeDictionaryDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dictionaryReplacement</code> · <code>boundaryField</code></p><h2>关联命令</h2><p><a href="/commands/?q=changeDictionary">changeDictionary</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/changeDictionaryDict -keywords
changeDictionary -help</code></pre><h2>7.13 system/changeDictionaryDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object changeDictionaryDict;
}
dictionaryReplacement
{
    U
    {
        boundaryField
        {
            inlet { type fixedValue; value uniform (2 0 0); }
        }
    }
}</code></pre>
<p>dictionaryReplacement 按目标文件名组织替换条目，运行 changeDictionary 后写回相应文件。-instance 指定目标实例目录。单个键值可直接通过 foamDictionary 修改。</p>
<h2>17.10 changeDictionaryDict</h2><pre><code>dictionaryReplacement
{
    boundary
    {
        minZ { type wall; }
    }
    U
    {
        boundaryField
        {
            &quot;(inlet|outlet)&quot; { type zeroGradient; }
        }
    }
}</code></pre>
<p>多区域算例（chtMultiRegionFoam）里，每个 region 一份，放在 system/&lt;region&gt;/changeDictionaryDict。</p>
{% endraw %}