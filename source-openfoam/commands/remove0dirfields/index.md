---
title: "remove0DirFields · 删除 0 目录中指定名称的场文件"
layout: reference
description: "删除 0 目录中指定名称的场文件。"
cms_slug: "command-remove0dirfields"
---

<p>删除 0 目录中指定名称的场文件。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
remove0DirFields Ux Uy Uz
</code></pre>
<p>仅用于准备好的练习副本；三个参数分别指定场名。多区域场可使用 -region 区域名。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type remove0DirFields
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">remove0DirFields()
{
    local region

    # Parse options
    while [ "$#" -gt 0 ]
    do
        case "$1" in
        ('')  ;;                # Ignore empty option
        (--)  shift; break ;;   # Stop option parsing

        (-region)   region="$2"; shift ;;
        (*) break ;;
        esac
        shift
    done

    # safety
    if [ "$region" = "--" ]; then unset region; fi

    if [ "$#" -eq 0 ]
    then
        echo "No fields specified for ${region:+region=$region }" 1&gt;&amp;2
        return 0
    fi

    echo "Remove 0/ fields${region:+ [$region]} : $@" 1&gt;&amp;2

    local subdir
    for subdir in 0/"$region" processor*/0/"$region"
    do
        if [ -d "$subdir" ]
        then
            for field in $@  ## unquoted for IFS splitting [SIC]
            do
                # Cautious with removal
                if [ -f "$subdir/$field" ]
                then
                    rm -f -- "$subdir/$field"
                fi
            done
        fi
    done
    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
