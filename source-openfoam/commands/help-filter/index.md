---
title: "help-filter · 过滤 -help-full 的输出，供文档生成使用"
layout: reference
description: "过滤 -help-full 的输出，供文档生成使用。"
cms_slug: "command-help-filter"
---

<p>过滤 -help-full 的输出，供文档生成使用。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/help-filter&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: help-filter
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/help-filter

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Feed with output from -help-full. For example, blockMesh -help-full | ./help-filter</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/help-filter">源码与说明</a> · <a href="/assets/command-help/help-filter.txt">帮助文本</a></p>
