---
title: "computeSensitivities · 利用已有原始场与伴随场计算优化目标对设计变量的灵敏度"
layout: reference
description: "利用已有原始场与伴随场计算优化目标对设计变量的灵敏度。"
cms_slug: "command-computesensitivities"
---

<p>利用已有原始场与伴随场计算优化目标对设计变量的灵敏度。</p><h2>开始前</h2>
<p>已有完整optimisationDict、优化管理器、目标函数、设计变量，以及相同状态的原始和伴随解。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算当前设计灵敏度</h2>
<pre><code class="language-bash">computeSensitivities
</code></pre>
<p>读取优化设置，更新目标函数并计算相应设计变量的灵敏度，写出配置的结果场或设计导数。</p>
<h2>示例 2：使用最新收敛状态</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set latestTime
computeSensitivities
</code></pre>
<p>将读取状态设为最新结果；该时刻需有与目标匹配的原始和伴随场。</p>
<h2>示例 3：核对指定设计迭代</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set startTime
foamDictionary system/controlDict -entry startTime -set 20
computeSensitivities
</code></pre>
<p>时间20保存了完整设计状态时，重算该状态的目标和灵敏度，便于对照设计更新记录。</p>
<h2>示例 4：并行计算设计导数</h2>
<pre><code class="language-bash">mpirun -np 4 computeSensitivities -parallel
</code></pre>
<p>已有4分区原始和伴随解，按同一优化定义汇集各分区贡献，输出对应设计导数。</p>
<h2>示例 5：比较另一目标函数</h2>
<pre><code class="language-bash">computeSensitivities -case ./dragObjective
computeSensitivities -case ./pressureLossObjective
</code></pre>
<p>两案例各自已有对应目标的伴随解和配置；分别输出阻力目标与压降目标的灵敏度，比较设计区域的贡献差异。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: computeSensitivities [OPTIONS]
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

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/optimisation/computeSensitivities/computeSensitivities.C">源码与说明</a> · <a href="/assets/command-help/computesensitivities.txt">帮助文本</a></p>
