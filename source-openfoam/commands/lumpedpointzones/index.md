---
title: "lumpedPointZones · 显示集中点压力积分区域及插值权重关系"
layout: reference
description: "显示集中点压力积分区域及插值权重关系。"
cms_slug: "command-lumpedpointzones"
---

<p>显示集中点压力积分区域及插值权重关系。</p><h2>开始前</h2>
<p>已有lumpedPoint运动和边界配置；完整模式需要原始网格。</p>
<h2>示例 1：检查初始控制点</h2>
<pre><code class="language-bash">lumpedPointZones -dry-run
</code></pre>
<p>只读取初始集中点状态并写state.vtp，可先检查参考位置与转角设置。</p>
<h2>示例 2：显示积分区域与插值关系</h2>
<pre><code class="language-bash">lumpedPointZones
</code></pre>
<p>生成state.vtp和lumpedPointZones.vtp，并报告每个控制点对应面积，检查边界分段。</p>
<h2>示例 3：仅查看区域分组</h2>
<pre><code class="language-bash">lumpedPointZones -no-interpolate
</code></pre>
<p>保留压力积分区域显示，关闭插值器计算和显示，让区域归属更容易观察。</p>
<h2>示例 4：调整控制平面显示大小</h2>
<pre><code class="language-bash">lumpedPointZones -visual-length 0.05
</code></pre>
<p>将用于显示方向的三角平面长度设为0.05个几何长度单位，避免小模型被标记遮挡。</p>
<h2>示例 5：检查某一区域并显示过程</h2>
<pre><code class="language-bash">lumpedPointZones -region fluid -verbose
</code></pre>
<p>只处理fluid耦合边界，输出更详细的区域和控制点信息，便于核对多区域设置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Test initial lumped points state without a mesh Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-no-interpolate</code></td><td>Suppress calculation/display of point interpolators</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) Visualization length for planes (visualized as triangles)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lumpedPointZones [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test initial lumped points state without a mesh
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
  -no-interpolate   Suppress calculation/display of point interpolators
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -verbose          Additional verbosity (can be used multiple times)
  -visual-length &lt;len&gt;
                    Visualization length for planes (visualized as triangles)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create lumpedPointZones.vtp to verify the segmentation of pressure integration
zones used by lumpedPoint BC.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointZones/lumpedPointZones.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointzones.txt">帮助文本</a></p>
