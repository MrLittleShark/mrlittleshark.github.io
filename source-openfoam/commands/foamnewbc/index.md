---
title: "foamNewBC · 创建自定义边界条件的源码和编译配置"
layout: reference
description: "创建自定义边界条件的源码和编译配置。"
cms_slug: "command-foamnewbc"
---

<p>创建自定义边界条件的源码和编译配置。</p><h2>开始前</h2>
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
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewBC">源码与说明</a> · <a href="/assets/command-help/foamnewbc.txt">帮助文本</a></p>
