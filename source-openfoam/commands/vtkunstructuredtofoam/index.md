---
title: "vtkUnstructuredToFoam · 输入采用旧式 ASCII VTK 格式"
layout: reference
description: "输入采用旧式 ASCII VTK 格式。"
cms_slug: "command-vtkunstructuredtofoam"
---

<p>输入采用旧式 ASCII VTK 格式。</p><h2>开始前</h2>
<p>准备旧式 ASCII VTK UNSTRUCTURED_GRID 文件；转换器读取体网格，物理边界分组需后续建立。</p>
<h2>示例 1：导入 VTK 体网格</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh.vtk
</code></pre>
<p>读取点坐标和支持的单元连接，生成 OpenFOAM 网格。查看转换日志中的单元类型及数量。</p>
<h2>示例 2：检查混合单元网格</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mixed.vtk
checkMesh -constant -allTopology -allGeometry
</code></pre>
<p>输入包含多种受支持的体单元时，检查转换后的连接和单元质量。关注未识别单元以及异常体积报告。</p>
<h2>示例 3：换算毫米坐标</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh-mm.vtk
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>转换后缩放全网格到米制，便于与其他 OpenFOAM 案例的物性和边界条件一致。</p>
<h2>示例 4：按外形建立边界分区</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh.vtk
autoPatch 45 -overwrite
</code></pre>
<p>转换器没有物理边界信息，第二步按特征角划分外表面。根据实际位置进一步命名和配置场边界。</p>
<h2>示例 5：在独立案例提取表面核对</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam /data/mesh.vtk -case ../vtkCase
foamToSurface vtk-boundary.obj -case ../vtkCase -constant
</code></pre>
<p>将转换结果放入 vtkCase，并导出外表面。与原 VTK 数据叠加查看，检查几何位置、尺度和边界是否完整。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/vtkUnstructuredToFoam/vtkUnstructuredToFoam.C">源码与说明</a> · <a href="/assets/command-help/vtkunstructuredtofoam.txt">帮助文本</a></p>
