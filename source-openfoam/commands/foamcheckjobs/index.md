---
title: "foamCheckJobs · 通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH"
layout: reference
description: "通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。"
cms_slug: "command-foamcheckjobs"
---

<p>通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。</p><h2>开始前</h2>
<p>依赖传统 FOAM_JOB_DIR 的 runningJobs/finishedJobs 记录。该设施需由安装配置启用，作业主机通过 SSH 可达，且 foamProcessInfo 可用。foamCheckJobs 会检查失效锁并询问是否释放；它不是系统全部进程的查询器。</p>
<h2>示例 1：处理默认作业目录</h2>
<pre><code class="language-bash">foamCheckJobs
</code></pre>
<p>检查默认作业记录，必要时通过本机或 SSH 查询进程状态。</p>
<h2>示例 2：指定状态快照</h2>
<pre><code class="language-bash">foamCheckJobs jobs.state
</code></pre>
<p>将实际进程状态保存到 jobs.state，后续可交给 foamPrintJobs。</p>
<h2>示例 3：结合检查与显示</h2>
<pre><code class="language-bash">foamCheckJobs current-jobs.state
foamPrintJobs current-jobs.state
</code></pre>
<p>先刷新状态再生成表，输出包含用户、算例、机器、PID 和程序。</p>
<h2>示例 4：使用独立作业记录库</h2>
<pre><code class="language-bash">FOAM_JOB_DIR="$HOME/.OpenFOAM/jobControl-projectA" foamCheckJobs projectA.state
</code></pre>
<p>该目录须已有 runningJobs 和 finishedJobs，且实际运行任务在此登记；只处理这一组作业记录。</p>
<h2>示例 5：保留带日期的报告</h2>
<pre><code class="language-bash">snapshot="jobs-$(date +%Y%m%d-%H%M%S).state"
foamCheckJobs "$snapshot"
foamPrintJobs "$snapshot" &gt; "$snapshot.txt"
</code></pre>
<p>保存独立快照或表格，便于比较多个检查时刻；写文件不会发起新的求解。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCheckJobs [stateFile]

This program checks all the locks in the FOAM_JOB_DIR directory to see if
their processes are still running. Processes will not release their
lock if they exit abnormally. This program will try to obtain process
information on the machine the process ran on and release the lock
if the program is no longer running.

Note: all machines have to be reachable using ssh.

The output from checking all running jobs is collected in an optional
file.

FILES:
    \$FOAM_JOB_DIR/runningJobs   locks for running  processes
                  /finishedJobs  locks for finished processes</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCheckJobs">源码与说明</a> · <a href="/assets/command-help/foamcheckjobs.txt">帮助文本</a></p>
