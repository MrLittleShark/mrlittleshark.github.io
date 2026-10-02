---
title: "cleanPostProcessing · 清理后处理、VTK 和表面采样输出"
layout: reference
description: "清理后处理、VTK 和表面采样输出。"
cms_slug: "command-cleanpostprocessing"
---

<p>清理后处理、VTK 和表面采样输出。</p><h2>开始前</h2>
<p>先执行 source "$WM_PROJECT_DIR/bin/tools/CleanFunctions"。下列空文件用于观察范围；每例先创建独立临时目录，然后只在该目录操作。</p>
<h2>示例 1：清除函数对象结果</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'postProcessing/probes' 'system'
    touch 'postProcessing/probes/U' 'system/controlDict'
    cleanPostProcessing
    find . -type f
)
</code></pre>
<p>移除整个 postProcessing，保留配置。 末行列出剩余文件。</p>
<h2>示例 2：清除 VTK 导出</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'VTK' '1'
    touch 'VTK/mesh.vtu' '1/U'
    cleanPostProcessing
    find . -type f
)
</code></pre>
<p>VTK 目录移除，原始场仍在时间目录中。 末行列出剩余文件。</p>
<h2>示例 3：清除 EnSight 导出</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'EnSight' 'ensightWrite' 'constant'
    touch 'EnSight/case' 'ensightWrite/data' 'constant/file'
    cleanPostProcessing
    find . -type f
)
</code></pre>
<p>支持多个常见 EnSight 目录名字。 末行列出剩余文件。</p>
<h2>示例 4：清除切面采样</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'cuttingPlane' 'surfaceSampling'
    touch 'cuttingPlane/p.raw' 'surfaceSampling/U.raw'
    cleanPostProcessing
    find . -type f
)
</code></pre>
<p>两个旧式采样输出目录均被移除。 末行列出剩余文件。</p>
<h2>示例 5：清除多个后处理批次</h2>
<pre><code class="language-bash">demoDir=$(mktemp -d "$HOME/foam-clean-demo.XXXXXX")
(
    cd "$demoDir" || exit 1
    mkdir -p 'postProcessing-old' 'postProcessing-new' 'system'
    touch 'postProcessing-old/a' 'postProcessing-new/b' 'system/controlDict'
    cleanPostProcessing
    find . -type f
)
</code></pre>
<p>postProcessing-* 也匹配，所有这些批次将被清除。 末行列出剩余文件。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">源码与说明</a></p>
