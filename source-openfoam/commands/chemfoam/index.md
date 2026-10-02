---
title: "chemFoam · 单单元化学反应积分"
layout: reference
description: "单单元化学反应积分。"
cms_slug: "command-chemfoam"
---

<p>单单元化学反应积分。</p><h2>用法</h2><pre><code class="language-bash">chemFoam -help-full</code></pre><h2>运行计算</h2><pre><code class="language-bash">chemFoam &gt; log.chemFoam 2&gt;&amp;1
tail -n 20 log.chemFoam</code></pre><p>在已经准备好网格、物性和初始场的算例目录运行。第一行把终端输出保存到日志，计算结束后，第二行显示日志最后 20 行。计算结果按 controlDict 的设置写入时间目录。</p><h2>指定算例目录</h2><pre><code class="language-bash">chemFoam -help-full -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-listScalarBCs</td><td>List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)</td></tr><tr><td>-listVectorBCs</td><td>List vector field boundary conditions (fvPatchField&lt;vector&gt;)</td></tr><tr><td>-postProcess</td><td>Execute functionObjects only</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/h2">combustion/chemFoam/h2</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/gri">combustion/chemFoam/gri</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18">combustion/chemFoam/ic8h18</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/nc7h16">combustion/chemFoam/nc7h16</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18_TDAC">combustion/chemFoam/ic8h18_TDAC</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
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
