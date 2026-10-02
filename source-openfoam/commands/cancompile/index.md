---
title: "canCompile · 检查 make、wmake 和 C++ 编译器是否可用"
layout: reference
description: "检查 make、wmake 和 C++ 编译器是否可用。"
cms_slug: "command-cancompile"
---

<p>检查 make、wmake 和 C++ 编译器是否可用。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
canCompile
echo $?
</code></pre>
<p>退出码 0 表示检查通过。缺少工具时，函数在错误输出中说明缺项。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type canCompile
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">canCompile()
{
    # system
    if ! command -v make &gt;/dev/null
    then
        echo "No system 'make' command found ... cannot compile" 1&gt;&amp;2
        return 1
    fi

    # OpenFOAM-specific
    if ! command -v wmake &gt;/dev/null
    then
        echo "No openfoam 'wmake' command found ... cannot compile" 1&gt;&amp;2
        return 1
    fi

    local cxx_compiler
    cxx_compiler="$(wmake -show-cxx 2&gt;/dev/null)"

    if [ -z "$cxx_compiler" ]
    then
        echo "No wmake rule for C++ compiler ... cannot compile" 1&gt;&amp;2
        return 1
    elif ! command -v "$cxx_compiler"  &gt;/dev/null
    then
        echo "No path to C++ compiler ($cxx_compiler) ... cannot compile" 1&gt;&amp;2
        return 1
    fi

    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
