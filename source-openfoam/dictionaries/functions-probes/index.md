---
title: "system/controlDict → functions → probes"
layout: "reference"
description: "探针位置应位于有效流体单元内，压力结果输出至 postProcessing/pressureProbes/起始时刻/p。冲击和快速瞬态计算需按目标时间尺度设置采样频率，以记录峰值及波形变化。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/controlDict → functions → probes</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>probes</code> · <code>libs</code> · <code>fields</code> · <code>probeLocations</code> · <code>writeControl</code> · <code>writeInterval</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/controlDict -entry functions -value
postProcess -help</code></pre><h2>10.2 点探针采样</h2><pre><code>// 放入 functions 内
pressureProbes
{
    type probes;
    libs (&quot;libsampling.so&quot;);
    writeControl timeStep;
    writeInterval 1;
    fields (p U);
    probeLocations
    (
        (0.25 0.05 0.005)
        (0.75 0.05 0.005)
    );
}</code></pre>
<p>探针位置应位于有效流体单元内，压力结果输出至 postProcessing/pressureProbes/起始时刻/p。冲击和快速瞬态计算需按目标时间尺度设置采样频率，以记录峰值及波形变化。</p>
{% endraw %}