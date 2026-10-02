---
title: "foamCreateManpage · 根据程序的 -help-man 输出生成手册页"
layout: reference
description: "根据程序的 -help-man 输出生成手册页。"
cms_slug: "command-foamcreatemanpage"
---

<p>根据程序的 -help-man 输出生成手册页。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamCreateManpage&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-dir=DIR</td><td>Input directory to process</td></tr><tr><td>-output=DIR</td><td>Write to alternative output directory</td></tr><tr><td>-pdf</td><td>Process as nroff man content and pass to ps2pdf</td></tr><tr><td>-gz | -gzip</td><td>Compress manpage output</td></tr><tr><td>-version=VER</td><td>Specify an alternative version</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCreateManpage [OPTION] [appName .. [appNameN]]
options:
  -dir=DIR          Input directory to process
  -output=DIR       Write to alternative output directory
  -pdf              Process as nroff man content and pass to ps2pdf
  -gz | -gzip       Compress manpage output
  -version=VER      Specify an alternative version
  -h | -help        Print the usage

Query OpenFOAM applications with -help-man for their manpage content
and redirect to corresponding directory location.
Default input:  \$FOAM_APPBIN only.
Default output: $defaultOutputDir

Uses the search directory if individual applications are specified.

Copyright (C) 2018-2019 OpenCFD Ltd.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateManpage">源码与说明</a> · <a href="/assets/command-help/foamcreatemanpage.txt">帮助文本</a></p>
