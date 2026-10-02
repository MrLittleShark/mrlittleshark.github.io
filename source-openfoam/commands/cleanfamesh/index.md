---
title: "cleanFaMesh · 清理有限面积网格 faMesh"
layout: reference
description: "清理有限面积网格 faMesh。"
cms_slug: "command-cleanfamesh"
---

<p>清理有限面积网格 faMesh。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanFaMesh -region film
</code></pre>
<p>区域名称决定 constant/finite-area 下的目标位置。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanFaMesh
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanFaMesh()
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

    local meshDir="constant/finite-area/${region}${region:+/}faMesh"

    if [ -e "$meshDir" ]
    then
        [ -n "$region" ] &amp;&amp; echo "Clearing $meshDir" 1&gt;&amp;2
        rm -rf -- "$meshDir"
    fi

    # Legacy location &lt;constant/faMesh&gt;
    # - may still have remnant &lt;constant/faMesh/faMeshDefinition&gt;

    meshDir="constant/faMesh"
    if [ -e "$meshDir" ] &amp;&amp; [ -z "$region" ]
    then
        if [ -e "$meshDir"/faMeshDefinition ]
        then
            # VERY OLD LOCATION
            echo
            echo "WARNING: not removing $meshDir/"
            echo "    It contains a 'faMeshDefinition' file"
            echo "    Please relocate file(s) to system/finite-area/ !!"
            echo
        else
            # Can remove constant/faMesh/ entirely (no faMeshDefinition)
            echo "Clearing $meshDir" 1&gt;&amp;2
            rm -rf -- "$meshDir"
        fi
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
