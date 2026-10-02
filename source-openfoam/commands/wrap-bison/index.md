---
title: "wrap-bison · 封装 Bison，调整生成文件的名称和位置"
layout: reference
description: "封装 Bison，调整生成文件的名称和位置。"
cms_slug: "command-wrap-bison"
---

<p>封装 Bison，调整生成文件的名称和位置。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wrap-bison&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-dry-run</td><td>Process m4 only (output on stdout)</td></tr><tr><td>-grammar</td><td>Output grammar tables (ignored)</td></tr><tr><td>-no-tmp</td><td>Do not retain temporary m4 processed files</td></tr><tr><td>-output=NAME</td><td>Request renaming actions</td></tr><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wrap-bison [options] [bison args/options]

options:
  -dry-run          Process m4 only (output on stdout)
  -grammar          Output grammar tables (ignored)
  -no-tmp           Do not retain temporary m4 processed files
  -output=NAME      Request renaming actions
  -h, -help         Print the usage

A bison wrapper with renaming of skeleton files</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-bison">源码与说明</a> · <a href="/assets/command-help/wrap-bison.txt">帮助文本</a></p>
