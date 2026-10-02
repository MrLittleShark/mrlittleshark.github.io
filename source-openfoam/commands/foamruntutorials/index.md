---
title: "foamRunTutorials · 执行目标目录中的 Allrun 或 Alltest"
layout: reference
description: "执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。"
cms_slug: "command-foamruntutorials"
---

<p>执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在个人工作目录中准备 caseA 算例副本。新目标目录使用未占用的名称。 递归范围限定于个人教程副本 tutorial-study，包含 Allrun 或完整算例输入。</p>
<h2>示例 1：预览将执行的脚本</h2>
<pre><code class="language-bash">foamRunTutorials -dry-run -case tutorial-study
</code></pre>
<p>列出选中的 Allrun/Alltest 或回退流程，不运行求解器。</p>
<h2>示例 2：执行默认流程</h2>
<pre><code class="language-bash">foamRunTutorials -case tutorial-study
</code></pre>
<p>递归运行教程；没有 Allrun 时尝试 blockMesh 与 controlDict 指定的程序。</p>
<h2>示例 3：优先串行版本</h2>
<pre><code class="language-bash">foamRunTutorials -serial -case tutorial-study
</code></pre>
<p>有 Allrun-serial 时优先选用，适合先调通串行流程。</p>
<h2>示例 4：优先并行版本</h2>
<pre><code class="language-bash">foamRunTutorials -parallel -case tutorial-study
</code></pre>
<p>有 Allrun-parallel 时优先使用，MPI 和分区设置由教程脚本准备。</p>
<h2>示例 5：运行测试流程</h2>
<pre><code class="language-bash">foamRunTutorials -test -case tutorial-study
</code></pre>
<p>优先 Alltest，并将 -test 传给脚本；具体测试规模由教程实现决定。</p>
<h2>示例 6：在外层 Allrun 中递归</h2>
<pre><code class="language-bash">foamRunTutorials -self -case tutorial-study
</code></pre>
<p>-self 跳过起点自己的 Allrun，防止外层脚本再次调用自身。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case=DIR</code></td><td>指定起始目录，默认使用当前目录。</td></tr><tr><td><code>-serial</code></td><td>优先执行 Allrun-serial 脚本。</td></tr><tr><td><code>-parallel</code></td><td>优先执行 Allrun-parallel 脚本。</td></tr><tr><td><code>-test</code></td><td>优先执行 Alltest，并向脚本传入 -test 参数。</td></tr><tr><td><code>-dry-run</code></td><td>仅显示准备执行的脚本。</td></tr><tr><td><code>-self</code></td><td>跳过入口层的 Allrun、Alltest，避免脚本递归调用自身。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamRunTutorials">源码与说明</a> · <a href="/assets/command-help/foamruntutorials.txt">帮助文本</a></p>
