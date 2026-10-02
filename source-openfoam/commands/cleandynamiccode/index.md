---
title: "cleanDynamicCode · 清理动态编译生成的 dynamicCode 目录"
layout: reference
description: "清理动态编译生成的 dynamicCode 目录。"
cms_slug: "command-cleandynamiccode"
---

<p>清理动态编译生成的 dynamicCode 目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanDynamicCode
</code></pre>
<p>后续读到相应 coded 条目时会重新生成和编译动态代码。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanDynamicCode
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanDynamicCode()
{
    if [ -d dynamicCode ] &amp;&amp; [ -d system ]
    then
        rm -rf dynamicCode
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
