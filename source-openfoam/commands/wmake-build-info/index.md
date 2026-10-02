---
title: "wmake-build-info · 显示项目版本和编译信息"
layout: reference
description: "显示项目版本和编译信息。"
cms_slug: "command-wmake-build-info"
---

<p>显示项目版本和编译信息。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 查询构建 API、分支和 build 标识，来源为 Make 规则、Git 与 META-INFO。只读例子不改安装。</p>
<h2>示例 1：查询两类来源</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -query
</code></pre>
<p>同时报告 Make 与 META-INFO 的构建信息。</p>
<h2>示例 2：只读 Make 信息</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -query-make
</code></pre>
<p>查看构建系统推导出的 API、分支、build 值。</p>
<h2>示例 3：只读打包信息</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -query-meta
</code></pre>
<p>读取发行包或构建时记录的 META-INFO。</p>
<h2>示例 4：比较是否一致</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -check
status=$?
printf 'comparison exit=%s\n' "$status"
</code></pre>
<p>一致返回 0，有差异时非零，可用于打包前检查。</p>
<h2>示例 5：显示差异与拟更新动作</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -diff
"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -update -dry-run
</code></pre>
<p>先看差异，再预览更新 META-INFO 所需的动作。</p>
<h2>示例 6：替换模板中的标记</h2>
<pre><code class="language-bash">printf 'api=@API@ build=@BUILD@\n' &gt; build-template.txt
"$WM_PROJECT_DIR/wmake/scripts/wmake-build-info" -filter build-template.txt
</code></pre>
<p>读取模板并替换构建标记，输出过滤内容用于发行说明。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-cmp, -check</code></td><td>Compare make and meta information (exit 0 for no changes)</td></tr><tr><td><code>-diff</code></td><td>Display differences between make and meta information (exit code 0 for no changes)</td></tr><tr><td><code>-dry-run</code></td><td>In combination with -update</td></tr><tr><td><code>-filter FILE</code></td><td>Filter @API@, @BUILD@ tags in file with make information</td></tr><tr><td><code>-no-git</code></td><td>Disable use of git for obtaining information</td></tr><tr><td><code>-remove</code></td><td>Remove meta-info build information and exit</td></tr><tr><td><code>-update</code></td><td>Update meta-info from make information</td></tr><tr><td><code>-query</code></td><td>Report make-info and meta-info</td></tr><tr><td><code>-query-make</code></td><td>Report make-info values (api, branch, build)</td></tr><tr><td><code>-query-meta</code></td><td>Report meta-info values (api, branch, build)</td></tr><tr><td><code>-show-api</code></td><td>Print api value from wmake/rules, or meta-info and exit</td></tr><tr><td><code>-show-patch</code></td><td>Print patch value from meta-info and exit</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake-build-info [OPTION]
       wmake-build-info [-update] -filter FILE
options:
  -cmp, -check  Compare make and meta information (exit 0 for no changes)
  -diff         Display differences between make and meta information
                (exit code 0 for no changes)
  -dry-run      In combination with -update
  -filter FILE  Filter @API@, @BUILD@ tags in file with make information
  -no-git       Disable use of git for obtaining information
  -remove       Remove meta-info build information and exit
  -update       Update meta-info from make information
  -query        Report make-info and meta-info
  -query-make   Report make-info values (api, branch, build)
  -query-meta   Report meta-info values (api, branch, build)
  -show-api     Print api value from wmake/rules, or meta-info and exit
  -show-patch   Print patch value from meta-info and exit
  -help         Print the usage

Query/manage status of {api,branch,build} information.
Default without any arguments is the same as &#x27;-query-make&#x27;.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-build-info">源码与说明</a> · <a href="/assets/command-help/wmake-build-info.txt">帮助文本</a></p>
