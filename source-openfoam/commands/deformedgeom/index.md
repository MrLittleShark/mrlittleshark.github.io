---
title: "deformedGeom · 用名为 U 的单元位移场生成变形网格"
layout: reference
description: "用名为 U 的单元位移场生成变形网格。"
cms_slug: "command-deformedgeom"
---

<p>用名为 U 的单元位移场生成变形网格。</p><h2>开始前</h2>
<p>时间目录中已有 volVectorField U，其物理意义为位移；程序将它插值到顶点，再乘位置参数 factor。各例使用同一未变形网格的独立副本。</p>
<h2>示例 1：显示实际位移</h2>
<pre><code class="language-bash">deformedGeom 1
</code></pre>
<p>系数 1 采用原位移幅值。程序遍历结果时间，在存在 U 的时刻写出变形网格，适合结构位移结果的几何显示。</p>
<h2>示例 2：放大微小变形</h2>
<pre><code class="language-bash">deformedGeom 20
</code></pre>
<p>顶点位移乘 20，便于观察很小的挠曲。所得几何用于放大显示，空间尺寸中的变形量已改变。</p>
<h2>示例 3：缩小显示幅度</h2>
<pre><code class="language-bash">deformedGeom 0.2
</code></pre>
<p>将位移缩到原来的五分之一；对大位移数据可先检查整体变形趋势，输出仍覆盖该副本的结果网格。</p>
<h2>示例 4：比较正反方向</h2>
<pre><code class="language-bash">deformedGeom -case ./reverseView -1
</code></pre>
<p>reverseView 中保存原网格与位移结果；负系数把每个顶点沿相反位移方向移动，适合检查位移符号约定。</p>
<h2>示例 5：检查放大后的网格质量</h2>
<pre><code class="language-bash">deformedGeom 5
checkMesh -latestTime
</code></pre>
<p>先生成五倍位移几何，再检查最后时刻的体积和质量指标；局部负体积能指出放大后发生穿越的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: deformedGeom [OPTIONS] &lt;factor&gt;
Arguments:
  &lt;factor&gt;          The deformation scaling factor
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

Deforms a polyMesh using a displacement field U and a scaling factor supplied
as an argument

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/deformedGeom/deformedGeom.C">源码与说明</a> · <a href="/assets/command-help/deformedgeom.txt">帮助文本</a></p>
