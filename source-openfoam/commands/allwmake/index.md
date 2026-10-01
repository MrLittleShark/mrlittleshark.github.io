---
title: "Allwmake"
layout: reference
description: "项目提供的批量编译脚本；需先阅读脚本和构建说明。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>项目提供的批量编译脚本；需先阅读脚本和构建说明。</p><h2>使用入口</h2><pre><code class="language-bash">./Allwmake</code></pre><h2>使用条件与核对</h2><p>项目提供的批量编译脚本；需先阅读脚本和构建说明。 示例中的算例名、路径与主机名须按实际环境替换。

本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/allwmake.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: Allwmake
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/Allwmake

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
# Run from OPENFOAM top-level directory only
cd &quot;&#36;{0%/*}&quot; || exit
wmake -check-dir &quot;&#36;WM_PROJECT_DIR&quot; 2&gt;/dev/null || {
    echo &quot;Error (&#36;{0##*/}) : not located in \&#36;WM_PROJECT_DIR&quot;
    echo &quot;    Check your OpenFOAM environment and installation&quot;
    exit 1
}
if [ -f &quot;&#36;WM_PROJECT_DIR&quot;/wmake/scripts/AllwmakeParseArguments ]
then  . &quot;&#36;WM_PROJECT_DIR&quot;/wmake/scripts/AllwmakeParseArguments || \
    echo &quot;Argument parse error&quot;
else
    echo &quot;Error (&#36;{0##*/}) : WM_PROJECT_DIR appears to be incorrect&quot;
    echo &quot;    Check your OpenFOAM environment and installation&quot;
    exit 1
fi

#------------------------------------------------------------------------------
# Preamble. Report tools or at least the mpirun location
if [ -f &quot;&#36;WM_PROJECT_DIR&quot;/wmake/scripts/list_tools ]
then sh &quot;&#36;WM_PROJECT_DIR&quot;/wmake/scripts/list_tools || true
else
    echo &quot;mpirun=&#36;(command -v mpirun || true)&quot;
fi
echo
# Report compiler information. First non-blank line from --version output
compiler=&quot;&#36;(wmake -show-path-cxx 2&gt;/dev/null || true)&quot;
if [ -x &quot;&#36;compiler&quot; ]
then
    echo &quot;compiler=&#36;compiler&quot;
    &quot;&#36;compiler&quot; --version 2&gt;/dev/null | sed -e &#x27;/^&#36;/d;q&#x27;
else
    echo &quot;compiler=unknown&quot;
fi
echo &quot;cxxflags=\&quot;&#36;(wmake -show-cxxflags 2&gt;/dev/null || true)\&quot;&quot;

echo
echo ========================================
date &quot;+%Y-%m-%d %H:%M:%S %z&quot; 2&gt;/dev/null || echo &quot;date is unknown&quot;
echo &quot;Starting compile &#36;{WM_PROJECT_DIR##*/} &#36;{0##*/}&quot;
echo &quot;  &#36;WM_COMPILER &#36;{WM_COMPILER_TYPE:-system} compiler [&#36;{WM_COMPILE_CONTROL}]&quot;
echo &quot;  &#36;{WM_OPTIONS}, with &#36;{WM_MPLIB} &#36;{FOAM_MPI}&quot;
echo ========================================
echo

# Compile tools for wmake
&quot;&#36;{WM_DIR:-wmake}&quot;/src/Allmake

# Compile ThirdParty libraries and applications
if [ -d &quot;&#36;WM_THIRD_PARTY_DIR&quot; ]
then
    if [ -e &quot;&#36;WM_THIRD_PARTY_DIR&quot;/Allwmake.override ]
    then
        if [ -x &quot;&#36;WM_THIRD_PARTY_DIR&quot;/Allwmake.override ]
        then    &quot;&#36;WM_THIRD_PARTY_DIR&quot;/Allwmake.override
        fi
    elif [ -x &quot;&#36;WM_THIRD_PARTY_DIR&quot;/Allwmake ]
    then      &quot;&#36;WM_THIRD_PARTY_DIR&quot;/Allwmake
    else
        echo &quot;Skip ThirdParty (no Allwmake* files)&quot;
    fi
else
    echo &quot;Skip ThirdParty (no directory)&quot;
fi

# OpenFOAM libraries
src/Allwmake &#36;targetType &#36;*

# OpenFOAM applications
applications/Allwmake &#36;targetType &#36;*

#------------------------------------------------------------------------------
# Additional components

case &quot;&#36;FOAM_MODULE_PREFIX&quot; in
(false | none)
    echo ========================================
    echo &quot;OpenFOAM modules disabled (prefix=&#36;{FOAM_MODULE_PREFIX})&quot;
    echo &quot;Can be built separately:&quot;
    echo
    echo &quot;    ./Allwmake-modules -prefix=...&quot;
    echo
    echo ========================================
    echo
    ;;
(*)
    # Use wmake -all instead of Allwmake to allow for overrides
    ( cd &quot;&#36;WM_PROJECT_DIR/modules&quot; 2&gt;/dev/null &amp;&amp; wmake -all )

    echo ========================================
    echo &quot;The optional plugins can be built separately:&quot;
    echo
    echo &quot;    ./Allwmake-plugins -prefix=...&quot;
    echo
    echo ========================================
    echo
esac

#------------------------------------------------------------------------------
# Count files in given directory. Ignore &quot;Test-*&quot; binaries.
_foamCountDirEntries()
{
    (cd &quot;&#36;1&quot; 2&gt;/dev/null &amp;&amp; find . -mindepth 1 -maxdepth 1 -type f 2&gt;/dev/null) |\
        sed -e &#x27;\@/Test-@d&#x27; | wc -l
}

# Some summary information
echo
date &quot;+%Y-%m-%d %H:%M:%S %z&quot; 2&gt;/dev/null || echo &quot;date is unknown&quot;
echo ========================================
echo &quot;  &#36;{WM_PROJECT_DIR##*/}&quot;
echo &quot;  &#36;WM_COMPILER &#36;{WM_COMPILER_TYPE:-system} compiler&quot;
echo &quot;  &#36;{WM_OPTIONS}, with &#36;{WM_MPLIB} &#36;{FOAM_MPI}&quot;
echo

# The api/patch information
sed -e &#x27;s/^/  /; s/=/ = /&#x27; ./META-INFO/api-info 2&gt;/dev/null || true

echo &quot;  bin = &#36;(_foamCountDirEntries &quot;&#36;FOAM_APPBIN&quot;) entries&quot;
echo &quot;  lib = &#36;(_foamCountDirEntries &quot;&#36;FOAM_LIBBIN&quot;) entries&quot;
echo
echo ========================================

#------------------------------------------------------------------------------</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/Allwmake">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
