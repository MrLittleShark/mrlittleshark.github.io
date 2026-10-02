---
title: "notTest · 检查参数列表是否省略 -test"
layout: reference
description: "检查参数列表是否省略 -test。"
cms_slug: "command-nottest"
---

<p>检查参数列表是否省略 -test。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
notTest -parallel
echo $?
</code></pre>
<p>参数中没有 -test 时返回 0，可用于选择正常运行分支。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type notTest
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">notTest()
{
    for i; do [ "$i" = "-test" ] &amp;&amp; return 1; done
    return 0
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
