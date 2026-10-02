---
title: "topoSet · 按几何、网格属性和集合关系创建或修改 sets/zones"
layout: reference
description: "按几何、网格属性和集合关系创建或修改 sets/zones。"
cms_slug: "command-toposet"
---

<p>按几何、网格属性和集合关系创建或修改 sets/zones。</p><h2>开始前</h2>
<p>已有网格和 system/topoSetDict，actions 列表定义名称、类型、操作及选择源。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：执行标准选区字典</h2>
<pre><code class="language-bash">topoSet
</code></pre>
<p>按actions顺序建立集合或zone；日志列出各动作与选中数量，可据此核对几何选区。</p>
<h2>示例 2：使用另一选区方案</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-wakeDict
</code></pre>
<p>读取尾流选区专用字典，便于在同一网格上分别准备细化区、采样区和体积源区。</p>
<h2>示例 3：选最后时刻的运动网格</h2>
<pre><code class="language-bash">topoSet -latestTime -dict system/topoSet-probeDict
</code></pre>
<p>按最新顶点位置和拓扑重新执行几何选择，输出对应时刻的集合。</p>
<h2>示例 4：在时间区间内反复选区</h2>
<pre><code class="language-bash">topoSet -time '0.1:0.5' -dict system/topoSet-windowDict
</code></pre>
<p>对区间内已有时刻重复盒体或表面选择，适合跟踪固定空间窗口内的网格单元。</p>
<h2>示例 5：分区案例中建立区域集合</h2>
<pre><code class="language-bash">mpirun -np 4 topoSet -parallel -region fluid -dict system/topoSet-fluidDict
</code></pre>
<p>已有4分区fluid网格；每个进程执行选择并同步耦合边界信息，生成分区一致的集合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noSync</code></td><td>Do not synchronise selection across coupled patches</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-toposetdict/">topoSetDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: topoSet [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative topoSetDict
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
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noSync           Do not synchronise selection across coupled patches
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

Operates on cellSets/faceSets/pointSets through a dictionary, normally
system/topoSetDict

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/topoSet/topoSet.C">源码与说明</a> · <a href="/assets/command-help/toposet.txt">帮助文本</a></p>
