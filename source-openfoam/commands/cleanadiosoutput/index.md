---
title: "cleanAdiosOutput · 清理算例中的 adiosData 输出"
layout: reference
description: "清理算例中的 adiosData 输出。"
cms_slug: "command-cleanadiosoutput"
---

<p>清理算例中的 adiosData 输出。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanAdiosOutput
</code></pre>
<p>函数同时检查 adiosData 与 system 目录是否存在。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanAdiosOutput
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanAdiosOutput()
{
    if [ -d adiosData ] &amp;&amp; [ -d system ]
    then
        rm -rf adiosData
    fi
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
