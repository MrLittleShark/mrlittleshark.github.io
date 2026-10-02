---
title: "getNumberOfProcessors · 读取 decomposeParDict 中的 numberOfSubdomains"
layout: reference
description: "读取 decomposeParDict 中的 numberOfSubdomains。"
cms_slug: "command-getnumberofprocessors"
---

<p>读取 decomposeParDict 中的 numberOfSubdomains。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
getNumberOfProcessors
getNumberOfProcessors system/decomposeParDict
</code></pre>
<p>省略参数时使用 system/decomposeParDict。输出可用作 mpirun 的进程数。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type getNumberOfProcessors
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">getNumberOfProcessors()
{
    local dict="${1:-system/decomposeParDict}"

    case "$dict" in
    (system/*)  # Already qualified
        ;;
    (*)
        # If it does not exist, assume it refers to location in system/
        [ -f "$dict" ] || dict="system/$dict"
        ;;
    esac


    # Re-use positional parameters for automatic whitespace elimination
    set -- $(foamDictionary -entry numberOfSubdomains -value "$dict" 2&gt;/dev/null)

    if [ "$#" -eq 1 ]
    then
        echo "$1"
    else
        echo "Error getting 'numberOfSubdomains' from '$dict'" 1&gt;&amp;2
        echo 1      # Fallback is 1 proc (serial)
        return 1
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
