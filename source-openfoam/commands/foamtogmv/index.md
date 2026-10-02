---
title: "foamToGMV · 按 conversionProperties 导出六面体网格和字段为 GMV"
layout: reference
description: "按 conversionProperties 导出六面体网格和字段为 GMV。"
cms_slug: "command-foamtogmv"
---

<p>按 conversionProperties 导出六面体网格和字段为 GMV。</p><h2>开始前</h2>
<p>网格采用hex单元，constant/conversionProperties定义startTime、vector、format、cells；该旧式工具从字典而非时间CLI选择起始范围。</p>
<h2>示例 1：创建最小转换配置</h2>
<pre><code class="language-bash">cat &gt; constant/conversionProperties &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object conversionProperties; }
startTime -1;
vector U;
format ascii;
cells hex;
EOF
foamToGMV
</code></pre>
<p>写入完整转换字典；导出晚于-1的数值时间，U作为GMV速度，结果命名为plotGMV.*。</p>
<h2>示例 2：只处理较晚结果</h2>
<pre><code class="language-bash">foamDictionary constant/conversionProperties -entry startTime -set 1
foamToGMV
</code></pre>
<p>工具只转换严格晚于1的时间，适合跳过初始发展阶段。</p>
<h2>示例 3：把平均速度作为GMV速度</h2>
<pre><code class="language-bash">foamDictionary constant/conversionProperties -entry vector -set UMean
foamToGMV
</code></pre>
<p>结果中已有UMean时，将它作为GMV的velocity数据，便于查看统计平均流场。</p>
<h2>示例 4：导出生成的旋流场</h2>
<pre><code class="language-bash">engineSwirl
foamToGMV
</code></pre>
<p>发动机案例使用hex网格、vector为U且转换起始范围包含该场时，先生成初始旋流，再导出供GMV检查。</p>
<h2>示例 5：检查ASCII文件结构</h2>
<pre><code class="language-bash">foamToGMV
head -n 8 plotGMV.1
</code></pre>
<p>转换后查看首个实际生成文件的头部；如编号不同，使用日志中的文件名。应能看到gmvinput和nodes等记录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToGMV/foamToGMV.C">源码与说明</a> · <a href="/assets/command-help/foamtogmv.txt">帮助文本</a></p>
