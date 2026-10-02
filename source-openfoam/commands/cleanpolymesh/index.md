---
title: "cleanPolyMesh · 清理体网格 polyMesh"
layout: reference
description: "清理体网格 polyMesh。"
cms_slug: "command-cleanpolymesh"
---

<p>清理体网格 polyMesh。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanPolyMesh -region fluid
</code></pre>
<p>省略 -region 时处理 constant/polyMesh；给出区域时处理该区域的网格。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanPolyMesh
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanPolyMesh()
{
    local region

    # Parse options
    while [ "$#" -gt 0 ]
    do
        case "$1" in
        ('')  ;;                # Ignore empty option
        (--)  shift; break ;;   # Stop option parsing

        (-region=*) region="${1#*=}" ;;
        (-region)   region="$2"; shift ;;
        (*) break ;;
        esac
        shift
    done

    # safety
    if [ "$region" = "--" ]; then unset region; fi

    local meshDir="constant/${region}${region:+/}polyMesh"

    if [ -e "$meshDir" ]
    then
        [ -n "$region" ] &amp;&amp; echo "Clearing $meshDir" 1&gt;&amp;2

        if [ -e "$meshDir"/blockMeshDict ] \
        || [ -e "$meshDir"/blockMeshDict.m4 ]
        then
            # VERY OLD LOCATION
            echo
            echo "WARNING: not removing $meshDir/"
            echo "    It contains a 'blockMeshDict' or 'blockMeshDict.m4' file"
            echo "    Please relocate file(s) to system/ !!"
            echo
        else
            # Can remove constant/polyMesh/ entirely (no blockMeshDict)
            rm -rf -- "$meshDir"
        fi
    fi

    meshDir="system${region:+/}${region}"
    if [ -e "$meshDir"/blockMeshDict.m4 ]
    then
        rm -f -- "$meshDir"/blockMeshDict
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
