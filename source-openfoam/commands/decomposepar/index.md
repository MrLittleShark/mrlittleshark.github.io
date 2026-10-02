---
title: "decomposePar · 按照 decomposeParDict 将网格与场分成并行子域"
layout: reference
description: "按照 decomposeParDict 将网格与场分成并行子域。"
cms_slug: "command-decomposepar"
---

<p>按照 decomposeParDict 将网格与场分成并行子域。</p><h2>分解算例</h2>
<pre><code class="language-bash">decomposePar
</code></pre>
<p>读取 <code>numberOfSubdomains</code> 和 <code>method</code>，生成相应的分区数据。求解时的进程数应与分区数一致。</p>
<h2>显示分区分布</h2>
<pre><code class="language-bash">decomposePar -cellDist
</code></pre>
<p>同时写出分区分布，便于查看各子域的大小与形状。长条或狭窄子域可能增加通信，分区数也受单元总数约束。</p>
<h2>重新建立四个分区</h2>
<pre><code class="language-bash">foamDictionary system/decomposeParDict -entry numberOfSubdomains -set 4
decomposePar -force
</code></pre>
<p>第一行修改分区数，第二行替换已有分区数据。已有 processor 结果需要保留时，先重建或另存。</p>
<h2>分解后运行</h2>
<pre><code class="language-bash">mpirun -np 4 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1
</code></pre>
<p><code>-np 4</code> 启动 4 个进程，<code>-parallel</code> 让求解器读取分区网格。这里的物理和数值配置应当已经适用于 <code>simpleFoam</code>。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allAreas</td><td>Use all regions in finite-area regionProperties</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cellDist</td><td>写出单元所属子域，便于检查分区。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-copyUniform</td><td>Copy any uniform/ directories too</td></tr><tr><td>-copyZero</td><td>Copy 0/ directory to processor*/ rather than decompose the fields Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file</td></tr><tr><td>-domains &lt;N&gt;</td><td>Override numberOfSubdomains (-dry-run only)</td></tr><tr><td>-dry-run</td><td>Test without writing the decomposition. Changes -cellDist to only write VTK output.</td></tr><tr><td>-fields</td><td>按工具要求指定要处理的字段或仅处理字段。具体参数见完整帮助。</td></tr><tr><td>-force</td><td>Remove existing processor*/ subdirs before decomposing the geometry</td></tr><tr><td>-ifRequired</td><td>按已有分区和当前配置判断是否需要重新分解。</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-method &lt;name&gt;</td><td>Override decomposition method (-dry-run only)</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/decompositionConstraints/geometric">preProcessing/decompositionConstraints/geometric</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: decomposePar [OPTIONS]
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
  -cellDist         Write cell distribution as a labelList - for use with
                    &#x27;manual&#x27; decomposition method and as a volScalarField for
                    visualization.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -copyUniform      Copy any uniform/ directories too
  -copyZero         Copy 0/ directory to processor*/ rather than decompose the
                    fields
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -domains &lt;N&gt;      Override numberOfSubdomains (-dry-run only)
  -dry-run          Test without writing the decomposition. Changes -cellDist
                    to only write VTK output.
  -fields           Use existing geometry decomposition and convert fields only
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -force            Remove existing processor*/ subdirs before decomposing the
                    geometry
  -ifRequired       Only decompose geometry if the number of domains has changed
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -method &lt;name&gt;    Override decomposition method (-dry-run only)
  -no-fields        Suppress conversion of fields (volume, finite-area,
                    lagrangian)
  -no-finite-area   Suppress finiteArea mesh/field decomposition
  -no-lagrangian    Suppress lagrangian (cloud) decomposition
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-sets          Skip decomposing cellSets, faceSets, pointSets
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Decompose a mesh and fields of a case for parallel execution

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/decomposePar/decomposePar.C">源码与说明</a> · <a href="/assets/command-help/decomposepar.txt">帮助文本</a></p>
