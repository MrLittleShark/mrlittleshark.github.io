---
title: "transformPoints · 平移、旋转或缩放网格坐标，可同步旋转向量与张量场"
layout: reference
description: "平移、旋转或缩放网格坐标，可同步旋转向量与张量场。"
cms_slug: "command-transformpoints"
---

<p>平移、旋转或缩放网格坐标，可同步旋转向量与张量场。</p><h2>开始前</h2>
<p>已有网格；变换直接更新所选时间的坐标，各独立几何方案从相同基础网格副本开始。</p>
<h2>示例 1：毫米坐标转为米</h2>
<pre><code class="language-bash">transformPoints -scale 0.001
</code></pre>
<p>所有坐标乘0.001，适合CAD导入坐标以毫米存储、案例长度统一采用米的网格。</p>
<h2>示例 2：平移模型</h2>
<pre><code class="language-bash">transformPoints -translate '(0.5 0 0)'
</code></pre>
<p>沿x方向平移0.5个当前长度单位；几何尺寸与单元连接保持不变。</p>
<h2>示例 3：绕指定轴旋转</h2>
<pre><code class="language-bash">transformPoints -rotate-angle '((0 0 1) 30)'
</code></pre>
<p>绕z轴转30度，角度单位为度；用于调整模型相对来流的朝向。</p>
<h2>示例 4：绕模型中心旋转并处理场</h2>
<pre><code class="language-bash">transformPoints -auto-centre -rotate-y 15 -rotateFields -time 0
</code></pre>
<p>使用包围盒中心为旋转中心，对0时刻网格及向量、张量场一起绕y轴转15度。</p>
<h2>示例 5：统一多区域坐标</h2>
<pre><code class="language-bash">transformPoints -allRegions -translate '(0 0 1)' -scale 0.001
</code></pre>
<p>对regionProperties中的全部区域使用同一变换；先平移，再按工具变换顺序缩放，适合多部件坐标统一，需按原坐标单位给出平移量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-auto-centre</code></td><td>Use bounding box centre as centre for rotations</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-centre &lt;point&gt;</code></td><td>Use specified &lt;point&gt; as centre for rotations Tranform cylindrical coordinates to cartesian coordinates Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-recentre</code></td><td>Recentre the bounding box before other operations</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-rotate-x &lt;deg&gt;</code></td><td>Rotate (degrees) about x-axis</td></tr><tr><td><code>-rotate-y &lt;deg&gt;</code></td><td>Rotate (degrees) about y-axis</td></tr><tr><td><code>-rotate-z &lt;deg&gt;</code></td><td>Rotate (degrees) about z-axis</td></tr><tr><td><code>-rotateFields</code></td><td>Read and transform vector and tensor fields too Scale by the specified amount - Eg, for uniform [mm] to [m] scaling use either &#x27;(0.001 0.001 0.001)&#x27; or simply &#x27;0.001&#x27;</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: transformPoints [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -auto-centre      Use bounding box centre as centre for rotations
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -centre &lt;point&gt;   Use specified &lt;point&gt; as centre for rotations
  -cylToCart &lt;(originVec axisVec directionVec)&gt;
                    Tranform cylindrical coordinates to cartesian coordinates
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
  -recentre         Recentre the bounding box before other operations
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -rollPitchYaw &lt;vector&gt;
                    Rotate by &#x27;(roll pitch yaw)&#x27; degrees
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -rotate &lt;(vectorA vectorB)&gt;
                    Rotate from &lt;vectorA&gt; to &lt;vectorB&gt; - eg, &#x27;((1 0 0) (0 0 1))&#x27;
  -rotate-angle &lt;(vector angle)&gt;
                    Rotate &lt;angle&gt; degrees about &lt;vector&gt; - eg, &#x27;((1 0 0) 45)&#x27;
  -rotate-x &lt;deg&gt;   Rotate (degrees) about x-axis
  -rotate-y &lt;deg&gt;   Rotate (degrees) about y-axis
  -rotate-z &lt;deg&gt;   Rotate (degrees) about z-axis
  -rotateFields     Read and transform vector and tensor fields too
  -scale &lt;scalar | vector&gt;
                    Scale by the specified amount - Eg, for uniform [mm] to [m]
                    scaling use either &#x27;(0.001 0.001 0.001)&#x27; or simply &#x27;0.001&#x27;
  -time &lt;time&gt;      Specify the time to search from and apply the
                    transformation (default is latest)
  -translate &lt;vector&gt;
                    Translate by specified &lt;vector&gt; before rotations
  -world &lt;name&gt;     Name of the local world for parallel communication
  -yawPitchRoll &lt;vector&gt;
                    Rotate by &#x27;(yaw pitch roll)&#x27; degrees
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Transform (translate / rotate / scale) mesh points.
Note: roll=rotate about x, pitch=rotate about y, yaw=rotate about z

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/transformPoints/transformPoints.C">源码与说明</a> · <a href="/assets/command-help/transformpoints.txt">帮助文本</a></p>
