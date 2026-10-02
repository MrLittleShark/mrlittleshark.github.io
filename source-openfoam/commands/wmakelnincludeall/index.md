---
title: "wmakeLnIncludeAll · 为目录树中的库生成 lnInclude 链接目录"
layout: reference
description: "为目录树中的库生成 lnInclude 链接目录。"
cms_slug: "command-wmakelnincludeall"
---

<p>为目录树中的库生成 lnInclude 链接目录。</p><h2>开始前</h2>
<p>使用个人源码树 project-src，内部库目录的 Make/files 应有 LIB = 条目；工具据此识别库。</p>
<h2>示例 1：扫描一个源码树</h2>
<pre><code class="language-bash">wmakeLnIncludeAll project-src
</code></pre>
<p>查找库编译单元并为各库建立 lnInclude。</p>
<h2>示例 2：更新已有索引</h2>
<pre><code class="language-bash">wmakeLnIncludeAll -update project-src
</code></pre>
<p>头文件移动后更新各库链接。</p>
<h2>示例 3：限制并行任务</h2>
<pre><code class="language-bash">wmakeLnIncludeAll -j 4 project-src
</code></pre>
<p>以四个并发任务处理多个库。</p>
<h2>示例 4：为开发工具包含源码</h2>
<pre><code class="language-bash">wmakeLnIncludeAll -extra project-src
</code></pre>
<p>给库的 lnInclude 加入普通源文件索引。</p>
<h2>示例 5：处理两套用户库</h2>
<pre><code class="language-bash">wmakeLnIncludeAll -update user-models user-boundaries
</code></pre>
<p>分别扫描两个树，避免扫描整套官方源码。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-f | -force</code></td><td>Force remove of existing lnInclude before recreating</td></tr><tr><td><code>-u | -update</code></td><td>Update existing lnInclude directories</td></tr><tr><td><code>-j</code></td><td>Use all local cores/hyperthreads</td></tr><tr><td><code>-jN | -j N</code></td><td>Use N cores/hyperthreads</td></tr><tr><td><code>-extra</code></td><td>Also include all source files in lnInclude/</td></tr><tr><td><code>-no-extra</code></td><td>Do not include all source files in lnInclude/ [default]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmakeLnIncludeAll [OPTION] [dir1 .. dirN]

options:
  -f | -force       Force remove of existing lnInclude before recreating
  -u | -update      Update existing lnInclude directories
  -j                Use all local cores/hyperthreads
  -jN | -j N        Use N cores/hyperthreads
  -extra            Also include all source files in lnInclude/
  -no-extra         Do not include all source files in lnInclude/ [default]
  -help             Display short help and exit

Find directories with a &#x27;Make/files&#x27; containing a &#x27;LIB =&#x27; directive
and execute &#x27;wmakeLnInclude&#x27; for each.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnIncludeAll">源码与说明</a> · <a href="/assets/command-help/wmakelnincludeall.txt">帮助文本</a></p>
