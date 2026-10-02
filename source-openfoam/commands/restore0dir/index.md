---
title: "restore0Dir · 从 0.orig 恢复初始场目录"
layout: reference
description: "从 0.orig 恢复初始场目录。"
cms_slug: "command-restore0dir"
---

<p>从 0.orig 恢复初始场目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
restore0Dir
</code></pre>
<p>已有 0 目录会由模板替换。-processor 作用于分区，-all 同时处理主算例和分区。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type restore0Dir
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">restore0Dir()
{
    if [ ! -d 0.orig ]
    then
        echo "No 0.orig/ to restore..." 1&gt;&amp;2
        return 0
    fi

    case "$1" in
    (-all | -proc | -processor*)
        if [ "$1" = "-all" ]
        then
            echo "Restore 0/ from 0.orig/  [serial/processor dirs]" 1&gt;&amp;2
            \rm -rf 0
            \cp -r 0.orig 0 2&gt;/dev/null
        else
            echo "Restore 0/ from 0.orig/  [processor dirs]" 1&gt;&amp;2
        fi

        \ls -d processor* | xargs -I {} \rm -rf ./{}/0
        \ls -d processor* | xargs -I {} \cp -r 0.orig ./{}/0 &gt; /dev/null 2&gt;&amp;1
        ;;

    (*)
        echo "Restore 0/ from 0.orig/" 1&gt;&amp;2
        \rm -rf 0
        \cp -r 0.orig 0 2&gt;/dev/null
        ;;
    esac
    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
