---
title: "cleanCase0 · 清理算例结果，并删除 0 目录"
layout: reference
description: "清理算例结果，并删除 0 目录。"
cms_slug: "command-cleancase0"
---

<p>清理算例结果，并删除 0 目录。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下面只使用新建的演示树；函数会组合清理时间目录、网格、日志和结果。还会无条件移除 0。</p>
<h2>示例 1：恢复为输入结构</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'constant/polyMesh' '0' '1'
    touch 'system/controlDict' 'constant/polyMesh/points' '0/U' '1/U'
    cleanCase0
    find . -type f
)
</code></pre>
<p>本例的网格、后续时刻及辅助结果会清理，system、0.orig 和 triSurface 输入保留。0 也被移除。 末行可检查实际剩余文件。</p>
<h2>示例 2：移除并行结果</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'processor0/0' 'processor1/0' '0.orig'
    touch 'system/controlDict' 'processor0/0/U' 'processor1/0/U' '0.orig/U'
    cleanCase0
    find . -type f
)
</code></pre>
<p>本例的网格、后续时刻及辅助结果会清理，system、0.orig 和 triSurface 输入保留。0 也被移除。 末行可检查实际剩余文件。</p>
<h2>示例 3：清理后处理</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'postProcessing' 'VTK' '0'
    touch 'system/controlDict' 'postProcessing/probes.dat' 'VTK/mesh.vtu' '0/U'
    cleanCase0
    find . -type f
)
</code></pre>
<p>本例的网格、后续时刻及辅助结果会清理，system、0.orig 和 triSurface 输入保留。0 也被移除。 末行可检查实际剩余文件。</p>
<h2>示例 4：清理动态代码与日志</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'dynamicCode' '0'
    touch 'system/controlDict' 'dynamicCode/code.C' 'log.solver' '0/U'
    cleanCase0
    find . -type f
)
</code></pre>
<p>本例的网格、后续时刻及辅助结果会清理，system、0.orig 和 triSurface 输入保留。0 也被移除。 末行可检查实际剩余文件。</p>
<h2>示例 5：保留输入几何</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'constant/triSurface' 'constant/polyMesh' '0.orig'
    touch 'system/controlDict' 'constant/triSurface/body.stl' 'constant/polyMesh/points' '0.orig/U'
    cleanCase0
    find . -type f
)
</code></pre>
<p>本例的网格、后续时刻及辅助结果会清理，system、0.orig 和 triSurface 输入保留。0 也被移除。 末行可检查实际剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
