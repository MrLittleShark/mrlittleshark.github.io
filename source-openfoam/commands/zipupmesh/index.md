---
title: "zipUpMesh · 补齐含悬挂顶点的面连接，使多面体单元表面闭合"
layout: reference
description: "补齐含悬挂顶点的面连接，使多面体单元表面闭合。"
cms_slug: "command-zipupmesh"
---

<p>补齐含悬挂顶点的面连接，使多面体单元表面闭合。</p><h2>开始前</h2>
<p>输入网格的几何形状有效，但部分面边连接存在悬挂顶点；程序会更新网格拓扑。</p>
<h2>示例 1：修补悬挂顶点连接</h2>
<pre><code class="language-bash">zipUpMesh
</code></pre>
<p>读取网格并补齐单元面之间的边点连接，输出修补后的网格和处理统计。</p>
<h2>示例 2：修补后检查拓扑</h2>
<pre><code class="language-bash">zipUpMesh
checkMesh -allTopology
</code></pre>
<p>重点检查面连接和单元闭合，观察修补后原先的拓扑问题是否消失。</p>
<h2>示例 3：单独处理指定区域</h2>
<pre><code class="language-bash">zipUpMesh -region fluid
checkMesh -region fluid -allTopology
</code></pre>
<p>多区域案例只修补fluid，便于把问题定位到某个区域而保留其他区域的拓扑。</p>
<h2>示例 4：在独立副本上比较修补结果</h2>
<pre><code class="language-bash">cp -r importedMesh importedMesh-zipped
zipUpMesh -case importedMesh-zipped
checkMesh -case importedMesh-zipped
</code></pre>
<p>保留导入原网格，在副本中修补，再比较两份网格的连接与质量报告。</p>
<h2>示例 5：导出修补后的几何</h2>
<pre><code class="language-bash">zipUpMesh
foamToVTK -no-fields -name VTK-zipped
</code></pre>
<p>修补后仅转换网格几何，在ParaView中检查原先悬挂顶点附近的面是否闭合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: zipUpMesh [OPTIONS]
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

Reads in a mesh with hanging vertices and &#x27;zips&#x27; up the cells to guarantee that
all polyhedral cells of valid shape are closed.
Meshes with hanging vertices may occur as a result of split hex mesh conversion
or integration or coupled math face pairs.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/zipUpMesh/zipUpMesh.C">源码与说明</a> · <a href="/assets/command-help/zipupmesh.txt">帮助文本</a></p>
