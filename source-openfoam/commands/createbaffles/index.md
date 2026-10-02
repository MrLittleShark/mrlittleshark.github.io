---
title: "createBaffles · 将选定内部面改成挡板两侧的边界面"
layout: reference
description: "将选定内部面改成挡板两侧的边界面。"
cms_slug: "command-createbaffles"
---

<p>将选定内部面改成挡板两侧的边界面。</p><h2>开始前</h2>
<p>已有网格和 system/createBafflesDict；字典指定待转换面及两侧 patch。示例中的区域名、字典名应与案例一致。</p>
<h2>示例 1：生成挡板</h2>
<pre><code class="language-bash">createBaffles
</code></pre>
<p>读取默认字典，将选中内部面改成边界面，并在新的网格时间目录写入结果。日志给出选面与新边界信息。</p>
<h2>示例 2：使用另一套挡板位置</h2>
<pre><code class="language-bash">createBaffles -dict system/createBaffles-obliqueDict
</code></pre>
<p>预先准备描述斜挡板的字典；-dict 选择该文件，便于在相同基础网格上比较不同挡板位置。</p>
<h2>示例 3：直接更新预处理网格</h2>
<pre><code class="language-bash">createBaffles -overwrite
checkMesh
</code></pre>
<p>-overwrite 把改动写回当前网格。随后检查单元闭合、边界拓扑与网格质量，再继续初始化场。</p>
<h2>示例 4：只处理流体区域</h2>
<pre><code class="language-bash">createBaffles -region fluid -dict system/createBaffles-fluidDict -overwrite
</code></pre>
<p>多区域案例已有 fluid 网格；-region 限定修改对象，其他区域保持原有网格。结果是 fluid 内部新增的两侧挡板边界。</p>
<h2>示例 5：挡板生成后拆分共用顶点</h2>
<pre><code class="language-bash">createBaffles -overwrite
mergeOrSplitBaffles -split -overwrite
checkMesh
</code></pre>
<p>第一步创建面，第二步复制挡板两侧需要独立的顶点，适用于随后要让两侧独立运动的网格。最终检查拆分后的连通关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 createBafflesDict 文件。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-createbafflesdict/">createBafflesDict</a></p><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createBaffles/faceSelection/faceSelection.C">源码与说明</a> · <a href="/assets/command-help/createbaffles.txt">帮助文本</a></p>
