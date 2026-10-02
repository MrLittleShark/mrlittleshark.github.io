---
title: "cleanUcomponents · 删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件"
layout: reference
description: "删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件。"
cms_slug: "command-cleanucomponents"
---

<p>删除 0/Ux、0/Uy 和 0/Uz 三个速度分量文件。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除一个分量</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '0'
    touch '0/U' '0/Ux'
    cleanUcomponents
    find . -type f
)
</code></pre>
<p>只删除 Ux，保留向量场 U。 末行列出剩余文件。</p>
<h2>示例 2：清除三个分量</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '0'
    touch '0/U' '0/Ux' '0/Uy' '0/Uz'
    cleanUcomponents
    find . -type f
)
</code></pre>
<p>初始目录的 Ux、Uy、Uz 全部移除。 末行列出剩余文件。</p>
<h2>示例 3：保留其他标量</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '0'
    touch '0/Ux' '0/p' '0/T'
    cleanUcomponents
    find . -type f
)
</code></pre>
<p>p 与 T 不在指定文件列表中。 末行列出剩余文件。</p>
<h2>示例 4：区分初始与结果时刻</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '0' '1'
    touch '0/Ux' '1/Ux'
    cleanUcomponents
    find . -type f
)
</code></pre>
<p>函数只处理 0，时间 1 的分量场保留。 末行列出剩余文件。</p>
<h2>示例 5：处理子域的分量</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'processor0/0'
    touch 'processor0/0/Ux' 'processor0/0/U'
    cd processor0
    cleanUcomponents
    find . -type f
)
</code></pre>
<p>进入子域目录后调用，删除该子域 0/Ux，保留 U。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
