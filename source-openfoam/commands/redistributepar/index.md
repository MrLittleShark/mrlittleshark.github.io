---
title: "redistributePar · 并行重分区、分解或重构网格与场"
layout: reference
description: "并行重分区、分解或重构网格与场。"
cms_slug: "command-redistributepar"
---

<p>并行重分区、分解或重构网格与场。</p><h2>开始前</h2>
<p>system/decomposeParDict定义目标子域数；MPI进程数至少覆盖原布局和目标布局所需的处理器数量。</p>
<h2>示例 1：测试新的分区布局</h2>
<pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -dry-run -cellDist
</code></pre>
<p>已有数据与目标设置就绪时，只评估重分区并输出cellDist诊断，用于比较负载分布。</p>
<h2>示例 2：把串行案例分成8份</h2>
<pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -decompose
</code></pre>
<p>decomposeParDict中numberOfSubdomains为8；从完整案例分解网格与场，利用并行进程执行分区过程。</p>
<h2>示例 3：重新分配最新结果</h2>
<pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -latestTime -overwrite
</code></pre>
<p>原布局不超过8个子域，目标设为8时，将最新网格与场重分配并更新分区数据，便于更换计算资源。</p>
<h2>示例 4：并行重构完整案例</h2>
<pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -reconstruct -latestTime
</code></pre>
<p>输入是8分区结果时，在并行中重构最新完整状态，作用对应把分区数据集中回单一案例。</p>
<h2>示例 5：重分区全部区域</h2>
<pre><code class="language-bash">mpirun -np 8 redistributePar -parallel -allRegions -latestTime -overwrite
</code></pre>
<p>目标多区域分区设置已准备；同一流程处理流体和固体区域，输出可继续并行计算的区域场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cellDist</code></td><td>写出单元所属子域，便于检查分区。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-decompose</code></td><td>Decompose case Alternative decomposePar dictionary file</td></tr><tr><td><code>-dry-run</code></td><td>Test without writing the decomposition. Changes -cellDist to only write volScalarField. Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-newTimes</code></td><td>Only reconstruct new times (i.e. that do not exist already)</td></tr><tr><td><code>-no-finite-area</code></td><td>Suppress finiteArea mesh/field handling</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-reconstruct</code></td><td>Reconstruct case</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: redistributePar [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellDist         Write cell distribution as a labelList - for use with
                    &#x27;manual&#x27; decomposition method or as a volScalarField for
                    post-processing.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decompose        Decompose case
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test without writing the decomposition. Changes -cellDist
                    to only write volScalarField.
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
  -newTimes         Only reconstruct new times (i.e. that do not exist already)
  -no-finite-area   Suppress finiteArea mesh/field handling
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -reconstruct      Reconstruct case
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity. (Can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Redistribute decomposed mesh and fields according to the decomposeParDict
settings.
Optionally run in decompose/reconstruct mode

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/redistributePar/loadOrCreateMesh.C">源码与说明</a> · <a href="/assets/command-help/redistributepar.txt">帮助文本</a></p>
