---
title: "cleanOptimisation · 清理优化结果和控制点输出"
layout: reference
description: "清理优化结果和控制点输出。"
cms_slug: "command-cleanoptimisation"
---

<p>清理优化结果和控制点输出。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanOptimisation
</code></pre>
<p>清理 optimisation 与 constant/controlPoints，重新计算前保留所需的优化历史。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanOptimisation
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanOptimisation()
{
    rm -rf optimisation
    rm -rf constant/controlPoints
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
