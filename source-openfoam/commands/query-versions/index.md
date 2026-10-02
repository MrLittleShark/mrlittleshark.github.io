---
title: "query-versions · 读取 ThirdParty 环境配置中的软件版本"
layout: reference
description: "读取 ThirdParty 环境配置中的软件版本。"
cms_slug: "command-query-versions"
---

<p>读取 ThirdParty 环境配置中的软件版本。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/query-versions&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-compiler</td><td>Print clang,gcc compiler versions only</td></tr><tr><td>-clang</td><td>Print clang compiler versions only</td></tr><tr><td>-gcc</td><td>Print gcc compiler versions only</td></tr><tr><td>-h, -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: query-versions [OPTION]

options:
  -compiler         Print clang,gcc compiler versions only
  -clang            Print clang compiler versions only
  -gcc              Print gcc compiler versions only
  -h, -help         Print the usage

Query (ThirdParty) versions based on their etc/config.sh values.
Uses OpenFOAM wmake/scripts/have_* scripts.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/query-versions">源码与说明</a> · <a href="/assets/command-help/query-versions.txt">帮助文本</a></p>
