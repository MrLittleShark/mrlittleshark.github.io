---
title: "ideasUnvToFoam · 转换后检查边界、长度单位和单元类型"
layout: reference
description: "转换后检查边界、长度单位和单元类型。"
cms_slug: "command-ideasunvtofoam"
---

<p>转换后检查边界、长度单位和单元类型。</p><h2>开始前</h2>
<p>准备 I-DEAS Universal .unv 文件；按实际导出单位核对坐标，确保所需边界分组随文件一并导出。</p>
<h2>示例 1：导入 UNV 网格</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv
</code></pre>
<p>读取通用格式中的网格与分组，写出 OpenFOAM polyMesh。检查单元数量和边界名称与原模型是否对应。</p>
<h2>示例 2：导出边界调试几何</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv -dump
</code></pre>
<p>转换时额外写出 boundaryFaces.obj，便于可视化核对读取到的边界面。适合排查分组与几何位置不对应的问题。</p>
<h2>示例 3：转换毫米坐标</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh-mm.unv
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>导入完成后统一将节点坐标换算为米。后续 checkMesh 的边界框应对应模型的实际米制尺寸。</p>
<h2>示例 4：在独立案例检查全部连接</h2>
<pre><code class="language-bash">ideasUnvToFoam /data/mesh.unv -case ../unvCase
checkMesh -case ../unvCase -constant -allTopology
</code></pre>
<p>转换结果写入 unvCase，随后检查面连接和不连通区域。便于把格式转换问题与已有求解设置分开排查。</p>
<h2>示例 5：整理分组后查看外形</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv
createPatch -overwrite
foamToSurface unv-boundary.obj -constant
</code></pre>
<p>先依据导入名称编写 createPatchDict，再整理边界并导出外表面。对照原始几何检查入口、出口和壁面归属。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dump</code></td><td>将边界面写为 boundaryFaces.obj，便于调试。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ideasUnvToFoam/ideasUnvToFoam.C">源码与说明</a> · <a href="/assets/command-help/ideasunvtofoam.txt">帮助文本</a></p>
