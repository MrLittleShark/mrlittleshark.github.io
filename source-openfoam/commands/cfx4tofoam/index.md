---
title: "cfx4ToFoam · -scale 指定长度缩放系数"
layout: reference
description: "-scale 指定长度缩放系数。"
cms_slug: "command-cfx4tofoam"
---

<p>-scale 指定长度缩放系数。</p><h2>开始前</h2>
<p>准备 CFX4 的 .geo 几何文件和目标案例，输入格式应与 CFX4 转换器相符。</p>
<h2>示例 1：导入 CFX4 几何</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo
</code></pre>
<p>转换节点、单元和边界到 polyMesh。查看终端输出，核对读取的块数和边界分区。</p>
<h2>示例 2：换算毫米坐标</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo -scale 0.001
</code></pre>
<p>将输入节点坐标乘 0.001。转换后检查边界框尺寸，确保计算域长度与后续速度、黏度等 SI 制参数一致。</p>
<h2>示例 3：在目标案例中检查拓扑</h2>
<pre><code class="language-bash">cfx4ToFoam /data/mesh.geo -case ../cfxCase
checkMesh -case ../cfxCase -constant -allTopology
</code></pre>
<p>将网格写入指定案例后检查拓扑连接。关注内部面、边界面和不连通区域，判断多块网格是否正确连接。</p>
<h2>示例 4：整理转换后的边界</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo
createPatch -overwrite
</code></pre>
<p>先依据转换得到的 patch 名称编写 createPatchDict，再合并同一物理边界的分区。检查 boundary 文件并同步配置各场的 boundaryField。</p>
<h2>示例 5：导出外表面核对形状</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo -scale 0.001
foamToSurface cfx-boundary.stl -constant
</code></pre>
<p>把导入网格外边界写成 STL，便于与原始几何叠加检查。主要核对单位、朝向、孔洞以及入口出口的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/cfx4ToFoam/hexBlock.C">源码与说明</a> · <a href="/assets/command-help/cfx4tofoam.txt">帮助文本</a></p>
