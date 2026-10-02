---
title: "engineCompRatio · 用发动机运动网格的最大、最小体积计算几何压缩比"
layout: reference
description: "用发动机运动网格的最大、最小体积计算几何压缩比。"
cms_slug: "command-enginecompratio"
---

<p>用发动机运动网格的最大、最小体积计算几何压缩比。</p><h2>开始前</h2>
<p>已有发动机网格、engineGeometry和对应engineMesh模型；工具会把网格移动到下止点与上止点位置计算体积。</p>
<h2>示例 1：计算几何压缩比</h2>
<pre><code class="language-bash">engineCompRatio
</code></pre>
<p>日志输出Vmax、Vmin和Vmax/Vmin，可直接核对案例几何压缩比。</p>
<h2>示例 2：比较较大余隙</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry clearance -set '[0 1 0 0 0 0 0] 0.002'
engineCompRatio
</code></pre>
<p>在与该余隙一致的发动机几何副本中设置2毫米clearance，再计算上止点体积和压缩比。</p>
<h2>示例 3：比较另一活塞行程</h2>
<pre><code class="language-bash">engineCompRatio -case ./engine-longStroke
</code></pre>
<p>该副本的初始网格和stroke参数已成套更新；比较行程变化后的扫气体积与压缩比。</p>
<h2>示例 4：网格重建后重新核查</h2>
<pre><code class="language-bash">blockMesh -case ./engine-refined
engineCompRatio -case ./engine-refined
</code></pre>
<p>engine-refined已配置相同物理几何的细网格；比较数值体积得到的压缩比随分辨率的变化。</p>
<h2>示例 5：运动预演与压缩比配套检查</h2>
<pre><code class="language-bash">moveEngineMesh -case ./engine-preview
engineCompRatio -case ./engine-reference
</code></pre>
<p>两个独立案例使用相同初始几何；前者查看运动全过程，后者由原始参考网格计算止点体积，便于核对活塞运动模型。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: engineCompRatio [OPTIONS]
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

Calculate the engine geometric compression ratio

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/engineCompRatio/engineCompRatio.C">源码与说明</a> · <a href="/assets/command-help/enginecompratio.txt">帮助文本</a></p>
