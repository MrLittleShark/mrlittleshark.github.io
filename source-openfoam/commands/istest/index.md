---
title: "isTest · 检查参数列表是否包含 -test"
layout: reference
description: "检查参数列表是否包含 -test。"
cms_slug: "command-istest"
---

<p>检查参数列表是否包含 -test。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
isTest -test
echo $?
</code></pre>
<p>返回码表示是否启用测试模式。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type isTest
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">isTest()
{
    for i; do [ "$i" = "-test" ] &amp;&amp; return 0; done
    return 1
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
