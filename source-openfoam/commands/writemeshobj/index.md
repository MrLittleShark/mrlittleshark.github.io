---
title: "writeMeshObj · -cell、-face、-point 和 -cellSet 等选项指定诊断对象"
layout: reference
description: "-cell、-face、-point 和 -cellSet 等选项指定诊断对象。"
cms_slug: "command-writemeshobj"
---

<p>-cell、-face、-point 和 -cellSet 等选项指定诊断对象。</p><h2>用法</h2><pre><code class="language-bash">writeMeshObj -cell 10</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">writeMeshObj -cell 10 -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cell &lt;cellId&gt;</td><td>Write points for the specified cell</td></tr><tr><td>-cellSet &lt;name&gt;</td><td>Write points for specified cellSet</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-face &lt;faceId&gt;</td><td>Write specified face</td></tr><tr><td>-faceSet &lt;name&gt;</td><td>Write points for specified faceSet Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-patchEdges</td><td>Write patch boundary edges</td></tr><tr><td>-patchFaces</td><td>Write patch faces edges</td></tr><tr><td>-point &lt;pointId&gt;</td><td>Write specified point</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: writeMeshObj [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cell &lt;cellId&gt;    Write points for the specified cell
  -cellSet &lt;name&gt;   Write points for specified cellSet
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -face &lt;faceId&gt;    Write specified face
  -faceSet &lt;name&gt;   Write points for specified faceSet
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
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -patchEdges       Write patch boundary edges
  -patchFaces       Write patch faces edges
  -point &lt;pointId&gt;  Write specified point
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

For mesh debugging: write mesh as separate OBJ files

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/writeMeshObj/writeMeshObj.C">源码与说明</a> · <a href="/assets/command-help/writemeshobj.txt">帮助文本</a></p>
