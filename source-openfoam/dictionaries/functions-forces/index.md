---
title: "system/controlDict → functions → forces"
layout: "reference"
description: "下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/controlDict → functions → forces</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>forces</code> · <code>patches</code> · <code>rho</code> · <code>rhoInf</code> · <code>CofR</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/controlDict -entry functions -value
simpleFoam -help</code></pre><h2>10.5 力与力系数</h2><pre><code>bodyForces
{
    type forces;
    libs (&quot;libforces.so&quot;);
    patches (walls);
    p p;
    U U;
    rho rhoInf;
    rhoInf 1000;
    CofR (0 0 0);
    writeControl timeStep;
    writeInterval 1;
}</code></pre>
<p>下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。</p>
<p>计算力系数时，将 type 设为 forceCoeffs，并指定 liftDir、dragDir、pitchAxis、magUInf、lRef 和 Aref。若阻力沿 x 方向、升力沿 y 方向，可设置 dragDir (1 0 0); liftDir (0 1 0); pitchAxis (0 0 1);。lRef 和 Aref 分别为归一化参考长度和面积，二维算例的参考面积需计入所取厚度。</p>
{% endraw %}