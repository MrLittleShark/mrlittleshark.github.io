---
title: "selectCells · 按字典中的几何条件选择网格单元，生成单元集合"
layout: reference
description: "按字典中的几何条件选择网格单元，生成单元集合。"
cms_slug: "command-selectcells"
---

<p>按字典中的几何条件选择网格单元，生成单元集合。</p><h2>开始前</h2>
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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/selectCells/edgeStats.C">源码与说明</a> · <a href="/assets/command-help/selectcells.txt">帮助文本</a></p>
