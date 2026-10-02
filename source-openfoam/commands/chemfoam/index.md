---
title: "chemFoam · 单单元化学反应积分"
layout: reference
description: "单单元化学反应积分。"
cms_slug: "command-chemfoam"
---

<p>单单元化学反应积分。</p><h2>开始前</h2>
<p>使用已经建立单单元网格、反应机理、热物性和 <code>constant/initialConditions</code> 的化学算例 <code>baseCase</code>。以下温度和压力实验从各自的初始条件重新开始，保持同一反应机理与组成。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算单单元反应过程</h2>
<pre><code class="language-bash">chemFoam -case baseCase &gt; baseCase/log.chemFoam 2&gt;&amp;1
head -n 6 baseCase/chemFoam.out
</code></pre>
<p>程序积分反应过程，<code>chemFoam.out</code> 前三列为时间、温度 K 和压力 Pa。用这三列可以绘制点火升温及压力变化曲线。</p>
<h2>示例 2：延长反应观察时间</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry endTime -set 0.1
chemFoam -case baseCase
</code></pre>
<p>将计算结束时间设成 0.1 s，从 <code>initialConditions</code> 给定的初态重新积分。适用于原观察区间更短、需要查看后续升温或趋近平衡的案例。</p>
<h2>示例 3：提高初始温度</h2>
<pre><code class="language-bash">foamCloneCase baseCase hot-study
foamDictionary hot-study/constant/initialConditions -entry T -set 1200
chemFoam -case hot-study &gt; hot-study/log.chemFoam 2&gt;&amp;1
</code></pre>
<p>将初温设为 1200 K，其余压力、组成和机理保持一致。对适用温度范围内的同一混合物，比较两条温度曲线的点火延迟。</p>
<h2>示例 4：提高初始压力</h2>
<pre><code class="language-bash">foamCloneCase baseCase pressure-study
foamDictionary pressure-study/constant/initialConditions -entry p -set 200000
chemFoam -case pressure-study &gt; pressure-study/log.chemFoam 2&gt;&amp;1
</code></pre>
<p><code>p</code> 的单位是 Pa，200000 Pa 为 2 bar。与基准算例比较时保留相同初温和组成，可单独观察压力对反应进程的影响。</p>
<h2>示例 5：进行初始温度扫描</h2>
<pre><code class="language-bash">for temperature in 1000 1100 1200; do
    caseDir="chem-${temperature}K"
    foamCloneCase baseCase "$caseDir"
    foamDictionary "$caseDir/constant/initialConditions" -entry T -set "$temperature"
    chemFoam -case "$caseDir" &gt; "$caseDir/log.chemFoam" 2&gt;&amp;1
done
</code></pre>
<p>循环创建三个独立算例，分别在 1000、1100、1200 K 下求解。每个目录各有一份 <code>chemFoam.out</code>，可把曲线画在同一坐标系，并按统一的温升或升温速率标准提取点火延迟。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-postProcess</code></td><td>Execute functionObjects only</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/h2">combustion/chemFoam/h2</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/gri">combustion/chemFoam/gri</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18">combustion/chemFoam/ic8h18</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/nc7h16">combustion/chemFoam/nc7h16</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18_TDAC">combustion/chemFoam/ic8h18_TDAC</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/combustion/chemFoam/h2&quot; chemFoam-study
cd chemFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: chemFoam [OPTIONS]
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
  -listFunctionObjects
                    List functionObjects
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
  -listUnsetSwitches
                    Modifies switch listing to display values not set in
                    etc/controlDict
  -listVectorBCs    List vector field boundary conditions (fvPatchField&lt;vector&gt;)
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -postProcess      Execute functionObjects only
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Solver for chemistry problems, designed for use on single cell cases to provide
comparison against other chemistry solvers

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/chemFoam/chemFoam.C">源码与说明</a> · <a href="/assets/command-help/chemfoam.txt">帮助文本</a></p>
