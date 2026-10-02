---
title: "checkFaMesh · 检查对象为有限面积网格"
layout: reference
description: "检查对象为有限面积网格。"
cms_slug: "command-checkfamesh"
---

<p>检查对象为有限面积网格。</p><h2>开始前</h2>
<p>已由 makeFaMesh 建立有限面积网格。area-region 指面积网格区域，region 指其所属体网格区域。</p>
<h2>示例 1：检查默认面积网格</h2>
<pre><code class="language-bash">checkFaMesh
</code></pre>
<p>读取默认有限面积网格，报告面、边及几何检查结果。</p>
<h2>示例 2：输出可视化网格</h2>
<pre><code class="language-bash">checkFaMesh -write-vtk
</code></pre>
<p>在检查时写出VTP网格，可在ParaView定位异常边或面。</p>
<h2>示例 3：检查指定薄膜区域</h2>
<pre><code class="language-bash">checkFaMesh -area-region film
</code></pre>
<p>已有名为film的面积网格时，仅检查它，便于排查多个面积区域中的问题。</p>
<h2>示例 4：检查所有面积区域</h2>
<pre><code class="language-bash">checkFaMesh -allAreas -write-vtk
</code></pre>
<p>按有限面积regionProperties逐个检查，并输出各区域可视化文件。</p>
<h2>示例 5：检查已分区网格</h2>
<pre><code class="language-bash">mpirun -np 4 checkFaMesh -parallel -area-region film
</code></pre>
<p>前提是4个分区中已有匹配的面积网格；检查并行分区及耦合边连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>Use all regions in finite-area regionProperties Specify area-mesh region. Eg, -area-region shell Use specified area region. Eg, -area-regions film Or from regionProperties.  Eg, -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-write-vtk</code></td><td>输出块拓扑的 VTK 文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: checkFaMesh [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -geometryOrder &lt;N&gt;
                    Test different geometry order - experimental!!
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
  -write-vtk        Write mesh as a vtp (vtk) file for display or debugging
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Check a finite-area mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/checkFaMesh/checkFaMesh.C">源码与说明</a> · <a href="/assets/command-help/checkfamesh.txt">帮助文本</a></p>
