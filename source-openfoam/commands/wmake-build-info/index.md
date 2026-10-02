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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-cmp, -check</code></td><td>比较 Make 构建信息与元信息；一致时退出码为 0。</td></tr><tr><td><code>-diff</code></td><td>显示 Make 与元信息的差异；一致时退出码为 0。</td></tr><tr><td><code>-dry-run</code></td><td>配合 -update 使用，仅预览更新。</td></tr><tr><td><code>-filter FILE</code></td><td>用 Make 构建信息替换文件中的 @API@、@BUILD@ 标记。</td></tr><tr><td><code>-no-git</code></td><td>直接扫描文件获取信息，跳过 Git 查询。</td></tr><tr><td><code>-remove</code></td><td>删除元信息中的构建记录并退出。</td></tr><tr><td><code>-update</code></td><td>根据 Make 构建信息更新元信息。</td></tr><tr><td><code>-query</code></td><td>显示 Make 构建信息与元信息。</td></tr><tr><td><code>-query-make</code></td><td>显示 Make 中的 api、branch、build 值。</td></tr><tr><td><code>-query-meta</code></td><td>显示元信息中的 api、branch、build 值。</td></tr><tr><td><code>-show-api</code></td><td>显示 wmake/rules 或元信息中的 API 版本值并退出。</td></tr><tr><td><code>-show-patch</code></td><td>显示元信息中的补丁版本值并退出。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-build-info">源码与说明</a> · <a href="/assets/command-help/wmake-build-info.txt">帮助文本</a></p>
