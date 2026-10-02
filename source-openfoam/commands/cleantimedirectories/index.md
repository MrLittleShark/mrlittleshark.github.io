---
title: "cleanTimeDirectories · 清理非零数值时间目录"
layout: reference
description: "清理非零数值时间目录。"
cms_slug: "command-cleantimedirectories"
---

<p>清理非零数值时间目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanTimeDirectories
</code></pre>
<p>运行前在练习副本中用 ls 查看时间目录，并保存需要比较的结果。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanTimeDirectories
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanTimeDirectories()
{
    echo "Cleaning case $PWD"
    zeros=""
    while [ ${#zeros} -lt 8 ]
    do
        rm -rf ./"0.$zeros"[1-9]* ./"-0.$zeros"[1-9]*
        zeros="0$zeros"
    done
    rm -rf ./[1-9]* ./-[1-9]*
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
