---
title: "selectCells · 读取选择字典，生成 selected 集合"
layout: reference
description: "读取选择字典，生成 selected 集合。"
cms_slug: "command-selectcells"
---

<p>读取选择字典，生成 selected 集合。</p><h2>开始前</h2>
<p>准备网格、闭合三角表面和 system/selectCellsDict，含 surface、outsidePoints、useSurface、selectCut、selectInside、selectOutside、nearDistance。outsidePoints 取明确位于表面外侧的点。</p>
<h2>示例 1：按现有设置划分单元</h2>
<pre><code class="language-bash">selectCells
</code></pre>
<p>输出 inside、outside、cutCells 等分类集合，并把最终选区写为 selected。可在 ParaView 中显示集合检查表面与体网格的相对位置。</p>
<h2>示例 2：选择表面内及相交单元</h2>
<pre><code class="language-bash">foamDictionary system/selectCellsDict -entry selectInside -set true
foamDictionary system/selectCellsDict -entry selectCut -set true
foamDictionary system/selectCellsDict -entry selectOutside -set false
selectCells
</code></pre>
<p>使用已启用 useSurface 的字典，组合内部单元与被表面切过的单元。适合准备内部流体域的初步选区。</p>
<h2>示例 3：选择表面外侧</h2>
<pre><code class="language-bash">foamDictionary system/selectCellsDict -entry selectInside -set false
foamDictionary system/selectCellsDict -entry selectOutside -set true
foamDictionary system/selectCellsDict -entry selectCut -set true
selectCells
</code></pre>
<p>改为保留外部与相交单元，适用于物体绕流的背景网格。检查 outsidePoints 与目标外部连通域是否一致。</p>
<h2>示例 4：仅查看切割单元</h2>
<pre><code class="language-bash">foamDictionary system/selectCellsDict -entry selectInside -set false
foamDictionary system/selectCellsDict -entry selectOutside -set false
foamDictionary system/selectCellsDict -entry selectCut -set true
selectCells
</code></pre>
<p>强调表面穿过的单元带，便于评估局部网格尺寸。工具还会执行连通性相关整理，实际 selected 应与 cutCells 一起查看。</p>
<h2>示例 5：在副本比较表面距离参数</h2>
<pre><code class="language-bash">foamDictionary ../selectionTest/system/selectCellsDict -entry nearDistance -set 0.001
selectCells -case ../selectionTest
</code></pre>
<p>将近表面距离设为 0.001 个网格长度单位，再比较 selected 与原方案。该参数影响近表面处理，需结合局部单元尺寸解释选区变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: selectCells [OPTIONS]
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
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Select cells in relation to surface

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/selectCells/edgeStats.C">源码与说明</a> · <a href="/assets/command-help/selectcells.txt">帮助文本</a></p>
