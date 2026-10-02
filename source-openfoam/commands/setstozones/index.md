---
title: "setsToZones · 把 pointSet、faceSet、cellSet 转成同名网格 zone"
layout: reference
description: "把 pointSet、faceSet、cellSet 转成同名网格 zone。"
cms_slug: "command-setstozones"
---

<p>把 pointSet、faceSet、cellSet 转成同名网格 zone。</p><h2>开始前</h2>
<p>已有集合文件；需要定向的 faceSet 通常还需同名 cellSet 确定方向。</p>
<h2>示例 1：把现有集合转成zone</h2>
<pre><code class="language-bash">setsToZones
</code></pre>
<p>遍历网格集合并创建相应zone；cellSet转cellZone，pointSet转pointZone，faceSet转faceZone。</p>
<h2>示例 2：仅需区域成员而不需方向</h2>
<pre><code class="language-bash">setsToZones -noFlipMap
</code></pre>
<p>关闭 faceSet 的方向判定，适合只关注集合成员的zone转换；由面通量方向参与计算时应另外校正定向。</p>
<h2>示例 3：转换初始恒定网格集合</h2>
<pre><code class="language-bash">setsToZones -constant -noFlipMap
</code></pre>
<p>把 constant 纳入选择，读取初始网格的集合，适合网格预处理后建立源项或旋转体区域。</p>
<h2>示例 4：转换最新状态的集合</h2>
<pre><code class="language-bash">setsToZones -latestTime
</code></pre>
<p>动网格最后时刻已有重新选择的集合；转换后zone对应最新网格拓扑和编号。</p>
<h2>示例 5：多区域源区生成流程</h2>
<pre><code class="language-bash">topoSet -region fluid -dict system/topoSet-heaterDict
setsToZones -region fluid -noFlipMap
</code></pre>
<p>先在 fluid 中生成 heater 等cellSet，再转为同名cellZone，供该区域体积源模型使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noFlipMap</code></td><td>Ignore orientation of faceSet Do not execute function objects</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setsToZones [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times
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
  -noFlipMap        Ignore orientation of faceSet
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times (currently ignored)
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;value&gt;     Select the nearest time to the specified value
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Add point/face/cell Zones from similarly named point/face/cell Sets

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/setsToZones/setsToZones.C">源码与说明</a> · <a href="/assets/command-help/setstozones.txt">帮助文本</a></p>
