---
title: "lib-dir · 查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置"
layout: reference
description: "查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置。"
cms_slug: "command-lib-dir"
---

<p>查找 lib 或 lib64 目录，并输出 shell 或 Make 使用的库路径设置。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 在独立目录创建库布局：mkdir -p dependency/lib dependency64/lib64。脚本打印 shell 赋值或链接选项，不会在父 shell 自动执行它们。</p>
<h2>示例 1：生成 POSIX shell 配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/lib-dir" -sh "$PWD/dependency"
</code></pre>
<p>识别 lib 子目录，输出 LD_LIBRARY_PATH 赋值。</p>
<h2>示例 2：生成链接器搜索参数</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/lib-dir" -make "$PWD/dependency"
</code></pre>
<p>输出 -L&lt;绝对路径&gt;/lib，可加入 Make/options 的链接设置。</p>
<h2>示例 3：生成 C shell 配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/lib-dir" -csh "$PWD/dependency"
</code></pre>
<p>输出 setenv 语法，供 csh/tcsh 配置使用。</p>
<h2>示例 4：选择 lib64 布局</h2>
<pre><code class="language-bash">WM_COMPILER_LIB_ARCH=64 "$WM_PROJECT_DIR/bin/tools/lib-dir" -make "$PWD/dependency64"
</code></pre>
<p>环境变量指定架构后缀，识别 lib64 并生成 -L 路径。</p>
<h2>示例 5：显示环境生成过程</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/lib-dir" -sh-verbose "$PWD/dependency" &gt; dependency-env.sh
</code></pre>
<p>标准输出保存赋值，详细信息写到标准错误，可阅读脚本后再选择是否加载。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-sh</code></td><td>Emit POSIX shell syntax (default)</td></tr><tr><td><code>-csh</code></td><td>Emit C-shell shell syntax</td></tr><tr><td><code>-sh-verbose</code></td><td>Like -sh,  with additional verbosity</td></tr><tr><td><code>-csh-verbose</code></td><td>Like -csh, with additional verbosity</td></tr><tr><td><code>-make</code></td><td>Emit content for a Makefile</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lib-dir [OPTION] DIR [LIBEXT]

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
