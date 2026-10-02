---
title: "foamToFireMesh · -scale 指定长度缩放系数"
layout: reference
description: "-scale 指定长度缩放系数。"
cms_slug: "command-foamtofiremesh"
---

<p>-scale 指定长度缩放系数。</p><h2>开始前</h2>
<p>案例已有体网格；按时间导出示例需要相应网格时间目录。输出用于 AVL FIRE 格式交换。</p>
<h2>示例 1：导出初始网格</h2>
<pre><code class="language-bash">foamToFireMesh -constant
</code></pre>
<p>选择 constant 网格并转换为 FIRE 格式。转换日志给出实际写出的文件位置。</p>
<h2>示例 2：使用 ASCII 格式</h2>
<pre><code class="language-bash">foamToFireMesh -constant -ascii
</code></pre>
<p>以文本格式导出，便于排查交换文件问题。与二进制输出相比，文件通常更大。</p>
<h2>示例 3：转换为毫米坐标</h2>
<pre><code class="language-bash">foamToFireMesh -constant -scale 1000
</code></pre>
<p>输出坐标乘 1000，将米制网格改为毫米数值。接收软件应按毫米解释输出坐标。</p>
<h2>示例 4：导出最新变形网格</h2>
<pre><code class="language-bash">foamToFireMesh -latestTime
</code></pre>
<p>读取最新时间对应的几何。适用于动网格计算后将变形位置交给 FIRE 相关工具。</p>
<h2>示例 5：导出一组瞬态网格</h2>
<pre><code class="language-bash">foamToFireMesh -time '0.1:0.5' -ascii
</code></pre>
<p>遍历所选范围内已有的时间目录，导出相关网格。核对每个输出对应的时间，避免把静态网格重复文件误认为不同形状。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>Write in ASCII format instead of binary</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1 (none)</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToFireMesh [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of binary
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
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1 (none)
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Write an OpenFOAM mesh in AVL/FIRE fpma format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToFireMesh/foamToFireMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtofiremesh.txt">帮助文本</a></p>
