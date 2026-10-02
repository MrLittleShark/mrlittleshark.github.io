---
title: "boundaryFoam · 用于入口条件的一维湍流边界层"
layout: reference
description: "用于入口条件的一维湍流边界层。"
cms_slug: "command-boundaryfoam"
---

<p>用于入口条件的一维湍流边界层。</p><h2>开始前</h2>
<p>在已准备好一维网格、<code>U</code>、湍流量和 <code>constant/transportProperties</code> 的算例 <code>baseCase</code> 中学习。该求解器按指定平均速度迭代建立充分发展剖面；结果通过图线文件输出。新实验分别放入尚未存在的目录。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算一维速度与湍流剖面</h2>
<pre><code class="language-bash">boundaryFoam -case baseCase &gt; baseCase/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>程序以给定平均速度 <code>Ubar</code> 为目标，逐步修正驱动压力梯度，并在写出时刻生成剖面文件。日志中的 <code>pressure gradient</code> 给出维持该流量所需的压力梯度。</p>
<h2>示例 2：每十次迭代输出剖面</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry writeControl -set timeStep
foamDictionary baseCase/system/controlDict -entry writeInterval -set 10
boundaryFoam -case baseCase
</code></pre>
<p>将写出频率改成每 10 次迭代，可比较速度剖面如何趋于稳定。<code>deltaT</code> 沿用官方一维稳态教程中的迭代设置。</p>
<h2>示例 3：输出更高精度的文本剖面</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry writePrecision -set 10
foamDictionary baseCase/system/controlDict -entry graphFormat -set raw
boundaryFoam -case baseCase
</code></pre>
<p><code>raw</code> 保存便于绘图软件读取的坐标与场值列；<code>writePrecision 10</code> 保留更多有效数字。适合将入口剖面导入另一算例或比较两组结果。</p>
<h2>示例 4：增加迭代以比较剖面稳定性</h2>
<pre><code class="language-bash">foamCloneCase baseCase longer-study
foamDictionary longer-study/system/controlDict -entry startFrom -set startTime
foamDictionary longer-study/system/controlDict -entry endTime -set 2000
boundaryFoam -case longer-study &gt; longer-study/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>这个例子适用于原设置 <code>deltaT 1</code>、<code>endTime 1000</code> 的一维教程。把迭代上限增加到 2000，再比较最后两次输出的速度、湍流量和压力梯度。</p>
<h2>示例 5：改变目标平均速度</h2>
<pre><code class="language-bash">foamCloneCase baseCase faster-study
foamDictionary faster-study/constant/transportProperties -entry Ubar -set "[0 1 -1 0 0 0 0] (20 0 0)"
boundaryFoam -case faster-study &gt; faster-study/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>本例用于沿 x 方向流动、原平均速度低于 20 m/s 的教程。<code>Ubar</code> 是带量纲的目标平均速度。改变它后，比较壁面剪切、湍流剖面和日志中驱动压力梯度的变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step</td></tr><tr><td><code>-dry-run-write</code></td><td>Check case set-up and write only using a single time step Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-listFvOptions</code></td><td>List fvOptions List switches registered for run-time modification (see -listUnsetSwitches option)</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel">incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/boundaryFoam/steadyBoundaryLayer/setups.orig/common">incompressible/boundaryFoam/steadyBoundaryLayer/setups.orig/common</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel&quot; boundaryFoam-study
cd boundaryFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: boundaryFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dry-run          Check case set-up only using a single time step
  -dry-run-write    Check case set-up and write only using a single time step
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -listFunctionObjects
                    List functionObjects
  -listFvOptions    List fvOptions
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
  -listTurbulenceModels
                    List turbulenceModels
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Steady-state solver for incompressible, 1D turbulent flow, typically to
generate boundary layer conditions at an inlet.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/incompressible/boundaryFoam/boundaryFoam.C">源码与说明</a> · <a href="/assets/command-help/boundaryfoam.txt">帮助文本</a></p>
