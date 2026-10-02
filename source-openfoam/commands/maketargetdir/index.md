---
title: "makeTargetDir · 为指定目标文件创建父目录"
layout: reference
description: "为指定目标文件创建父目录。"
cms_slug: "command-maketargetdir"
---

<p>为指定目标文件创建父目录。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 输入是目标文件路径，工具只创建各文件的父目录，不生成文件。</p>
<h2>示例 1：建立一层目标目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeTargetDir" build/main.o
</code></pre>
<p>建立 build，main.o 尚未生成。</p>
<h2>示例 2：建立嵌套构建目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeTargetDir" build/models/transport/model.o
</code></pre>
<p>递归创建中间目录层级。</p>
<h2>示例 3：同时准备两个目标</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeTargetDir" build/a.o build/sub/b.o
</code></pre>
<p>分别为两个目标准备父目录。</p>
<h2>示例 4：准备个人输出位置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeTargetDir" "$FOAM_USER_APPBIN/myUtility" "$FOAM_USER_LIBBIN/libMyModel.so"
</code></pre>
<p>建立用户应用和库的父目录，便于后续链接。</p>
<h2>示例 5：为一组时间导出创建目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeTargetDir" exports/0/U.csv exports/0.5/U.csv exports/1/U.csv
</code></pre>
<p>虽然通常用于构建，该脚本同样可准备后处理导出的目录树。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: makeTargetDir
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeTargetDir

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Makes a directory hierarchy for the given target file(s) Usage: makeTargetDir file1 [..fileN]</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeTargetDir">源码与说明</a> · <a href="/assets/command-help/maketargetdir.txt">帮助文本</a></p>
