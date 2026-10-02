---
title: "transformPoints · 示例将毫米坐标换算为米"
layout: reference
description: "示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。"
cms_slug: "command-transformpoints"
---

<p>示例将毫米坐标换算为米。外部源项位置和参考点需同步换算。</p><h2>用法</h2><pre><code class="language-bash">transformPoints -scale &#x27;(0.001 0.001 0.001)&#x27;</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">transformPoints -scale &#x27;(0.001 0.001 0.001)&#x27; -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-auto-centre</td><td>Use bounding box centre as centre for rotations</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-centre &lt;point&gt;</td><td>Use specified &lt;point&gt; as centre for rotations Tranform cylindrical coordinates to cartesian coordinates Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-recentre</td><td>Recentre the bounding box before other operations</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-rotate-x &lt;deg&gt;</td><td>Rotate (degrees) about x-axis</td></tr><tr><td>-rotate-y &lt;deg&gt;</td><td>Rotate (degrees) about y-axis</td></tr><tr><td>-rotate-z &lt;deg&gt;</td><td>Rotate (degrees) about z-axis</td></tr><tr><td>-rotateFields</td><td>Read and transform vector and tensor fields too Scale by the specified amount - Eg, for uniform [mm] to [m] scaling use either &#x27;(0.001 0.001 0.001)&#x27; or simply &#x27;0.001&#x27;</td></tr><tr><td>-time &lt;time&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: transformPoints [OPTIONS]
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
