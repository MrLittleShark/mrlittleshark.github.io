---
title: "mergeOrSplitBaffles · 检测共用顶点的挡板面，并合并或拆分它们"
layout: reference
description: "检测共用顶点的挡板面，并合并或拆分它们。"
cms_slug: "command-mergeorsplitbaffles"
---

<p>检测共用顶点的挡板面，并合并或拆分它们。</p><h2>开始前</h2>
<p>当前网格存在重合挡板面；拆分用于两侧独立拓扑，合并用于恢复内部面。</p>
<h2>示例 1：只查找挡板</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -detectOnly
</code></pre>
<p>扫描共享顶点的重合面，报告检测结果并保留网格原状，适合先确认要处理的对象。</p>
<h2>示例 2：合并成内部面</h2>
<pre><code class="language-bash">mergeOrSplitBaffles
</code></pre>
<p>采用默认合并行为，把识别出的挡板面恢复成内部连接，结果写入新网格时间。</p>
<h2>示例 3：拆分两侧顶点</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -split -overwrite
</code></pre>
<p>-split 复制两侧需要分离的顶点；-overwrite 写回当前网格，使挡板两侧具有独立拓扑。</p>
<h2>示例 4：用字典选择处理动作</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -dict system/baffleActionsDict -overwrite
</code></pre>
<p>baffleActionsDict 已按该工具格式定义选定挡板及操作；用字典控制处理范围，结果写回网格。</p>
<h2>示例 5：在单一区域拆分并核查</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -region fluid -split -overwrite
checkMesh -region fluid
</code></pre>
<p>多区域案例仅修改 fluid，检查该区域拆分后的边界、单元闭合和连通关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-detectOnly</code></td><td>Find baffles only, but do not merge or split them</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-split</code></td><td>Topologically split duplicate surfaces</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mergeOrSplitBaffles [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -detectOnly       Find baffles only, but do not merge or split them
  -dict &lt;file&gt;      Specify a dictionary to read actions from
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -split            Topologically split duplicate surfaces
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Detect faces that share points (baffles).
Merge them or duplicate the points.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mergeOrSplitBaffles/mergeOrSplitBaffles.C">源码与说明</a> · <a href="/assets/command-help/mergeorsplitbaffles.txt">帮助文本</a></p>
