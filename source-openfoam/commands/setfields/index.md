---
title: "setFields · 按几何选区或拓扑集合给已有场设置初值"
layout: reference
description: "按几何选区或拓扑集合给已有场设置初值。"
cms_slug: "command-setfields"
---

<p>按几何选区或拓扑集合给已有场设置初值。</p><h2>开始前</h2>
<p>目标场已存在，system/setFieldsDict 定义 defaultFieldValues 和 regions。</p>
<h2>示例 1：执行初始场分区赋值</h2>
<pre><code class="language-bash">setFields -time 0
</code></pre>
<p>对0目录场先应用默认值，再按regions顺序设置局部值，常用于液位、热点或浓度团初始化。</p>
<h2>示例 2：采用另一液位方案</h2>
<pre><code class="language-bash">setFields -dict system/setFields-highWaterDict -time 0
</code></pre>
<p>替代字典定义另一液位选区，便于保持网格相同而比较不同初始水量。</p>
<h2>示例 3：在新网格上重新初始化</h2>
<pre><code class="language-bash">blockMesh
setFields -time 0
</code></pre>
<p>网格重建后重新执行几何选区，使非均匀初场与新单元数量匹配。</p>
<h2>示例 4：只对某个区域赋值</h2>
<pre><code class="language-bash">setFields -region fluid -dict system/setFields-fluidDict -time 0
</code></pre>
<p>多区域案例中只修改fluid的场，保持固体初始温度等设置不变。</p>
<h2>示例 5：设置有限面积场</h2>
<pre><code class="language-bash">setFields -area-region film -dict system/setFields-filmDict -time 0
</code></pre>
<p>已存在film有限面积网格及其场时，按专用字典设置表面初值，适用于薄膜或壳面计算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>Use all regions in finite-area regionProperties Specify area-mesh region. Eg, -area-region shell Use specified area region. Eg, -area-regions film Or from regionProperties.  Eg, -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-no-finite-area</code></td><td>Suppress handling of finite-area mesh/fields</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-setfieldsdict/">setFieldsDict</a> · <a href="/dictionaries/0-alpha-water/">alpha.water</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setFields [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative setFieldsDict
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
  -no-finite-area   Suppress handling of finite-area mesh/fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
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
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Set values on a selected set of cells/patch-faces via a dictionary

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setFields/setFields.C">源码与说明</a> · <a href="/assets/command-help/setfields.txt">帮助文本</a></p>
