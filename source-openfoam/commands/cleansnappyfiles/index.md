---
title: "cleanSnappyFiles · 清理 snappyHexMesh 的细化历史和辅助字段"
layout: reference
description: "清理 snappyHexMesh 的细化历史和辅助字段。"
cms_slug: "command-cleansnappyfiles"
---

<p>清理 snappyHexMesh 的细化历史和辅助字段。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除细化层级标记</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/polyMesh'
    touch 'constant/polyMesh/cellLevel' 'constant/polyMesh/pointLevel' 'constant/polyMesh/points'
    cleanSnappyFiles
    find . -type f
)
</code></pre>
<p>移除 cellLevel、pointLevel，保留网格 points。 末行列出剩余文件。</p>
<h2>示例 2：清除细化历史</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/polyMesh'
    touch 'constant/polyMesh/refinementHistory' 'constant/polyMesh/level0Edge' 'constant/polyMesh/faces'
    cleanSnappyFiles
    find . -type f
)
</code></pre>
<p>清除细化辅助信息，网格拓扑 faces 保留。 末行列出剩余文件。</p>
<h2>示例 3：处理并行辅助文件</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'processor0/constant/polyMesh' 'processor1/constant/polyMesh'
    touch 'processor0/constant/polyMesh/surfaceIndex' 'processor1/constant/polyMesh/cellLevel'
    cleanSnappyFiles
    find . -type f
)
</code></pre>
<p>同时匹配各 processor 子目录。 末行列出剩余文件。</p>
<h2>示例 4：清除旧位置层级字段</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant' '0'
    touch 'constant/cellLevel' 'constant/pointLevel' '0/cellLevel' '0/pointLevel' '0/U'
    cleanSnappyFiles
    find . -type f
)
</code></pre>
<p>清除这些旧位置的层级数据，保留速度场。 末行列出剩余文件。</p>
<h2>示例 5：保留表面输入</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/triSurface' 'constant/polyMesh'
    touch 'constant/triSurface/body.stl' 'constant/polyMesh/surfaceIndex'
    cleanSnappyFiles
    find . -type f
)
</code></pre>
<p>移除 surfaceIndex，STL 表面保留以供重新划分。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
