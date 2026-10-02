---
title: "wdep · 定位源文件对应的 .dep 依赖文件"
layout: reference
description: "定位源文件对应的 .dep 依赖文件。"
cms_slug: "command-wdep"
---

<p>定位源文件对应的 .dep 依赖文件。</p><h2>开始前</h2>
<p>在已经用 wmake 生成依赖的个人源码目录执行。输入为源文件名，输出为找到的 .dep 文件路径。</p>
<h2>示例 1：定位主程序依赖</h2>
<pre><code class="language-bash">cd myUtility
wdep myUtility.C
</code></pre>
<p>查找对应依赖文件，确认当前构建存放位置。</p>
<h2>示例 2：阅读依赖内容</h2>
<pre><code class="language-bash">cd myUtility
depFile=$(wdep myUtility.C)
[ -n "$depFile" ] &amp;&amp; cat "$depFile"
</code></pre>
<p>查看记录的头文件列表，便于判断 include 是否进入构建依赖。</p>
<h2>示例 3：定位子目录源码依赖</h2>
<pre><code class="language-bash">cd myLibrary
wdep models/myModel.C
</code></pre>
<p>传入相对源码路径，寻找该编译单元的依赖。</p>
<h2>示例 4：比较两个编译单元</h2>
<pre><code class="language-bash">cd myLibrary
wdep modelA.C
wdep modelB.C
</code></pre>
<p>分别返回路径，便于检查两个模块是否引用同一公共头文件。</p>
<h2>示例 5：生成依赖后查询</h2>
<pre><code class="language-bash">cd myUtility
wmake dep
wdep myUtility.C
</code></pre>
<p>先创建依赖信息，再定位文件，适用于首次构建前检查。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wdep &lt;file&gt;

Find the dep-file corresponding to &lt;file&gt; in the current directory
and print the path.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wdep">源码与说明</a> · <a href="/assets/command-help/wdep.txt">帮助文本</a></p>
