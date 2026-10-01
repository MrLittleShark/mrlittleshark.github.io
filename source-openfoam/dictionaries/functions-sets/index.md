---
title: "system/controlDict → functions → sets"
layout: "reference"
description: "转换面集合时需处理面方向信息。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/controlDict → functions → sets</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>sets</code> · <code>interpolationScheme</code> · <code>setFormat</code> · <code>fields</code> · <code>sets</code> · <code>axis</code> · <code>start</code> · <code>end</code> · <code>nPoints</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/controlDict -entry functions -value
postProcess -help</code></pre><h2>setsToZones  将集合转换为同名网格区域  源码</h2><p>转换面集合时需处理面方向信息。</p>
<p>用法：setsToZones [选项]</p>
<pre><code>示例：setsToZones</code></pre>
<h2>10.3 沿线采样</h2><pre><code>lineSample
{
    type sets;
    libs (&quot;libsampling.so&quot;);
    writeControl writeTime;
    setFormat raw;
    interpolationScheme cellPoint;
    fields (U p);
    sets
    {
        centreline
        {
            type uniform;
            axis x;
            start (0.01 0.05 0.005);
            end (0.99 0.05 0.005);
            nPoints 100;
        }
    }
}</code></pre>
<p>axis 指定输出横坐标类型，nPoints 指定采样点数，interpolationScheme 指定单元或点插值方法。</p>
{% endraw %}