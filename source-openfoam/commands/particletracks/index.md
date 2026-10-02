---
title: "particleTracks · 把瞬态粒子位置历史连接成轨迹并导出"
layout: reference
description: "把瞬态粒子位置历史连接成轨迹并导出。"
cms_slug: "command-particletracks"
---

<p>把瞬态粒子位置历史连接成轨迹并导出。</p><h2>开始前</h2>
<p>已有多个时间的粒子位置及身份信息；默认字典实际为constant/particleTrackProperties，包含cloud、sampleFrequency、maxPositions等。</p>
<h2>示例 1：导出完整时间轨迹</h2>
<pre><code class="language-bash">particleTracks
</code></pre>
<p>按字典选择粒子云和采样频率，依据粒子身份关联不同时间的位置，输出轨迹文件。</p>
<h2>示例 2：截取特定时间段</h2>
<pre><code class="language-bash">particleTracks -time '0.1:0.5'
</code></pre>
<p>只连接0.1至0.5区间的数据，适合查看喷射初期或指定运动阶段。</p>
<h2>示例 3：减少所跟踪粒子数量</h2>
<pre><code class="language-bash">particleTracks -stride 10 -time '0:1'
</code></pre>
<p>-stride覆盖字典sampleFrequency，对粒子编号按指定采样间隔抽取轨迹，减少密集粒子云的显示量。</p>
<h2>示例 4：给轨迹附加字段</h2>
<pre><code class="language-bash">particleTracks -fields '(U d T)' -format vtk
</code></pre>
<p>云中已有U、d、T时，随轨迹写速度、粒径和温度，便于沿路径着色分析。</p>
<h2>示例 5：采用另一云的轨迹方案</h2>
<pre><code class="language-bash">particleTracks -dict constant/particleTrackProperties-spray -region gas -time '0.1:1'
</code></pre>
<p>替代字典指定喷雾云；从gas区域读取粒子，生成该云在指定时段内的轨迹。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-format &lt;name&gt;</code></td><td>The writer format (default: vtk or &#x27;setFormat&#x27; from dictionary) Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-stride &lt;int&gt;</code></td><td>Override the sample-frequency</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: particleTracks [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative particleTracksProperties dictionary
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to write (default: all or
                    &#x27;fields&#x27; from dictionary)
                    Eg, &#x27;T&#x27; or &#x27;( &quot;U.*&quot; )&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -format &lt;name&gt;    The writer format (default: vtk or &#x27;setFormat&#x27; from
                    dictionary)
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
  -stride &lt;int&gt;     Override the sample-frequency
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generate a file of particle tracks for cases that were computed using a
tracked-parcel-type cloud

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/particleTracks/particleTracks.C">源码与说明</a> · <a href="/assets/command-help/particletracks.txt">帮助文本</a></p>
