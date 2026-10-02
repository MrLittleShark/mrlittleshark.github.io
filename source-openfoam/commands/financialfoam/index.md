---
title: "financialFoam · Black–Scholes 金融定价方程"
layout: reference
description: "Black–Scholes 金融定价方程。"
cms_slug: "command-financialfoam"
---

<p>Black–Scholes 金融定价方程。</p><h2>开始前</h2>
<p>使用欧洲看涨期权算例 <code>baseCase</code>。<code>financialFoam</code> 用网格横坐标表示标的价格，读取 <code>constant/financialProperties</code> 中的执行价、利率和波动率，初始化到期收益后求解 Black–Scholes 方程。以下各组从同一输入独立计算。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算期权价值曲线</h2>
<pre><code class="language-bash">financialFoam -case baseCase &gt; baseCase/log.financialFoam 2&gt;&amp;1
</code></pre>
<p>结果 <code>V</code> 是期权价值，<code>delta</code> 是价值相对标的价格的导数。写出时刻还生成图线数据，便于比较不同剩余期限下的价格曲线。</p>
<h2>示例 2：改变执行价格</h2>
<pre><code class="language-bash">foamCloneCase baseCase strike-study
foamDictionary strike-study/constant/financialProperties -entry strike -set "[0 1 0 0 0 0 0] 100"
financialFoam -case strike-study
</code></pre>
<p>把执行价设为 100。此模型借用网格的长度维度表示价格，因此输入保留源码要求的量纲形式。网格的标的价格范围应覆盖执行价及其两侧，再观察收益曲线拐点如何移动。</p>
<h2>示例 3：改变无风险利率</h2>
<pre><code class="language-bash">foamCloneCase baseCase rate-study
foamDictionary rate-study/constant/financialProperties -entry r -set "[0 0 -1 0 0 0 0] 0.05"
financialFoam -case rate-study
</code></pre>
<p>当算例时间单位为年时，0.05 表示年化利率 5%。保持执行价、波动率和期限一致，可单独比较利率对期权价值的影响。</p>
<h2>示例 4：改变波动率</h2>
<pre><code class="language-bash">foamCloneCase baseCase volatility-study
foamDictionary volatility-study/constant/financialProperties -entry sigma -set "[0 0 -0.5 0 0 0 0] 0.2"
financialFoam -case volatility-study
</code></pre>
<p>按年计时的模型中，0.2 对应年化波动率 20%。波动率进入扩散项，比较相同期限定价曲线，可以观察波动性对价值的影响。</p>
<h2>示例 5：批量比较三种波动率</h2>
<pre><code class="language-bash">for sigma in 0.1 0.2 0.3; do
    caseDir="sigma-${sigma}"
    foamCloneCase baseCase "$caseDir"
    foamDictionary "$caseDir/constant/financialProperties" -entry sigma \
        -set "[0 0 -0.5 0 0 0 0] $sigma"
    financialFoam -case "$caseDir" &gt; "$caseDir/log.financialFoam" 2&gt;&amp;1
done
</code></pre>
<p>三个新目录使用同一网格、执行价和利率，只改变波动率。在同一输出时刻比较 <code>V</code> 和 <code>delta</code>，就能把波动率变化与价格、敏感度的变化联系起来。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step</td></tr><tr><td><code>-dry-run-write</code></td><td>Check case set-up and write only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-listScalarBCs</code></td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td><code>-listVectorBCs</code></td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-postProcess</code></td><td>Execute functionObjects only Subprocess root directories for distributed running</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/financial/financialFoam/europeanCall">financial/financialFoam/europeanCall</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/financial/financialFoam/europeanCall&quot; financialFoam-study
cd financialFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: financialFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Check case set-up only using a single time step
  -dry-run-write    Check case set-up and write only using a single time step
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

Solves the Black-Scholes equation to price commodities.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/financial/financialFoam/financialFoam.C">源码与说明</a> · <a href="/assets/command-help/financialfoam.txt">帮助文本</a></p>
