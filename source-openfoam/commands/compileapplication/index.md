---
title: "compileApplication · 通过 wmake 编译指定目录中的应用程序"
layout: reference
description: "通过 wmake 编译指定目录中的应用程序。"
cms_slug: "command-compileapplication"
---

<p>通过 wmake 编译指定目录中的应用程序。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
compileApplication ./mySolver
</code></pre>
<p>目标目录包含 Make/files 与 Make/options。函数打印目标名称，再把目录传给 wmake。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type compileApplication
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">compileApplication()
{
    echo "Compiling $1 application"
    wmake $1
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
