---
title: "isParallel · 检查参数列表是否包含 -parallel"
layout: reference
description: "检查参数列表是否包含 -parallel。"
cms_slug: "command-isparallel"
---

<p>检查参数列表是否包含 -parallel。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 此函数检查传入参数列表，返回状态码；它本身不启动计算。</p>
<h2>示例 1：识别指定标记</h2>
<pre><code class="language-bash">if isParallel -parallel; then echo "true"; else echo "false"; fi
</code></pre>
<p>匹配到 -parallel 时，本例输出 true。</p>
<h2>示例 2：检查多个参数</h2>
<pre><code class="language-bash">if isParallel -case caseA -parallel; then echo "selected"; else echo "other"; fi
</code></pre>
<p>函数遍历整个参数列表，标记无需放在第一位。</p>
<h2>示例 3：处理未提供标记的情况</h2>
<pre><code class="language-bash">if isParallel -case caseA; then echo "selected"; else echo "other"; fi
</code></pre>
<p>本例未传 -parallel，返回状态 1，便于区分默认分支。</p>
<h2>示例 4：在 Allrun 中保留原参数</h2>
<pre><code class="language-bash">cat &gt; argument-demo.sh &lt;&lt;'EOF'
#!/bin/sh
. "$WM_PROJECT_DIR/bin/tools/RunFunctions"
if isParallel "$@"; then
    echo "selected workflow"
else
    echo "alternative workflow"
fi
EOF
sh argument-demo.sh -parallel
</code></pre>
<p>"$@" 按原参数边界传入，脚本输出对应流程名。</p>
<h2>示例 5：用状态控制实际步骤</h2>
<pre><code class="language-bash">if isParallel -parallel; then runParallel checkMesh; else runApplication checkMesh; fi
</code></pre>
<p>在已准备的算例目录执行；并行分支需先分区。测试分支只做网格检查，普通分支可运行求解器。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
