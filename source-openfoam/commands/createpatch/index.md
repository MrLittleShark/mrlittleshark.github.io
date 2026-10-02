---
title: "createPatch · 把已有边界面或 faceSet 重组为指定 patch"
layout: reference
description: "把已有边界面或 faceSet 重组为指定 patch。"
cms_slug: "command-createpatch"
---

<p>把已有边界面或 faceSet 重组为指定 patch。</p><h2>开始前</h2>
<p>已有网格和 system/createPatchDict；字典中的 patches/source 对应实际边界或 faceSet。</p>
<h2>示例 1：按默认字典重组边界</h2>
<pre><code class="language-bash">createPatch
</code></pre>
<p>读取 createPatchDict，把选定面归入新 patch，输出新网格时间目录；检查日志中的新 patch 名称和面数。</p>
<h2>示例 2：将入口拆分方案写回网格</h2>
<pre><code class="language-bash">createPatch -dict system/createPatch-inletDict -overwrite
</code></pre>
<p>替代字典描述入口面分组；-overwrite 更新当前 boundary 与相关网格文件，便于后续按新名称填写 0/ 下边界条件。</p>
<h2>示例 3：检查周期面配对</h2>
<pre><code class="language-bash">createPatch -writeObj
</code></pre>
<p>字典已经定义 cyclic 配对时，额外写 OBJ 匹配几何，供可视化检查两侧位置与对应关系。</p>
<h2>示例 4：为指定区域整理边界</h2>
<pre><code class="language-bash">createPatch -region fluid -overwrite
</code></pre>
<p>只重组 fluid 区域的边界，适合多区域案例中单独修正流体入口、出口和壁面名称。</p>
<h2>示例 5：依次处理所有区域</h2>
<pre><code class="language-bash">createPatch -allRegions -overwrite
checkMesh -allRegions
</code></pre>
<p>regionProperties 已列出各区域且相应字典已准备好；-allRegions 对所有区域执行重组，再逐区域检查结果。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 createPatchDict 文件。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-writeObj</code></td><td>将周期边界匹配过程写为 OBJ 文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-createpatchdict/">createPatchDict</a></p><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createPatch/createPatch.C">源码与说明</a> · <a href="/assets/command-help/createpatch.txt">帮助文本</a></p>
