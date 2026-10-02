---
title: "refinementLevel · 用于贴体变形前的网格"
layout: reference
description: "用于贴体变形前的网格。"
cms_slug: "command-refinementlevel"
---

<p>用于贴体变形前的网格。</p><h2>开始前</h2>
<p>用于经过 2×2×2 笛卡尔细化且尚未贴体变形的网格。程序按单元体积分类，写出级别场及相关集合。</p>
<h2>示例 1：识别体积对应的细化级别</h2>
<pre><code class="language-bash">refinementLevel
</code></pre>
<p>按体积分组生成 vol0、vol1 等 cellSet，以及用于显示的 refinementLevel 场。较小单元对应更高细化级别。</p>
<h2>示例 2：处理已有级别文件的案例</h2>
<pre><code class="language-bash">refinementLevel -readLevel
</code></pre>
<p>允许读取已经存在的 refinementLevel 标签文件继续处理；程序仍按当前体积分箱计算级别。适合检查已有细化状态与当前网格的对应关系。</p>
<h2>示例 3：在独立未贴体网格中检查</h2>
<pre><code class="language-bash">refinementLevel -case ../castellatedCase
</code></pre>
<p>指定只完成笛卡尔细化的案例。查看终端的体积组和每组单元数，判断目标区域细化是否达到预期。</p>
<h2>示例 4：使用建议集合继续细化</h2>
<pre><code class="language-bash">refinementLevel
refineHexMesh refCells
</code></pre>
<p>当工具明确报告写出非空 refCells 时执行第二步。该集合标出需要继续细化以改善相邻等级过渡的单元，之后重新检查等级关系。</p>
<h2>示例 5：并行检查细化等级</h2>
<pre><code class="language-bash">mpirun -np 4 refinementLevel -parallel
</code></pre>
<p>在已分解的未贴体网格上运行，写出各子域的级别信息。比较各进程报告，检查局部细化分布及跨子域的过渡区域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-readLevel</code></td><td>从 refinementLevel 文件读取细化等级。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/refinementLevel/refinementLevel.C">源码与说明</a> · <a href="/assets/command-help/refinementlevel.txt">帮助文本</a></p>
