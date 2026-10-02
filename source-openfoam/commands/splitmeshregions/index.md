---
title: "splitMeshRegions · 各目标区域分别配置字典和场文件"
layout: reference
description: "各目标区域分别配置字典和场文件。"
cms_slug: "command-splitmeshregions"
---

<p>各目标区域分别配置字典和场文件。</p><h2>用法</h2><pre><code class="language-bash">splitMeshRegions -cellZones -overwrite</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">splitMeshRegions -cellZones -overwrite -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cellZones</td><td>Additionally split cellZones off into separate regions Like -cellZonesOnly, but use specified file</td></tr><tr><td>-cellZonesOnly</td><td>Use cellZones only to split mesh into regions; do not use walking Combine zones in follow-on analysis Set named DebugSwitch (default value: 1). [Can be used multiple times] Alternative decomposePar dictionary file</td></tr><tr><td>-detectOnly</td><td>Do not write mesh Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times] Only write region containing point</td></tr><tr><td>-largestOnly</td><td>Only write largest region</td></tr><tr><td>-makeCellZones</td><td>Place cells into cellZones instead of splitting mesh</td></tr><tr><td>-overwrite</td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-prefixRegion</td><td>Prefix region name to all patches, not just coupling patches</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-sloppyCellZones</td><td>Try to match heuristically regions to existing cell zones</td></tr><tr><td>-useFaceZones</td><td>Use faceZones to patch inter-region faces instead of single patch</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/constant-regionproperties/">regionProperties</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: splitMeshRegions [OPTIONS]
Options:
  -addZones &lt;lists of zones&gt;
                    Combine zones in follow-on analysis
  -blockedFaces &lt;faceSet&gt;
                    Specify additional region boundaries that walking does not
                    cross
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellZones        Additionally split cellZones off into separate regions
  -cellZonesFileOnly &lt;file&gt;
                    Like -cellZonesOnly, but use specified file
  -cellZonesOnly    Use cellZones only to split mesh into regions; do not use
                    walking
  -combineZones &lt;lists of zones&gt;
                    Combine zones in follow-on analysis
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -detectOnly       Do not write mesh
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -insidePoint &lt;point&gt;
                    Only write region containing point
  -largestOnly      Only write largest region
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -makeCellZones    Place cells into cellZones instead of splitting mesh
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -prefixRegion     Prefix region name to all patches, not just coupling patches
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -sloppyCellZones  Try to match heuristically regions to existing cell zones
  -useFaceZones     Use faceZones to patch inter-region faces instead of single
                    patch
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split mesh into multiple regions (detected by walking across faces)

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMeshRegions/splitMeshRegions.C">源码与说明</a> · <a href="/assets/command-help/splitmeshregions.txt">帮助文本</a></p>
