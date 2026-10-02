---
title: "foamFormatConvert · 按 controlDict 写出设置转换现有场和网格文件格式"
layout: reference
description: "按 controlDict 写出设置转换现有场和网格文件格式。"
cms_slug: "command-foamformatconvert"
---

<p>按 controlDict 写出设置转换现有场和网格文件格式。</p><h2>开始前</h2>
<p>已有结果；目标格式、精度与压缩由controlDict中的writeFormat、writePrecision、writeCompression决定，文件会重写。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：把最新结果转成ASCII</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set ascii
foamFormatConvert -latestTime
</code></pre>
<p>修改目标写格式后转换最新状态，便于直接查看字段数值。</p>
<h2>示例 2：把一段结果转成二进制</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set binary
foamFormatConvert -time '1:2' -noConstant
</code></pre>
<p>将1至2秒结果改为二进制并跳过constant，适合减小场文件体积和读写时间。</p>
<h2>示例 3：提高文本输出精度</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set ascii
foamDictionary system/controlDict -entry writePrecision -set 12
foamFormatConvert -latestTime
</code></pre>
<p>以12位精度重写当前可读数据；输出精度提高，已有低精度文件丢失的数值位数仍无法补回。</p>
<h2>示例 4：只转换流体区域</h2>
<pre><code class="language-bash">foamFormatConvert -region fluid -latestTime
</code></pre>
<p>用当前controlDict写出设置处理fluid最新文件，保持其他区域原格式。</p>
<h2>示例 5：转换并行结果格式</h2>
<pre><code class="language-bash">mpirun -np 4 foamFormatConvert -parallel -latestTime
</code></pre>
<p>已有4分区，分别重写各processor的最新场，适合直接改变并行重启数据格式。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noConstant</code></td><td>Exclude the &#x27;constant/&#x27; dir in the times list Do not execute function objects</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamFormatConvert [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
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
  -noConstant       Exclude the &#x27;constant/&#x27; dir in the times list
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

Converts all IOobjects associated with a case into the format specified in the
controlDict

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamFormatConvert/foamFormatConvert.C">源码与说明</a> · <a href="/assets/command-help/foamformatconvert.txt">帮助文本</a></p>
