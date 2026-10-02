---
title: "foamToVTK · 将 OpenFOAM 网格和场转换为 VTK 数据"
layout: reference
description: "将 OpenFOAM 网格和场转换为 VTK 数据。"
cms_slug: "command-foamtovtk"
---

<p>将 OpenFOAM 网格和场转换为 VTK 数据。</p><h2>导出最新时刻</h2>
<pre><code class="language-bash">foamToVTK -latestTime
</code></pre>
<p>结果写入 VTK 输出目录，便于在其他后处理工具中打开。</p>
<h2>只导出速度和压力</h2>
<pre><code class="language-bash">foamToVTK -latestTime -fields "(U p)"
</code></pre>
<p>限制导出字段可以减少文件大小。点数据和单元数据含义不同，绘图时保留所选数据关联。</p>
<h2>导出一段时间</h2>
<pre><code class="language-bash">foamToVTK -time "0.1:0.5"
</code></pre>
<p>只导出指定时间范围中已有的结果，适合制作短时间段动画。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allAreas</td><td>Use all regions in finite-area regionProperties</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-ascii</td><td>Write in ASCII format instead of binary</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cellSet &lt;name&gt;</td><td>Convert mesh subset corresponding to specified cellSet</td></tr><tr><td>-cellZone &lt;name&gt;</td><td>Convert mesh subset corresponding to specified cellZone</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-faceSet &lt;name&gt;</td><td>Convert specified faceSet only Specify single or multiple faceZones to write Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;. Specify single or multiple fields to write (all by default) Eg, &#x27;T&#x27; or &#x27;(p T U &quot;alpha.*&quot;)&#x27; Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-legacy</td><td>Write legacy format instead of xml</td></tr><tr><td>-name &lt;subdir&gt;</td><td>Directory name for VTK output (default: &#x27;VTK&#x27;)</td></tr><tr><td>-nearCellValue</td><td>Use cell value on patches instead of patch value itself</td></tr><tr><td>-no-boundary</td><td>Suppress output for boundary patches</td></tr><tr><td>-no-fields</td><td>Suppress conversion of fields</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToVTK [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -ascii            Write in ASCII format instead of binary
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellSet &lt;name&gt;   Convert mesh subset corresponding to specified cellSet
  -cellZone &lt;name&gt;  Convert mesh subset corresponding to specified cellZone
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
  -faceSet &lt;name&gt;   Convert specified faceSet only
  -faceZones &lt;wordRes&gt;
                    Specify single or multiple faceZones to write
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;.
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to write (all by default)
                    Eg, &#x27;T&#x27; or &#x27;(p T U &quot;alpha.*&quot;)&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -legacy           Write legacy format instead of xml
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -name &lt;subdir&gt;    Directory name for VTK output (default: &#x27;VTK&#x27;)
  -nearCellValue    Use cell value on patches instead of patch value itself
  -no-boundary      Suppress output for boundary patches
  -no-fields        Suppress conversion of fields
  -no-finite-area   Suppress output of finite-area mesh/fields
  -no-internal      Suppress output for internal volume mesh
  -no-lagrangian    Suppress writing lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-point-data    Suppress conversion of pointFields. No interpolated
                    PointData.
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -one-boundary     Combine all patches into a single file
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Remove any existing VTK output directory
  -parallel         Run in parallel
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to write
                    Eg, &#x27;top&#x27; or &#x27;( front &quot;.*back&quot; )&#x27;
  -pointSet &lt;name&gt;  Convert specified pointSet only
  -poly-decomp      Decompose polyhedral cells into tets/pyramids
  -processor-fields
                    Write field values on processor boundaries only
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -surfaceFields    Write surfaceScalarFields (eg, phi)
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -with-ids         Additional mesh id fields (cellID, procID, patchID)
  -with-point-ids   Additional pointID field for internal mesh
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

General OpenFOAM to VTK file writer

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToVTK/foamToVTK.C">源码与说明</a> · <a href="/assets/command-help/foamtovtk.txt">帮助文本</a></p>
