---
title: "rotateMesh · 按两个方向向量确定旋转，同时旋转网格与向量、张量场"
layout: reference
description: "按两个方向向量确定旋转，同时旋转网格与向量、张量场。"
cms_slug: "command-rotatemesh"
---

<p>按两个方向向量确定旋转，同时旋转网格与向量、张量场。</p><h2>开始前</h2>
<p>已有网格和要旋转的结果时间；from、to 是非零方向向量，二者确定刚体旋转。</p>
<h2>示例 1：把x方向转到y方向</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)'
</code></pre>
<p>旋转网格，并同步处理所读向量、张量场的分量，适合改变整个案例的空间朝向。</p>
<h2>示例 2：仅处理最后时刻</h2>
<pre><code class="language-bash">rotateMesh '(0 0 1)' '(1 0 0)' -latestTime
</code></pre>
<p>选择最新结果，把原z方向转到x方向；输出该状态下经过一致旋转的几何和场。</p>
<h2>示例 3：旋转指定时间区间</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 0 1)' -time '0.1:0.5'
</code></pre>
<p>仅处理0.1到0.5之间已有时间目录，便于统一一段动画数据的朝向。</p>
<h2>示例 4：旋转指定区域</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)' -region fluid -time 0
</code></pre>
<p>只处理 fluid 的0时刻网格与场；适合区域输入数据的坐标系转换。</p>
<h2>示例 5：多区域一致旋转</h2>
<pre><code class="language-bash">rotateMesh '(1 0 0)' '(0 1 0)' -allRegions -constant
</code></pre>
<p>regionProperties 已登记各区域；所有区域按同一旋转变换处理，并将 constant 纳入选择，保持相对空间位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: rotateMesh [OPTIONS] &lt;from&gt; &lt;to&gt;
Arguments:
  &lt;from&gt;            The vector to rotate from
  &lt;to&gt;              The vector to rotate to
Options:
  -allRegions       Use all regions in regionProperties
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
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Rotate mesh points and vector/tensor fields
Rotation from the &lt;from&gt; vector to the &lt;to&gt; vector

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/rotateMesh/rotateMesh.C">源码与说明</a> · <a href="/assets/command-help/rotatemesh.txt">帮助文本</a></p>
