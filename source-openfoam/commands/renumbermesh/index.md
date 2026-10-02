---
title: "renumberMesh · 重排单元与面编号以减小矩阵带宽，并同步重排场"
layout: reference
description: "重排单元与面编号以减小矩阵带宽，并同步重排场。"
cms_slug: "command-renumbermesh"
---

<p>重排单元与面编号以减小矩阵带宽，并同步重排场。</p><h2>开始前</h2>
<p>已有网格；选定时间的场与网格相匹配。默认重编号方法为 CuthillMcKee。</p>
<h2>示例 1：测试编号效果</h2>
<pre><code class="language-bash">renumberMesh -dry-run -frontWidth
</code></pre>
<p>只计算重排方案与带宽、前沿宽度指标，保留原网格；可判断该网格是否值得重排。</p>
<h2>示例 2：应用默认重编号</h2>
<pre><code class="language-bash">renumberMesh -overwrite
</code></pre>
<p>把重排后的网格和相应场写回当前案例，几何形状和物理场分布保持对应。</p>
<h2>示例 3：保存编号映射</h2>
<pre><code class="language-bash">renumberMesh -overwrite -write-maps
</code></pre>
<p>额外保存旧编号与新编号的映射，用于对照外部单元数据、源项选区或调试信息。</p>
<h2>示例 4：显式选择反向编号</h2>
<pre><code class="language-bash">renumberMesh -renumber-method CuthillMcKee -renumber-coeffs 'reverse true;' -overwrite
</code></pre>
<p>命令行选择方法并传入 reverse 系数，使用反向 Cuthill–McKee 排序，比较带宽和线性求解性能。</p>
<h2>示例 5：对最后时刻的动网格重排</h2>
<pre><code class="language-bash">renumberMesh -latestTime -overwrite -write-maps
</code></pre>
<p>读取最后保存状态的网格和场，重排并输出映射；后续重启使用这一时间的匹配数据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-decompose</code></td><td>Aggregate initially with a decomposition method (serial only) Alternative decomposePar dictionary file</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-dry-run</code></td><td>Test without writing. Changes -write-maps to write VTK output. Override the file handler type</td></tr><tr><td><code>-frontWidth</code></td><td>Calculate the RMS of the front-width Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-list-renumber</code></td><td>List available renumbering methods</td></tr><tr><td><code>-no-fields</code></td><td>Suppress renumbering of fields (eg, when they are only uniform)</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-renumbermeshdict/">renumberMeshDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: renumberMesh [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decompose        Aggregate initially with a decomposition method (serial
                    only)
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative renumberMeshDict
  -dry-run          Test without writing. Changes -write-maps to write VTK
                    output.
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -frontWidth       Calculate the RMS of the front-width
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -list-renumber    List available renumbering methods
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-fields        Suppress renumbering of fields (eg, when they are only
                    uniform)
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times (currently ignored)
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -renumber-coeffs &lt;string-content&gt;
                    Specify renumber coefficients (dictionary content) as
                    string. eg, &#x27;reverse true;&#x27;
  -renumber-method &lt;name&gt;
                    Specify renumber method (default: CuthillMcKee) without
                    dictionary
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;value&gt;     Select the nearest time to the specified value
  -verbose          Additional verbosity (can be used multiple times)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -write-maps       Write renumber mappings
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Renumber mesh cells to reduce the bandwidth. Use the -lib option or dictionary
&#x27;libs&#x27; entry to load additional libraries

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/renumberMesh/renumberMesh.C">源码与说明</a> · <a href="/assets/command-help/renumbermesh.txt">帮助文本</a></p>
