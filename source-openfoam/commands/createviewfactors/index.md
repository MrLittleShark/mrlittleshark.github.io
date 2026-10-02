---
title: "createViewFactors · 按 viewFactorsDict 选择的模型计算辐射视角因子"
layout: reference
description: "按 viewFactorsDict 选择的模型计算辐射视角因子。"
cms_slug: "command-createviewfactors"
---

<p>按 viewFactorsDict 选择的模型计算辐射视角因子。</p><h2>开始前</h2>
<p>已有辐射边界、constant/viewFactorsDict，以及所选模型需要的面聚合或几何输入。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算默认区域视角因子</h2>
<pre><code class="language-bash">createViewFactors
</code></pre>
<p>从constant/viewFactorsDict创建视角因子模型并执行计算，输出后续辐射模型所需数据。</p>
<h2>示例 2：为辐射区域单独计算</h2>
<pre><code class="language-bash">createViewFactors -region enclosure
</code></pre>
<p>enclosure区域已有完整辐射设置；只处理该封闭腔体的表面关系。</p>
<h2>示例 3：先生成粗面映射</h2>
<pre><code class="language-bash">faceAgglomerate
createViewFactors
</code></pre>
<p>使用依赖面聚合的模型时，先生成fine-to-coarse映射，再计算粗面之间的视角因子，降低计算量。</p>
<h2>示例 4：在并行分区上计算</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 createViewFactors -parallel
</code></pre>
<p>decomposeParDict已设置4分区；在对应分区几何上计算视角因子，输出与并行布局配套的数据。</p>
<h2>示例 5：几何修改后重新生成</h2>
<pre><code class="language-bash">blockMesh -case ./enclosure-wide
faceAgglomerate -case ./enclosure-wide
createViewFactors -case ./enclosure-wide
</code></pre>
<p>enclosure-wide是改变腔体宽度后的独立案例；重建网格、聚合和因子，使结果反映新的可见关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createViewFactors [OPTIONS]
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

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createViewFactors/createViewFactors/createViewFactors.C">源码与说明</a> · <a href="/assets/command-help/createviewfactors.txt">帮助文本</a></p>
