---
title: "smoothSurfaceData · 对外部表面标量数据进行中值滤波"
layout: reference
description: "对外部表面标量数据进行中值滤波。"
cms_slug: "command-smoothsurfacedata"
---

<p>对外部表面标量数据进行中值滤波。</p><h2>开始前</h2>
<p>输入为受支持的表面结果文件；默认读取EnSight，默认处理标量T。半径单位为米。</p>
<h2>示例 1：平滑表面温度</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -radius 0.002
</code></pre>
<p>输入EnSight表面结果含T；以2毫米邻域执行默认一次中值滤波，输出滤波后的表面数据。</p>
<h2>示例 2：改为处理压力</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -field p -radius 0.002
</code></pre>
<p>选择标量p，对局部压力尖峰进行中值过滤，几何仍取输入表面。</p>
<h2>示例 3：增加过滤遍数</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -field T -radius 0.002 -sweeps 3
</code></pre>
<p>连续执行3级中值滤波，抑制孤立异常值的同时也会改变较细的空间变化。</p>
<h2>示例 4：比较较大邻域</h2>
<pre><code class="language-bash">smoothSurfaceData coarseStudy.case -field T -radius 0.01 -sweeps 1
</code></pre>
<p>独立输入副本使用1厘米滤波半径，比较平滑尺度对温度梯度的影响。</p>
<h2>示例 5：明确格式并输出详细过程</h2>
<pre><code class="language-bash">smoothSurfaceData surface.case -read-format ensight -field T -radius 0.002 -sweeps 2 -verbose
</code></pre>
<p>显式选择EnSight读取器，执行两遍过滤并显示更多处理信息，便于核对字段和邻域构建。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>Field &lt;scalar&gt; to process (default: T) Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-radius &lt;m&gt;</code></td><td>Specify filter radius [metres] Input format (default: ensight) Subprocess root directories for distributed running</td></tr><tr><td><code>-sweeps &lt;N&gt;</code></td><td>Number of median filter stages</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: smoothSurfaceData [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -field &lt;name&gt;     Field &lt;scalar&gt; to process (default: T)
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
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -radius &lt;m&gt;       Specify filter radius [metres]
  -read-format &lt;type&gt;
                    Input format (default: ensight)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -sweeps &lt;N&gt;       Number of median filter stages
  -verbose          Additional verbosity (can be used multiple times)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Testing, pre-processing, filtering of surface field data

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/smoothSurfaceData/smoothSurfaceData.C">源码与说明</a> · <a href="/assets/command-help/smoothsurfacedata.txt">帮助文本</a></p>
