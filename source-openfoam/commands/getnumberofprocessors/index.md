---
title: "getNumberOfProcessors · 读取 decomposeParDict 中的 numberOfSubdomains"
layout: reference
description: "读取 decomposeParDict 中的 numberOfSubdomains。"
cms_slug: "command-getnumberofprocessors"
---

<p>读取 decomposeParDict 中的 numberOfSubdomains。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。</p>
<h2>示例 1：读取默认分解数</h2>
<pre><code class="language-bash">cd caseA
getNumberOfProcessors
</code></pre>
<p>从 system/decomposeParDict 读取 numberOfSubdomains 并输出整数。</p>
<h2>示例 2：读取另一份方案</h2>
<pre><code class="language-bash">cd caseA
getNumberOfProcessors decomposeParDict.scotch
</code></pre>
<p>文件若不在当前目录，函数会继续按 system/decomposeParDict.scotch 查找。</p>
<h2>示例 3：使用明确路径</h2>
<pre><code class="language-bash">cd caseA
getNumberOfProcessors system/decomposeParDict.four
</code></pre>
<p>指定已经准备的替代字典；输出该字典中的子域数。</p>
<h2>示例 4：传递给 MPI</h2>
<pre><code class="language-bash">cd caseA
n=$(getNumberOfProcessors) || exit 1
mpirun -np "$n" checkMesh -parallel
</code></pre>
<p>先按相同字典完成 decomposePar；MPI 数量与子域数一致，终端显示分区网格检查。</p>
<h2>示例 5：比较两套方案</h2>
<pre><code class="language-bash">cd caseA
for dict in system/decomposeParDict.*; do printf '%s: ' "$dict"; getNumberOfProcessors "$dict"; done
</code></pre>
<p>为每份匹配字典输出分区数；适用于并行规模试验前整理配置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
