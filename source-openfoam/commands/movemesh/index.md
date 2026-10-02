---
title: "moveMesh · 用 motionSolver 推进网格运动"
layout: reference
description: "用 motionSolver 推进网格运动。"
cms_slug: "command-movemesh"
---

<p>用 motionSolver 推进网格运动。</p><h2>开始前</h2>
<p>已有 motionSolver 所需字典和运动场；controlDict 给出基础时间设置。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：按案例设置运动</h2>
<pre><code class="language-bash">moveMesh
</code></pre>
<p>读取运动求解器，逐步计算顶点位置并写结果，适合独立检查给定位移或速度边界。</p>
<h2>示例 2：快速检查短时间运动</h2>
<pre><code class="language-bash">moveMesh -endTime 0.02
</code></pre>
<p>-endTime 临时覆盖终止时间，在已知起始时间小于0.02的案例中只预演初始阶段。</p>
<h2>示例 3：采用更细时间步</h2>
<pre><code class="language-bash">moveMesh -deltaT 0.001 -endTime 0.1
</code></pre>
<p>每步0.001秒，运行至0.1秒；更密的几何状态便于观察运动边界与内部网格响应。</p>
<h2>示例 4：比较较大的运动步长</h2>
<pre><code class="language-bash">moveMesh -case ./motion-coarseStep -deltaT 0.01 -endTime 0.1
</code></pre>
<p>在同一初态的独立副本上把时间步增大到0.01，比较最终顶点位置和中间网格质量。</p>
<h2>示例 5：并行推进运动</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 moveMesh -parallel -deltaT 0.001 -endTime 0.1
</code></pre>
<p>已有4分区设置，运动求解在各分区执行并交换边界数据，输出 processor 目录下的运动网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-deltaT &lt;time&gt;</code></td><td>Override deltaT (eg, for accelerated motion)</td></tr><tr><td><code>-endTime &lt;time&gt;</code></td><td>Override endTime (eg, for shorter tests) Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: moveMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -deltaT &lt;time&gt;    Override deltaT (eg, for accelerated motion)
  -endTime &lt;time&gt;   Override endTime (eg, for shorter tests)
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

A solver utility for moving meshes

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveMesh/moveMesh.C">源码与说明</a> · <a href="/assets/command-help/movemesh.txt">帮助文本</a></p>
