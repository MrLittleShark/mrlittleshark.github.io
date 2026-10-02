---
title: "cleanTimeDirectories · 清理非零数值时间目录"
layout: reference
description: "清理非零数值时间目录。"
cms_slug: "command-cleantimedirectories"
---

<p>清理非零数值时间目录。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除普通时间结果</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' '0' '0.1' '1'
    touch 'system/controlDict' '0/U' '0.1/U' '1/U'
    cleanTimeDirectories
    find . -type f
)
</code></pre>
<p>移除 0.1 和 1，保留 0 与 system。 末行列出剩余文件。</p>
<h2>示例 2：处理负时间结果</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' '-0.1' '-1'
    touch 'system/controlDict' '-0.1/U' '-1/U'
    cleanTimeDirectories
    find . -type f
)
</code></pre>
<p>负时间目录也在匹配范围内，system 保留。 末行列出剩余文件。</p>
<h2>示例 3：保留初始场模板</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '0' '0.orig' '2'
    touch '0/U' '0.orig/U' '2/U'
    cleanTimeDirectories
    find . -type f
)
</code></pre>
<p>0 与 0.orig 保留，2 被移除。 末行列出剩余文件。</p>
<h2>示例 4：在单个子域中清理</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'processor0/0' 'processor0/1'
    touch 'processor0/0/U' 'processor0/1/U'
    cd processor0
    cleanTimeDirectories
    find . -type f
)
</code></pre>
<p>先进入 processor0，仅清除该子域时间结果，保留其 0。 末行列出剩余文件。</p>
<h2>示例 5：观察数字前缀匹配</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p '123-notes' 'system'
    touch '123-notes/readme' 'system/controlDict'
    cleanTimeDirectories
    find . -type f
)
</code></pre>
<p>源码按数字前缀通配，因此 123-notes 也会移除；演示说明清理目录需只存算例数据。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
