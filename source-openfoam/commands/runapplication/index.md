---
title: "runApplication · 在 Allrun 中执行程序并保存命名日志"
layout: reference
description: "在 Allrun 中执行程序并保存命名日志。"
cms_slug: "command-runapplication"
---

<p>在 Allrun 中执行程序并保存命名日志。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 在算例根目录执行。选项放在程序名前；程序自己的选项放在程序名后。默认已有同名日志时跳过运行。</p>
<h2>示例 1：生成网格</h2>
<pre><code class="language-bash">runApplication blockMesh
</code></pre>
<p>执行 blockMesh，标准输出和错误写入 log.blockMesh。</p>
<h2>示例 2：检查网格</h2>
<pre><code class="language-bash">runApplication checkMesh -allGeometry -allTopology
</code></pre>
<p>两个网格检查选项透传给 checkMesh，输出在 log.checkMesh。</p>
<h2>示例 3：运行字典指定求解器</h2>
<pre><code class="language-bash">runApplication "$(getApplication)"
</code></pre>
<p>读取 controlDict 的 application，生成对应 log.&lt;程序名&gt;。</p>
<h2>示例 4：保留多个检查批次</h2>
<pre><code class="language-bash">runApplication -s afterRefine checkMesh
</code></pre>
<p>-s 为日志增加 .afterRefine 后缀，得到 log.checkMesh.afterRefine。</p>
<h2>示例 5：分别保存一组日志</h2>
<pre><code class="language-bash">mkdir -p diagnostics
runApplication -d diagnostics -o checkMesh
</code></pre>
<p>-d 指定已经建立的日志目录，-o 允许覆盖该目录内的旧日志并重新执行。</p>
<h2>示例 6：追加新的诊断</h2>
<pre><code class="language-bash">runApplication -a checkMesh
</code></pre>
<p>-a 无论日志是否存在都执行，并把输出追加到 log.checkMesh。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
