---
title: "star4ToFoam · 将 STAR-CD/PROSTAR v4 网格转换为 OpenFOAM 体网格"
layout: reference
description: "将 STAR-CD/PROSTAR v4 网格转换为 OpenFOAM 体网格。"
cms_slug: "command-star4tofoam"
---

<p>将 STAR-CD/PROSTAR v4 网格转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备 STAR-CD v4 的同名前缀 .vrt、.cel 和 .bnd 文件；默认缩放因子 0.001，通常把毫米转换为米。</p>
<h2>示例 1：按文件前缀导入</h2>
<pre><code class="language-bash">star4ToFoam mesh
</code></pre>
<p>读取 mesh.vrt、mesh.cel 和对应边界文件。默认将顶点坐标乘 0.001，检查输出尺寸是否符合输入单位。</p>
<h2>示例 2：导入已经为米制的网格</h2>
<pre><code class="language-bash">star4ToFoam mesh -scale 1
</code></pre>
<p>保持原始坐标数值，适用于顶点文件已采用米制的输入。显式比例能避免二次缩放。</p>
<h2>示例 3：写出文本格式网格</h2>
<pre><code class="language-bash">star4ToFoam mesh -ascii
</code></pre>
<p>导入后以 ASCII 保存 polyMesh，便于直接阅读连接和边界数据。大型网格需要预留更多磁盘空间。</p>
<h2>示例 4：保留固体单元</h2>
<pre><code class="language-bash">star4ToFoam mesh -solids
</code></pre>
<p>将输入中的固体单元也转换并保留。多区域传热应用需继续按区域拆分，并为各区域配置独立物性与求解设置。</p>
<h2>示例 5：在独立案例组合导入</h2>
<pre><code class="language-bash">star4ToFoam /data/engine -case ../starCase -scale 0.001 -ascii -solids
checkMesh -case ../starCase -constant -allTopology
</code></pre>
<p>从绝对前缀路径读取网格，保留全部目标区域并检查连接。核对区域之间的界面和外边界，作为后续多区域配置的依据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>以 ASCII 文本格式写出，替代二进制格式。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 0.001，即将毫米转换为米。</td></tr><tr><td><code>-solids</code></td><td>保留固体单元，并按流体单元处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/star4ToFoam/star4ToFoam.C">源码与说明</a> · <a href="/assets/command-help/star4tofoam.txt">帮助文本</a></p>
