---
title: "snappyHexMesh · 细化背景网格，贴合几何表面，并按设置生成边界层"
layout: reference
description: "细化背景网格，贴合几何表面，并按设置生成边界层。"
cms_slug: "command-snappyhexmesh"
---

<p>细化背景网格，贴合几何表面，并按设置生成边界层。</p><h2>开始前</h2>
<p>先有blockMesh背景网格、snappyHexMeshDict和表面几何。每个网格方案在独立副本生成。</p>
<h2>示例 1：检查几何输入</h2>
<pre><code class="language-bash">snappyHexMesh -checkGeometry
</code></pre>
<p>检查字典引用的几何与区域，先定位表面缺陷和尺寸问题。</p>
<h2>示例 2：检查算例设置</h2>
<pre><code class="language-bash">snappyHexMesh -dry-run
</code></pre>
<p>执行简化设置检查流程，便于发现缺失几何、字典条目和不合理选择。</p>
<h2>示例 3：生成贴体网格</h2>
<pre><code class="language-bash">snappyHexMesh
</code></pre>
<p>执行字典启用的细化、贴合、层生成阶段，默认保留各阶段对应的网格输出。</p>
<h2>示例 4：使用另一套控制</h2>
<pre><code class="language-bash">snappyHexMesh -dict system/snappyHexMeshDict.fine
</code></pre>
<p>已准备fine字典时选择它，比较表面细化等级、间隙分辨率和边界层厚度。</p>
<h2>示例 5：并行生成并检查</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 snappyHexMesh -parallel
mpirun -np 4 checkMesh -parallel -latestTime
</code></pre>
<p>decomposeParDict的numberOfSubdomains设为4；在各分区生成最新网格，再检查并行网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkGeometry</code></td><td>Check all surface geometry for quality Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Check case set-up only using a single time step Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-outFile &lt;file&gt;</code></td><td>Name of the file to save the simplified surface to</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-profiling</code></td><td>Activate application-level profiling</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-snappyhexmeshdict/">snappyHexMeshDict</a> · <a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/cylinder">mesh/refineMesh/cylinder</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/flange">mesh/snappyHexMesh/flange</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/insidePoints">mesh/snappyHexMesh/insidePoints</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/gap_detection">mesh/snappyHexMesh/gap_detection</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/rotated_block">mesh/snappyHexMesh/rotated_block</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: snappyHexMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkGeometry    Check all surface geometry for quality
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative snappyHexMeshDict
  -dry-run          Check case set-up only using a single time step
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -outFile &lt;file&gt;   Name of the file to save the simplified surface to
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -patches &lt;(patch0 .. patchN)&gt;
                    Only triangulate selected patches (wildcards supported)
  -profiling        Activate application-level profiling
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -surfaceSimplify &lt;boundBox&gt;
                    Simplify the surface using snappyHexMesh starting from a
                    boundBox
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Automatic split hex mesher. Refines and snaps to surface

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/snappyHexMesh/snappyHexMesh.C">源码与说明</a> · <a href="/assets/command-help/snappyhexmesh.txt">帮助文本</a></p>
