---
title: "mapFields · 把源算例的场映射到目标算例网格"
layout: reference
description: "把源算例的场映射到目标算例网格。"
cms_slug: "command-mapfields"
---

<p>把源算例的场映射到目标算例网格。</p><h2>映射同类边界</h2>
<pre><code class="language-bash">mapFields ../coarseCase -sourceTime latestTime -consistent
</code></pre>
<p>在目标算例中执行。<code>../coarseCase</code> 是源算例；<code>latestTime</code> 选择源结果；<code>-consistent</code> 适合两边边界拓扑匹配的情况。</p>
<h2>映射不同边界</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceTime 0.5
</code></pre>
<p>在目标的 <code>system/mapFieldsDict</code> 设置 <code>patchMap</code> 和 <code>cuttingPatches</code>。映射后检查初始场范围和边界，尤其是新网格中源域未覆盖的区域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-consistent</td><td>按匹配的边界拓扑进行场映射。</td></tr><tr><td>-parallelSource</td><td>The source is decomposed</td></tr><tr><td>-parallelTarget</td><td>The target is decomposed Read decomposePar dictionary from specified location Specify the source region Specify the source time</td></tr><tr><td>-subtract</td><td>Subtract mapped source from target Read decomposePar dictionary from specified location Specify the target region</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-mapfieldsdict/">mapFieldsDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mapFields [OPTIONS] &lt;sourceCase&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -consistent       Source and target geometry and boundary conditions identical
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mapMethod &lt;word&gt;
                    Specify the mapping method
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallelSource   The source is decomposed
  -parallelTarget   The target is decomposed
  -sourceDecomposeParDict &lt;file&gt;
                    Read decomposePar dictionary from specified location
  -sourceRegion &lt;word&gt;
                    Specify the source region
  -sourceTime &lt;scalar|&#x27;latestTime&#x27;&gt;
                    Specify the source time
  -subtract         Subtract mapped source from target
  -targetDecomposeParDict &lt;file&gt;
                    Read decomposePar dictionary from specified location
  -targetRegion &lt;word&gt;
                    Specify the target region
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Map volume fields from one mesh to another

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mapFields/mapLagrangian.C">源码与说明</a> · <a href="/assets/command-help/mapfields.txt">帮助文本</a></p>
