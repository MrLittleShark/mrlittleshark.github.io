---
title: "cleanCase0 · 清理算例结果，并删除 0 目录"
layout: reference
description: "清理算例结果，并删除 0 目录。"
cms_slug: "command-cleancase0"
---

<p>清理算例结果，并删除 0 目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanCase0
</code></pre>
<p>通常与 0.orig 模板配合，随后用 restore0Dir 重建初始场。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanCase0
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanCase0()
{
    cleanCase
    rm -rf 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
