---
title: "runParallel · 在 Allrun 中按算例分区设置启动并行程序"
layout: reference
description: "在 Allrun 中按算例分区设置启动并行程序。"
cms_slug: "command-runparallel"
---

<p>在 Allrun 中按算例分区设置启动并行程序。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 先按 decomposeParDict 完成 decomposePar。MPI 环境需可用；选项放程序名前，程序参数放其后。函数自动给程序添加 -parallel。</p>
<h2>示例 1：检查分区网格</h2>
<pre><code class="language-bash">runParallel checkMesh
</code></pre>
<p>默认从 system/decomposeParDict 读取进程数，日志为 log.checkMesh。</p>
<h2>示例 2：运行并行求解器</h2>
<pre><code class="language-bash">runParallel "$(getApplication)"
</code></pre>
<p>启动与分区数相同的 MPI 进程，求解器名来自 controlDict。</p>
<h2>示例 3：明确使用四个进程</h2>
<pre><code class="language-bash">runParallel -np 4 checkMesh
</code></pre>
<p>已有四个未合并子域时使用；-np 覆盖自动读取的进程数。</p>
<h2>示例 4：用另一份分解设置</h2>
<pre><code class="language-bash">runParallel -decomposeParDict system/decomposeParDict.scotch checkMesh
</code></pre>
<p>读取该字典的分区数，并将同一路径传给程序；分区须按该字典生成。</p>
<h2>示例 5：保留不同规模的日志</h2>
<pre><code class="language-bash">runParallel -np 4 -s np4 "$(getApplication)"
</code></pre>
<p>日志末尾增加 .np4，便于区分进程规模试验。</p>
<h2>示例 6：集中保存并行诊断</h2>
<pre><code class="language-bash">mkdir -p parallel-logs
runParallel -d parallel-logs -o checkMesh
</code></pre>
<p>输出写入 parallel-logs/log.checkMesh，-o 重新执行并覆盖同名日志。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
