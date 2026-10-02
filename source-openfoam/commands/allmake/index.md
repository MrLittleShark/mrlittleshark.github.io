---
title: "Allmake · 该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码"
layout: reference
description: "该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。"
cms_slug: "command-allmake"
---

<p>该脚本服务于 OpenFOAM 源码构建或维护，具体入口和前置条件见源码。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 此处是 wmake/src/Allmake，用于编译 Lemon 和依赖分析器，不是算例运行脚本。先完整复制 wmake/src 为个人 tools-src；设置 WMAKE_BIN 为新的个人输出目录，WM_DIR 仍指向已安装的规则。</p>
<h2>示例 1：构建工具链</h2>
<pre><code class="language-bash">cp -a "$WM_PROJECT_DIR/wmake/src" tools-src
WMAKE_BIN="$PWD/tools-bin" bash tools-src/Allmake
</code></pre>
<p>在副本中编译 lemon 和 wmkdepend，输出到个人 tools-bin。</p>
<h2>示例 2：限定并行任务</h2>
<pre><code class="language-bash">WMAKE_BIN="$PWD/tools-bin" bash tools-src/Allmake -j 2
</code></pre>
<p>参数传给底层 make，两项工具可并行编译。</p>
<h2>示例 3：预览编译动作</h2>
<pre><code class="language-bash">WMAKE_BIN="$PWD/tools-bin-preview" bash tools-src/Allmake -n
</code></pre>
<p>-n 是 make 的试运行选项，打印命令而不执行编译。</p>
<h2>示例 4：构建旧式 Flex 工具</h2>
<pre><code class="language-bash">WMAKE_BIN="$PWD/tools-bin" bash tools-src/Allmake old
</code></pre>
<p>old 目标生成 wmkdep，需要 Flex；默认目标则是 wmkdepend。</p>
<h2>示例 5：构建到另一目录</h2>
<pre><code class="language-bash">WMAKE_BIN="$PWD/tools-bin-secondary" bash tools-src/Allmake all
</code></pre>
<p>在另一输出位置生成相同工具，适合比较工具链或打包布局。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
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
