---
title: "wclean · 清理当前源码目标的编译中间文件"
layout: reference
description: "清理当前源码目标的编译中间文件。"
cms_slug: "command-wclean"
---

<p>清理当前源码目标的编译中间文件。</p><h2>开始前</h2>
<p>在个人源码副本中清理编译中间文件。它读取当前配置 WM_OPTIONS，Make/files 和 Make/options 是输入文件。</p>
<h2>示例 1：清理当前应用</h2>
<pre><code class="language-bash">cd myUtility
wclean
</code></pre>
<p>清理当前编译配置的中间目录及生成的 lnInclude。</p>
<h2>示例 2：从父目录清理</h2>
<pre><code class="language-bash">wclean myUtility
</code></pre>
<p>显式指定源码目录，当前工作目录不变。</p>
<h2>示例 3：清理库构建</h2>
<pre><code class="language-bash">wclean libso myLibrary
</code></pre>
<p>以库目标清理对应编译产物，再次构建可运行 wmake libso。</p>
<h2>示例 4：清理整个开发树</h2>
<pre><code class="language-bash">wclean -all user-project
</code></pre>
<p>递归执行子目录清理或已有 Allwclean/Allclean；user-project 为自己的源码副本。</p>
<h2>示例 5：清除空中间目录</h2>
<pre><code class="language-bash">wclean empty myUtility
</code></pre>
<p>清理空子目录，适用于移动或移除源文件后的目录整理。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-a | -all</code></td><td>清理全部子目录；存在 Allwclean 或 Allclean 时调用相应脚本。</td></tr><tr><td><code>-s | -silent</code></td><td>为兼容 wmake 而保留的静默选项，当前会被忽略。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr><tr><td><code>-build</code></td><td>删除指定的 build/ 中间产物目录。</td></tr><tr><td><code>-platform</code></td><td>删除指定的 platforms/ 中间产物目录。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wclean">源码与说明</a> · <a href="/assets/command-help/wclean.txt">帮助文本</a></p>
