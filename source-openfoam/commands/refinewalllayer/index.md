---
title: "refineWallLayer · 输入比例指定边的细分位置"
layout: reference
description: "输入比例指定边的细分位置。"
cms_slug: "command-refinewalllayer"
---

<p>输入比例指定边的细分位置。</p><h2>开始前</h2>
<p>已有包含指定壁面 patch 的网格；edgeFraction 决定沿壁面相连边切分的位置，取 0–1 之间的比例。</p>
<h2>示例 1：细化一个壁面附近的单元</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.5
</code></pre>
<p>对 walls 相邻的单元按一半比例切分，形成更细的近壁层。输出后检查壁面法向的单元尺寸。</p>
<h2>示例 2：获得更薄的第一层</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.2
</code></pre>
<p>将壁面附近切分比例设为 0.2，得到较薄的靠壁部分。与 0.5 的独立副本比较第一层高度和网格质量。</p>
<h2>示例 3：同时选择多组壁面</h2>
<pre><code class="language-bash">refineWallLayer '(upperWall lowerWall)' 0.3
</code></pre>
<p>同时处理上下壁面。两侧边界名称应与 boundary 文件一致，检查狭窄区域是否产生互相影响的切分。</p>
<h2>示例 4：把处理限制到单元集合</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.25 -useSet nearWallCells
</code></pre>
<p>仅在指定壁面附近且属于 nearWallCells 的单元中进行操作。适合局部壁面加密，保留其余区域原有分辨率。</p>
<h2>示例 5：在副本更新并检查</h2>
<pre><code class="language-bash">refineWallLayer '(walls)' 0.2 -overwrite
checkMesh -constant -allGeometry
</code></pre>
<p>更新原网格后检查近壁单元的长宽比、体积与非正交性。第一层高度仍需结合雷诺数、壁面模型及目标 y⁺ 估算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-useSet &lt;name&gt;</code></td><td>仅细化指定 cellSet 内的单元。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refineWallLayer/refineWallLayer.C">源码与说明</a> · <a href="/assets/command-help/refinewalllayer.txt">帮助文本</a></p>
