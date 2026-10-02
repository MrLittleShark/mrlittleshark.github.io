---
title: "reconstructParMesh · 将分区网格重新合成为完整网格"
layout: reference
description: "将分区网格重新合成为完整网格。"
cms_slug: "command-reconstructparmesh"
---

<p>将分区网格重新合成为完整网格。</p><h2>重建静态网格</h2>
<pre><code class="language-bash">reconstructParMesh -constant
</code></pre>
<p>用于网格位于各分区 <code>constant/polyMesh</code> 的情况，常见于并行网格生成。</p>
<h2>重建最近时刻网格</h2>
<pre><code class="language-bash">reconstructParMesh -latestTime
</code></pre>
<p>选择最新时间的网格。网格重建完成后，再用 <code>reconstructPar</code> 合并相应场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-addressing-only</td><td>Create procAddressing only without overwriting the mesh</td></tr><tr><td>-allAreas</td><td>Use all regions in finite-area regionProperties</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cellDist</td><td>写出单元所属子域，便于检查分区。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-fullMatch</td><td>Do (slower) geometric matching on all boundary faces Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-no-finite-area</td><td>Suppress finiteArea mesh reconstruction</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-procMatch</td><td>Do matching on processor faces only</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times)</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: reconstructParMesh [OPTIONS]
Options:
  -addressing-only  Create procAddressing only without overwriting the mesh
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellDist         Write cell distribution as a labelList - for use with
                    &#x27;manual&#x27; decomposition method or as a volScalarField for
                    post-processing.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -fullMatch        Do (slower) geometric matching on all boundary faces
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mergeTol &lt;scalar&gt;
                    The merge distance relative to the bounding box size
                    (default 1e-7)
  -no-finite-area   Suppress finiteArea mesh reconstruction
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -procMatch        Do matching on processor faces only
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Reconstruct a mesh using geometric/topological information only

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructParMesh/reconstructParMesh.C">源码与说明</a> · <a href="/assets/command-help/reconstructparmesh.txt">帮助文本</a></p>
