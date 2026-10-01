---
title: "0/p"
layout: "reference"
description: "下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>0/p</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>fixedValue</code> · <code>zeroGradient</code> · <code>totalPressure</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary 0/p -keywords
icoFoam -help</code></pre><h2>9.1 速度场与压力场</h2><p>下例给出与第 7 章二维通道网格对应的速度和压力场。内部初始速度等于入口速度，壁面采用无滑移条件，出口速度采用零梯度条件。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class volVectorField; object U;
}
dimensions [0 1 -1 0 0 0 0];
internalField uniform (1 0 0);
boundaryField
{
    inlet { type fixedValue; value uniform (1 0 0); }
    outlet { type zeroGradient; }
    walls { type noSlip; }
    frontAndBack { type empty; }
}
FoamFile
{
    version 2.0; format ascii;
    class volScalarField; object p;
}
dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{
    inlet { type zeroGradient; }
    outlet { type fixedValue; value uniform 0; }
    walls { type zeroGradient; }
    frontAndBack { type empty; }
}</code></pre>
<p>本例 p 为运动学压力，适用于相应的不可压缩求解器。采用绝对压力的可压缩求解器时，dimensions 设为 [1 -1 -2 0 0 0 0]，压力值按状态方程设置，如 101325 Pa。</p>
{% endraw %}