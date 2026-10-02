---
title: "Allwmake · 项目提供的批量编译脚本；需先阅读脚本和构建说明"
layout: reference
description: "项目提供的批量编译脚本；需先阅读脚本和构建说明。"
cms_slug: "command-allwmake"
---

<p>项目提供的批量编译脚本；需先阅读脚本和构建说明。</p><h2>用法</h2><pre><code class="language-bash">./Allwmake</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: Allwmake
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/Allwmake

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
# Run from OPENFOAM top-level directory only
cd &quot;${0%/*}&quot; || exit
wmake -check-dir &quot;$WM_PROJECT_DIR&quot; 2&gt;/dev/null || {
    echo &quot;Error (${0##*/}) : not located in \$WM_PROJECT_DIR&quot;
    echo &quot;    Check your OpenFOAM environment and installation&quot;
    exit 1
}
if [ -f &quot;$WM_PROJECT_DIR&quot;/wmake/scripts/AllwmakeParseArguments ]
then  . &quot;$WM_PROJECT_DIR&quot;/wmake/scripts/AllwmakeParseArguments || \
    echo &quot;Argument parse error&quot;
else
    echo &quot;Error (${0##*/}) : WM_PROJECT_DIR appears to be incorrect&quot;
    echo &quot;    Check your OpenFOAM environment and installation&quot;
    exit 1
fi

#------------------------------------------------------------------------------
# Preamble. Report tools or at least the mpirun location
if [ -f &quot;$WM_PROJECT_DIR&quot;/wmake/scripts/list_tools ]
then sh &quot;$WM_PROJECT_DIR&quot;/wmake/scripts/list_tools || true
else
    echo &quot;mpirun=$(command -v mpirun || true)&quot;
fi
echo
# Report compiler information. First non-blank line from --version output
compiler=&quot;$(wmake -show-path-cxx 2&gt;/dev/null || true)&quot;
if [ -x &quot;$compiler&quot; ]
then
    echo &quot;compiler=$compiler&quot;
    &quot;$compiler&quot; --version 2&gt;/dev/null | sed -e &#x27;/^$/d;q&#x27;
else
    echo &quot;compiler=unknown&quot;
fi
echo &quot;cxxflags=\&quot;$(wmake -show-cxxflags 2&gt;/dev/null || true)\&quot;&quot;

echo
echo ========================================
date &quot;+%Y-%m-%d %H:%M:%S %z&quot; 2&gt;/dev/null || echo &quot;date is unknown&quot;
echo &quot;Starting compile ${WM_PROJECT_DIR##*/} ${0##*/}&quot;
echo &quot;  $WM_COMPILER ${WM_COMPILER_TYPE:-system} compiler [${WM_COMPILE_CONTROL}]&quot;
echo &quot;  ${WM_OPTIONS}, with ${WM_MPLIB} ${FOAM_MPI}&quot;
echo ========================================
echo

# Compile tools for wmake
&quot;${WM_DIR:-wmake}&quot;/src/Allmake

# Compile ThirdParty libraries and applications
if [ -d &quot;$WM_THIRD_PARTY_DIR&quot; ]
then
    if [ -e &quot;$WM_THIRD_PARTY_DIR&quot;/Allwmake.override ]
    then
        if [ -x &quot;$WM_THIRD_PARTY_DIR&quot;/Allwmake.override ]
        then    &quot;$WM_THIRD_PARTY_DIR&quot;/Allwmake.override
        fi
    elif [ -x &quot;$WM_THIRD_PARTY_DIR&quot;/Allwmake ]
    then      &quot;$WM_THIRD_PARTY_DIR&quot;/Allwmake
    else
        echo &quot;Skip ThirdParty (no Allwmake* files)&quot;
    fi
else
    echo &quot;Skip ThirdParty (no directory)&quot;
fi

# OpenFOAM libraries
src/Allwmake $targetType $*

# OpenFOAM applications
applications/Allwmake $targetType $*

#------------------------------------------------------------------------------
# Additional components

case &quot;$FOAM_MODULE_PREFIX&quot; in
(false | none)
    echo ========================================
    echo &quot;OpenFOAM modules disabled (prefix=${FOAM_MODULE_PREFIX})&quot;
    echo &quot;Can be built separately:&quot;
    echo
    echo &quot;    ./Allwmake-modules -prefix=...&quot;
    echo
    echo ========================================
    echo
    ;;
(*)
    # Use wmake -all instead of Allwmake to allow for overrides
    ( cd &quot;$WM_PROJECT_DIR/modules&quot; 2&gt;/dev/null &amp;&amp; wmake -all )

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
    (cd &quot;$1&quot; 2&gt;/dev/null &amp;&amp; find . -mindepth 1 -maxdepth 1 -type f 2&gt;/dev/null) |\
        sed -e &#x27;\@/Test-@d&#x27; | wc -l
}

# Some summary information
echo
date &quot;+%Y-%m-%d %H:%M:%S %z&quot; 2&gt;/dev/null || echo &quot;date is unknown&quot;
echo ========================================
echo &quot;  ${WM_PROJECT_DIR##*/}&quot;
echo &quot;  $WM_COMPILER ${WM_COMPILER_TYPE:-system} compiler&quot;
echo &quot;  ${WM_OPTIONS}, with ${WM_MPLIB} ${FOAM_MPI}&quot;
echo

# The api/patch information
sed -e &#x27;s/^/  /; s/=/ = /&#x27; ./META-INFO/api-info 2&gt;/dev/null || true

echo &quot;  bin = $(_foamCountDirEntries &quot;$FOAM_APPBIN&quot;) entries&quot;
echo &quot;  lib = $(_foamCountDirEntries &quot;$FOAM_LIBBIN&quot;) entries&quot;
echo
echo ========================================

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/Allwmake">源码与说明</a> · <a href="/assets/command-help/allwmake.txt">帮助文本</a></p>
