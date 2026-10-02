---
title: "chemkinToFoam · 把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典"
layout: reference
description: "把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典。"
cms_slug: "command-chemkintofoam"
---

<p>把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典。</p><h2>开始前</h2>
<p>准备同一机理对应的CHEMKIN反应文件、热力学文件和输运文件；五个位置参数最后两项是输出化学与热物性字典。</p>
<h2>示例 1：转换一套完整机理</h2>
<pre><code class="language-bash">chemkinToFoam chem.inp therm.dat tran.dat reactions thermodynamics
</code></pre>
<p>前三个文件提供反应、JANAF热物性和输运信息，结果写为reactions与thermodynamics。</p>
<h2>示例 2：直接放入案例constant目录</h2>
<pre><code class="language-bash">mkdir -p constant
chemkinToFoam mechanism/chem.inp mechanism/therm.dat mechanism/tran.dat constant/reactions constant/thermo.compressibleGas
</code></pre>
<p>集中从mechanism读取输入，生成案例中可引用的两个字典；thermophysicalProperties应指向相应文件。</p>
<h2>示例 3：读取新版热力学格式</h2>
<pre><code class="language-bash">chemkinToFoam -newFormat chem.inp therm-new.dat tran.dat reactions-new thermodynamics-new
</code></pre>
<p>热力学文件采用该解析器支持的newFormat时启用选项，输出使用不同文件名便于比较。</p>
<h2>示例 4：转换后检查物种清单</h2>
<pre><code class="language-bash">chemkinToFoam chem.inp therm.dat tran.dat constant/reactions constant/thermo.compressibleGas
foamDictionary constant/reactions -entry species -value
</code></pre>
<p>列出转换后注册的物种，核对后续组分初始场的名称、大小写和机理中的物种是否一致。</p>
<h2>示例 5：比较简化机理与详细机理</h2>
<pre><code class="language-bash">mkdir -p converted/detailed converted/reduced
chemkinToFoam detailed/chem.inp detailed/therm.dat detailed/tran.dat converted/detailed/reactions converted/detailed/thermo
chemkinToFoam reduced/chem.inp reduced/therm.dat reduced/tran.dat converted/reduced/reactions converted/reduced/thermo
</code></pre>
<p>两套机理各用自身配套热物性、输运文件，输出分开保存，再比较物种数、反应数和目标工况的计算成本。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-newFormat</code></td><td>Read Chemkin thermo file in new format</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: chemkinToFoam [OPTIONS] &lt;CHEMKINFile&gt; &lt;CHEMKINThermodynamicsFile&gt; &lt;CHEMKINTransport&gt; &lt;FOAMChemistryFile&gt; &lt;FOAMThermodynamicsFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -newFormat        Read Chemkin thermo file in new format
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert CHEMKINIII thermodynamics and reaction data files into OpenFOAM format.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/chemkinToFoam/chemkinToFoam.C">源码与说明</a> · <a href="/assets/command-help/chemkintofoam.txt">帮助文本</a></p>
