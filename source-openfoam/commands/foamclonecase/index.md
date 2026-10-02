---
title: "foamCloneCase · 默认复制初始时刻、constant 和 system"
layout: reference
description: "默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。"
cms_slug: "command-foamclonecase"
---

<p>默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在个人工作目录中准备 caseA 算例副本。新目标目录使用未占用的名称。 默认复制首个时间目录及 constant/system，包含源网格。</p>
<h2>示例 1：从现有输入开始</h2>
<pre><code class="language-bash">foamCloneCase caseA caseB
</code></pre>
<p>目标包含首个时间的场及网格、配置，适合作为新试验起点。</p>
<h2>示例 2：从最新结果开始</h2>
<pre><code class="language-bash">foamCloneCase -latestTime caseA restart-case
</code></pre>
<p>复制最新时间而非初始时间；续算前设置 startFrom latestTime。</p>
<h2>示例 3：复制官方方腔</h2>
<pre><code class="language-bash">foamCloneCase "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-study
</code></pre>
<p>得到教程初始副本，可修改网格而不影响安装目录。</p>
<h2>示例 4：准备网格对比组</h2>
<pre><code class="language-bash">mkdir -p grid-study
foamCloneCase caseA grid-study/coarse
foamCloneCase caseA grid-study/fine
</code></pre>
<p>两个副本起点一致，分别改变 blockMeshDict 即可比较网格影响。</p>
<h2>示例 5：生成参数组</h2>
<pre><code class="language-bash">for re in 100 400 1000; do foamCloneCase caseA "Re-$re" || break; done
</code></pre>
<p>为三个参数点创建独立副本，之后逐个编辑物性或入口。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-force</code></td><td>覆盖已有目标。</td></tr><tr><td><code>-l | -latestTime</code></td><td>选择最新的时间目录。</td></tr><tr><td><code>-h | -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCloneCase">源码与说明</a> · <a href="/assets/command-help/foamclonecase.txt">帮助文本</a></p>
