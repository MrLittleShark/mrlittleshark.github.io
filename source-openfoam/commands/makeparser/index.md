---
title: "makeParser · 预生成 Ragel 或 Lemon 解析器代码"
layout: reference
description: "预生成 Ragel 或 Lemon 解析器代码。"
cms_slug: "command-makeparser"
---

<p>预生成 Ragel 或 Lemon 解析器代码。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 需要 Ragel 或 OpenFOAM 编译的 Lemon。先复制扫描器：cp "$WM_PROJECT_DIR/wmake/src/wmkdepend.rl" ./wmkdepend.rl。Lemon 示例另建 toy.lyy，内容为三行：%token_type {double}、%default_type {double}、input ::= NUMBER.。所有生成文件在练习目录中。</p>
<h2>示例 1：生成 Ragel 扫描器</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeParser" -scanner=wmkdepend.rl
</code></pre>
<p>输出 wmkdepend.cc，供依赖解析工具编译。</p>
<h2>示例 2：省略行号指令</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeParser" -no-lines -scanner=wmkdepend.rl
</code></pre>
<p>向 Ragel 传递 -L，生成代码不含源文件 #line 映射。</p>
<h2>示例 3：只生成 Lemon 头文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeParser" -parser=toy.lyy -header
</code></pre>
<p>使用默认头文件模式，得到 token 定义的 toy.h。</p>
<h2>示例 4：生成 Lemon 实现</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeParser" -parser=toy.lyy -code
</code></pre>
<p>生成解析器实现，.lyy 对应 .cc 扩展名，同时可能输出头文件和分析报告。</p>
<h2>示例 5：使用文件名前缀</h2>
<pre><code class="language-bash">cp toy.lyy demo-toy.lyy
"$WM_PROJECT_DIR/wmake/scripts/makeParser" -prefix=demo- -parser=toy.lyy -code
</code></pre>
<p>实际输入由 prefix 与 parser 拼接，读取 demo-toy.lyy。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-prefix=NAME</code></td><td>Common prefix for parser and scanner</td></tr><tr><td><code>-parser=FILE</code></td><td>Generate lemon parser header</td></tr><tr><td><code>-scanner=FILE</code></td><td>Generate ragel scanner code</td></tr><tr><td><code>-code</code></td><td>Generate parser code, not header</td></tr><tr><td><code>-header</code></td><td>Generate parser header, not code (default)</td></tr><tr><td><code>-grammar</code></td><td>Output grammar tables (if supported)</td></tr><tr><td><code>-dry-run</code></td><td>Process m4 only (output on stdout)</td></tr><tr><td><code>-no-lines</code></td><td>Suppress generation of #line directives</td></tr><tr><td><code>-no-tmp</code></td><td>Do not retain temporary m4 processed files</td></tr><tr><td><code>-remove</code></td><td>Remove generated code</td></tr><tr><td><code>-h, -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: makeParser [options]

options:
  -prefix=NAME      Common prefix for parser and scanner
  -parser=FILE      Generate lemon parser header
  -scanner=FILE     Generate ragel scanner code
  -code             Generate parser code, not header
  -header           Generate parser header, not code (default)
  -grammar          Output grammar tables (if supported)
  -dry-run          Process m4 only (output on stdout)
  -no-lines         Suppress generation of #line directives
  -no-tmp           Do not retain temporary m4 processed files
  -remove           Remove generated code
  -h, -help         Print the usage

Pregenerate ragel code and/or lemon parser headers</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeParser">源码与说明</a> · <a href="/assets/command-help/makeparser.txt">帮助文本</a></p>
