---
title: "system/fvSchemes"
layout: "reference"
description: "下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/fvSchemes</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>ddtSchemes</code> · <code>gradSchemes</code> · <code>divSchemes</code> · <code>laplacianSchemes</code> · <code>interpolationSchemes</code> · <code>snGradSchemes</code> · <code>fluxRequired</code> · <code>wallDist</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/fvSchemes -keywords
icoFoam -help</code></pre><h2>8.2 system/fvSchemes</h2><p>下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvSchemes;
}
ddtSchemes { default Euler; }
gradSchemes { default Gauss linear; }
divSchemes
{
    default none;
    div(phi,U) Gauss linearUpwind grad(U);
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
laplacianSchemes { default Gauss linear corrected; }
interpolationSchemes { default linear; }
snGradSchemes { default corrected; }
wallDist { method meshWave; }</code></pre>
<div class="table-scroll"><table>
<tr><th>字典</th><th>控制对象</th><th>常用设置</th></tr>
<tr><td>ddtSchemes</td><td>时间导数</td><td>Euler 为一阶；backward 为二阶；CrankNicolson 0.9 为混合格式；steadyState 用于稳态</td></tr>
<tr><td>gradSchemes</td><td>梯度</td><td>Gauss linear、leastSquares、cellLimited Gauss linear 1</td></tr>
<tr><td>divSchemes</td><td>对流及显式散度</td><td>Gauss upwind 耗散较强；linearUpwind 阶数较高；limitedLinear 等限制格式按字段类型选择</td></tr>
<tr><td>laplacianSchemes</td><td>扩散项</td><td>常用 Gauss linear corrected；非正交程度较高时可采用 limited 修正</td></tr>
<tr><td>interpolationSchemes</td><td>面插值</td><td>linear 等</td></tr>
<tr><td>snGradSchemes</td><td>面法向梯度</td><td>corrected、uncorrected、limited 0.5 等</td></tr>
<tr><td>fluxRequired</td><td>指定需保留通量的场</td><td>按求解器要求标记 p 等场</td></tr>
<tr><td>wallDist</td><td>壁距算法</td><td>meshWave 等</td></tr>
<tr><td>default none</td><td>无默认格式</td><td>所需离散项必须显式配置，缺失时报告错误</td></tr>
</table></div>
<p>湍流方程可采用 div(phi,k) Gauss upwind; 和 div(phi,omega) Gauss upwind;，字段名称随模型确定。VOF 求解器的 div(phi,alpha)、div(phirb,alpha) 等条目采用其配套教程的定义。rhoCentralFoam 还需设置 fluxScheme 及变量重构格式。</p>
<h2>第 13 章　system/fvSchemes（离散格式）</h2><p>它管什么：每一项微分算子用什么数值格式离散。这是精度与稳定性的主要旋钮，也是初学者最容易被卡住的地方。</p>
{% endraw %}