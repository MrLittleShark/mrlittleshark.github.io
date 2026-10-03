---
title: "mshToFoam · 将 Adventure 系统的 MSH 网格转换为 OpenFOAM 体网格"
layout: reference
description: "将 Adventure 系统的 MSH 网格转换为 OpenFOAM 体网格。"
cms_slug: "command-mshtofoam"
---

<p>将 Adventure 系统的 MSH 网格转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备 Adventure 格式的 .msh 文件。默认读取四面体网格，六面体使用 -hex；Gmsh 文件应使用 gmshToFoam。</p>
<h2>示例 1：导入四面体网格</h2>
<pre><code class="language-bash">mshToFoam mesh.msh
</code></pre>
<p>按 Adventure 四面体连接格式读取网格，建立 polyMesh。检查单元数与原始网格是否一致。</p>
<h2>示例 2：导入六面体网格</h2>
<pre><code class="language-bash">mshToFoam hexMesh.msh -hex
</code></pre>
<p>切换到六面体单元格式。该选项改变单元连接的读取方式，应与输入每个单元的节点数对应。</p>
<h2>示例 3：在目标案例检查连接</h2>
<pre><code class="language-bash">mshToFoam /data/mesh.msh -case ../adventureCase
checkMesh -case ../adventureCase -constant -allTopology
</code></pre>
<p>将转换限制到独立案例，并检查外边界及内部面的连接。适合先验证输入格式再配置求解。</p>
<h2>示例 4：将毫米网格换算为米</h2>
<pre><code class="language-bash">mshToFoam mesh-mm.msh
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>转换后统一缩放坐标。确认边界框尺寸与后续使用的米制速度、黏度参数一致。</p>
<h2>示例 5：按几何棱边划分边界</h2>
<pre><code class="language-bash">mshToFoam mesh.msh
autoPatch 45 -overwrite
checkMesh -constant
</code></pre>
<p>根据 45° 特征角对边界进一步分区，适用于输入未提供所需物理边界名称的模型。分区后按几何位置命名并设置边界条件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-hex</code></td><td>按六面体单元解析输入，替代默认的四面体单元。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/mshToFoam/mshToFoam.C">源码与说明</a> · <a href="/assets/command-help/mshtofoam.txt">帮助文本</a></p>
