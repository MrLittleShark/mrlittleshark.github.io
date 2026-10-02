---
title: "isParallel · 检查参数列表是否包含 -parallel"
layout: reference
description: "检查参数列表是否包含 -parallel。"
cms_slug: "command-isparallel"
---

<p>检查参数列表是否包含 -parallel。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
isParallel -parallel
echo $?
</code></pre>
<p>匹配到 -parallel 时返回 0，否则返回 1；用于脚本条件判断。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type isParallel
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">isParallel()
{
    for i; do [ "$i" = "-parallel" ] &amp;&amp; return 0; done
    return 1
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
