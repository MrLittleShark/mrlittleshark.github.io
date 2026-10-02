---
title: "foamToGMV · 按 conversionProperties 导出六面体网格和字段为 GMV"
layout: reference
description: "按 conversionProperties 导出六面体网格和字段为 GMV。"
cms_slug: "command-foamtogmv"
---

<p>按 conversionProperties 导出六面体网格和字段为 GMV。</p><h2>开始前</h2>
<p>网格采用hex单元，constant/conversionProperties定义startTime、vector、format、cells；该旧式工具从字典而非时间CLI选择起始范围。</p>
<h2>示例 1：创建最小转换配置</h2>
<pre><code class="language-bash">cat &gt; constant/conversionProperties &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object conversionProperties; }
startTime -1;
vector U;
format ascii;
cells hex;
EOF
foamToGMV
</code></pre>
<p>写入完整转换字典；导出晚于-1的数值时间，U作为GMV速度，结果命名为plotGMV.*。</p>
<h2>示例 2：只处理较晚结果</h2>
<pre><code class="language-bash">foamDictionary constant/conversionProperties -entry startTime -set 1
foamToGMV
</code></pre>
<p>工具只转换严格晚于1的时间，适合跳过初始发展阶段。</p>
<h2>示例 3：把平均速度作为GMV速度</h2>
<pre><code class="language-bash">foamDictionary constant/conversionProperties -entry vector -set UMean
foamToGMV
</code></pre>
<p>结果中已有UMean时，将它作为GMV的velocity数据，便于查看统计平均流场。</p>
<h2>示例 4：导出生成的旋流场</h2>
<pre><code class="language-bash">engineSwirl
foamToGMV
</code></pre>
<p>发动机案例使用hex网格、vector为U且转换起始范围包含该场时，先生成初始旋流，再导出供GMV检查。</p>
<h2>示例 5：检查ASCII文件结构</h2>
<pre><code class="language-bash">foamToGMV
head -n 8 plotGMV.1
</code></pre>
<p>转换后查看首个实际生成文件的头部；如编号不同，使用日志中的文件名。应能看到gmvinput和nodes等记录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToGMV [OPTIONS]
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
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Translate OpenFOAM output to GMV readable files

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToGMV/foamToGMV.C">源码与说明</a> · <a href="/assets/command-help/foamtogmv.txt">帮助文本</a></p>
