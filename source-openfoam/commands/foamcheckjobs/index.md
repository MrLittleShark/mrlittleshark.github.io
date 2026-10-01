---
title: "foamCheckJobs  检查作业记录及运行锁状态"
layout: reference
description: "通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。</p><h2>v2512 源码中的用途</h2><p>Uses runningJobs/, finishedJobs/ and foamProcessInfo to create stateFile. stateFile contains per pid information on state of process. Format: pid state command where state is one of &#x27;RUNN&#x27;, &#x27;SUSP&#x27;, &#x27;OTHR&#x27;, &#x27;FINI&#x27;, &#x27;ABRT&#x27; (&#x27;PEND&#x27;) (first three are from foamProcessInfo, others from jobInfo files) (PEND is special state from when user has submitted but no jobInfo file yet. Not supported by this script yet)</p><h2>使用入口</h2><pre><code class="language-bash">foamCheckJobs jobState</code></pre><h2>使用条件与核对</h2><p>通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。 用法：foamCheckJobs [状态输出文件] 示例：foamCheckJobs jobState
Uses runningJobs/, finishedJobs/ and foamProcessInfo to create stateFile. stateFile contains per pid information on state of process. Format: pid state command where state is one of &#x27;RUNN&#x27;, &#x27;SUSP&#x27;, &#x27;OTHR&#x27;, &#x27;FINI&#x27;, &#x27;ABRT&#x27; (&#x27;PEND&#x27;) (first three are from foamProcessInfo, others from jobInfo files) (PEND is special state from when user has submitted but no jobInfo file yet. Not supported by this script yet)
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcheckjobs.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCheckJobs
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCheckJobs

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCheckJobs [stateFile]

This program checks all the locks in the FOAM_JOB_DIR directory to see if
their processes are still running. Processes will not release their
lock if they exit abnormally. This program will try to obtain process
information on the machine the process ran on and release the lock
if the program is no longer running.

Note: all machines have to be reachable using ssh.

The output from checking all running jobs is collected in an optional
file.

FILES:
    \&#36;FOAM_JOB_DIR/runningJobs   locks for running  processes
                  /finishedJobs  locks for finished processes</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCheckJobs">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
