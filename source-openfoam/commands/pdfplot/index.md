---
title: "pdfPlot · 对选定概率分布随机采样并输出直方图数据"
layout: reference
description: "对选定概率分布随机采样并输出直方图数据。"
cms_slug: "command-pdfplot"
---

<p>对选定概率分布随机采样并输出直方图数据。</p><h2>开始前</h2>
<p>已有最小OpenFOAM案例及constant/pdfDict；nSamples为抽样数，nIntervals为分箱数，writeData控制是否保存原始样本。</p>
<h2>示例 1：生成均匀分布样本</h2>
<pre><code class="language-bash">cat &gt; constant/pdfDict &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object pdfDict; }
type uniform;
uniformDistribution { minValue 1e-5; maxValue 5e-5; }
nSamples 10000;
nIntervals 40;
writeData false;
EOF
pdfPlot
</code></pre>
<p>在10至50微米数值范围内抽样10000次，写pdf目录下的分箱计数图数据。该输出是计数，归一化后才是概率密度。</p>
<h2>示例 2：增加样本数量</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry nSamples -set 100000
pdfPlot
</code></pre>
<p>分箱不变时增加到10万次抽样，比较随机起伏随样本数的降低趋势。</p>
<h2>示例 3：提高分箱分辨率</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry nIntervals -set 100
pdfPlot
</code></pre>
<p>将区间细分为100箱，能显示更细的分布形状，同时每箱样本数减少。</p>
<h2>示例 4：保存每个随机样本</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry writeData -set true
pdfPlot
</code></pre>
<p>额外写pdf/uniform.data，便于自行计算均值、方差或制作归一化概率密度图。</p>
<h2>示例 5：扩大分布范围</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry uniformDistribution/maxValue -set 1e-4
pdfPlot
</code></pre>
<p>上界改为100微米，重新采样并比较均值和宽度，适合检查粒径分布参数。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: pdfPlot [OPTIONS]
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

Generate a graph of a probability distribution function

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/pdfPlot/pdfPlot.C">源码与说明</a> · <a href="/assets/command-help/pdfplot.txt">帮助文本</a></p>
