---
title: "cleanApplication · 调用 wclean 清理当前应用的编译中间文件"
layout: reference
description: "调用 wclean 清理当前应用的编译中间文件。"
cms_slug: "command-cleanapplication"
---

<p>调用 wclean 清理当前应用的编译中间文件。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。在个人源码副本中操作，函数始终对当前目录调用 wclean。</p>
<h2>示例 1：清除当前应用中间文件</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_USER_DIR/applications/utilities/fieldStats"
cleanApplication
</code></pre>
<p>移除该配置的编译中间项；Make/files 和 Make/options 保留。</p>
<h2>示例 2：修改头文件后完整重编译</h2>
<pre><code class="language-bash">cd fieldStats
cleanApplication
wmake
</code></pre>
<p>wclean 清除旧中间项，wmake 重新编译。</p>
<h2>示例 3：在子 shell 中清理</h2>
<pre><code class="language-bash">(cd fieldStats &amp;&amp; cleanApplication)
</code></pre>
<p>清理限定于 fieldStats，外层终端目录不变。</p>
<h2>示例 4：清理多个独立程序</h2>
<pre><code class="language-bash">for appDir in fieldStats meshReport; do (cd "$appDir" &amp;&amp; cleanApplication); done
</code></pre>
<p>两个目录需各自包含 Make 配置，分别清理。</p>
<h2>示例 5：清理用户动态库</h2>
<pre><code class="language-bash">cd myBoundary
cleanApplication
wmake libso
</code></pre>
<p>清理库源码后重新构建共享库，输出位置由 Make/files 的 LIB 决定。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
