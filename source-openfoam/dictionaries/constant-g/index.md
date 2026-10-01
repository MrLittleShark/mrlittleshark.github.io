---
title: "constant/g"
layout: "reference"
description: "g 定义重力矢量，其方向与几何坐标系对应。hRef 定义静水压参考高度，通常采用 uniformDimensionedScalarField 和长度量纲；pRef 按求解器接口设置。fvSolution 中的 pRefCell/pRefValue 用于压力方程参考值，作用不同。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/g</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>value</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/g -keywords
interFoam -help</code></pre><h2>9.8 重力与压力参考值</h2><pre><code>// constant/g 完整示例
FoamFile
{
    version 2.0; format ascii;
    class uniformDimensionedVectorField; object g;
}
dimensions [0 1 -2 0 0 0 0];
value (0 -9.81 0);</code></pre>
<p>g 定义重力矢量，其方向与几何坐标系对应。hRef 定义静水压参考高度，通常采用 uniformDimensionedScalarField 和长度量纲；pRef 按求解器接口设置。fvSolution 中的 pRefCell/pRefValue 用于压力方程参考值，作用不同。</p>
{% endraw %}