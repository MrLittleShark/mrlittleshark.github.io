---
title: "cleanAuxiliary · 清理求解日志、ParaView 入口和辅助输出"
layout: reference
description: "清理求解日志、ParaView 入口和辅助输出。"
cms_slug: "command-cleanauxiliary"
---

<p>清理求解日志、ParaView 入口和辅助输出。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：移除日志</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system'
    touch 'log.icoFoam' 'log.checkMesh' 'system/controlDict'
    cleanAuxiliary
    find . -type f
)
</code></pre>
<p>移除 log.*，字典保留。 末行列出剩余文件。</p>
<h2>示例 2：移除可视化入口</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system'
    touch 'case.foam' 'case.OpenFOAM' 'case.blockMesh' 'system/controlDict'
    cleanAuxiliary
    find . -type f
)
</code></pre>
<p>清除阅读器标记文件，system 保留。 末行列出剩余文件。</p>
<h2>示例 3：移除 ParaView 临时文件</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'ParaView-cache' 'system'
    touch 'ParaView-cache/state' 'view.xml' 'system/controlDict'
    cleanAuxiliary
    find . -type f
)
</code></pre>
<p>ParaView* 和 *.xml 在清理范围内。 末行列出剩余文件。</p>
<h2>示例 4：清除调试清单</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system' 'mpirun.log'
    touch 'mpirun.files' 'mpirun.log/rank0' 'system/controlDict'
    cleanAuxiliary
    find . -type f
)
</code></pre>
<p>mpirun.files 移除；mpirun.log 目录按源码保留，方便诊断。 末行列出剩余文件。</p>
<h2>示例 5：清除分阶段日志</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'system'
    touch 'log-mesh' 'logSummary.run' 'system/controlDict'
    cleanAuxiliary
    find . -type f
)
</code></pre>
<p>处理 log-* 和 logSummary.*；不修改 controlDict。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
