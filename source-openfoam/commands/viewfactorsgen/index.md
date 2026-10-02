---
title: "viewFactorsGen · 计算表面间辐射视角因子及分布映射"
layout: reference
description: "计算表面间辐射视角因子及分布映射。"
cms_slug: "command-viewfactorsgen"
---

<p>计算表面间辐射视角因子及分布映射。</p><h2>开始前</h2>
<p>已有constant/viewFactorsDict、辐射边界和需要的faceAgglomerate结果。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：生成辐射交换数据</h2>
<pre><code class="language-bash">viewFactorsGen
</code></pre>
<p>按网格表面可见关系计算视角因子，写出后续viewFactor辐射模型需要的矩阵和映射数据。</p>
<h2>示例 2：写出视角因子矩阵诊断</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry writeViewFactorMatrix -set true
viewFactorsGen
</code></pre>
<p>开启矩阵输出选项，便于检查表面对之间的交换比例和结果分布。</p>
<h2>示例 3：导出可见射线</h2>
<pre><code class="language-bash">foamDictionary constant/viewFactorsDict -entry dumpRays -set true
viewFactorsGen
</code></pre>
<p>额外生成allVisibleFaces.obj等可见性诊断，适合检查遮挡与表面朝向。</p>
<h2>示例 4：针对命名区域计算</h2>
<pre><code class="language-bash">faceAgglomerate -region enclosure
viewFactorsGen -region enclosure
</code></pre>
<p>为enclosure生成聚合映射后计算其视角因子，适合多区域中的辐射腔体。</p>
<h2>示例 5：并行生成</h2>
<pre><code class="language-bash">mpirun -np 4 faceAgglomerate -parallel
mpirun -np 4 viewFactorsGen -parallel
</code></pre>
<p>网格已有4分区且viewFactorsDict一致；先聚合再计算，输出与各分区对应的交换数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: viewFactorsGen [OPTIONS]
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Calculate view factors from face agglomeration array. The finalAgglom generated
by faceAgglomerate utility.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/viewFactorsGen/viewFactorsGen.C">源码与说明</a> · <a href="/assets/command-help/viewfactorsgen.txt">帮助文本</a></p>
