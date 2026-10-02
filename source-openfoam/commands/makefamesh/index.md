---
title: "makeFaMesh · v2512 的常用字典位置为 system/finite-area/faMeshDefiniti"
layout: reference
description: "v2512 的常用字典位置为 system/finite-area/faMeshDefinition。"
cms_slug: "command-makefamesh"
---

<p>v2512 的常用字典位置为 system/finite-area/faMeshDefinition。</p><h2>开始前</h2>
<p>已有体网格及与其patch匹配的faMeshDefinition；命名面积区域还需对应区域配置。</p>
<h2>示例 1：先构造但不保存</h2>
<pre><code class="language-bash">makeFaMesh -dry-run
</code></pre>
<p>读取定义并尝试构造面积网格，先检查边界选择和连接关系，暂不写网格。</p>
<h2>示例 2：生成默认面积网格</h2>
<pre><code class="language-bash">makeFaMesh
</code></pre>
<p>从定义选定的体网格边界面创建有限面积网格，供液膜或壳体模型使用。</p>
<h2>示例 3：使用另一份定义</h2>
<pre><code class="language-bash">makeFaMesh -dict system/faMeshDefinition.test
</code></pre>
<p>已准备该完整定义时选择它，适合对照不同patch组合；字典路径由-dict明确指定。</p>
<h2>示例 4：生成命名区域并输出图形</h2>
<pre><code class="language-bash">makeFaMesh -area-region film -write-vtk -write-edges-obj
</code></pre>
<p>生成film面积网格，同时导出面与边的可视化数据，检查薄膜边界是否闭合。</p>
<h2>示例 5：在分区网格上生成</h2>
<pre><code class="language-bash">mpirun -np 4 makeFaMesh -parallel -area-region film -no-fields
</code></pre>
<p>4个体网格分区已经存在；生成面积网格及分区寻址，-no-fields暂不分解面积场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>Use all regions in finite-area regionProperties Specify area-mesh region. Eg, -area-region shell Use specified area region. Eg, -area-regions film Or from regionProperties.  Eg, -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Create but do not write Specify name for a default empty patch Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-no-decompose</code></td><td>Suppress procAddressing creation and field decomposition (parallel)</td></tr><tr><td><code>-no-fields</code></td><td>Suppress field decomposition (parallel)</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-write-edges-obj</code></td><td>Write mesh edges as obj files (one per processor)</td></tr><tr><td><code>-write-vtk</code></td><td>输出块拓扑的 VTK 文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: makeFaMesh [OPTIONS]
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
  -dict &lt;file&gt;      Alternative faMeshDefinition
  -dry-run          Create but do not write
  -empty-patch &lt;name&gt;
                    Specify name for a default empty patch
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
  -no-decompose     Suppress procAddressing creation and field decomposition
                    (parallel)
  -no-fields        Suppress field decomposition (parallel)
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
  -write-edges-obj  Write mesh edges as obj files (one per processor)
  -write-vtk        Write mesh as a vtp (vtk) file for display or debugging
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

A mesh generator for finiteArea mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/finiteArea/makeFaMesh/makeFaMesh.C">源码与说明</a> · <a href="/assets/command-help/makefamesh.txt">帮助文本</a></p>
