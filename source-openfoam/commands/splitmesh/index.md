---
title: "splitMesh · 把 faceSet 指定的内部面拆成两侧边界"
layout: reference
description: "把 faceSet 指定的内部面拆成两侧边界。"
cms_slug: "command-splitmesh"
---

<p>把 faceSet 指定的内部面拆成两侧边界。</p><h2>开始前</h2>
<p>已有内部faceSet，且 master/slave 指定的边界patch已按案例要求准备好；三个参数依次为集合、主侧、从侧。</p>
<h2>示例 1：沿指定面集拆分</h2>
<pre><code class="language-bash">splitMesh interfaceFaces sideA sideB
</code></pre>
<p>interfaceFaces 的内部面被转换为 sideA 与 sideB 两侧边界，结果写入新的网格时间。</p>
<h2>示例 2：把拆分结果用于后续预处理</h2>
<pre><code class="language-bash">splitMesh interfaceFaces sideA sideB -overwrite
</code></pre>
<p>写回当前网格；后续为新两侧配置边界条件时使用 sideA、sideB 名称。</p>
<h2>示例 3：先生成切割集合</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-cutDict
splitMesh cutFaces cutMaster cutSlave -overwrite
</code></pre>
<p>topoSet-cutDict 已定义 cutFaces faceSet；选择与拆分连成可重复流程，输出沿该切面分开的网格。</p>
<h2>示例 4：检查拆分后的连通区域</h2>
<pre><code class="language-bash">splitMesh interfaceFaces sideA sideB -overwrite
splitMeshRegions -detectOnly
</code></pre>
<p>第二条只检测网格连通区域，检查这次拆分是否确实把预期区域隔开。</p>
<h2>示例 5：查看新边界的场类型</h2>
<pre><code class="language-bash">splitMesh interfaceFaces sideA sideB -overwrite
patchSummary -time 0 -expand
</code></pre>
<p>0时刻场已补充新patch条目后，用 patchSummary 展开每个边界，检查拆分两侧的边界条件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: splitMesh [OPTIONS] &lt;faceSet&gt; &lt;master&gt; &lt;slave&gt;
Arguments:
  &lt;faceSet&gt;         The faces used for splitting
  &lt;master&gt;          The master patch name
  &lt;slave&gt;           The slave patch name
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Splits mesh by making internal faces external at defined faceSet

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMesh/regionSide.C">源码与说明</a> · <a href="/assets/command-help/splitmesh.txt">帮助文本</a></p>
