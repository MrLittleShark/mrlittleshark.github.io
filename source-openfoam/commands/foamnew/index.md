---
title: "foamNew · 示例生成 MyModel.H"
layout: reference
description: "示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。"
cms_slug: "command-foamnew"
---

<p>示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。</p><h2>开始前</h2>
<p>在独立源码练习目录操作，目标文件名不能已存在。source 生成普通类，template 生成带模板参数的类。</p>
<h2>示例 1：生成类声明</h2>
<pre><code class="language-bash">foamNew source H myModel
</code></pre>
<p>生成 myModel.H，并替换模板中的类名。</p>
<h2>示例 2：生成类实现</h2>
<pre><code class="language-bash">foamNew source C myModel
</code></pre>
<p>生成 myModel.C，与上一例声明配套，成员逻辑仍需自行填写。</p>
<h2>示例 3：生成内联成员文件</h2>
<pre><code class="language-bash">foamNew source I myModel
</code></pre>
<p>生成 myModelI.H，适合放入短内联成员实现。</p>
<h2>示例 4：生成模板类头文件</h2>
<pre><code class="language-bash">foamNew template H fieldAccumulator Type
</code></pre>
<p>Type 是模板参数名，生成 fieldAccumulator.H。</p>
<h2>示例 5：生成模板类实现</h2>
<pre><code class="language-bash">foamNew template C fieldAccumulator Type
</code></pre>
<p>生成配套 fieldAccumulator.C，模板参数与声明保持一致。</p>
<h2>示例 6：查看应用模板</h2>
<pre><code class="language-bash">foamNew source App -preview
</code></pre>
<p>类名以短横线开头时仅输出原始模板，便于先阅读应用入口结构。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNew">源码与说明</a> · <a href="/assets/command-help/foamnew.txt">帮助文本</a></p>
