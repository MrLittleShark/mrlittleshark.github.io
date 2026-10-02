---
title: "wrap-lemon · 使用 OpenFOAM 的解析器模板封装 Lemon"
layout: reference
description: "使用 OpenFOAM 的解析器模板封装 Lemon。"
cms_slug: "command-wrap-lemon"
---

<p>使用 OpenFOAM 的解析器模板封装 Lemon。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wrap-lemon&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-header</td><td>Generate header only, suppressing other output</td></tr><tr><td>-dry-run</td><td>Process m4 only (output on stdout)</td></tr><tr><td>-grammar</td><td>Output grammar tables (stdout)</td></tr><tr><td>-no-tmp</td><td>Do not retain temporary m4 processed files</td></tr><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wrap-lemon [options] [lemon args/options]

options:
  -header           Generate header only, suppressing other output
  -dry-run          Process m4 only (output on stdout)
  -grammar          Output grammar tables (stdout)
  -no-tmp           Do not retain temporary m4 processed files
  -h, -help         Print the usage

A lemon wrapper using predefined executable and skeleton locations.
Files ending with &#x27;m4&#x27; (eg, .lyym4, .lyy-m4) will be filtered through
the m4(1) macro processor and lemon will be called with &#x27;m4&#x27; as a macro
definition, which can be used in conditions (%ifdef m4, %ifndef m4)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-lemon">源码与说明</a> · <a href="/assets/command-help/wrap-lemon.txt">帮助文本</a></p>
