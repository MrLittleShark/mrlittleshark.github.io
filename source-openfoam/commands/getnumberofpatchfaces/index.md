---
title: "getNumberOfPatchFaces · 读取指定网格边界的面数"
layout: reference
description: "读取指定网格边界的面数。"
cms_slug: "command-getnumberofpatchfaces"
---

<p>读取指定网格边界的面数。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
getNumberOfPatchFaces movingWall
</code></pre>
<p>读取 constant/polyMesh/boundary。第二个位置参数可指定多区域网格的区域名称。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type getNumberOfPatchFaces
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">getNumberOfPatchFaces()
{
    local patch="${1:-}"
    local file="${2:-}"

    file="constant/$file${file:+/}polyMesh/boundary"

    [ -n "$patch" ] || {
        echo "No patch name given" 1&gt;&amp;2
        return 1
    }

    [ -f "$file" ] || {
        echo "No such file: $file" 1&gt;&amp;2
        return 2
    }

    local nFaces
    nFaces=$(sed -ne \
        '/^ *'"$patch"' *$/,/}/{s/^ *nFaces  *\([0-9][0-9]*\) *;.*$/\1/p}' \
        "$file")

    if [ -n "$nFaces" ]
    then
        echo "$nFaces"
    else
        echo "No patch entry found for '$patch' in $file" 1&gt;&amp;2
        echo 0      # Report as 0
        return 2
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
