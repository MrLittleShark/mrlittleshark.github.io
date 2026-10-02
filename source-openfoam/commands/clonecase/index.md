---
title: "cloneCase · 复制算例的 constant、system 和初始场目录"
layout: reference
description: "复制算例的 constant、system 和初始场目录。"
cms_slug: "command-clonecase"
---

<p>复制算例的 constant、system 和初始场目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
cloneCase cavity cavity-study
</code></pre>
<p>第一个参数是源算例，第二个是尚不存在的目标目录。已有目标目录时函数返回错误，便于脚本避免混合两套输入。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cloneCase
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cloneCase()
{
    local src=$1
    local dst=$2
    shift 2

    if [ -e "$dst" ]
    then
        echo "Case already cloned: remove case directory $dst prior to cloning"
        return 1
    elif [ ! -d "$src" ]
    then
        echo "Error: no directory to clone:  $src"
        return 1
    fi

    echo "Cloning $dst case from $src"
    mkdir $dst
    # These must exist, so do not hide error messages
    for f in constant system
    do
        \cp -r $src/$f $dst
    done

    # Either (or both) may exist, so error messages may be spurious
    for f in 0 0.orig
    do
        \cp -r $src/$f $dst 2&gt;/dev/null
    done
    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
