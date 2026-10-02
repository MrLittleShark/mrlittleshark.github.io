---
title: "cleanApplication · 调用 wclean 清理当前应用的编译中间文件"
layout: reference
description: "调用 wclean 清理当前应用的编译中间文件。"
cms_slug: "command-cleanapplication"
---

<p>调用 wclean 清理当前应用的编译中间文件。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanApplication
</code></pre>
<p>在应用源码目录调用；后续可重新运行 wmake。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanApplication
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanApplication()
{
    echo "Cleaning application $PWD"
    wclean
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
