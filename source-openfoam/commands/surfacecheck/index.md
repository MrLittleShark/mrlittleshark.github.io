---
title: "surfaceCheck · 检查三角化表面的范围、连通性和质量"
layout: reference
description: "检查三角化表面的范围、连通性和质量。"
cms_slug: "command-surfacecheck"
---

<p>检查三角化表面的范围、连通性和质量。</p><h2>开始前</h2>
<p>输入为STL、OBJ等支持的表面；检查会输出统计，部分选项还生成问题集合或分割结果。</p>
<h2>示例 1：检查基本质量</h2>
<pre><code class="language-bash">surfaceCheck body.stl
</code></pre>
<p>查看点数、三角面数、包围盒、开边及区域数，先确认几何尺度和闭合状态。</p>
<h2>示例 2：检查自相交</h2>
<pre><code class="language-bash">surfaceCheck -checkSelfIntersection body.stl
</code></pre>
<p>额外检测相互穿过的三角形，适合CAD修补或表面平滑之后检查。</p>
<h2>示例 3：输出缺陷集合</h2>
<pre><code class="language-bash">surfaceCheck -checkSelfIntersection -writeSets vtk body.stl
</code></pre>
<p>把问题三角形或边转换为VTK数据，便于在ParaView定位具体缺陷。</p>
<h2>示例 4：限制诊断文件数量</h2>
<pre><code class="language-bash">surfaceCheck -outputThreshold 0 body.stl
</code></pre>
<p>输出统计但抑制诊断文件写出，适合只需快速读取质量信息的大型表面。</p>
<h2>示例 5：识别并拆分非流形连接</h2>
<pre><code class="language-bash">surfaceCheck -splitNonManifold -writeSets vtk body.stl
</code></pre>
<p>针对多重连接边检查并分开相应表面连接，查看分割结果后再确定所需几何拓扑。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-blockMesh</code></td><td>输出可用于 blockMeshDict 的 vertices 和 blocks。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkSelfIntersection</code></td><td>同时检查表面自相交。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-outputThreshold &lt;number&gt;</code></td><td>限制输出文件数，默认为 10；设为 0 时仅显示检查结果。</td></tr><tr><td><code>-splitNonManifold</code></td><td>沿非流形边拆分表面；默认按完全断开的部分拆分。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-writeSets &lt;surfaceFormat&gt;</code></td><td>重建问题三角形或边，并按指定表面格式输出。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceCheck/surfaceCheck.C">源码与说明</a> · <a href="/assets/command-help/surfacecheck.txt">帮助文本</a></p>
