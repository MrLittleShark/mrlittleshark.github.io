---
title: "surfacePatch · 按几何选择规则修改表面网格的区域划分"
layout: reference
description: "按几何选择规则修改表面网格的区域划分。"
cms_slug: "command-surfacepatch"
---

<p>按几何选择规则修改表面网格的区域划分。</p><h2>开始前</h2>
<p>案例有 system/surfacePatchDict，geometry 中声明实际表面。以下字典修改针对 surfaces/body.stl；工具把变更表面另存为 body_patched.stl。</p>
<h2>示例 1：按特征角拆分表面区域</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl' -set '{ type autoPatch; featureAngle 45; }'
surfacePatch
</code></pre>
<p>为 body.stl 的整体表面指定 autoPatch，按 45° 特征角形成区域。-entry 使用斜杠分隔字典层级，保留文件名 body.stl 中的点号。检查输出表面的区域数量与位置。</p>
<h2>示例 2：保留更多棱边分区</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl/featureAngle' -set 20
surfacePatch
</code></pre>
<p>把分区角度改为 20°，较小的折角也可形成区域边界。比较输出区域数，判断是否过度分割了曲面离散带来的小折角。</p>
<h2>示例 3：合并较平滑的区域</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl/featureAngle' -set 80
surfacePatch
</code></pre>
<p>较大阈值保留更明显的几何棱边，通常形成更少的区域。检查入口、出口等需要独立边界的部分是否仍能识别。</p>
<h2>示例 4：只处理一个已有区域</h2>
<pre><code class="language-bash">surfacePatch -dict system/surfacePatch-top.dict
</code></pre>
<p>前提是在该字典 surfaces/body.stl/regions 内给 maxZ 设置 { type autoPatch; featureAngle 45; }。只重新划分目标区域，便于保留其他已命名表面。</p>
<h2>示例 5：按搜索几何切分区域</h2>
<pre><code class="language-bash">surfacePatch -dict system/surfacePatch-cut.dict
</code></pre>
<p>该字典在 geometry 声明 box，在目标 surfaces 条目设置 type cut; cutters (box);。输出表面按与 box 的几何关系形成分区，便于划定局部边界区域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 surfacePatchDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfacePatch/searchableSurfaceModifier/searchableSurfaceModifier.C">源码与说明</a> · <a href="/assets/command-help/surfacepatch.txt">帮助文本</a></p>
