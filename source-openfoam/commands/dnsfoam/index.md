---
title: "dnsFoam · 各向同性湍流盒中的直接数值模拟"
layout: reference
description: "各向同性湍流盒中的直接数值模拟。"
cms_slug: "command-dnsfoam"
---

<p>各向同性湍流盒中的直接数值模拟。</p><h2>开始前</h2>
<p>以下示例使用已完成网格和初始场准备的官方 boxTurb16 案例，目录记为 baseCase。其规则周期网格用于各向同性湍流盒，初始时间为 0，原时间步为 0.025，运动黏度为 0.025。每项对照从同一份初始数据开始，使用尚未存在的新目录。配套输入见<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16">官方 boxTurb16 算例</a>。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：运行湍流盒基准计算</h2>
<pre><code class="language-bash">dnsFoam -case baseCase &gt; baseCase/log.dnsFoam 2&gt;&amp;1
tail -n 30 baseCase/log.dnsFoam
</code></pre>
<p>按 controlDict 设置推进速度和压力，并在指定波数范围施加随机驱动力。官方设置从 0 计算到 10，步长 0.025，每 0.25 保存结果。查看日志中的 Number of forced K、速度与压力求解信息以及动能等统计量。</p>
<h2>示例 2：缩短计算区间检查初始演化</h2>
<pre><code class="language-bash">foamCloneCase baseCase short-study
foamDictionary short-study/system/controlDict -entry startFrom -set startTime
foamDictionary short-study/system/controlDict -entry startTime -set 0
foamDictionary short-study/system/controlDict -entry stopAt -set endTime
foamDictionary short-study/system/controlDict -entry endTime -set 1
dnsFoam -case short-study &gt; short-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>保持官方步长 0.025，将结束时刻设为 1，共推进 40 步。先观察速度场和能量统计的初始变化，适合检查周期边界、初始场以及驱动力设置。新目录保留完整输入，便于与基准结果比较。</p>
<h2>示例 3：减半时间步比较统计结果</h2>
<pre><code class="language-bash">foamCloneCase baseCase half-step-study
foamDictionary half-step-study/system/controlDict -entry startFrom -set startTime
foamDictionary half-step-study/system/controlDict -entry startTime -set 0
foamDictionary half-step-study/system/controlDict -entry deltaT -set 0.0125
foamDictionary half-step-study/system/controlDict -entry writeControl -set runTime
foamDictionary half-step-study/system/controlDict -entry writeInterval -set 0.25
dnsFoam -case half-step-study &gt; half-step-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>把时间步由 0.025 减为 0.0125，保留结束时刻，并保持每 0.25 输出一次。随机驱动的增量随时间步变化，适合比较动能均值、波动幅度和能谱等统计量；统计区间和采样长度也应保持一致。</p>
<h2>示例 4：增大黏度观察耗散变化</h2>
<pre><code class="language-bash">foamCloneCase baseCase viscosity-study
foamDictionary viscosity-study/system/controlDict -entry startFrom -set startTime
foamDictionary viscosity-study/system/controlDict -entry startTime -set 0
foamDictionary viscosity-study/constant/transportProperties -entry nu -set 0.05
dnsFoam -case viscosity-study &gt; viscosity-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>nu 是运动黏度，量纲为 m²/s；0.05 是官方基准值 0.025 的两倍。其余参数保持相同，比较稳定统计区间的动能、耗散及高波数能谱，观察黏性增强后小尺度波动的变化。</p>
<h2>示例 5：减半随机驱动力的幅度参数</h2>
<pre><code class="language-bash">foamCloneCase baseCase forcing-study
foamDictionary forcing-study/system/controlDict -entry startFrom -set startTime
foamDictionary forcing-study/system/controlDict -entry startTime -set 0
foamDictionary forcing-study/constant/turbulenceProperties -entry UOsigma -set 0.0451475
dnsFoam -case forcing-study &gt; forcing-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>UOsigma 乘在 UO 随机过程的增量幅度上，这里取原值 0.090295 的一半。保持 UOalpha=0.81532 和波数范围 7&lt;|K|&lt;10，比较动能与能谱对驱动强度的响应。波数范围由 UOKlower、UOKupper 控制，可在下一组独立试验中改变，以研究驱动尺度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-postProcess</code></td><td>Execute functionObjects only Subprocess root directories for distributed running</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16">DNS/dnsFoam/boxTurb16</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/DNS/dnsFoam/boxTurb16&quot; dnsFoam-study
cd dnsFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: dnsFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
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
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -postProcess      Execute functionObjects only
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Direct numerical simulation for boxes of isotropic turbulence.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/DNS/dnsFoam/dnsFoam.C">源码与说明</a> · <a href="/assets/command-help/dnsfoam.txt">帮助文本</a></p>
