---
title: "reconstructPar · 将并行子域中的场重建到完整网格上"
layout: reference
description: "将并行子域中的场重建到完整网格上。"
cms_slug: "command-reconstructpar"
---

<p>将并行子域中的场重建到完整网格上。</p><h2>重建最新结果</h2>
<pre><code class="language-bash">reconstructPar -latestTime
</code></pre>
<p>读取最近时刻的分区场，将完整场写到主算例时间目录。</p>
<h2>只重建部分场</h2>
<pre><code class="language-bash">reconstructPar -latestTime -fields "(U p)"
</code></pre>
<p>仅合并速度和压力，可减少读写量。字段名使用实际求解器输出的名称。</p>
<h2>选择时间范围</h2>
<pre><code class="language-bash">reconstructPar -time "0.1:0.5"
</code></pre>
<p>合并 0.1 至 0.5 范围内已存在的时刻。动态网格或拓扑变化算例还需处理各时刻的网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allAreas</td><td>Use all regions in finite-area regionProperties</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-newTimes</td><td>Only reconstruct new times (i.e. that do not exist already)</td></tr><tr><td>-no-fields</td><td>Skip reconstructing fields</td></tr><tr><td>-no-lagrangian</td><td>Skip reconstructing lagrangian positions and fields</td></tr><tr><td>-no-sets</td><td>Skip reconstructing cellSets, faceSets, pointSets Do not execute function objects</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td>-withZero</td><td>Include &#x27;0/&#x27; dir in the times list</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: reconstructPar [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to reconstruct (all by
                    default). Eg, &#x27;T&#x27; or &#x27;(p T U &quot;alpha.*&quot;)&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lagrangianFields &lt;wordRes&gt;
                    Specify single or multiple lagrangian fields to reconstruct
                    (all by default). Eg, &#x27;(U d)&#x27; - Positions are always
                    included.
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -newTimes         Only reconstruct new times (i.e. that do not exist already)
  -no-fields        Skip reconstructing fields
  -no-lagrangian    Skip reconstructing lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-sets          Skip reconstructing cellSets, faceSets, pointSets
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
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

Reconstruct fields of a parallel case

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructPar/reconstructPar.C">源码与说明</a> · <a href="/assets/command-help/reconstructpar.txt">帮助文本</a></p>
