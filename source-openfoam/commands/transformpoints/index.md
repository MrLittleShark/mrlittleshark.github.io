---
title: "transformPoints · 平移、旋转或缩放网格坐标，可同步旋转向量与张量场"
layout: reference
description: "平移、旋转或缩放网格坐标，可同步旋转向量与张量场。"
cms_slug: "command-transformpoints"
---

<p>平移、旋转或缩放网格坐标，可同步旋转向量与张量场。</p><h2>开始前</h2>
<p>已有网格；变换直接更新所选时间的坐标，各独立几何方案从相同基础网格副本开始。</p>
<h2>示例 1：毫米坐标转为米</h2>
<pre><code class="language-bash">transformPoints -scale 0.001
</code></pre>
<p>所有坐标乘0.001，适合CAD导入坐标以毫米存储、案例长度统一采用米的网格。</p>
<h2>示例 2：平移模型</h2>
<pre><code class="language-bash">transformPoints -translate '(0.5 0 0)'
</code></pre>
<p>沿x方向平移0.5个当前长度单位；几何尺寸与单元连接保持不变。</p>
<h2>示例 3：绕指定轴旋转</h2>
<pre><code class="language-bash">transformPoints -rotate-angle '((0 0 1) 30)'
</code></pre>
<p>绕z轴转30度，角度单位为度；用于调整模型相对来流的朝向。</p>
<h2>示例 4：绕模型中心旋转并处理场</h2>
<pre><code class="language-bash">transformPoints -auto-centre -rotate-y 15 -rotateFields -time 0
</code></pre>
<p>使用包围盒中心为旋转中心，对0时刻网格及向量、张量场一起绕y轴转15度。</p>
<h2>示例 5：统一多区域坐标</h2>
<pre><code class="language-bash">transformPoints -allRegions -translate '(0 0 1)' -scale 0.001
</code></pre>
<p>对regionProperties中的全部区域使用同一变换；先平移，再按工具变换顺序缩放，适合多部件坐标统一，需按原坐标单位给出平移量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-auto-centre</code></td><td>以包围盒中心作为旋转中心。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-centre &lt;point&gt;</code></td><td>以指定点作为旋转中心。</td></tr><tr><td><code>-cylToCart &lt;(originVec axisVec directionVec)&gt;</code></td><td>将圆柱坐标转换为笛卡尔坐标；依次提供原点、轴向和参考方向向量。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-recentre</code></td><td>在其他操作前，将包围盒重新居中。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-rollPitchYaw &lt;vector&gt;</code></td><td>按 &#x27;(roll pitch yaw)&#x27; 指定滚转、俯仰、偏航角，单位为度。</td></tr><tr><td><code>-rotate &lt;(vectorA vectorB)&gt;</code></td><td>将 vectorA 方向旋转到 vectorB 方向，例如 &#x27;((1 0 0) (0 0 1))&#x27;。</td></tr><tr><td><code>-rotate-angle &lt;(vector angle)&gt;</code></td><td>绕指定向量旋转给定角度，例如 &#x27;((1 0 0) 45)&#x27;，角度单位为度。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（27 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-rotate-x &lt;deg&gt;</code></td><td>绕 x 轴旋转，角度单位为度。</td></tr><tr><td><code>-rotate-y &lt;deg&gt;</code></td><td>绕 y 轴旋转，角度单位为度。</td></tr><tr><td><code>-rotate-z &lt;deg&gt;</code></td><td>绕 z 轴旋转，角度单位为度。</td></tr><tr><td><code>-rotateFields</code></td><td>同时读取并变换向量场与张量场。</td></tr><tr><td><code>-scale &lt;scalar | vector&gt;</code></td><td>按指定系数缩放；例如从毫米转为米时使用 0.001 或 &#x27;(0.001 0.001 0.001)&#x27;。</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>指定查找网格并施加变换的时刻，默认使用最新时刻。</td></tr><tr><td><code>-translate &lt;vector&gt;</code></td><td>在旋转前按指定向量平移。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-yawPitchRoll &lt;vector&gt;</code></td><td>按 &#x27;(yaw pitch roll)&#x27; 指定偏航、俯仰、滚转角，单位为度。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/transformPoints/transformPoints.C">源码与说明</a> · <a href="/assets/command-help/transformpoints.txt">帮助文本</a></p>
