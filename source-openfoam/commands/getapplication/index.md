---
title: "getApplication · 读取 controlDict 中的 application"
layout: reference
description: "读取 controlDict 中的 application。"
cms_slug: "command-getapplication"
---

<p>读取 controlDict 中的 application。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
getApplication
</code></pre>
<p>返回求解器名称，常与 runApplication 的命令替换配合。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type getApplication
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">getApplication()
{
    # Re-use positional parameters for automatic whitespace elimination
    set -- $(foamDictionary -entry application -value system/controlDict 2&gt;/dev/null)

    if [ "$#" -eq 1 ]
    then
        echo "$1"
    else
        echo "Error getting 'application' from system/controlDict" 1&gt;&amp;2
        echo false  # Fallback
        return 1
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
