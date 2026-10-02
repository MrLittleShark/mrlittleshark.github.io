---
title: "surfaceRedistributePar · 示例采用 4 个进程，并读取 constant/triSurface/body.stl"
layout: reference
description: "示例采用 4 个进程，并读取 constant/triSurface/body.stl。分配方式包括 follow、independent、distributed 和 frozen；follow 按网格包围盒划分。"
cms_slug: "command-surfaceredistributepar"
---

<p>示例采用 4 个进程，并读取 constant/triSurface/body.stl。分配方式包括 follow、independent、distributed 和 frozen；follow 按网格包围盒划分。</p><h2>开始前</h2>
<p>准备已分解的体网格、system/decomposeParDict 和 constant/triSurface/body.stl；MPI 进程数应等于子域数。操作写入分区表面，宜在案例副本内进行。</p>
<h2>示例 1：按两个网格子域分配表面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -parallel
</code></pre>
<p>follow 按各进程网格边界框分配相交三角面。完成后各进程拥有其局部网格需要查询的表面部分。</p>
<h2>示例 2：在四个子域使用同一流程</h2>
<pre><code class="language-bash">mpirun -np 4 surfaceRedistributePar body.stl follow -parallel
</code></pre>
<p>适用于已分为四个子域的案例。比较各进程报告的表面规模，可判断几何在当前网格分区中的负载分布。</p>
<h2>示例 3：保留网格之外的三角面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -keepNonMapped -parallel
</code></pre>
<p>保留没有映射到当前网格边界框的表面三角形。适合后续网格范围还会扩展、需要保留完整几何的工作流程。</p>
<h2>示例 4：按表面独立分配</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl independent -parallel
</code></pre>
<p>独立确定表面的分布，而不是逐步跟随体网格边界框。对照 follow 的各进程三角面数，评估所选分配方式的负载。</p>
<h2>示例 5：重新分配已有分区表面</h2>
<pre><code class="language-bash">mpirun -np 2 surfaceRedistributePar body.stl follow -parallel -case ../redistributedCase
</code></pre>
<p>目标案例需已经完成体网格重新分区。工具可读取已有分区表面，并使其分布跟随新网格，供后续并行几何查询使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-keepNonMapped</code></td><td>Preserve surface outside of mesh bounds</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceRedistributePar [OPTIONS] &lt;triSurfaceMesh&gt; &lt;distributionType&gt;
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
  -keepNonMapped    Preserve surface outside of mesh bounds
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

Redistribute a triSurface. The specified surface must be located in the
constant/triSurface directory

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceRedistributePar/surfaceRedistributePar.C">源码与说明</a> · <a href="/assets/command-help/surfaceredistributepar.txt">帮助文本</a></p>
