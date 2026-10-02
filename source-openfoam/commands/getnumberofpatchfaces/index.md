---
title: "getNumberOfPatchFaces · 读取指定网格边界的面数"
layout: reference
description: "读取指定网格边界的面数。"
cms_slug: "command-getnumberofpatchfaces"
---

<p>读取指定网格边界的面数。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 先生成网格并确认实际 patch 名。第二个参数是 region 名，不是文件路径。</p>
<h2>示例 1：查看入口面数</h2>
<pre><code class="language-bash">cd caseA
getNumberOfPatchFaces inlet
</code></pre>
<p>从 constant/polyMesh/boundary 提取 inlet 的 nFaces。</p>
<h2>示例 2：比较入口出口</h2>
<pre><code class="language-bash">cd caseA
for patch in inlet outlet; do printf '%s: ' "$patch"; getNumberOfPatchFaces "$patch"; done
</code></pre>
<p>打印两块边界的面数，可用于检查划分规模。</p>
<h2>示例 3：查询流体区域</h2>
<pre><code class="language-bash">cd caseA
getNumberOfPatchFaces inlet fluid
</code></pre>
<p>第二个参数 fluid 将读取位置改为 constant/fluid/polyMesh/boundary。</p>
<h2>示例 4：在脚本中使用面数</h2>
<pre><code class="language-bash">cd caseA
n=$(getNumberOfPatchFaces inlet) || exit 1
if [ "$n" -gt 0 ]; then echo "inlet has $n faces"; fi
</code></pre>
<p>成功读取后比较整数，入口非空时输出说明。</p>
<h2>示例 5：比较两套网格</h2>
<pre><code class="language-bash">for c in caseA caseB; do (cd "$c" &amp;&amp; getNumberOfPatchFaces inlet); done
</code></pre>
<p>在具有同名 inlet 的两组网格中输出边界面数，观察加密后面数变化。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
