---
title: "Allclean · 算例提供的清理脚本，执行前检查其删除范围"
layout: reference
description: "算例提供的清理脚本，执行前检查其删除范围。"
cms_slug: "command-allclean"
---

<p>算例提供的清理脚本，执行前检查其删除范围。</p><h2>用法</h2><pre><code class="language-bash">less Allclean</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: Allclean
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
cd &quot;${0%/*}&quot; || exit                            # Run from this directory
. &quot;${WM_PROJECT_DIR:?}&quot;/bin/tools/LogFunctions  # Tutorial log-file functions
#------------------------------------------------------------------------------

echo &quot;--------&quot;

# Remove old build/ directory
buildDir=&quot;${WM_PROJECT_DIR}/build/${WM_OPTIONS}/${PWD##*/}&quot;
if [ -d &quot;$buildDir&quot; ]
then
    echo &quot;Removing old build directory: $buildDir&quot; 1&gt;&amp;2
    rm -rf -- &quot;$buildDir&quot;
fi

removeLogs

echo &quot;Cleaning tutorials ...&quot;
foamCleanTutorials -self    # Run recursively but avoid self

echo &quot;--------&quot;

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allclean">源码与说明</a> · <a href="/assets/command-help/allclean.txt">帮助文本</a></p>
