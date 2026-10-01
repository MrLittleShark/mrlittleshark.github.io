---
title: "constant/transportProperties"
layout: "reference"
description: "不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/transportProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>transportModel</code> · <code>nu</code> · <code>rho</code> · <code>phases</code> · <code>sigma</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/transportProperties -keywords
icoFoam -help</code></pre><h2>9.5 constant/transportProperties</h2><p>不可压缩牛顿流体的配置如下。求解器可直接读取 nu，也可通过 transportModel 创建输运模型，相应条目采用该求解器的配置结构。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object transportProperties;
}
transportModel Newtonian;
nu [0 2 -1 0 0 0 0] 1e-6;</code></pre>
<p>nu 为运动黏度，mu 为动力黏度，两者满足 \(\mu = \rho*\nu\)。powerLaw、BirdCarreau 等非牛顿模型采用各自的系数字典，参数定义见对应模型源码和教程。</p>
<p>不可压缩 VOF 的两相物性配置如下。</p>
<pre><code>phases (water air);
water { transportModel Newtonian; nu 1e-6; rho 1000; }
air   { transportModel Newtonian; nu 1.5e-5; rho 1.2; }
sigma 0.072;</code></pre>
<p>rho 表示相密度，sigma 表示表面张力系数。示例数值为常温条件下的近似示例。可压缩多相模型通常分别设置各相热物性。</p>
<h2>18.1 transportProperties（物性）</h2><p>单相不可压</p>
<pre><code>transportModel  Newtonian;
nu              [0 2 -1 0 0 0 0] 1e-05;      // 运动粘度 m²/s
// 新版也可以简写（量纲由程序推断）：nu 1e-05;</code></pre>
<p>非牛顿流体可选 CrossPowerLaw、BirdCarreau、HerschelBulkley、powerLaw，各自再跟一个系数子字典。</p>
<p>两相（interFoam）</p>
<pre><code>phases (water air);

water { transportModel Newtonian; nu 1e-06; rho 1000; }
air   { transportModel Newtonian; nu 1.48e-05; rho 1; }

sigma  0.07;          // 表面张力系数 N/m</code></pre>
<p>laplacianFoam</p>
<pre><code>DT              [0 2 -1 0 0 0 0] 4e-05;      // 扩散系数</code></pre>
{% endraw %}