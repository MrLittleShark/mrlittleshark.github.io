---
title: "restore0Dir · 从 0.orig 恢复初始场目录"
layout: reference
description: "从 0.orig 恢复初始场目录。"
cms_slug: "command-restore0dir"
---

<p>从 0.orig 恢复初始场目录。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 在算例副本中保留完整 0.orig。函数先移除目标 0 再复制模板，目标目录中新增加的文件也会被替换。</p>
<h2>示例 1：恢复串行初始场</h2>
<pre><code class="language-bash">restore0Dir
</code></pre>
<p>从 0.orig 重建顶层 0，适合参数试验后恢复起点。</p>
<h2>示例 2：网格生成后恢复</h2>
<pre><code class="language-bash">runApplication blockMesh
restore0Dir
</code></pre>
<p>先完成网格，再恢复与该网格边界匹配的初始场。</p>
<h2>示例 3：恢复各并行子域模板</h2>
<pre><code class="language-bash">restore0Dir -processor
</code></pre>
<p>复制同一 0.orig 到 processor*/0；该模板需含适用于分区的边界配置。</p>
<h2>示例 4：同时恢复顶层和子域</h2>
<pre><code class="language-bash">restore0Dir -all
</code></pre>
<p>重建顶层及 processor*/0，适用于用统一模板初始化的流程。</p>
<h2>示例 5：恢复后调整速度</h2>
<pre><code class="language-bash">restore0Dir
foamDictionary 0/U -entry internalField -set "uniform (1 0 0)"
</code></pre>
<p>对有 U 字段的算例，从一致模板开始改内部初值；入口等边界项仍按实际模型另行设置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
