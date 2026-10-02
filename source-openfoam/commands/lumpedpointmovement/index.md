---
title: "lumpedPointMovement · 用响应表预览集中点运动，或测试外部耦合响应"
layout: reference
description: "用响应表预览集中点运动，或测试外部耦合响应。"
cms_slug: "command-lumpedpointmovement"
---

<p>用响应表预览集中点运动，或测试外部耦合响应。</p><h2>开始前</h2>
<p>已有lumpedPoint运动配置及responseFile响应表；带网格预览还需要对应耦合边界。</p>
<h2>示例 1：只预览响应点运动</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -dry-run
</code></pre>
<p>读取响应表并输出集中点状态VTP序列，-dry-run可在没有体网格时检查运动输入。</p>
<h2>示例 2：预览边界随控制点变形</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat
</code></pre>
<p>已有耦合网格时同时写控制点状态和边界几何序列，查看结构响应如何传到表面。</p>
<h2>示例 3：只查看前20个状态</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -max 20
</code></pre>
<p>限制最多20个输出，适合先检查较长响应表的起始阶段。</p>
<h2>示例 4：抽样查看长时间序列</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -span 5 -max 100
</code></pre>
<p>每隔5个表项取一个，最多输出100帧，减少预览文件数量。</p>
<h2>示例 5：缩小运动幅度</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -scale 0.5 -visual-length 0.1
</code></pre>
<p>相对初始状态把运动幅度缩到一半，同时设控制平面显示长度0.1，便于分辨运动方向与局部转角。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Test movement without a mesh Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-max &lt;N&gt;</code></td><td>Maximum number of outputs</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-removeLock</code></td><td>Remove lock-file on termination of slave Subprocess root directories for distributed running</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Relaxation/scaling factor for movement (default: 1)</td></tr><tr><td><code>-slave</code></td><td>Invoke as a slave responder for testing</td></tr><tr><td><code>-span &lt;N&gt;</code></td><td>Increment each input by N (default: 1) Visualization length for planes (visualized as triangles)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lumpedPointMovement [OPTIONS] &lt;responseFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test movement without a mesh
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
  -max &lt;N&gt;          Maximum number of outputs
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -removeLock       Remove lock-file on termination of slave
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -scale &lt;factor&gt;   Relaxation/scaling factor for movement (default: 1)
  -slave            Invoke as a slave responder for testing
  -span &lt;N&gt;         Increment each input by N (default: 1)
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

Visualize lumpedPoint movements or provide a slave responder for diagnostic
purposes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/lumpedPointMovement.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointmovement.txt">帮助文本</a></p>
