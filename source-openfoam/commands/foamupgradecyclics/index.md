---
title: "foamUpgradeCyclics · 用于迁移旧版算例"
layout: reference
description: "用于迁移旧版算例。"
cms_slug: "command-foamupgradecyclics"
---

<p>用于迁移旧版算例。</p><h2>开始前</h2>
<p>用于迁移采用旧式未拆分 cyclic 的网格与场。先对独立副本预览，再选择需转换的时间和区域。</p>
<h2>示例 1：预览需要转换的内容</h2>
<pre><code class="language-bash">foamUpgradeCyclics -dry-run
</code></pre>
<p>扫描当前算例并报告转换操作，保持文件原样，可先确认受影响边界。</p>
<h2>示例 2：转换初始网格与场</h2>
<pre><code class="language-bash">foamUpgradeCyclics -constant -time 0
</code></pre>
<p>在副本中处理 constant 网格与0时刻场，使周期边界拆分关系同步更新。</p>
<h2>示例 3：只更新最新结果</h2>
<pre><code class="language-bash">foamUpgradeCyclics -latestTime
</code></pre>
<p>已有较多时间目录时选择最大数值时间目录，更新其周期边界字段。</p>
<h2>示例 4：指定区域迁移</h2>
<pre><code class="language-bash">foamUpgradeCyclics -region air -time 0
</code></pre>
<p>处理多区域算例中的 air 网格和初场；其他区域按各自周期配置分别检查。</p>
<h2>示例 5：处理含指令的字典</h2>
<pre><code class="language-bash">foamUpgradeCyclics -enableFunctionEntries -time '0:0.5'
</code></pre>
<p>允许展开可信算例中的 include 等指令，并选择0至0.5范围的时间；转换后对照展开后的边界名称。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dry-run</code></td><td>Test only do not change any files Enable expansion of dictionary directives - #include, #codeStream etc Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamUpgradeCyclics [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test only do not change any files
  -enableFunctionEntries
                    Enable expansion of dictionary directives - #include,
                    #codeStream etc
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Tool to upgrade mesh and fields for split cyclics

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/foamUpgradeCyclics/foamUpgradeCyclics.C">源码与说明</a> · <a href="/assets/command-help/foamupgradecyclics.txt">帮助文本</a></p>
