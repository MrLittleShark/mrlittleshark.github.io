---
title: "surfaceFind · 用于定位和检查表面坐标"
layout: reference
description: "用于定位和检查表面坐标。"
cms_slug: "command-surfacefind"
---

<p>用于定位和检查表面坐标。</p><h2>开始前</h2>
<p>给定表面文件和查询点；未指定的坐标分量为0。输出最近面、顶点等定位信息。</p>
<h2>示例 1：查询原点附近表面</h2>
<pre><code class="language-bash">surfaceFind body.stl
</code></pre>
<p>以(0,0,0)查询最近面与顶点，用于确认几何与坐标原点的位置关系。</p>
<h2>示例 2：定位入口中心附近</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 body.stl
</code></pre>
<p>查询点为(0.1,0,0)，适合轴向沿x的管道入口或截面附近定位。</p>
<h2>示例 3：查询侧壁附近</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 body.stl
</code></pre>
<p>明确两个坐标分量，查询侧壁附近最近三角面，便于定位局部几何。</p>
<h2>示例 4：查询三维缺陷点</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 -z 0.01 body.stl
</code></pre>
<p>使用检查报告给出的三维坐标，找出对应面和顶点编号。</p>
<h2>示例 5：比较修补前后位置</h2>
<pre><code class="language-bash">surfaceFind -x 0.1 -y 0.025 -z 0.01 raw.stl
surfaceFind -x 0.1 -y 0.025 -z 0.01 repaired.stl
</code></pre>
<p>对同一个查询点比较两份表面，观察最近点距离及所在面是否随修补发生明显改变。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-x &lt;X&gt;</code></td><td>设置点的 x 坐标（非零值时采用）。</td></tr><tr><td><code>-y &lt;Y&gt;</code></td><td>设置点的 y 坐标（非零值时采用）。</td></tr><tr><td><code>-z &lt;Z&gt;</code></td><td>设置点的 y 坐标（非零值时采用）。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFind/surfaceFind.C">源码与说明</a> · <a href="/assets/command-help/surfacefind.txt">帮助文本</a></p>
