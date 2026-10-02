---
title: "mapFieldsPar · 在并行或串行布局间执行网格到网格场映射"
layout: reference
description: "在并行或串行布局间执行网格到网格场映射。"
cms_slug: "command-mapfieldspar"
---

<p>在并行或串行布局间执行网格到网格场映射。</p><h2>开始前</h2>
<p>源、目标网格及字段可读；MPI执行时目标分区与进程数一致，非一致边界映射规则已准备。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：按体积权重映射</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -mapMethod cellVolumeWeight
</code></pre>
<p>从源案例计算重叠体积权重，映射到当前目标；适合不同分辨率但空间重叠的网格。</p>
<h2>示例 2：只映射速度与压力</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -fields '(U p)' -sourceTime latestTime
</code></pre>
<p>限制字段为U、p，读取源最新时刻；其他目标字段保留原设置。</p>
<h2>示例 3：相同网格直接映射</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -consistent -mapMethod direct
</code></pre>
<p>源目标几何和边界一致且满足直接寻址条件时，采用direct方法传递字段。</p>
<h2>示例 4：选择边界面积加权</h2>
<pre><code class="language-bash">mapFieldsPar ../sourceCase -mapMethod cellVolumeWeight -patchMapMethod faceAreaWeight
</code></pre>
<p>内部按体积、边界按面积加权，适合面划分不同但边界相互覆盖的映射。</p>
<h2>示例 5：并行映射并保留欧拉场</h2>
<pre><code class="language-bash">mpirun -np 4 mapFieldsPar ../sourceCase -parallel -fields '(U p T)' -no-lagrangian
</code></pre>
<p>目标已有4分区；并行映射所选欧拉场，-no-lagrangian跳过粒子位置和粒子属性。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-consistent</code></td><td>用于源与目标的几何、边界条件完全一致的映射。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-fields &lt;wordRes&gt;</code></td><td>选择要处理的一个或多个场，默认全部；例如 T 或 &#x27;(p T U &quot;alpha.*&quot;)&#x27;。</td></tr><tr><td><code>-mapMethod &lt;word&gt;</code></td><td>指定映射方法：direct、mapNearest、cellVolumeWeight 或 correctedCellVolumeWeight。</td></tr><tr><td><code>-no-lagrangian</code></td><td>跳过拉格朗日粒子位置和场的映射。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-patchMapMethod &lt;word&gt;</code></td><td>指定边界映射方法：direct、mapNearest 或 faceAreaWeight。</td></tr><tr><td><code>-procMapMethod &lt;word&gt;</code></td><td>指定进程分布映射方法：AABB 或 LOD。</td></tr><tr><td><code>-sourceRegion &lt;word&gt;</code></td><td>指定源网格区域。</td></tr><tr><td><code>-sourceTime &lt;scalar|&#x27;latestTime&#x27;&gt;</code></td><td>指定源算例时刻；latestTime 表示最新时刻。</td></tr><tr><td><code>-subtract</code></td><td>从目标场中减去映射后的源场。</td></tr><tr><td><code>-targetRegion &lt;word&gt;</code></td><td>指定目标网格区域。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-mapfieldsdict/">mapFieldsDict</a></p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mapFieldsPar/mapLagrangian.C">源码与说明</a> · <a href="/assets/command-help/mapfieldspar.txt">帮助文本</a></p>
