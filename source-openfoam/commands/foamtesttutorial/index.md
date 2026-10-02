---
title: "foamTestTutorial · 默认在临时目录运行一个时间步"
layout: reference
description: "默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。"
cms_slug: "command-foamtesttutorial"
---

<p>默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。</p><h2>开始前</h2>
<p>加载 v2512 环境。输入使用相对于 $FOAM_TUTORIALS 的教程路径，例如 incompressible/icoFoam/cavity/cavity。指定 -output 时须先建立该目录。工具将教程复制到独立目录后测试。</p>
<h2>示例 1：运行一步检查</h2>
<pre><code class="language-bash">foamTestTutorial incompressible/icoFoam/cavity/cavity
</code></pre>
<p>默认修改测试副本，仅运行一个时间步；结束后清理临时副本。</p>
<h2>示例 2：保留测试副本</h2>
<pre><code class="language-bash">mkdir -p tests-one-step
foamTestTutorial -output=tests-one-step incompressible/icoFoam/cavity/cavity
</code></pre>
<p>输出目录内按教程路径生成子目录，日志与结果保留。</p>
<h2>示例 3：完成整个算例</h2>
<pre><code class="language-bash">mkdir -p tests-full
foamTestTutorial -full -output=tests-full incompressible/icoFoam/cavity/cavity
</code></pre>
<p>-full 保留原 controlDict 的运行区间。</p>
<h2>示例 4：测试两个不同几何</h2>
<pre><code class="language-bash">mkdir -p tests-batch
foamTestTutorial -output=tests-batch incompressible/icoFoam/cavity/cavity incompressible/icoFoam/elbow
</code></pre>
<p>按列表分别测试方腔与弯管；elbow 的 Allrun 会从官方资源目录读取网格输入。</p>
<h2>示例 5：优先串行脚本</h2>
<pre><code class="language-bash">mkdir -p tests-serial
foamTestTutorial -serial -full -output=tests-serial incompressible/icoFoam/cavity/cavity
</code></pre>
<p>优先使用 Allrun-serial；不存在时回退到教程默认流程。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-1</code></td><td>Run only one time step (modifies controlDict) [default]</td></tr><tr><td><code>-full</code></td><td>Run to completion (does not modify controlDict)</td></tr><tr><td><code>-force</code></td><td>Force overwrite of existing output directories</td></tr><tr><td><code>-debian</code></td><td>Adjust for running with autopkgtest</td></tr><tr><td><code>-serial</code></td><td>Prefer Allrun-serial if available</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-output=DIR</code></td><td>Output directory (default: a temporary directory)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
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
