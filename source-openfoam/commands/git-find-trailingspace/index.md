---
title: "git-find-trailingspace · 查找源码行末的多余空白"
layout: reference
description: "查找源码行末的多余空白。"
cms_slug: "command-git-find-trailingspace"
---

<p>查找源码行末的多余空白。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 在个人 Git 工作树中运行，检测已被 Git 跟踪的文件。此脚本将额外参数作为 git grep 的路径模式传入。</p>
<h2>示例 1：检查整个工作树</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/git-find-trailingspace"
</code></pre>
<p>按文件输出尾部空白的匹配行数；无匹配时 grep 返回 1。</p>
<h2>示例 2：只检查 C++ 实现</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/git-find-trailingspace" '*.C'
</code></pre>
<p>引号把模式交给 Git，而非 shell 展开。</p>
<h2>示例 3：只检查头文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/git-find-trailingspace" '*.H'
</code></pre>
<p>限定 OpenFOAM 常用头文件扩展名。</p>
<h2>示例 4：检查一个模块</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/git-find-trailingspace" src/myModel
</code></pre>
<p>只检查该相对路径内的已跟踪文件。</p>
<h2>示例 5：检查两类配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/git-find-trailingspace" '*/Make/files' '*/Make/options'
</code></pre>
<p>同时检查源码清单和编译选项文件，输出每个问题文件的计数。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: git-find-trailingspace
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-trailingspace

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Use git grep to find files with trailing whitespace</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-trailingspace">源码与说明</a> · <a href="/assets/command-help/git-find-trailingspace.txt">帮助文本</a></p>
