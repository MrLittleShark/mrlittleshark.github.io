---
title: "foamSolverSweeps · 启动后交互输入日志名，如 log.simpleFoam"
layout: reference
description: "启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。"
cms_slug: "command-foamsolversweeps"
---

<p>启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。</p><h2>用法</h2><pre><code class="language-bash">foamSolverSweeps</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: foamSolverSweeps
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSolverSweeps

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

#!/bin/sh
#------------------------------------------------------------------------------
# =========                 |
# \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
#  \\    /   O peration     |
#   \\  /    A nd           | www.openfoam.com
#    \\/     M anipulation  |
#-------------------------------------------------------------------------------
#     Copyright (C) 2011 OpenFOAM Foundation
#------------------------------------------------------------------------------
# License
#     This file is part of OpenFOAM, distributed under GPL-3.0-or-later.
#
# Script
#     foamSolverSweeps
#
# Description
#
#------------------------------------------------------------------------------

#-- settings
timeFile=/tmp/FOAM_iters.time
runTimeFile=/tmp/FOAM_iters.rtime
piterFile=/tmp/FOAM_iters.piters
uiterFile=/tmp/FOAM_iters.uiters

echo &quot;timeFile=$timeFile&quot;
echo &quot;runTimeFile=$runTimeFile&quot;
echo &quot;piterFile=$piterFile&quot;
echo &quot;uiterFile=$uiterFile&quot;
echo &quot;&quot;


# sumFile &lt;file&gt;
#
# prints sum of all numbers in file
sumFile () {
  sum=0
  for num in `cat $1`
  do
    sum=`expr $sum + $num`
  done
  echo $sum
}


# Main
#~~~~~~

echo &quot;Name of log file (LOG) : \c&quot;
read logFile
logFile=${logFile:-LOG}


foamProgram=`grep &#x27;&lt; .* &gt;&#x27; ${logFile} | awk &#x27;{print $2}&#x27;`
echo &quot;&quot;
echo &quot;Program: ${foamProgram}&quot;


grep &#x27;ExecutionTime =&#x27; ${logFile} &gt; ${runTimeFile}
echo &quot;&quot;
echo &quot;Runtime:&quot;
echo &quot;  1st iter  : &quot;`head -1 ${runTimeFile}`
echo &quot;  overall   : &quot;`tail -1 ${runTimeFile}`

grep &#x27;^Time =&#x27; ${logFile} &gt; ${timeFile}
echo &quot;&quot;
echo &quot;Simulation:&quot;
echo &quot;  steps: &quot;`wc -l ${timeFile} | awk &#x27;{print $1}&#x27;`
echo &quot;  from : &quot;`head -1 ${timeFile}`
echo &quot;  to   : &quot;`tail -1 ${timeFile}`
echo &quot;&quot;

grep &#x27;Solving for p,&#x27; ${logFile} | awk &#x27;{print $15}&#x27; &gt; ${piterFile}
grep &#x27;Solving for U&#x27; ${logFile} | awk &#x27;{print $15}&#x27; &gt; ${uiterFile}


echo &quot;Solver sweeps:&quot;
echo &quot;  p           : &quot;`sumFile ${piterFile}`
echo &quot;  U(U0,U1,U2) : &quot;`sumFile ${uiterFile}`
echo &quot;&quot;


rm ${timeFile}
rm ${runTimeFile}
rm ${piterFile}
rm ${uiterFile}

#------------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSolverSweeps">源码与说明</a> · <a href="/assets/command-help/foamsolversweeps.txt">帮助文本</a></p>
