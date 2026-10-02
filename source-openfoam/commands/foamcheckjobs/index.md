---
title: "foamCheckJobs · 通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH"
layout: reference
description: "通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。"
cms_slug: "command-foamcheckjobs"
---

<p>通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。</p><h2>用法</h2><pre><code class="language-bash">foamCheckJobs jobState</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCheckJobs [stateFile]

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
