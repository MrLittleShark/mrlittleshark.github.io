---
title: "subsetMesh · 按 cellSet 或 cellZone 提取子网格并映射场"
layout: reference
description: "按 cellSet 或 cellZone 提取子网格并映射场。"
cms_slug: "command-subsetmesh"
---

<p>按 cellSet 或 cellZone 提取子网格并映射场。</p><h2>开始前</h2>
<p>已有目标cellSet/cellZone；切割后暴露的内部面需要合适的边界patch。</p>
<h2>示例 1：按单元集合提取</h2>
<pre><code class="language-bash">subsetMesh coreCells
</code></pre>
<p>保留 coreCells 中的单元，新增切割面默认进入 oldInternalFaces，并写新网格时间。</p>
<h2>示例 2：指定切割边界名称</h2>
<pre><code class="language-bash">subsetMesh coreCells -patch cutBoundary -overwrite
</code></pre>
<p>cutBoundary 是已准备的目标patch；暴露内部面归入此边界，结果写回当前网格。</p>
<h2>示例 3：按cellZone提取</h2>
<pre><code class="language-bash">subsetMesh -zone rotor -resultTime 2
</code></pre>
<p>把 rotor 解释为cellZone名称，并将子网格写到时间2，便于和原网格分开查看。</p>
<h2>示例 4：合并选择多个zone</h2>
<pre><code class="language-bash">subsetMesh -zone '(fluid "channel.*")' -resultTime 3
</code></pre>
<p>选择 fluid 及匹配 channel.* 的zone，保留它们包含的单元，用于提取相关连通部件。</p>
<h2>示例 5：把切割面分配给最近边界</h2>
<pre><code class="language-bash">subsetMesh coreCells -patches '(inlet outlet walls)' -exclude-patches outlet -overwrite
</code></pre>
<p>已有这些patch时，在候选边界中按最近位置分配暴露面，并排除outlet，减少手工整理切割面的工作。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-patch &lt;name&gt;</code></td><td>Add exposed internal faces to specified patch instead of &quot;oldInternalFaces&quot; Add exposed internal faces to closest of specified patches instead of &quot;oldInternalFaces&quot;</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-zone</code></td><td>Subset with cellZone(s) instead of cellSet. The command argument may be a list of words or regexs</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBody/floatingBody">multiphase/overInterDyMFoam/floatingBody/floatingBody</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody">multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: subsetMesh [OPTIONS] &lt;cell-selection&gt;
Arguments:
  &lt;cell-selection&gt;  The cellSet name, but with the -zone option this is
                    interpreted to be a cellZone selection by name(s) or regex.
                    Eg &#x27;mixer&#x27; or &#x27;( mixer &quot;moving.*&quot; )&#x27;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches from the -patches
                    selection
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -patch &lt;name&gt;     Add exposed internal faces to specified patch instead of
                    &quot;oldInternalFaces&quot;
  -patches &lt;wordRes&gt;
                    Add exposed internal faces to closest of specified patches
                    instead of &quot;oldInternalFaces&quot;
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -resultTime &lt;time&gt;
                    Specify a time for the resulting mesh
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -zone             Subset with cellZone(s) instead of cellSet. The command
                    argument may be a list of words or regexs
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create a mesh subset for a particular region of interest based on a cellSet or
cellZone(s) specified as the first command argument.
See setSet/topoSet utilities on how to select cells based on various shapes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/subsetMesh/subsetMesh.C">源码与说明</a> · <a href="/assets/command-help/subsetmesh.txt">帮助文本</a></p>
