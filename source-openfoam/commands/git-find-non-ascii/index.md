---
title: "git-find-non-ascii · 在 Git 管理的源文件中查找非 ASCII 字符"
layout: reference
description: "在 Git 管理的源文件中查找非 ASCII 字符。"
cms_slug: "command-git-find-non-ascii"
---

<p>在 Git 管理的源文件中查找非 ASCII 字符。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 v2512 此脚本的 git grep 行末缺少续行符，会额外执行一条名为 -- 的命令。先在独立练习目录复制脚本并修正该行：cp "$WM_PROJECT_DIR/bin/tools/git-find-non-ascii" ./git-find-non-ascii；用文本编辑器在 git grep 开头那一行末加一个反斜杠。以下 ./git-find-non-ascii 指该本地修正版。它检查暂存区中的 C/C++ 文件。</p>
<h2>示例 1：检查当前暂存区</h2>
<pre><code class="language-bash">./git-find-non-ascii
</code></pre>
<p>输出含控制字符或非 ASCII 字节的源码行与行号；没有匹配时 grep 返回 1。</p>
<h2>示例 2：检查新增源码</h2>
<pre><code class="language-bash">git add myModel.C
./git-find-non-ascii
</code></pre>
<p>先暂存新文件，再按暂存内容检查，未暂存修改不参与。</p>
<h2>示例 3：检查头文件修改</h2>
<pre><code class="language-bash">git add myModel.H
./git-find-non-ascii
</code></pre>
<p>检查类声明和注释中的非 ASCII 字符，输出仍可能包含其他已暂存文件。</p>
<h2>示例 4：保存匹配清单</h2>
<pre><code class="language-bash">./git-find-non-ascii &gt; non-ascii-report.txt
</code></pre>
<p>保存具体文件和行号，便于逐项查看字符是否符合项目约定。</p>
<h2>示例 5：修改后重新核对</h2>
<pre><code class="language-bash">${EDITOR:-vi} myModel.C
git add myModel.C
./git-find-non-ascii
</code></pre>
<p>修正文本后重新暂存，否则脚本仍读取旧暂存版本。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/git-find-non-ascii">源码与说明</a> · <a href="/assets/command-help/git-find-non-ascii.txt">帮助文本</a></p>
