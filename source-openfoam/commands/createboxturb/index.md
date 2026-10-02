---
title: "createBoxTurb · 按给定能谱和模态叠加生成各向同性湍流盒"
layout: reference
description: "按给定能谱和模态叠加生成各向同性湍流盒。"
cms_slug: "command-createboxturb"
---

<p>按给定能谱和模态叠加生成各向同性湍流盒。</p><h2>开始前</h2>
<p>constant/createBoxTurbDict 包含 L、N、nModes 和 Ek；L 是盒长，N 是网格数，Ek 为波数能谱函数。</p>
<h2>示例 1：仅创建周期盒网格</h2>
<pre><code class="language-bash">createBoxTurb -createBlockMesh
</code></pre>
<p>按L、N生成带周期边界的盒网格后退出，先检查尺寸和分辨率。</p>
<h2>示例 2：生成湍流速度</h2>
<pre><code class="language-bash">createBoxTurb
</code></pre>
<p>在已有对应盒网格上叠加nModes个模态，写出U、k与div(U)，日志报告波数范围和场统计。</p>
<h2>示例 3：连贯创建并检查</h2>
<pre><code class="language-bash">createBoxTurb -createBlockMesh
checkMesh
createBoxTurb
</code></pre>
<p>先生成网格、检查周期连接，再生成速度；把几何错误与谱参数问题分开定位。</p>
<h2>示例 4：增加模态数量</h2>
<pre><code class="language-bash">foamDictionary constant/createBoxTurbDict -entry nModes -set 500
createBoxTurb
</code></pre>
<p>已有有效L、N、Ek时把模态数设为500，比较能谱近似与生成成本；模态数至少应大于1。</p>
<h2>示例 5：加密周期盒</h2>
<pre><code class="language-bash">foamDictionary constant/createBoxTurbDict -entry N -set '(64 64 64)'
createBoxTurb -createBlockMesh
createBoxTurb
</code></pre>
<p>在独立副本上改为64立方网格，重新生成网格和场；更小单元允许更高的离散最大波数。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-createBlockMesh</code></td><td>生成块网格后退出。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createBoxTurb/createBoxTurb.C">源码与说明</a> · <a href="/assets/command-help/createboxturb.txt">帮助文本</a></p>
