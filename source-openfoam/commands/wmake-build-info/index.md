---
title: "wmake-build-info · 显示项目版本和编译信息"
layout: reference
description: "显示项目版本和编译信息。"
cms_slug: "command-wmake-build-info"
---

<p>显示项目版本和编译信息。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/scripts/wmake-build-info&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-cmp, -check</td><td>Compare make and meta information (exit 0 for no changes)</td></tr><tr><td>-diff</td><td>Display differences between make and meta information (exit code 0 for no changes)</td></tr><tr><td>-dry-run</td><td>In combination with -update</td></tr><tr><td>-filter FILE</td><td>Filter @API@, @BUILD@ tags in file with make information</td></tr><tr><td>-no-git</td><td>Disable use of git for obtaining information</td></tr><tr><td>-remove</td><td>Remove meta-info build information and exit</td></tr><tr><td>-update</td><td>Update meta-info from make information</td></tr><tr><td>-query</td><td>Report make-info and meta-info</td></tr><tr><td>-query-make</td><td>Report make-info values (api, branch, build)</td></tr><tr><td>-query-meta</td><td>Report meta-info values (api, branch, build)</td></tr><tr><td>-show-api</td><td>Print api value from wmake/rules, or meta-info and exit</td></tr><tr><td>-show-patch</td><td>Print patch value from meta-info and exit</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake-build-info [OPTION]
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
