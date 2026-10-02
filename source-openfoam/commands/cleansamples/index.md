---
title: "cleanSamples · 清理 sets、samples 和 sampleSurfaces 采样结果"
layout: reference
description: "清理 sets、samples 和 sampleSurfaces 采样结果。"
cms_slug: "command-cleansamples"
---

<p>清理 sets、samples 和 sampleSurfaces 采样结果。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除集合采样</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'sets' 'system'
    touch 'sets/p.xy' 'system/controlDict'
    cleanSamples
    find . -type f
)
</code></pre>
<p>sets 被移除，system 保留。 末行列出剩余文件。</p>
<h2>示例 2：清除 samples 目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'samples' '0'
    touch 'samples/U.xy' '0/U'
    cleanSamples
    find . -type f
)
</code></pre>
<p>samples 被移除，初始速度场保留。 末行列出剩余文件。</p>
<h2>示例 3：清除表面采样</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'sampleSurfaces' 'constant'
    touch 'sampleSurfaces/p.raw' 'constant/transportProperties'
    cleanSamples
    find . -type f
)
</code></pre>
<p>sampleSurfaces 被移除，物性保留。 末行列出剩余文件。</p>
<h2>示例 4：同时处理三种旧式输出</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'sets' 'samples' 'sampleSurfaces'
    touch 'sets/a' 'samples/b' 'sampleSurfaces/c'
    cleanSamples
    find . -type f
)
</code></pre>
<p>三个目录均属该函数处理范围。 末行列出剩余文件。</p>
<h2>示例 5：区分新旧输出目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'sets' 'postProcessing'
    touch 'sets/p.xy' 'postProcessing/p.dat'
    cleanSamples
    find . -type f
)
</code></pre>
<p>本函数只清理旧式采样目录，postProcessing 保留。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
