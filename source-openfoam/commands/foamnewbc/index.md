---
title: "foamNewBC · 在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库"
layout: reference
description: "在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。"
cms_slug: "command-foamnewbc"
---

<p>在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。</p><h2>开始前</h2>
<p>在个人源码目录运行，名称须未存在。骨架需要填写 updateCoeffs 等具体公式；加载共享库并在字段 boundaryField 中使用注册类型。</p>
<h2>示例 1：固定值标量边界</h2>
<pre><code class="language-bash">foamNewBC fixedValue scalar heatedWall
</code></pre>
<p>生成标量 fixedValue 派生边界骨架，适合温度等标量。</p>
<h2>示例 2：固定值矢量边界</h2>
<pre><code class="language-bash">foamNewBC fixedValue vector pulsedInlet
</code></pre>
<p>生成矢量边界骨架，适合速度入口。</p>
<h2>示例 3：混合标量边界</h2>
<pre><code class="language-bash">foamNewBC mixed scalar convectiveWall
</code></pre>
<p>生成 mixed 派生类，后续设置 refValue、refGrad 与 valueFraction。</p>
<h2>示例 4：张量边界骨架</h2>
<pre><code class="language-bash">foamNewBC fixedValue symmTensor prescribedStress
</code></pre>
<p>类型为对称张量，适合对称应力场的边界开发。</p>
<h2>示例 5：建立通用模板类</h2>
<pre><code class="language-bash">foamNewBC fixedValue all uniformProfile
</code></pre>
<p>all 生成模板类，供多个字段类型使用。</p>
<h2>示例 6：编译自己的边界库</h2>
<pre><code class="language-bash">foamNewBC mixed vector vectorRobin
wmake libso vectorRobin
</code></pre>
<p>生成并编译共享库，目标由 Make/files 的 LIB 指定。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewBC [-h | -help] &lt;base&gt; &lt;type&gt; &lt;boundaryConditionName&gt;

* Create directory of source and compilation files for a new boundary condition
  &lt;boundaryConditionName&gt; (dir)
  - .C and .H source files
  - Make (dir)
    - files
    - options
  Compiles a library named lib&lt;boundaryConditionName&gt;.so in \$FOAM_USER_LIBBIN:
  $FOAM_USER_LIBBIN

&lt;base&gt; conditions:
-f | -fixedValue    | fixedValue
-m | -mixed         | mixed

&lt;type&gt; options:
-a | -all    | all  | template (creates a template class)
-s | -scalar | scalar
-v | -vector | vector
-t | -tensor | tensor
-symmTensor  | symmTensor
-sphericalTensor | sphericalTensor</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewBC">源码与说明</a> · <a href="/assets/command-help/foamnewbc.txt">帮助文本</a></p>
