---
title: "makeParser · 预生成 Ragel 或 Lemon 解析器代码"
layout: reference
description: "预生成 Ragel 或 Lemon 解析器代码。"
cms_slug: "command-makeparser"
---

<p>预生成 Ragel 或 Lemon 解析器代码。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/makeParser&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-prefix=NAME</td><td>Common prefix for parser and scanner</td></tr><tr><td>-parser=FILE</td><td>Generate lemon parser header</td></tr><tr><td>-scanner=FILE</td><td>Generate ragel scanner code</td></tr><tr><td>-code</td><td>Generate parser code, not header</td></tr><tr><td>-header</td><td>Generate parser header, not code (default)</td></tr><tr><td>-grammar</td><td>Output grammar tables (if supported)</td></tr><tr><td>-dry-run</td><td>Process m4 only (output on stdout)</td></tr><tr><td>-no-lines</td><td>Suppress generation of #line directives</td></tr><tr><td>-no-tmp</td><td>Do not retain temporary m4 processed files</td></tr><tr><td>-remove</td><td>Remove generated code</td></tr><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: makeParser [options]

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
