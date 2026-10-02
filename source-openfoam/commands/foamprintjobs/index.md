---
title: "foamPrintJobs · 与 foamCheckJobs 配合使用"
layout: reference
description: "与 foamCheckJobs 配合使用。"
cms_slug: "command-foamprintjobs"
---

<p>与 foamCheckJobs 配合使用。</p><h2>开始前</h2>
<p>依赖传统 FOAM_JOB_DIR 的 runningJobs/finishedJobs 记录。该设施需由安装配置启用，作业主机通过 SSH 可达，且 foamProcessInfo 可用。foamCheckJobs 会检查失效锁并询问是否释放；它不是系统全部进程的查询器。</p>
<h2>示例 1：处理默认作业目录</h2>
<pre><code class="language-bash">foamPrintJobs
</code></pre>
<p>打印默认目录的 Running/Finished 表及已有状态文件信息。</p>
<h2>示例 2：指定状态快照</h2>
<pre><code class="language-bash">foamPrintJobs jobs.state
</code></pre>
<p>读取 jobs.state，把进程状态合并到作业表中。</p>
<h2>示例 3：结合检查与显示</h2>
<pre><code class="language-bash">foamCheckJobs current-jobs.state
foamPrintJobs current-jobs.state
</code></pre>
<p>先刷新状态再生成表，输出包含用户、算例、机器、PID 和程序。</p>
<h2>示例 4：使用独立作业记录库</h2>
<pre><code class="language-bash">FOAM_JOB_DIR="$HOME/.OpenFOAM/jobControl-projectA" foamPrintJobs projectA.state
</code></pre>
<p>该目录须已有 runningJobs 和 finishedJobs，且实际运行任务在此登记；只处理这一组作业记录。</p>
<h2>示例 5：保留带日期的报告</h2>
<pre><code class="language-bash">foamPrintJobs jobs.state &gt; "jobs-table-$(date +%Y%m%d-%H%M%S).txt"
</code></pre>
<p>保存独立快照或表格，便于比较多个检查时刻；写文件不会发起新的求解。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamPrintJobs">源码与说明</a> · <a href="/assets/command-help/foamprintjobs.txt">帮助文本</a></p>
