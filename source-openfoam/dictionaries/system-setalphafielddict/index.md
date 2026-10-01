---
title: "system/setAlphaFieldDict"
layout: "reference"
description: "比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/setAlphaFieldDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>field</code> · <code>surfaces</code> · <code>plane</code> · <code>sphere</code></p><h2>关联命令</h2><p><a href="/commands/?q=setAlphaField">setAlphaField</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/setAlphaFieldDict -keywords
setAlphaField -help</code></pre><h2>17.12 setAlphaFieldDict</h2><pre><code>field       alpha.water;
type        sphere;            // sphere / plane / cylinder / sin
origin      (0.5 0.5 0);
radius      0.15;
direction   (1 0 0);</code></pre>
<p>比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。</p>
{% endraw %}