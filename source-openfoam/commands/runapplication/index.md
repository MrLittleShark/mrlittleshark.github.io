---
title: "runApplication · 在 Allrun 中执行程序并保存命名日志"
layout: reference
description: "在 Allrun 中执行程序并保存命名日志。"
cms_slug: "command-runapplication"
---

<p>在 Allrun 中执行程序并保存命名日志。</p><h2>载入脚本函数</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
runApplication blockMesh
</code></pre>
<p><code>runApplication</code> 是脚本函数。载入 RunFunctions 后调用，输出写入 <code>log.blockMesh</code>。默认情况下，同名日志已存在时会跳过，以避免重复运行。</p>
<h2>运行算例指定的求解器</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
runApplication $(getApplication)
</code></pre>
<p><code>getApplication</code> 从 controlDict 读取 application，命令替换把名称传给 runApplication。脚本执行结果可在对应求解器日志中查看。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
