---
title: "combinePatchFaces · 将同一单元上符合角度和质量要求的相邻边界面合并"
layout: reference
description: "将同一单元上符合角度和质量要求的相邻边界面合并。"
cms_slug: "command-combinepatchfaces"
---

<p>将同一单元上符合角度和质量要求的相邻边界面合并。</p><h2>开始前</h2>
<p>网格某些单元在同一 patch 上有多个近共面的边界面；工具将符合角度与凸凹条件的面合并。示例应在独立案例副本比较。</p>
<h2>示例 1：合并近共面的边界面</h2>
<pre><code class="language-bash">combinePatchFaces 5
</code></pre>
<p>以 5° 特征角判断可合并面，写出修改后的网格。适合整理几乎共面的碎面，检查边界面数变化。</p>
<h2>示例 2：提高允许折角</h2>
<pre><code class="language-bash">combinePatchFaces 20
</code></pre>
<p>允许更大的夹角参与合并，简化程度通常提高。比较外形与网格质量，确认曲面细节仍满足所需分辨率。</p>
<h2>示例 3：限制允许的凹角</h2>
<pre><code class="language-bash">combinePatchFaces 10 -concaveAngle 15
</code></pre>
<p>同时使用 10° 特征角和 15° 凹角参数，控制形成多边形面的几何形状。检查输出面是否出现不适合的凹形结构。</p>
<h2>示例 4：启用网格质量约束</h2>
<pre><code class="language-bash">combinePatchFaces 10 -meshQuality
</code></pre>
<p>读取 system/meshQualityDict 中的质量约束来检查合并操作。该字典应已配置完整，适合在面简化时保留明确质量条件。</p>
<h2>示例 5：在分解网格中合并</h2>
<pre><code class="language-bash">mpirun -np 4 combinePatchFaces 10 -parallel -overwrite
mpirun -np 4 checkMesh -parallel
</code></pre>
<p>四个子域均使用同一角度设置，直接更新分区网格。完成后检查处理器边界和新面质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-concaveAngle &lt;degrees&gt;</code></td><td>设置凹角阈值，范围 0–180°，默认为 30°。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-meshQuality</code></td><td>从 system/meshQualityDict 读取自定义网格质量标准。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/combinePatchFaces/combinePatchFaces.C">源码与说明</a> · <a href="/assets/command-help/combinepatchfaces.txt">帮助文本</a></p>
