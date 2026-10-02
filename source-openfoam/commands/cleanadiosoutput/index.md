---
title: "cleanAdiosOutput · 清理算例中的 adiosData 输出"
layout: reference
description: "清理算例中的 adiosData 输出。"
cms_slug: "command-cleanadiosoutput"
---

<p>清理算例中的 adiosData 输出。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：移除 ADIOS 数据</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'adiosData'
    touch 'system/controlDict' 'adiosData/step1.bp'
    cleanAdiosOutput
    find . -type f
)
</code></pre>
<p>存在 system 时移除整个 adiosData。 末行列出剩余文件。</p>
<h2>示例 2：清理多个时间输出</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'adiosData/0' 'adiosData/1'
    touch 'adiosData/0/U' 'adiosData/1/U' 'system/controlDict'
    cleanAdiosOutput
    find . -type f
)
</code></pre>
<p>整个输出树被移除，而非仅最新时刻。 末行列出剩余文件。</p>
<h2>示例 3：保留标准场目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'adiosData' '1'
    touch 'adiosData/data' '1/U' 'system/controlDict'
    cleanAdiosOutput
    find . -type f
)
</code></pre>
<p>只清理 ADIOS 目录，标准时间目录保留。 末行列出剩余文件。</p>
<h2>示例 4：检查目录条件</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'adiosData'
    touch 'adiosData/data'
    cleanAdiosOutput
    find . -type f
)
</code></pre>
<p>没有 system 目录时函数不执行移除。 末行列出剩余文件。</p>
<h2>示例 5：处理一个算例子目录</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'caseA/system' 'caseA/adiosData' 'caseB/system' 'caseB/adiosData'
    touch 'caseA/adiosData/a' 'caseB/adiosData/b'
    cd caseA
    cleanAdiosOutput
    find . -type f
)
</code></pre>
<p>进入 caseA 后仅清理其 ADIOS 输出，caseB 保留。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
