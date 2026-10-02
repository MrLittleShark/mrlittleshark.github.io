---
title: "reconstructParMesh · 从处理器子域重构网格和寻址关系"
layout: reference
description: "从处理器子域重构网格和寻址关系。"
cms_slug: "command-reconstructparmesh"
---

<p>从处理器子域重构网格和寻址关系。</p><h2>开始前</h2>
<p>已有匹配的分区网格；动网格或并行网格生成的各时间拓扑需要分别处理。</p>
<h2>示例 1：重构恒定网格</h2>
<pre><code class="language-bash">reconstructParMesh -constant
</code></pre>
<p>从各processor的constant网格恢复全域网格，适合并行网格生成结束后的整理。</p>
<h2>示例 2：恢复最新动网格</h2>
<pre><code class="language-bash">reconstructParMesh -latestTime
</code></pre>
<p>选择最后保存的分区网格状态，重构完整几何和连接关系。</p>
<h2>示例 3：按处理器接口匹配</h2>
<pre><code class="language-bash">reconstructParMesh -constant -procMatch
</code></pre>
<p>只在processor边界上进行几何匹配，适合接口定义可靠的标准分区网格。</p>
<h2>示例 4：采用全边界几何匹配</h2>
<pre><code class="language-bash">reconstructParMesh -constant -fullMatch -mergeTol 1e-7
</code></pre>
<p>在全部边界上做更全面的匹配；mergeTol是相对包围盒尺寸的合并容差。</p>
<h2>示例 5：先恢复寻址再拼场</h2>
<pre><code class="language-bash">reconstructParMesh -latestTime -addressing-only
reconstructPar -latestTime
</code></pre>
<p>完整网格已存在且与分区几何一致时，只建立procAddressing而保留网格，再利用寻址重构字段。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-addressing-only</code></td><td>Create procAddressing only without overwriting the mesh</td></tr><tr><td><code>-allAreas</code></td><td>Use all regions in finite-area regionProperties</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cellDist</code></td><td>写出单元所属子域，便于检查分区。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-fullMatch</code></td><td>Do (slower) geometric matching on all boundary faces Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-no-finite-area</code></td><td>Suppress finiteArea mesh reconstruction</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-procMatch</code></td><td>Do matching on processor faces only</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: reconstructParMesh [OPTIONS]
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
