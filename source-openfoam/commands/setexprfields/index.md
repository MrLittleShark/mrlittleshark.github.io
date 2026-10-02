---
title: "setExprFields · 用数学表达式创建或修改单元场"
layout: reference
description: "用数学表达式创建或修改单元场。"
cms_slug: "command-setexprfields"
---

<p>用数学表达式创建或修改单元场。</p><h2>开始前</h2>
<p>已有网格；修改模式要求目标场存在，创建模式需指定字段名、表达式和合适量纲。</p>
<h2>示例 1：把已有标量场设为常数</h2>
<pre><code class="language-bash">setExprFields -field T -expression '300' -time 0
</code></pre>
<p>T已存在时，将选中场值设为300；应按T的物理单位解释，温度场通常以K填写。</p>
<h2>示例 2：创建无量纲标记场</h2>
<pre><code class="language-bash">setExprFields -create -field marker -dimensions '[0 0 0 0 0 0 0]' -expression '1' -time 0
</code></pre>
<p>生成新的无量纲场marker，内部赋值1，可用作区域标记或后续表达式输入。</p>
<h2>示例 3：由速度计算单位质量动能</h2>
<pre><code class="language-bash">setExprFields -create -field kineticEnergy -dimensions '[0 2 -2 0 0 0 0]' -load-fields '(U)' -expression '0.5*magSqr(U)' -time 0
</code></pre>
<p>读取U，创建单位质量动能场，量纲为平方米每二次方秒；便于观察速度非均匀性。</p>
<h2>示例 4：保留边界只改内部温度</h2>
<pre><code class="language-bash">setExprFields -field T -expression '350' -keepPatches -time 0
</code></pre>
<p>内部T改为350，-keepPatches保留已有边界设置，适合调整初始温度而继续使用原边界条件。</p>
<h2>示例 5：先检查字典中的多场表达式</h2>
<pre><code class="language-bash">setExprFields -dict system/setExprFields-initialDict -dry-run -time 0
setExprFields -dict system/setExprFields-initialDict -time 0
</code></pre>
<p>字典已配置多项场表达式时，先求值检查，再正式写入，适合同时构造速度、标量或几何指示场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>Write in ASCII format instead of the controlDict setting</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-create</code></td><td>Create a new field (command-line operation)</td></tr><tr><td><code>-debug-parser</code></td><td>Additional debugging information Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Evaluate but do not write</td></tr><tr><td><code>-dummy-phi</code></td><td>Provide a zero phi field (command-line operation) The expression to evaluate (command-line operation)</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>The field to create/overwrite (command-line operation) The field mask (logical condition) when to apply the expression (command-line operation) Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-keepPatches</code></td><td>Leave patches unaltered (command-line operation)</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-setexprfieldsdict/">setExprFieldsDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setExprFields [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of the controlDict setting
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -create           Create a new field (command-line operation)
  -debug-parser     Additional debugging information
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for setExprFieldsDict
  -dimensions &lt;dims&gt;
                    The dimensions for created fields (command-line operation)
  -dry-run          Evaluate but do not write
  -dummy-phi        Provide a zero phi field (command-line operation)
  -expression &lt;expr&gt;
                    The expression to evaluate (command-line operation)
  -field &lt;name&gt;     The field to create/overwrite (command-line operation)
  -field-mask &lt;logic&gt;
                    The field mask (logical condition) when to apply the
                    expression (command-line operation)
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keepPatches      Leave patches unaltered (command-line operation)
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -load-fields &lt;wordList&gt;
                    Specify field or fields to preload. Eg, &#x27;T&#x27; or &#x27;(p T U)&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-variable-cache
                    Disable caching of expression variables
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -value-patches &lt;(patches)&gt;
                    A list of patches that receive a fixed value (command-line
                    operation)
  -verbose          Additional verbosity
  -withFunctionObjects
                    Execute functionObjects
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/setExprFields.C">源码与说明</a> · <a href="/assets/command-help/setexprfields.txt">帮助文本</a></p>
