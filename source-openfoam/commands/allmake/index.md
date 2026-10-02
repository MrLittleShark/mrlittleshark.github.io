---
title: "Allmake · 该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码"
layout: reference
description: "该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。"
cms_slug: "command-allmake"
---

<p>该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/wmake/src/Allmake&quot;</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: Allmake
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/src/Allmake

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
cd &quot;${0%/*}&quot; || exit            # This directory (/path/project/wmake/src)

if [ -z &quot;$WM_DIR&quot; ]             # Require WM_DIR (/path/project/wmake)
then
    WM_DIR=&quot;$(dirname &quot;$(pwd -L)&quot;)&quot;
    export WM_DIR
fi

if [ -z &quot;$WM_PROJECT_DIR&quot; ]     # Expect WM_PROJECT_DIR (/path/project)
then
    echo &quot;Warning (${0##*/}) : No WM_PROJECT_DIR set&quot; 1&gt;&amp;2
    WM_PROJECT_DIR=&quot;${WM_DIR%/*}&quot;
    export WM_PROJECT_DIR
fi

if [ -z &quot;$WM_ARCH&quot; ] || [ -z &quot;$WM_COMPILER&quot; ]
then
    echo &quot;Error (${0##*/}) : No WM_ARCH or WM_COMPILER set&quot;
    echo &quot;    Check your OpenFOAM environment and installation&quot;
    exit 1
fi


if [ &quot;${WM_COMPILER%Mingw}&quot; != &quot;$WM_COMPILER&quot; ] &amp;&amp; [ &quot;$WM_ARCH&quot; != win64 ]
then
    # Mingw cross-compilation

    # Toolchain for build (system gcc)
    make \
        WM_COMPILER=Gcc WM_COMPILER_TYPE=system \
        WMAKE_BIN=&quot;${WM_PROJECT_DIR}/platforms/tools/${WM_ARCH}${WM_COMPILER}&quot; \
        &quot;$@&quot;

    # Toolchain for target (mingw)
    make \
        WMAKE_BIN=&quot;${WM_PROJECT_DIR}/platforms/tools/win64${WM_COMPILER}&quot; \
        &quot;$@&quot;
else

    # Regular wmake toolchain
    make &quot;$@&quot;

fi

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/src/Allmake">源码与说明</a> · <a href="/assets/command-help/allmake.txt">帮助文本</a></p>
