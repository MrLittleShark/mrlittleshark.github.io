---
title: "setExprBoundaryFields · 用表达式设置边界场的数值或条目"
layout: reference
description: "用表达式设置边界场的数值或条目。"
cms_slug: "command-setexprboundaryfields"
---

<p>用表达式设置边界场的数值或条目。</p><h2>开始前</h2>
<p>已有场和system/setExprBoundaryFieldsDict；字典明确字段、边界、表达式及所需引用场。</p>
<h2>示例 1：先计算表达式预览</h2>
<pre><code class="language-bash">setExprBoundaryFields -dry-run -time 0
</code></pre>
<p>求值并检查字段、patch和表达式，保留原场，适合先定位字段名或表达式问题。</p>
<h2>示例 2：写入初始边界值</h2>
<pre><code class="language-bash">setExprBoundaryFields -time 0
</code></pre>
<p>按默认字典更新0时刻边界，适合空间变化的入口温度或速度分布。</p>
<h2>示例 3：保留被替换子条目</h2>
<pre><code class="language-bash">setExprBoundaryFields -backup -time 0
</code></pre>
<p>写新设置时把原子条目保留为.backup，便于比较表达式施加前后的边界内容。</p>
<h2>示例 4：预加载引用场</h2>
<pre><code class="language-bash">setExprBoundaryFields -load-fields '(U T)' -dict system/setExprBoundaryFields-inletDict -time 0
</code></pre>
<p>表达式引用U、T时先加载它们，按入口专用字典生成耦合分布。</p>
<h2>示例 5：批量处理一段时间</h2>
<pre><code class="language-bash">setExprBoundaryFields -time '0.1:0.5' -ascii
</code></pre>
<p>对已有时间区间逐次求值，并强制ASCII写出，方便检查每个时刻边界值的变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>Write in ASCII format instead of the controlDict setting</td></tr><tr><td><code>-backup</code></td><td>Preserve sub-entry as .backup</td></tr><tr><td><code>-cache-fields</code></td><td>Cache fields between calls</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Evaluate but do not write Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: setExprBoundaryFields [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of the controlDict setting
  -backup           Preserve sub-entry as .backup
  -cache-fields     Cache fields between calls
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for setExprBoundaryFieldsDict
  -dry-run          Evaluate but do not write
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
  -load-fields &lt;wordList&gt;
                    Specify field or fields to preload. Eg, &#x27;T&#x27; or &#x27;(p T U)&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
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
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprBoundaryFields/setExprBoundaryFields.C">源码与说明</a> · <a href="/assets/command-help/setexprboundaryfields.txt">帮助文本</a></p>
