---
title: "foamTestTutorial · 默认在临时目录运行一个时间步"
layout: reference
description: "默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。"
cms_slug: "command-foamtesttutorial"
---

<p>默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。</p><h2>用法</h2><pre><code class="language-bash">foamTestTutorial -1 incompressible/icoFoam/cavity/cavity</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-1</td><td>Run only one time step (modifies controlDict) [default]</td></tr><tr><td>-full</td><td>Run to completion (does not modify controlDict)</td></tr><tr><td>-force</td><td>Force overwrite of existing output directories</td></tr><tr><td>-debian</td><td>Adjust for running with autopkgtest</td></tr><tr><td>-serial</td><td>Prefer Allrun-serial if available</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-output=DIR</td><td>Output directory (default: a temporary directory)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: foamTestTutorial
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamTestTutorial

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: foamTestTutorial [OPTION] dir [.. dirN]

options:
  -1            Run only one time step (modifies controlDict) [default]
  -full         Run to completion (does not modify controlDict)
  -force        Force overwrite of existing output directories
  -debian       Adjust for running with autopkgtest
  -serial       Prefer Allrun-serial if available
  -parallel     Prefer Allrun-parallel if available
  -output=DIR   Output directory (default: a temporary directory)
  -help         Print the usage

Run foamRunTutorials with specified tutorial directories
Creates/destroys a temporary directory for each test unless
an output directory has been specified.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamTestTutorial">源码与说明</a> · <a href="/assets/command-help/foamtesttutorial.txt">帮助文本</a></p>
