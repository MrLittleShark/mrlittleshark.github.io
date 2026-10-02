---
title: "cleanUcomponents · 删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件"
layout: reference
description: "删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件。"
cms_slug: "command-cleanucomponents"
---

<p>删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanUcomponents
</code></pre>
<p>完整速度矢量场 0/U 保持原样。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanUcomponents
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanUcomponents()
{
    rm -rf 0/Ux 0/Uy 0/Uz
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
