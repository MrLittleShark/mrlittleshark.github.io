---
title: "runParallel · 在 Allrun 中按算例分区设置启动并行程序"
layout: reference
description: "在 Allrun 中按算例分区设置启动并行程序。"
cms_slug: "command-runparallel"
---

<p>在 Allrun 中按算例分区设置启动并行程序。</p><h2>并行运行算例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
runApplication decomposePar
runParallel $(getApplication)
</code></pre>
<p>先分解算例，再读取 controlDict 的 application 并启动并行求解。分区数来自 decomposeParDict，输出保存在求解器日志。</p>
<h2>用于并行网格生成</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
runParallel snappyHexMesh -overwrite
</code></pre>
<p>在已分解的背景网格上运行。这里 -overwrite 传给 snappyHexMesh，控制生成网格的写出位置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
