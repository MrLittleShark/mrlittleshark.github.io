---
title: "faceAgglomerate · 把边界细面聚合为粗面并写映射"
layout: reference
description: "把边界细面聚合为粗面并写映射。"
cms_slug: "command-faceagglomerate"
---

<p>把边界细面聚合为粗面并写映射。</p><h2>开始前</h2>
<p>已有边界网格和constant/viewFactorsDict，其中包含聚合参数与writeFacesAgglomeration。</p>
<h2>示例 1：生成细面到粗面映射</h2>
<pre><code class="language-bash">faceAgglomerate
</code></pre>
<p>读取默认viewFactorsDict，按pairPatchAgglomeration执行聚合，并写finalAgglom供视角因子计算使用。</p>
<h2>示例 2：写出可视化分组场</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry writeFacesAgglomeration -set true
faceAgglomerate
</code></pre>
<p>启用聚合可视化场，便于在ParaView中检查哪些细面归入同一粗面。</p>
<h2>示例 3：比较另一聚合设置</h2>
<pre><code class="language-bash">faceAgglomerate -dict constant/viewFactors-coarseDict
</code></pre>
<p>替代字典采用不同粗化参数；在副本中比较粗面数量与后续视角因子计算成本。</p>
<h2>示例 4：仅聚合指定区域</h2>
<pre><code class="language-bash">faceAgglomerate -region enclosure
</code></pre>
<p>只为enclosure区域生成映射，适合多区域辐射计算的几何预处理。</p>
<h2>示例 5：聚合后计算视角因子</h2>
<pre><code class="language-bash">faceAgglomerate
viewFactorsGen
</code></pre>
<p>使用viewFactorsGen流程的案例先创建finalAgglom，再计算粗面之间的辐射交换关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: faceAgglomerate [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative viewFactorsDict
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Agglomerate boundary faces using the pairPatchAgglomeration algorithm. Writes a
map of fine to coarse grid.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/faceAgglomerate/faceAgglomerate.C">源码与说明</a> · <a href="/assets/command-help/faceagglomerate.txt">帮助文本</a></p>
