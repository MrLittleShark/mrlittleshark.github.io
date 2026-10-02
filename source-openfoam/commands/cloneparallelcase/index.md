---
title: "cloneParallelCase · 复制已分区的算例及选定时间数据"
layout: reference
description: "复制已分区的算例及选定时间数据。"
cms_slug: "command-cloneparallelcase"
---

<p>复制已分区的算例及选定时间数据。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
cloneParallelCase sourceCase parallel-copy 0.5
</code></pre>
<p>两个目录参数之后可给出要复制的时间；省略时间时复制完整 processor 目录。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cloneParallelCase
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cloneParallelCase()
{
    local src=$1
    local dst=$2
    shift 2

    if [ -e "$dst" ]
    then
        echo "Case already cloned: remove case directory $dst prior to cloning"
        return 1
    fi

    [ -d "$src" ] || {
        echo "Error: no directory to clone: $src"
        return 1
    }

    echo "Cloning $dst parallel case from $src"
    mkdir $dst
    # These must exist, so do not hide error messages
    for f in constant system
    do
        \cp -r $src/$f $dst
    done

    [ -d $src/processor0 ] || {
        echo "Does not appear to be a parallel case"
        return 1
    }

    if [ "$#" -eq 0 ]
    then
        # Copy all processor directories
        echo "    clone processor* directories"
        \cp -r $src/processor* $dst
    else
        # Only copy some time directories
        echo "    clone processor directories with $# times: $@"

        for proc in $(\cd $src &amp;&amp; \ls -d processor*)
        do
            srcProc=$src/$proc
            dstProc=$dst/$proc

            mkdir $dstProc
            \cp -r $srcProc/constant $dstProc/

            for time
            do
                [ -d $srcProc/$time ] &amp;&amp; \cp -r $srcProc/$time $dstProc/
            done

        done
    fi

    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
