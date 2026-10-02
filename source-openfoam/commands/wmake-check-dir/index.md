---
title: "wmake-check-dir · 比较解析后的绝对目录；相同时返回退出码 0"
layout: reference
description: "比较解析后的绝对目录；相同时返回退出码 0。"
cms_slug: "command-wmake-check-dir"
---

<p>比较解析后的绝对目录；相同时返回退出码 0。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-q | -quiet</td><td>suppress all normal output</td></tr><tr><td>-h | -help</td><td>display short help and exit</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake-check-dir [OPTION] dir [dir2]

options:
  -q | -quiet       suppress all normal output
  -h | -help        display short help and exit

Check that two directories are identical after resolving the absolute paths.
If only a single directory is specified, check against the working directory.

Exit status 0 when directories are identical
Exit status 1 on error</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-check-dir">源码与说明</a> · <a href="/assets/command-help/wmake-check-dir.txt">帮助文本</a></p>
