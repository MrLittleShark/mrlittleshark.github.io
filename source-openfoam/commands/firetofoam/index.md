---
title: "fireToFoam · 将 AVL/FIRE 多面体网格转换为 OpenFOAM 体网格"
layout: reference
description: "将 AVL/FIRE 多面体网格转换为 OpenFOAM 体网格。"
cms_slug: "command-firetofoam"
---

<p>将 AVL/FIRE 多面体网格转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备 AVL FIRE 的多面体网格文件，目标案例包含基本 system 配置。</p>
<h2>示例 1：导入 FIRE 网格</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma
</code></pre>
<p>读取 FIRE 多面体网格并写入 OpenFOAM。默认采用二进制网格输出，转换后可通过 checkMesh 查看结构。</p>
<h2>示例 2：导出为可读的网格文件</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -ascii
</code></pre>
<p>把网格写为 ASCII 格式，便于直接查看 points、faces 和 boundary。大型网格的文件体积会相应增加。</p>
<h2>示例 3：开启额外边检查</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -check
</code></pre>
<p>转换时增加边相关检查，帮助定位输入面连接问题。结合后续 checkMesh 的拓扑报告判断错误位置。</p>
<h2>示例 4：将毫米网格换算为米</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -scale 0.001
</code></pre>
<p>对顶点坐标进行单位转换。检查输出包围盒，再设置以米为长度单位的物性和边界条件。</p>
<h2>示例 5：在指定案例进行完整检查</h2>
<pre><code class="language-bash">fireToFoam /data/mesh.fpma -case ../fireCase -ascii -check
checkMesh -case ../fireCase -constant -allGeometry -allTopology
</code></pre>
<p>将转换和检查集中到 fireCase。查看负体积、面连接和边界分区，确认网格可用于后续求解。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>以 ASCII 文本格式写出，替代二进制格式。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-check</code></td><td>同时执行边检查。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;scale&gt;</code></td><td>设置几何缩放系数，默认为 1，即保持原尺寸。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fireToFoam/fireToFoam.C">源码与说明</a> · <a href="/assets/command-help/firetofoam.txt">帮助文本</a></p>
