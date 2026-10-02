---
title: "git-find-non-ascii · 在 Git 管理的源文件中查找非 ASCII 字符"
layout: reference
description: "在 Git 管理的源文件中查找非 ASCII 字符。"
cms_slug: "command-git-find-non-ascii"
---

<p>在 Git 管理的源文件中查找非 ASCII 字符。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/git-find-non-ascii&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: git-find-non-ascii
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-non-ascii

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Use git grep to find source files with non-ASCII characters. Use cached files for speed. C files: .c .h C++ files: .C .cc .cpp .cxx .H .hh .hpp .hxx</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-non-ascii">源码与说明</a> · <a href="/assets/command-help/git-find-non-ascii.txt">帮助文本</a></p>
