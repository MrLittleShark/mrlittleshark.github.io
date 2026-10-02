---
title: "cloneCase · 复制算例的 constant、system 和初始场目录"
layout: reference
description: "复制算例的 constant、system 和初始场目录。"
cms_slug: "command-clonecase"
---

<p>复制算例的 constant、system 和初始场目录。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 源目录应有 constant、system，以及 0 或 0.orig；目标必须不存在，父目录须已建立。函数只复制初始设置，不复制后续时间目录。</p>
<h2>示例 1：建立第一份副本</h2>
<pre><code class="language-bash">cloneCase caseA caseB
</code></pre>
<p>复制初始设置到 caseB，用于修改参数。</p>
<h2>示例 2：从官方方腔开始</h2>
<pre><code class="language-bash">cloneCase "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-study
</code></pre>
<p>源路径为标准方腔教程；目标中包含初始场、物性和网格配置。</p>
<h2>示例 3：准备粗细网格组</h2>
<pre><code class="language-bash">mkdir -p mesh-study
cloneCase caseA mesh-study/coarse
cloneCase caseA mesh-study/fine
</code></pre>
<p>父目录先建立，再生成相互独立的配置副本。</p>
<h2>示例 4：保存初始条件模板</h2>
<pre><code class="language-bash">cloneCase caseA reference-input
find reference-input -maxdepth 2 -type f
</code></pre>
<p>列出复制的文件；存在 0.orig 时也会保留。</p>
<h2>示例 5：生成多个参数组</h2>
<pre><code class="language-bash">for re in 100 400 1000; do cloneCase caseA "Re-$re" || break; done
</code></pre>
<p>三个新目录起点一致，随后分别编辑黏度或边界速度。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
