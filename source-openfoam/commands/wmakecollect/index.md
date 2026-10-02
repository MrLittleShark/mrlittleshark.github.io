---
title: "wmakeCollect · 调度并行编译任务"
layout: reference
description: "调度并行编译任务。"
cms_slug: "command-wmakecollect"
---

<p>调度并行编译任务。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/wmakeCollect&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-clean</td><td>Cleanup before compilation (removes old makefiles)</td></tr><tr><td>-kill</td><td>Cleanup after termination (removes makefiles)</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmakeCollect [OPTION] &lt;command&gt;

options:
  -clean        Cleanup before compilation (removes old makefiles)
  -kill         Cleanup after termination (removes makefiles)
  -h | -help    Print the usage

A collecting scheduler for fast parallel compilation of large numbers of
object files.

When called with a compilation command it is written into a file in the
directory \$WM_COLLECT_DIR.

When called without a command the files in the \$WM_COLLECT_DIR directory are
combined into a single Makefile which is passed to make to compile all of the
object files efficiently in parallel.

Typical usage for compiling OpenFOAM:

  - Ensure all lnInclude directories are up-to-date:
    wmakeLnIncludeAll

  - Compile all with this scheduler:
    wmake -queue</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeCollect">源码与说明</a> · <a href="/assets/command-help/wmakecollect.txt">帮助文本</a></p>
