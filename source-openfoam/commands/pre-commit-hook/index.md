---
title: "pre-commit-hook · 在 Git 提交前检查源码中的制表符和行宽"
layout: reference
description: "在 Git 提交前检查源码中的制表符和行宽。"
cms_slug: "command-pre-commit-hook"
---

<p>在 Git 提交前检查源码中的制表符和行宽。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/pre-commit-hook&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: pre-commit-hook
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/pre-commit-hook

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

pre-commit hook for git. Copy or link this file as &quot;.git/hooks/pre-commit&quot; Eg, ( cd $WM_PROJECT_DIR/.git/hooks &amp;&amp; ln -sf ../../bin/tools/pre-commit-hook pre-commit ) Hook receives: empty Checks for - illegal code, e.g. &lt;TAB&gt; - columns greater than 80 for *.[CH] files</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/pre-commit-hook">源码与说明</a> · <a href="/assets/command-help/pre-commit-hook.txt">帮助文本</a></p>
