---
title: "cleanSamples · 清理 sets、samples 和 sampleSurfaces 采样结果"
layout: reference
description: "清理 sets、samples 和 sampleSurfaces 采样结果。"
cms_slug: "command-cleansamples"
---

<p>清理 sets、samples 和 sampleSurfaces 采样结果。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanSamples
</code></pre>
<p>适合更改采样设置后重新输出，避免旧文件与新文件混合。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanSamples
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanSamples()
{
    rm -rf sets samples sampleSurfaces
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
