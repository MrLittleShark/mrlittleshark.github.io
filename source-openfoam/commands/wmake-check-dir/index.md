---
title: "wmake-check-dir · 比较解析后的绝对目录；相同时返回退出码 0"
layout: reference
description: "比较解析后的绝对目录；相同时返回退出码 0。"
cms_slug: "command-wmake-check-dir"
---

<p>比较解析后的绝对目录；相同时返回退出码 0。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 对比解析后的绝对目录；相同返回 0，不同或无法访问返回 1。目录需存在。</p>
<h2>示例 1：确认在项目根目录</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
"$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir" "$WM_PROJECT_DIR"
</code></pre>
<p>只给一个路径时与当前工作目录比较。</p>
<h2>示例 2：比较相对与绝对路径</h2>
<pre><code class="language-bash">mkdir -p compare-dir
"$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir" compare-dir "$PWD/compare-dir"
</code></pre>
<p>两个写法指向同一目录，应返回成功。</p>
<h2>示例 3：检查符号链接指向</h2>
<pre><code class="language-bash">mkdir -p real-dir
ln -s real-dir linked-dir
"$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir" real-dir linked-dir
</code></pre>
<p>解析链接后比较位置，适合检查别名路径。</p>
<h2>示例 4：给脚本加目录条件</h2>
<pre><code class="language-bash">if "$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir" -quiet "$WM_PROJECT_DIR"; then echo "project root"; else echo "another directory"; fi
</code></pre>
<p>-quiet 关闭常规诊断，通过退出码选择分支。</p>
<h2>示例 5：阻止在错误目录构建</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-check-dir" "$WM_PROJECT_DIR" || exit 1
./Allwmake -j 2
</code></pre>
<p>用于项目根目录的构建脚本；目录不匹配时在编译前退出。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-q | -quiet</code></td><td>suppress all normal output</td></tr><tr><td><code>-h | -help</code></td><td>display short help and exit</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake-check-dir [OPTION] dir [dir2]

options:
  -q | -quiet       suppress all normal output
  -h | -help        display short help and exit

Check that two directories are identical after resolving the absolute paths.
If only a single directory is specified, check against the working directory.

Exit status 0 when directories are identical
Exit status 1 on error</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-check-dir">源码与说明</a> · <a href="/assets/command-help/wmake-check-dir.txt">帮助文本</a></p>
