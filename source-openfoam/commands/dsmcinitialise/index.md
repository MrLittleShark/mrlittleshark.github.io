---
title: "dsmcInitialise · 按数密度、温度和平均速度初始化 DSMC 模拟粒子"
layout: reference
description: "按数密度、温度和平均速度初始化 DSMC 模拟粒子。"
cms_slug: "command-dsmcinitialise"
---

<p>按数密度、温度和平均速度初始化 DSMC 模拟粒子。</p><h2>开始前</h2>
<p>已有网格、system/dsmcInitialiseDict、constant/dsmcProperties；物种名称与属性一致，粒子权重已设置。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：生成初始DSMC云</h2>
<pre><code class="language-bash">dsmcInitialise
</code></pre>
<p>读取numberDensities、temperature、velocity，生成dsmc云并写初始粒子数据，日志报告模拟粒子数量。</p>
<h2>示例 2：初始化更高温气体</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry temperature -set 600
dsmcInitialise
</code></pre>
<p>在初始案例副本中改为600K；随机热运动速度分布随温度改变，平均速度仍取velocity。</p>
<h2>示例 3：加入定向平均流</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry velocity -set '(500 0 0)'
dsmcInitialise
</code></pre>
<p>平均速度设为沿x方向500米每秒，在此基础上叠加热运动；输出粒子用于研究有来流的稀薄气体。</p>
<h2>示例 4：比较不同数密度</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry numberDensities/N2 -set 1e20
dsmcInitialise
</code></pre>
<p>字典已有N2物种时增改其数密度；固定体积与粒子权重下，模拟粒子数量随数密度变化。</p>
<h2>示例 5：直接在分区网格中初始化</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 dsmcInitialise -parallel
</code></pre>
<p>已有4分区设置；各进程生成本地粒子，日志汇总全域数量，供随后并行dsmcFoam读取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: dsmcInitialise [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Initialise a case for dsmcFoam from the system/dsmcInitialise dictionary

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/dsmcInitialise/dsmcInitialise.C">源码与说明</a> · <a href="/assets/command-help/dsmcinitialise.txt">帮助文本</a></p>
