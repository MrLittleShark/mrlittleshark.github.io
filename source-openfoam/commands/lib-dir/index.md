---
title: "lib-dir · 查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置"
layout: reference
description: "查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置。"
cms_slug: "command-lib-dir"
---

<p>查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/lib-dir&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-sh</td><td>Emit POSIX shell syntax (default)</td></tr><tr><td>-csh</td><td>Emit C-shell shell syntax</td></tr><tr><td>-sh-verbose</td><td>Like -sh,  with additional verbosity</td></tr><tr><td>-csh-verbose</td><td>Like -csh, with additional verbosity</td></tr><tr><td>-make</td><td>Emit content for a Makefile</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lib-dir [OPTION] DIR [LIBEXT]

options:
  -sh               Emit POSIX shell syntax (default)
  -csh              Emit C-shell shell syntax
  -sh-verbose       Like -sh,  with additional verbosity
  -csh-verbose      Like -csh, with additional verbosity
  -make             Emit content for a Makefile
  -help             Print the usage

Resolves for the existence of DIR/lib64 and DIR/lib, or uses the fallback
LIBEXT if these failed. A DIR ending in &quot;-none&quot; or &quot;-system&quot; is skipped.

With -sh             LD_LIBRARY_PATH=dir/lib:\$LD_LIBRARY_PATH
With -csh            setenv LD_LIBRARY_PATH dir/lib:\$LD_LIBRARY_PATH
With -make           -Ldir/lib

Exit status is zero (success) or non-zero (failure)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/lib-dir">源码与说明</a> · <a href="/assets/command-help/lib-dir.txt">帮助文本</a></p>
