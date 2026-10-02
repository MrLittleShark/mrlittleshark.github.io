---
title: "foamRestoreFields · 在原场与 Mean 平均场之间切换文件，并维护 .orig 备份"
layout: reference
description: "在原场与 Mean 平均场之间切换文件，并维护 .orig 备份。"
cms_slug: "command-foamrestorefields"
---

<p>在原场与 Mean 平均场之间切换文件，并维护 .orig 备份。</p><h2>开始前</h2>
<p>已有UMean、pMean等平均场，或此前生成的.orig备份；-method必须为mean或orig。</p>
<h2>示例 1：预览用均值替换速度的动作</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -latestTime -dry-run U
</code></pre>
<p>只报告文件重命名计划，检查UMean与U的对应关系。</p>
<h2>示例 2：使用平均速度和压力</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -latestTime U p
</code></pre>
<p>用UMean、pMean替代U、p，原有文件保存为.orig，便于把均值场交给后处理。</p>
<h2>示例 3：恢复原始字段</h2>
<pre><code class="language-bash">foamRestoreFields -method orig -latestTime U p
</code></pre>
<p>存在U.orig、p.orig时将其恢复为原字段名称，返回切换前的瞬时结果。</p>
<h2>示例 4：处理明确的时间范围</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -time '1:2' U
</code></pre>
<p>仅对1至2秒已有平均速度的时刻切换U，保留其他时间。</p>
<h2>示例 5：切换并行案例的均值场</h2>
<pre><code class="language-bash">foamRestoreFields -method mean -processor -latestTime U p
</code></pre>
<p>串行调用但扫描processor目录，在各子域最新时间进行相同字段切换，适合并行结果的统一整理。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dry-run</code></td><td>Report action without moving/renaming Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-method &lt;name&gt;</code></td><td>The restore method (mean|orig) [MANDATORY]. With &lt;mean&gt; renames files ending with &#x27;Mean&#x27; (with backup of existing as &#x27;.orig&#x27;). With &lt;orig&gt; renames files ending with &#x27;.orig&#x27;</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-processor</code></td><td>In serial mode use times from processor0/ directory, but operate on processor\d+ directories</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-withZero</code></td><td>Include &#x27;0/&#x27; dir in the times list</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamRestoreFields [OPTIONS] [&lt;fieldName ... fieldName&gt;]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Report action without moving/renaming
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
  -method &lt;name&gt;    The restore method (mean|orig) [MANDATORY]. With &lt;mean&gt;
                    renames files ending with &#x27;Mean&#x27; (with backup of existing
                    as &#x27;.orig&#x27;). With &lt;orig&gt; renames files ending with &#x27;.orig&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -processor        In serial mode use times from processor0/ directory, but
                    operate on processor\d+ directories
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Restore field names by removing the ending. Fields are selected automatically
or can be specified as optional command arguments

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamRestoreFields/foamRestoreFields.C">源码与说明</a> · <a href="/assets/command-help/foamrestorefields.txt">帮助文本</a></p>
