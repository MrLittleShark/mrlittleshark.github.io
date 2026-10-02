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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMesh/regionSide.C">源码与说明</a> · <a href="/assets/command-help/splitmesh.txt">帮助文本</a></p>
