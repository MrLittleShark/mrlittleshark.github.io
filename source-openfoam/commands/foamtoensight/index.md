---
title: "foamToEnsight · 将网格和结果导出为 EnSight 格式"
layout: reference
description: "将网格和结果导出为 EnSight 格式。"
cms_slug: "command-foamtoensight"
---

<p>将网格和结果导出为 EnSight 格式。</p><h2>开始前</h2>
<p>已有结果场；默认写EnSight目录，-name可为不同导出方案指定独立目录。</p>
<h2>示例 1：导出最终状态</h2>
<pre><code class="language-bash">foamToEnsight -latestTime -fields '(U p)'
</code></pre>
<p>转换最终几何、速度与压力，生成EnSight案例文件和对应数据。</p>
<h2>示例 2：导出时间区间</h2>
<pre><code class="language-bash">foamToEnsight -time '0.1:1' -fields '(U T)' -name EnSight-thermal
</code></pre>
<p>在含U、T的案例中仅导出指定区间，输出独立热流动数据集。</p>
<h2>示例 3：导出边界压力</h2>
<pre><code class="language-bash">foamToEnsight -latestTime -no-internal -patches '(walls)' -fields '(p)'
</code></pre>
<p>关闭内部网格输出，仅写walls边界压力，适合外部表面后处理。</p>
<h2>示例 4：将单元值插到节点</h2>
<pre><code class="language-bash">foamToEnsight -latestTime -nodeValues -fields '(U p)'
</code></pre>
<p>将字段插值到节点，适合需要节点数据的显示或外部接口；插值后的极值可能与单元原值有差异。</p>
<h2>示例 5：输出ASCII数据并统一文件编号</h2>
<pre><code class="language-bash">foamToEnsight -time '2:3' -ascii -index 0 -width 6 -no-lagrangian -name EnSight-ascii
</code></pre>
<p>输出 2 至 3 秒的已有结果；-ascii 便于读取文本，-index 0 从 0 开始连续编号，-width 6 使用六位数据目录名，-no-lagrangian 跳过粒子数据。结果写入独立 EnSight-ascii 目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>Use all regions in finite-area regionProperties</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-ascii</code></td><td>Write in ASCII format instead of &#x27;C Binary&#x27;</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-index &lt;start&gt;</code></td><td>Starting index for consecutive number of Ensight data/ files. Ignore the time index contained in the uniform/time file. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-name &lt;subdir&gt;</code></td><td>Sub-directory name for Ensight output (default: &#x27;EnSight&#x27;)</td></tr><tr><td><code>-nearCellValue</code></td><td>Use zero-gradient cell values on patches</td></tr><tr><td><code>-no-boundary</code></td><td>Suppress writing any patches</td></tr><tr><td><code>-no-cellZones</code></td><td>Suppress writing any cellZones</td></tr><tr><td><code>-no-fields</code></td><td>Suppress conversion of fields</td></tr><tr><td><code>-no-finite-area</code></td><td>Suppress output of finite-area mesh/fields</td></tr><tr><td><code>-no-internal</code></td><td>Suppress writing the internal mesh</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToEnsight [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -ascii            Write in ASCII format instead of &#x27;C Binary&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellZones &lt;wordRes&gt;
                    Specify single or multiple cellZones to write
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -exclude-fields &lt;wordRes&gt;
                    Exclude single or multiple fields
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches from writing
                    Eg, &#x27;outlet&#x27; or &#x27;( inlet &quot;.*Wall&quot; )&#x27;
  -faceZones &lt;wordRes&gt;
                    Specify single or multiple faceZones to write
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;.
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to write (all by default)
                    Eg, &#x27;T&#x27; or &#x27;( &quot;U.*&quot; )&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -index &lt;start&gt;    Starting index for consecutive number of Ensight data/
                    files. Ignore the time index contained in the uniform/time
                    file.
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
  -name &lt;subdir&gt;    Sub-directory name for Ensight output (default: &#x27;EnSight&#x27;)
  -nearCellValue    Use zero-gradient cell values on patches
  -no-boundary      Suppress writing any patches
  -no-cellZones     Suppress writing any cellZones
  -no-fields        Suppress conversion of fields
  -no-finite-area   Suppress output of finite-area mesh/fields
  -no-internal      Suppress writing the internal mesh
  -no-lagrangian    Suppress writing lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-mesh          Suppress writing the geometry. Can be useful for converting
                    partial results for a static geometry
  -no-overwrite     Suppress removal of existing EnSight output directory
  -no-point-data    Suppress conversion of pointFields, disable -nodeValues
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -nodeValues       Force interpolation of values to nodes
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to write
                    Eg, &#x27;inlet&#x27; or &#x27;(outlet &quot;inlet.*&quot;)&#x27;
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -width &lt;n&gt;        Width of Ensight data subdir
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Translate OpenFOAM data to Ensight format with individual parts for cellZones,
unzoned cells and patches

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToEnsight/readFields.C">源码与说明</a> · <a href="/assets/command-help/foamtoensight.txt">帮助文本</a></p>
