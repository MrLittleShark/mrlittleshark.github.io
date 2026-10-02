---
title: "mapFieldsPar · 在并行或串行布局间执行网格到网格场映射"
layout: reference
description: "在并行或串行布局间执行网格到网格场映射。"
cms_slug: "command-mapfieldspar"
---

<p>在并行或串行布局间执行网格到网格场映射。</p><h2>开始前</h2>
<p>源、目标网格及字段可读；MPI执行时目标分区与进程数一致，非一致边界映射规则已准备。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：按体积权重映射</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -mapMethod cellVolumeWeight
</code></pre>
<p>从源案例计算重叠体积权重，映射到当前目标；适合不同分辨率但空间重叠的网格。</p>
<h2>示例 2：只映射速度与压力</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -fields '(U p)' -sourceTime latestTime
</code></pre>
<p>限制字段为U、p，读取源最新时刻；其他目标字段保留原设置。</p>
<h2>示例 3：相同网格直接映射</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -consistent -mapMethod direct
</code></pre>
<p>源目标几何和边界一致且满足直接寻址条件时，采用direct方法传递字段。</p>
<h2>示例 4：选择边界面积加权</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -mapMethod cellVolumeWeight -patchMapMethod faceAreaWeight
</code></pre>
<p>内部按体积、边界按面积加权，适合面划分不同但边界相互覆盖的映射。</p>
<h2>示例 5：并行映射并保留欧拉场</h2>
<pre><code class="language-bash">mpirun -np 4 mapFieldsPar ../sourceCase -parallel -fields '(U p T)' -no-lagrangian
</code></pre>
<p>目标已有4分区；并行映射所选欧拉场，-no-lagrangian跳过粒子位置和粒子属性。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-consistent</code></td><td>按匹配的边界拓扑进行场映射。</td></tr><tr><td><code>-no-lagrangian</code></td><td>Skip mapping lagrangian positions and fields</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-subtract</code></td><td>Subtract mapped source from target Specify the target region</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-mapfieldsdict/">mapFieldsDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mapFieldsPar [OPTIONS] &lt;sourceCase&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -consistent       Source and target geometry and boundary conditions identical
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to reconstruct (all by
                    default). Eg, &#x27;T&#x27; or &#x27;(p T U &quot;alpha.*&quot;)&#x27;
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
  -mapMethod &lt;word&gt;
                    Specify the mapping method
                    (direct|mapNearest|cellVolumeWeight|
                    correctedCellVolumeWeight)
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-lagrangian    Skip mapping lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -patchMapMethod &lt;word&gt;
                    Specify the patch mapping method
                    (direct|mapNearest|faceAreaWeight)
  -procMapMethod &lt;word&gt;
                    Specify the processor distribution map method (AABB|LOD)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -sourceRegion &lt;word&gt;
                    Specify the source region
  -sourceTime &lt;scalar|&#x27;latestTime&#x27;&gt;
                    Specify the source time
  -subtract         Subtract mapped source from target
  -targetRegion &lt;word&gt;
                    Specify the target region
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Map volume fields from one mesh to another

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mapFieldsPar/mapLagrangian.C">源码与说明</a> · <a href="/assets/command-help/mapfieldspar.txt">帮助文本</a></p>
