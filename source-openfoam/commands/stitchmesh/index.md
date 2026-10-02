---
title: "stitchMesh · 把几何上可配对的两侧边界缝合为内部面"
layout: reference
description: "把几何上可配对的两侧边界缝合为内部面。"
cms_slug: "command-stitchmesh"
---

<p>把几何上可配对的两侧边界缝合为内部面。</p><h2>开始前</h2>
<p>同一网格中已有待拼接的 master、slave patch；其重叠关系决定 perfect、integral 或 partial 方式。</p>
<h2>示例 1：缝合完全吻合的面</h2>
<pre><code class="language-bash">stitchMesh -perfect interfaceA interfaceB -overwrite
</code></pre>
<p>两侧顶点和面分割完全一致时使用-perfect，写回网格并把接口改成内部面。</p>
<h2>示例 2：缝合完整覆盖但分割不同的接口</h2>
<pre><code class="language-bash">stitchMesh -integral interfaceA interfaceB -overwrite
</code></pre>
<p>两侧整体覆盖一致但面划分不同，用-integral进行完整接口耦合。</p>
<h2>示例 3：处理局部重叠</h2>
<pre><code class="language-bash">stitchMesh -partial masterPatch slavePatch -overwrite
</code></pre>
<p>只缝合两侧几何重叠部分，适合覆盖范围不完全一致的网格接口。</p>
<h2>示例 4：根据字典处理多组接口</h2>
<pre><code class="language-bash">stitchMesh -dict system/stitchMeshDict -overwrite
</code></pre>
<p>字典已列出接口操作时省略位置参数，按文件中的操作顺序完成多组缝合。</p>
<h2>示例 5：查看拼接中间阶段</h2>
<pre><code class="language-bash">stitchMesh -integral interfaceA interfaceB -intermediate -toleranceDict system/stitchTolerances
</code></pre>
<p>已有容差字典时，采用指定几何容差并保存中间阶段网格，便于定位小缝隙或错配面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 stitchMeshDict 文件。</td></tr><tr><td><code>-integral</code></td><td>耦合完整重叠的主从边界；这是双参数模式的默认方式。</td></tr><tr><td><code>-intermediate</code></td><td>写出各个中间阶段及最终结果。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-partial</code></td><td>耦合部分重叠的主从边界，适用于双参数模式。</td></tr><tr><td><code>-perfect</code></td><td>耦合完全对齐的主从边界，适用于双参数模式。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-toleranceDict &lt;file&gt;</code></td><td>从指定字典读取容差。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1">mesh/stitchMesh/simple-cube1</a></li></ul><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/stitchMesh.C">源码与说明</a> · <a href="/assets/command-help/stitchmesh.txt">帮助文本</a></p>
