---
title: "removeCase · 删除参数指定的整个算例目录"
layout: reference
description: "删除参数指定的整个算例目录。"
cms_slug: "command-removecase"
---

<p>删除参数指定的整个算例目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
removeCase ./discarded-practice
</code></pre>
<p>参数应指向已确认可以删除的练习副本。该函数递归删除整个目标目录。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type removeCase
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">removeCase()
{
    echo "Removing case ${1:-unknown}"
    [ "$#" -ge 1 ] &amp;&amp; rm -rf -- "$1"
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
