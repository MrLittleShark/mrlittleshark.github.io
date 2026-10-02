---
title: "setSet · 交互式或批量创建、修改网格集合"
layout: reference
description: "交互式或批量创建、修改网格集合。"
cms_slug: "command-setset"
---

<p>交互式或批量创建、修改网格集合。</p><h2>开始前</h2>
<p>已有网格；批处理文件逐行使用 cellSet、faceSet 或 pointSet 的动作和选择源。</p>
<h2>示例 1：交互创建盒内单元集</h2>
<pre><code class="language-bash">setSet
# 在 setSet 提示符中输入：
# cellSet core new boxToCell (0 0 0) (1 1 1)
# quit
</code></pre>
<p>进入交互终端后，去掉示例注释符输入两条指令；new 创建 core，boxToCell 按单元中心选择指定盒内单元。</p>
<h2>示例 2：用批处理文件重复选区</h2>
<pre><code class="language-bash">printf 'cellSet core new boxToCell (0 0 0) (1 1 1)\nquit\n' &gt; select.setSet
setSet -batch select.setSet
</code></pre>
<p>把交互指令保存成文本，-batch 读取并执行，便于网格重建后重新生成相同几何选区。</p>
<h2>示例 3：把选区扩大到另一盒体</h2>
<pre><code class="language-bash">printf 'cellSet core new boxToCell (0 0 0) (1 1 1)\ncellSet core add boxToCell (1 0 0) (2 1 1)\nquit\n' &gt; twoBoxes.setSet
setSet -batch twoBoxes.setSet
</code></pre>
<p>第一条创建集合，第二条 add 做并集；最终 core 包含两盒范围内的单元。</p>
<h2>示例 4：只生成集合文件</h2>
<pre><code class="language-bash">setSet -batch select.setSet -noVTK
</code></pre>
<p>批处理已定义所需集合；-noVTK 关闭辅助VTK输出，保留供 topoSet、subsetMesh 等工具使用的集合。</p>
<h2>示例 5：在运动网格的多个状态重选</h2>
<pre><code class="language-bash">setSet -batch select.setSet -loop -time '0.1:0.5'
</code></pre>
<p>-loop 对选中的每个已有时间执行批指令；几何运动时，盒内单元集合会随各时刻位置更新。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-batch &lt;file&gt;</code></td><td>Process in batch mode, using input from specified file</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-loop</code></td><td>Execute batch commands for all timesteps</td></tr><tr><td><code>-noSync</code></td><td>Do not synchronise selection across coupled patches</td></tr><tr><td><code>-noVTK</code></td><td>Do not write VTK files</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setSet [OPTIONS]
Options:
  -batch &lt;file&gt;     Process in batch mode, using input from specified file
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
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
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -loop             Execute batch commands for all timesteps
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noSync           Do not synchronise selection across coupled patches
  -noVTK            Do not write VTK files
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Manipulate a cell/face/point Set or Zone interactively.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/setSet/setSet.C">源码与说明</a> · <a href="/assets/command-help/setset.txt">帮助文本</a></p>
