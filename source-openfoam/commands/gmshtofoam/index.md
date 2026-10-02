---
title: "gmshToFoam · 常用输入为 ASCII MSH2"
layout: reference
description: "常用输入为 ASCII MSH2。转换后检查物理组与边界名称。"
cms_slug: "command-gmshtofoam"
---

<p>常用输入为 ASCII MSH2。转换后检查物理组与边界名称。</p><h2>开始前</h2>
<p>准备 Gmsh 的 ASCII MSH 2 格式网格；建议在 Gmsh 中定义 Physical Volume 和 Physical Surface 来表达体区及边界。</p>
<h2>示例 1：导入现有 Gmsh 网格</h2>
<pre><code class="language-bash">gmshToFoam mesh.msh
</code></pre>
<p>读取节点、单元和物理分组，生成 polyMesh。转换后查看 boundary 和 cellZones，核对 Physical 分组是否完整。</p>
<h2>示例 2：从几何文件生成再导入</h2>
<pre><code class="language-bash">gmsh channel.geo -3 -format msh2 -o channel.msh
gmshToFoam channel.msh
</code></pre>
<p>需要系统已安装 gmsh。第一步生成三维 MSH 2 网格，第二步转换为 OpenFOAM，适合可重复的几何—网格工作流程。</p>
<h2>示例 3：导入命名区域</h2>
<pre><code class="language-bash">gmshToFoam solid.msh -region solid
</code></pre>
<p>将网格写到名为 solid 的区域路径。适合多区域案例中单独准备固体网格，随后需要相应的 constant/solid 和 system/solid 配置。</p>
<h2>示例 4：保留输入的单元方向</h2>
<pre><code class="language-bash">gmshToFoam mesh.msh -keepOrientation
</code></pre>
<p>保留输入棱柱和六面体的方向信息。适用于已确认节点顺序的网格，之后用 checkMesh 查看负体积和面方向。</p>
<h2>示例 5：换算毫米模型并检查</h2>
<pre><code class="language-bash">gmshToFoam mesh-mm.msh
transformPoints -scale '(0.001 0.001 0.001)'
checkMesh -constant -allGeometry
</code></pre>
<p>转换器通过输入坐标建立网格；第二步统一缩放为米。检查单元质量和尺寸，再配置求解器物性。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-keepOrientation</code></td><td>保留棱柱和六面体的原始方向。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/gmshToFoam/gmshToFoam.C">源码与说明</a> · <a href="/assets/command-help/gmshtofoam.txt">帮助文本</a></p>
