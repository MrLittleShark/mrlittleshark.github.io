---
title: "moveEngineMesh · 按发动机曲轴转角设置推进发动机网格运动"
layout: reference
description: "按发动机曲轴转角设置推进发动机网格运动。"
cms_slug: "command-moveenginemesh"
---

<p>按发动机曲轴转角设置推进发动机网格运动。</p><h2>开始前</h2>
<p>已有 engineGeometry、发动机网格运动配置和初始网格；controlDict 的时间设置与 engineTime 的转角约定匹配。</p>
<h2>示例 1：检查完整活塞运动</h2>
<pre><code class="language-bash">moveEngineMesh
</code></pre>
<p>程序按发动机时间循环更新网格，日志以 CA-deg 显示曲轴转角，结果时间保存运动几何。</p>
<h2>示例 2：只检查起始转角段</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 10
moveEngineMesh
</code></pre>
<p>在以曲轴转角为用户时间、起始角小于10的案例中，将终止角设为10度，集中观察这一段活塞运动。</p>
<h2>示例 3：减小转角步长</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry deltaT -set 0.25
moveEngineMesh
</code></pre>
<p>本案例时间步以曲轴角计时；0.25度提供更密的运动状态，可比较单步变形与质量变化。</p>
<h2>示例 4：比较另一发动机几何</h2>
<pre><code class="language-bash">moveEngineMesh -case ./engine-longStroke
</code></pre>
<p>engine-longStroke 已有独立的行程和运动参数；生成该几何的运动序列，和基准案例比较活塞位置。</p>
<h2>示例 5：检查运动末态网格</h2>
<pre><code class="language-bash">moveEngineMesh
checkMesh -latestTime
</code></pre>
<p>先完成运动，再检查最后保存状态的体积和质量，适合检查接近上止点的狭小空间。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: moveEngineMesh [OPTIONS]
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

A solver utility for moving meshes for engine calculations

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveEngineMesh/moveEngineMesh.C">源码与说明</a> · <a href="/assets/command-help/moveenginemesh.txt">帮助文本</a></p>
