---
title: "system/controlDict → functions → surfaces"
layout: "reference"
description: "面采样还支持 patch、isoSurface 等类型。采用 isoSurface 时，通过字段、等值和采样算法定义所需相界面或涡结构。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/controlDict → functions → surfaces</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>surfaces</code> · <code>surfaceFormat</code> · <code>fields</code> · <code>surfaces</code> · <code>cuttingPlane</code> · <code>point</code> · <code>normal</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/controlDict -entry functions -value
postProcess -help</code></pre><h2>10.4 面采样</h2><pre><code>sectionSample
{
    type surfaces;
    libs (&quot;libsampling.so&quot;);
    writeControl writeTime;
    surfaceFormat vtk;
    fields (U p);
    interpolationScheme cellPoint;
    surfaces
    {
        midPlane
        {
            type cuttingPlane;
            planeType pointAndNormal;
            pointAndNormalDict
            {
                point (0.5 0 0);
                normal (1 0 0);
            }
            interpolate true;
        }
    }
}</code></pre>
<p>面采样还支持 patch、isoSurface 等类型。采用 isoSurface 时，通过字段、等值和采样算法定义所需相界面或涡结构。</p>
{% endraw %}