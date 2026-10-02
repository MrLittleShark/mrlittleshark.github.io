---
title: "cleanPolyMesh · 清理体网格 polyMesh"
layout: reference
description: "清理体网格 polyMesh。"
cms_slug: "command-cleanpolymesh"
---

<p>清理体网格 polyMesh。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。以下每例使用独立空文件演示目录；清理真实算例会移除对应网格。</p>
<h2>示例 1：清除默认网格</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/polyMesh' 'system'
    touch 'constant/polyMesh/points' 'system/controlDict'
    cleanPolyMesh
    find . -type f
)
</code></pre>
<p>移除默认网格目录，system 配置保留。</p>
<h2>示例 2：清除指定区域</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/fluid/polyMesh' 'constant/polyMesh'
    touch 'constant/fluid/polyMesh/points' 'constant/polyMesh/points'
    cleanPolyMesh -region fluid
    find . -type f
)
</code></pre>
<p>-region 只选择 fluid，默认区域网格保留。</p>
<h2>示例 3：使用等号形式</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/fluid/polyMesh'
    touch 'constant/fluid/polyMesh/points'
    cleanPolyMesh -region=fluid
    find . -type f
)
</code></pre>
<p>-region=fluid 与两个参数的写法等效。</p>
<h2>示例 4：识别旧配置存放位置</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/polyMesh'
    touch 'constant/polyMesh/blockMeshDict' 'constant/polyMesh/points'
    cleanPolyMesh
    find . -type f
)
</code></pre>
<p>旧目录内含 blockMeshDict 时，源码保留目录并给出迁移提示，防止连同网格生成配置一起移除。</p>
<h2>示例 5：分别清除两个区域</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/fluid/polyMesh' 'constant/regionB/polyMesh'
    touch 'constant/fluid/polyMesh/points' 'constant/regionB/polyMesh/points'
    cleanPolyMesh -region fluid
    cleanPolyMesh -region regionB
    find . -type f
)
</code></pre>
<p>逐个指定区域，避免把多区域网格误当成默认区域处理。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
