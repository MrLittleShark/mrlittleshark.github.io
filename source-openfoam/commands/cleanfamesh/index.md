---
title: "cleanFaMesh · 清理有限面积网格 faMesh"
layout: reference
description: "清理有限面积网格 faMesh。"
cms_slug: "command-cleanfamesh"
---

<p>清理有限面积网格 faMesh。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。以下每例使用独立空文件演示目录；清理真实算例会移除对应网格。</p>
<h2>示例 1：清除默认网格</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/finite-area/faMesh' 'system'
    touch 'constant/finite-area/faMesh/faceLabels' 'system/controlDict'
    cleanFaMesh
    find . -type f
)
</code></pre>
<p>移除默认网格目录，system 配置保留。</p>
<h2>示例 2：清除指定区域</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/finite-area/film/faMesh' 'constant/finite-area/faMesh'
    touch 'constant/finite-area/film/faMesh/faceLabels' 'constant/finite-area/faMesh/faceLabels'
    cleanFaMesh -region film
    find . -type f
)
</code></pre>
<p>-region 只选择 film，默认区域网格保留。</p>
<h2>示例 3：使用等号形式</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/finite-area/film/faMesh'
    touch 'constant/finite-area/film/faMesh/faceLabels'
    cleanFaMesh -region=film
    find . -type f
)
</code></pre>
<p>-region=film 与两个参数的写法等效。</p>
<h2>示例 4：识别旧配置存放位置</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/faMesh'
    touch 'constant/faMesh/faMeshDefinition' 'constant/faMesh/faceLabels'
    cleanFaMesh
    find . -type f
)
</code></pre>
<p>旧目录内含 faMeshDefinition 时，源码保留目录并给出迁移提示，防止连同网格生成配置一起移除。</p>
<h2>示例 5：分别清除两个区域</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'constant/finite-area/film/faMesh' 'constant/finite-area/regionB/faMesh'
    touch 'constant/finite-area/film/faMesh/faceLabels' 'constant/finite-area/regionB/faMesh/faceLabels'
    cleanFaMesh -region film
    cleanFaMesh -region regionB
    find . -type f
)
</code></pre>
<p>逐个指定区域，避免把多区域网格误当成默认区域处理。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
