---
title: "wcleanLnIncludeAll · 删除目录树中的 lnInclude 头文件链接目录"
layout: reference
description: "删除目录树中的 lnInclude 头文件链接目录。"
cms_slug: "command-wcleanlnincludeall"
---

<p>删除目录树中的 lnInclude 头文件链接目录。</p><h2>开始前</h2>
<p>只在个人源码副本中使用，此脚本移除目标树里所有名为 lnInclude 的目录。源码头文件应在其他源目录中。</p>
<h2>示例 1：清理单个库的索引</h2>
<pre><code class="language-bash">wcleanLnIncludeAll libraryA
</code></pre>
<p>删除 libraryA 内生成的 lnInclude 目录。</p>
<h2>示例 2：清理整个用户库树</h2>
<pre><code class="language-bash">wcleanLnIncludeAll user-libraries
</code></pre>
<p>递归清理各库索引，适用于目录移动后重建。</p>
<h2>示例 3：清理两组库</h2>
<pre><code class="language-bash">wcleanLnIncludeAll user-models user-boundaries
</code></pre>
<p>两个路径均作为扫描起点。</p>
<h2>示例 4：从项目内部执行</h2>
<pre><code class="language-bash">cd user-libraries
wcleanLnIncludeAll
</code></pre>
<p>无路径参数时使用当前树。</p>
<h2>示例 5：清理后重建</h2>
<pre><code class="language-bash">wcleanLnIncludeAll user-libraries
wmakeLnIncludeAll user-libraries
</code></pre>
<p>删除旧索引后按当前源码位置重建，实际头文件保留。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-h, -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wcleanLnIncludeAll">源码与说明</a> · <a href="/assets/command-help/wcleanlnincludeall.txt">帮助文本</a></p>
