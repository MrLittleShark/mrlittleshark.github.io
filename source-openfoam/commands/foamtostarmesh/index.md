---
title: "foamToStarMesh · 输出 bnd、cel 和 vrt 等文件"
layout: reference
description: "输出 bnd、cel 和 vrt 等文件。"
cms_slug: "command-foamtostarmesh"
---

<p>输出 bnd、cel 和 vrt 等文件。</p><h2>开始前</h2>
<p>案例已有网格；默认导出比例为 1000，即常见米制 OpenFOAM 网格转为毫米制 STAR-CD 坐标。</p>
<h2>示例 1：按默认比例导出</h2>
<pre><code class="language-bash">foamToStarMesh -constant
</code></pre>
<p>输出 STAR-CD 的顶点、单元和边界文件。默认坐标乘 1000，原 1 m 长度写为 1000。</p>
<h2>示例 2：保持原坐标数值</h2>
<pre><code class="language-bash">foamToStarMesh -constant -scale 1
</code></pre>
<p>显式指定比例 1，适合接收端也使用米制坐标的情况。导入外部软件后核对边界框。</p>
<h2>示例 3：仅导出几何连接</h2>
<pre><code class="language-bash">foamToStarMesh -constant -noBnd
</code></pre>
<p>输出顶点和单元，跳过 .bnd 边界文件。适合接收端计划重新建立边界分区的流程。</p>
<h2>示例 4：导出最新网格位置</h2>
<pre><code class="language-bash">foamToStarMesh -latestTime -scale 1
</code></pre>
<p>选择最新时间的网格，保持米制坐标。动网格输出可用于检查最后时刻的几何形状。</p>
<h2>示例 5：导出选定时间的网格</h2>
<pre><code class="language-bash">foamToStarMesh -time '0.2,0.5,1' -scale 1000
</code></pre>
<p>选择已有的 0.2、0.5 和 1 时间目录。比较输出几何可以分析位移过程；所有输出采用相同的毫米坐标尺度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noBnd</code></td><td>Suppress writing a boundary (.bnd) file Do not execute function objects</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1000 ([m] to [mm])</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToStarMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noBnd            Suppress writing a boundary (.bnd) file
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1000 ([m] to [mm])
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Write an OpenFOAM mesh in STARCD/PROSTAR (v4) bnd/cel/vrt format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToStarMesh/foamToStarMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtostarmesh.txt">帮助文本</a></p>
