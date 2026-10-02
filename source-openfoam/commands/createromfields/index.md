---
title: "createROMfields · 根据已训练的降阶模型数据重建指定时刻的场"
layout: reference
description: "根据已训练的降阶模型数据重建指定时刻的场。"
cms_slug: "command-createromfields"
---

<p>根据已训练的降阶模型数据重建指定时刻的场。</p><h2>开始前</h2>
<p>已有网格、system/ROMfieldsDict、相应模态与系数数据；目标时间目录需要满足所选ROM模型的读取要求。</p>
<h2>示例 1：按默认ROM字典重建</h2>
<pre><code class="language-bash">createROMfields
</code></pre>
<p>读取ROMfieldsDict选择模型，使用现有降阶数据创建并写字段，省去重新求解完整CFD方程。</p>
<h2>示例 2：只重建最新已选时刻</h2>
<pre><code class="language-bash">createROMfields -latestTime
</code></pre>
<p>选择最新可用时间，根据模态与时间系数生成该状态的重建场。</p>
<h2>示例 3：重建一段时间序列</h2>
<pre><code class="language-bash">createROMfields -time '0.1:1'
</code></pre>
<p>对该区间内可选择的已有时间目录重建，适合与高保真结果逐时刻比较。</p>
<h2>示例 4：比较另一模态截断方案</h2>
<pre><code class="language-bash">createROMfields -dict system/ROMfields-lowRankDict -time '0.1:1'
</code></pre>
<p>替代字典已配置较少模态及对应数据；在独立案例比较重建细节与误差。</p>
<h2>示例 5：重建指定区域后导出</h2>
<pre><code class="language-bash">createROMfields -region fluid -latestTime
foamToVTK -region fluid -latestTime -fields '(U p)' -name VTK-ROM
</code></pre>
<p>ROM模型配置为重建U、p时，先生成fluid区域场，再导出检查模态重建的空间结构。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createROMfields [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for ROMfieldsDict
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create fields using reduced-order modelling (ROM) data at specific time
instants without requiring any CFD computations.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/createROMfields/ROMmodels/ROMmodel/ROMmodel.C">源码与说明</a> · <a href="/assets/command-help/createromfields.txt">帮助文本</a></p>
