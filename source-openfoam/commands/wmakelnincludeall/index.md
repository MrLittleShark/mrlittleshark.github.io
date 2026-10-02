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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-f | -force</code></td><td>删除已有 lnInclude 后重新创建。</td></tr><tr><td><code>-u | -update</code></td><td>更新已有 lnInclude 目录。</td></tr><tr><td><code>-j</code></td><td>使用本机全部处理器核心或硬件线程。</td></tr><tr><td><code>-jN | -j N</code></td><td>使用指定数量的处理器核心或硬件线程。</td></tr><tr><td><code>-extra</code></td><td>同时将所有源文件加入 lnInclude/。</td></tr><tr><td><code>-no-extra</code></td><td>仅包含默认类型的文件，省略其余源文件；此项为默认设置。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnIncludeAll">源码与说明</a> · <a href="/assets/command-help/wmakelnincludeall.txt">帮助文本</a></p>
