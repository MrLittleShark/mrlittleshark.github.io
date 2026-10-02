---
title: "cleanOptimisation · 清理优化结果和控制点输出"
layout: reference
description: "清理优化结果和控制点输出。"
cms_slug: "command-cleanoptimisation"
---

<p>清理优化结果和控制点输出。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除优化历史</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'optimisation' 'system'
    touch 'optimisation/history' 'system/controlDict'
    cleanOptimisation
    find . -type f
)
</code></pre>
<p>移除 optimisation 输出，system 保留。 末行列出剩余文件。</p>
<h2>示例 2：清除控制点</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/controlPoints' 'constant'
    touch 'constant/controlPoints/points' 'constant/transportProperties'
    cleanOptimisation
    find . -type f
)
</code></pre>
<p>移除 constant/controlPoints，其他物性文件保留。 末行列出剩余文件。</p>
<h2>示例 3：同时处理两类优化数据</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'optimisation' 'constant/controlPoints'
    touch 'optimisation/objective' 'constant/controlPoints/points'
    cleanOptimisation
    find . -type f
)
</code></pre>
<p>两处数据一并移除，适合开始新的优化试验。 末行列出剩余文件。</p>
<h2>示例 4：保留常规后处理</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'optimisation' 'postProcessing'
    touch 'optimisation/history' 'postProcessing/forces.dat'
    cleanOptimisation
    find . -type f
)
</code></pre>
<p>postProcessing 不属于此函数范围，保留原输出。 末行列出剩余文件。</p>
<h2>示例 5：清理单个优化方案</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'designA/optimisation' 'designB/optimisation'
    touch 'designA/optimisation/data' 'designB/optimisation/data'
    cd designA
    cleanOptimisation
    find . -type f
)
</code></pre>
<p>只进入 designA 清理，另一方案的数据保留。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
