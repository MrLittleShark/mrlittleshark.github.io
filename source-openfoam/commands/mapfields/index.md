---
title: "mapFields · 将一个案例的场映射到当前目标案例"
layout: reference
description: "将一个案例的场映射到当前目标案例。"
cms_slug: "command-mapfields"
---

<p>将一个案例的场映射到当前目标案例。</p><h2>开始前</h2>
<p>源案例已有结果，目标案例已有网格和相容字段；非一致边界映射需要system/mapFieldsDict。</p>
<h2>示例 1：同几何案例之间映射</h2>
<pre><code class="language-bash">mapFields ../sourceCase -consistent
</code></pre>
<p>在目标案例目录执行；源、目标几何及边界对应一致时使用-consistent，映射源场作为目标初值。</p>
<h2>示例 2：明确源结果时间</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceTime 5 -consistent
</code></pre>
<p>读取源时间5，避免由默认时间选择引入混淆；目标写入时刻由目标controlDict确定。</p>
<h2>示例 3：使用最新源场</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceTime latestTime
</code></pre>
<p>源案例已有最新结果且目标配置mapFieldsDict；将源最终场映射到目标网格。</p>
<h2>示例 4：映射两个命名区域</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceRegion fluid -targetRegion gas -sourceTime 5
</code></pre>
<p>源fluid映射到目标gas；两区域字段和边界映射已准备，用于区域名称不同的案例迁移。</p>
<h2>示例 5：从分区结果映射到目标</h2>
<pre><code class="language-bash">mapFields ../sourceCase -parallelSource -sourceTime latestTime
</code></pre>
<p>源结果位于processor目录时启用-parallelSource；工具从分区源数据读取，写目标案例字段。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-consistent</code></td><td>按匹配的边界拓扑进行场映射。</td></tr><tr><td><code>-parallelSource</code></td><td>The source is decomposed</td></tr><tr><td><code>-parallelTarget</code></td><td>The target is decomposed Read decomposePar dictionary from specified location Specify the source region Specify the source time</td></tr><tr><td><code>-subtract</code></td><td>Subtract mapped source from target Read decomposePar dictionary from specified location Specify the target region</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-mapfieldsdict/">mapFieldsDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mapFields [OPTIONS] &lt;sourceCase&gt;
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
