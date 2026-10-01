---
title: "foamSolverSweeps  统计求解迭代次数及耗时"
layout: reference
description: "启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。</p><h2>使用入口</h2><pre><code class="language-bash">foamSolverSweeps</code></pre><h2>使用条件与核对</h2><p>启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。 用法：foamSolverSweeps 随后输入日志文件名 示例：foamSolverSweeps

本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamsolversweeps.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
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

echo &quot;timeFile=&#36;timeFile&quot;
echo &quot;runTimeFile=&#36;runTimeFile&quot;
echo &quot;piterFile=&#36;piterFile&quot;
echo &quot;uiterFile=&#36;uiterFile&quot;
echo &quot;&quot;


# sumFile &lt;file&gt;
#
# prints sum of all numbers in file
sumFile () {
  sum=0
  for num in `cat &#36;1`
  do
    sum=`expr &#36;sum + &#36;num`
  done
  echo &#36;sum
}



# Main
#~~~~~~

echo &quot;Name of log file (LOG) : \c&quot;
read logFile
logFile=&#36;{logFile:-LOG}


foamProgram=`grep &#x27;&lt; .* &gt;&#x27; &#36;{logFile} | awk &#x27;{print &#36;2}&#x27;`
echo &quot;&quot;
echo &quot;Program: &#36;{foamProgram}&quot;


grep &#x27;ExecutionTime =&#x27; &#36;{logFile} &gt; &#36;{runTimeFile}
echo &quot;&quot;
echo &quot;Runtime:&quot;
echo &quot;  1st iter  : &quot;`head -1 &#36;{runTimeFile}`
echo &quot;  overall   : &quot;`tail -1 &#36;{runTimeFile}`

grep &#x27;^Time =&#x27; &#36;{logFile} &gt; &#36;{timeFile}
echo &quot;&quot;
echo &quot;Simulation:&quot;
echo &quot;  steps: &quot;`wc -l &#36;{timeFile} | awk &#x27;{print &#36;1}&#x27;`
echo &quot;  from : &quot;`head -1 &#36;{timeFile}`
echo &quot;  to   : &quot;`tail -1 &#36;{timeFile}`
echo &quot;&quot;

grep &#x27;Solving for p,&#x27; &#36;{logFile} | awk &#x27;{print &#36;15}&#x27; &gt; &#36;{piterFile}
grep &#x27;Solving for U&#x27; &#36;{logFile} | awk &#x27;{print &#36;15}&#x27; &gt; &#36;{uiterFile}


echo &quot;Solver sweeps:&quot;
echo &quot;  p           : &quot;`sumFile &#36;{piterFile}`
echo &quot;  U(U0,U1,U2) : &quot;`sumFile &#36;{uiterFile}`
echo &quot;&quot;


rm &#36;{timeFile}
rm &#36;{runTimeFile}
rm &#36;{piterFile}
rm &#36;{uiterFile}

#------------------------------------------------------------------------------</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSolverSweeps">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
