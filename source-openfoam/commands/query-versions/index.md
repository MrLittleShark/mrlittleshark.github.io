---
title: "query-versions · 读取 ThirdParty 环境配置中的软件版本"
layout: reference
description: "读取 ThirdParty 环境配置中的软件版本。"
cms_slug: "command-query-versions"
---

<p>读取 ThirdParty 环境配置中的软件版本。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 输出来自配置脚本中的版本设定，不表示所有这些版本已安装；实际安装位置用 query-detect 检查。</p>
<h2>示例 1：查看依赖版本配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-versions"
</code></pre>
<p>调用各 have_* 脚本的版本查询，输出配置中的依赖版本。</p>
<h2>示例 2：只查询编译器</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-versions" -compiler
</code></pre>
<p>显示 GCC 与 Clang 的配置映射和默认版本。</p>
<h2>示例 3：只查询 GCC</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-versions" -gcc
</code></pre>
<p>筛选 GCC 相关版本配置。</p>
<h2>示例 4：只查询 Clang</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-versions" -clang
</code></pre>
<p>筛选 Clang 相关版本配置。</p>
<h2>示例 5：对比配置版本与正在使用的编译器</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/query-versions" -gcc
compiler=$(wmake -show-path-cxx)
"$compiler" --version
</code></pre>
<p>前者显示打包/构建配置，后者由实际选中的编译器报告版本。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-compiler</code></td><td>Print clang,gcc compiler versions only</td></tr><tr><td><code>-clang</code></td><td>Print clang compiler versions only</td></tr><tr><td><code>-gcc</code></td><td>Print gcc compiler versions only</td></tr><tr><td><code>-h, -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: query-versions [OPTION]

options:
  -compiler         Print clang,gcc compiler versions only
  -clang            Print clang compiler versions only
  -gcc              Print gcc compiler versions only
  -h, -help         Print the usage

Query (ThirdParty) versions based on their etc/config.sh values.
Uses OpenFOAM wmake/scripts/have_* scripts.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/query-versions">源码与说明</a> · <a href="/assets/command-help/query-versions.txt">帮助文本</a></p>
