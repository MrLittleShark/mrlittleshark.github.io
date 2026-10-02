---
title: "foamNewFunctionObject · 在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象"
layout: reference
description: "在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象。"
cms_slug: "command-foamnewfunctionobject"
---

<p>在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象。</p><h2>开始前</h2>
<p>在个人源码目录运行。生成的是开发骨架，execute/write 中的统计逻辑需自行编写。</p>
<h2>示例 1：建立统计对象</h2>
<pre><code class="language-bash">foamNewFunctionObject fieldSummary
</code></pre>
<p>生成 .H、.C、IOfieldSummary.H 和 Make 配置。</p>
<h2>示例 2：编译骨架</h2>
<pre><code class="language-bash">foamNewFunctionObject meshSummary
wmake libso meshSummary
</code></pre>
<p>生成 libmeshSummaryFunctionObject.so，通常位于 FOAM_USER_LIBBIN。</p>
<h2>示例 3：阅读运行时接口</h2>
<pre><code class="language-bash">foamNewFunctionObject timeReporter
less timeReporter/timeReporter.H
</code></pre>
<p>在头文件中查看 read、execute、write 接口，确定参数读取与输出职责。</p>
<h2>示例 4：建立独立统计原型</h2>
<pre><code class="language-bash">for name in pressureHistory velocityHistory; do foamNewFunctionObject "$name"; done
</code></pre>
<p>两个对象各自拥有编译单元，可分别添加标量与矢量统计。</p>
<h2>示例 5：把对象放进用户库目录</h2>
<pre><code class="language-bash">mkdir -p "$WM_PROJECT_USER_DIR/src/functionObjects"
cd "$WM_PROJECT_USER_DIR/src/functionObjects"
foamNewFunctionObject volumeAudit
</code></pre>
<p>以用户库形式组织项目，避免与官方源码混放。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewFunctionObject [-h | -help] &lt;functionObjectName&gt;

* Create directory with source and compilation files for a new function object
  &lt;functionObjectName&gt; (dir)
  - &lt;functionObjectName&gt;.H
  - &lt;functionObjectName&gt;.C
  - IO&lt;functionObjectName&gt;.H
  - Make (dir)
    - files
    - options
  Compiles a library named lib&lt;functionObjectName&gt;FunctionObject.so in
  \$FOAM_USER_LIBBIN:
  $FOAM_USER_LIBBIN</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewFunctionObject">源码与说明</a> · <a href="/assets/command-help/foamnewfunctionobject.txt">帮助文本</a></p>
