---
title: "patchSummary · 列出各边界patch上的字段边界条件"
layout: reference
description: "列出各边界patch上的字段边界条件。"
cms_slug: "command-patchsummary"
---

<p>列出各边界patch上的字段边界条件。</p><h2>开始前</h2>
<p>已有网格和所选时间的场；适合检查边界名称与各字段的类型是否一致。</p>
<h2>示例 1：查看初始边界条件</h2>
<pre><code class="language-bash">patchSummary -time 0
</code></pre>
<p>读取0时刻字段，汇总各patch采用的边界类型，适合求解前检查。</p>
<h2>示例 2：逐patch展开显示</h2>
<pre><code class="language-bash">patchSummary -time 0 -expand
</code></pre>
<p>关闭相同条件的合并展示，逐个列出patch，便于定位某一小边界。</p>
<h2>示例 3：检查最新重启状态</h2>
<pre><code class="language-bash">patchSummary -latestTime
</code></pre>
<p>查看最新结果场的边界类型，确认重启文件与预期边界设置一致。</p>
<h2>示例 4：比较多个时刻</h2>
<pre><code class="language-bash">patchSummary -time '0,1,2' -expand
</code></pre>
<p>三个时间均存在时，逐时刻列出边界条件，检查中途修改或重启是否改变了字段设置。</p>
<h2>示例 5：检查多区域流体边界</h2>
<pre><code class="language-bash">patchSummary -region fluid -latestTime -expand
</code></pre>
<p>仅查看fluid的最新场，便于把流固界面、入口和壁面条件分开核对。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-expand</code></td><td>展开字典引用和函数条目；#codeStream 等条目可能执行代码。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: patchSummary [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -expand           Do not combine patches
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

Write field and boundary condition info for each patch at each requested time
instance

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/patchSummary/patchSummary.C">源码与说明</a> · <a href="/assets/command-help/patchsummary.txt">帮助文本</a></p>
