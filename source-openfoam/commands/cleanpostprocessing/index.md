---
title: "cleanPostProcessing · 清理后处理、VTK 和表面采样输出"
layout: reference
description: "清理后处理、VTK 和表面采样输出。"
cms_slug: "command-cleanpostprocessing"
---

<p>清理后处理、VTK 和表面采样输出。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"
cleanPostProcessing
</code></pre>
<p>包括 postProcessing、VTK、EnSight 等目录，随后可重新执行后处理。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type cleanPostProcessing
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">cleanPostProcessing()
{
    rm -rf Ensight EnSight ensightWrite insitu VTK
    rm -rf postProcessing
    rm -rf postProcessing-*
    rm -rf cuttingPlane
    rm -rf surfaceSampling
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
