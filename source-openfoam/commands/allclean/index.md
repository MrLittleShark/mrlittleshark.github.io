---
title: "Allclean"
layout: reference
description: "算例提供的清理脚本，执行前检查其删除范围。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>算例提供的清理脚本，执行前检查其删除范围。</p><h2>使用入口</h2><pre><code class="language-bash">less Allclean</code></pre><h2>使用条件与核对</h2><p>算例提供的清理脚本，执行前检查其删除范围。 示例中的算例名、路径与主机名须按实际环境替换。

本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/allclean.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: Allclean
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
cd &quot;&#36;{0%/*}&quot; || exit                            # Run from this directory
. &quot;&#36;{WM_PROJECT_DIR:?}&quot;/bin/tools/LogFunctions  # Tutorial log-file functions
#------------------------------------------------------------------------------

echo &quot;--------&quot;

# Remove old build/ directory
buildDir=&quot;&#36;{WM_PROJECT_DIR}/build/&#36;{WM_OPTIONS}/&#36;{PWD##*/}&quot;
if [ -d &quot;&#36;buildDir&quot; ]
then
    echo &quot;Removing old build directory: &#36;buildDir&quot; 1&gt;&amp;2
    rm -rf -- &quot;&#36;buildDir&quot;
fi

removeLogs

echo &quot;Cleaning tutorials ...&quot;
foamCleanTutorials -self    # Run recursively but avoid self

echo &quot;--------&quot;

#------------------------------------------------------------------------------</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
