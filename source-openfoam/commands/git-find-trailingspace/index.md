---
title: "git-find-trailingspace · 查找源码行末的多余空白"
layout: reference
description: "查找源码行末的多余空白。"
cms_slug: "command-git-find-trailingspace"
---

<p>查找源码行末的多余空白。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/git-find-trailingspace&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: git-find-trailingspace
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-trailingspace

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Use git grep to find files with trailing whitespace</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-trailingspace">源码与说明</a> · <a href="/assets/command-help/git-find-trailingspace.txt">帮助文本</a></p>
