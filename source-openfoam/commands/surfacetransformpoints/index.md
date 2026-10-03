---
title: "surfaceTransformPoints · 对表面网格进行平移、旋转或缩放"
layout: reference
description: "对表面网格进行平移、旋转或缩放。"
cms_slug: "command-surfacetransformpoints"
---

<p>对表面网格进行平移、旋转或缩放。</p><h2>开始前</h2>
<p>准备受支持的表面文件；输入与输出使用不同文件名，便于直接比较变换前后的边界框。</p>
<h2>示例 1：将毫米转换为米</h2>
<pre><code class="language-bash">surfaceTransformPoints body-mm.stl body-m.stl -read-scale 0.001
</code></pre>
<p>读取坐标时统一乘 0.001。长度 100 的零件变为 0.1，与 OpenFOAM 算例常用的米制输入对应。</p>
<h2>示例 2：平移几何</h2>
<pre><code class="language-bash">surfaceTransformPoints body.stl shifted.stl -translate '(0.1 0 0)'
</code></pre>
<p>将全部顶点沿 x 正方向移动 0.1 个坐标单位。形状和尺寸保持不变，边界框的 x 范围整体平移。</p>
<h2>示例 3：绕指定轴旋转</h2>
<pre><code class="language-bash">surfaceTransformPoints blade.stl blade-rotated.stl -rotate-angle '((0 0 1) 45)'
</code></pre>
<p>绕过原点的 z 轴旋转 45°。查看叶片与入口方向的关系，确认旋转正向符合右手规则。</p>
<h2>示例 4：绕几何中心旋转</h2>
<pre><code class="language-bash">surfaceTransformPoints body.stl body-rotated.stl -auto-centre -rotate-z 90
</code></pre>
<p>自动使用几何中心作为旋转中心，绕 z 轴转 90°。适合改变零件方向，同时保持其中心位置。</p>
<h2>示例 5：缩放并对齐方向</h2>
<pre><code class="language-bash">surfaceTransformPoints body-mm.stl aligned.stl -read-scale 0.001 -rotate '((1 0 0) (0 0 1))'
</code></pre>
<p>先转换长度单位，再将原 x 方向转到 z 方向。组合变换后检查包围盒和关键定位点，供后续网格划分使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-auto-centre</code></td><td>以包围盒中心作为旋转中心。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-centre &lt;point&gt;</code></td><td>以指定点作为旋转中心。</td></tr><tr><td><code>-cylToCart &lt;(originVec axisVec directionVec)&gt;</code></td><td>将圆柱坐标转换为笛卡尔坐标；依次提供原点、轴向和参考方向向量。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式；默认由文件扩展名判断。</td></tr><tr><td><code>-read-scale &lt;scalar | vector&gt;</code></td><td>对输入几何进行等比例或分方向缩放。</td></tr><tr><td><code>-recentre</code></td><td>在其他操作前，将包围盒重新居中。</td></tr><tr><td><code>-rollPitchYaw &lt;vector&gt;</code></td><td>按 &#x27;(roll pitch yaw)&#x27; 指定滚转、俯仰、偏航角，单位为度。</td></tr><tr><td><code>-rotate &lt;(vectorA vectorB)&gt;</code></td><td>将 vectorA 方向旋转到 vectorB 方向，例如 &#x27;((1 0 0) (0 0 1))&#x27;。</td></tr><tr><td><code>-rotate-angle &lt;(vector angle)&gt;</code></td><td>绕指定向量旋转给定角度，例如 &#x27;((1 0 0) 45)&#x27;，角度单位为度。</td></tr><tr><td><code>-rotate-x &lt;deg&gt;</code></td><td>绕 x 轴旋转，角度单位为度。</td></tr><tr><td><code>-rotate-y &lt;deg&gt;</code></td><td>绕 y 轴旋转，角度单位为度。</td></tr><tr><td><code>-rotate-z &lt;deg&gt;</code></td><td>绕 z 轴旋转，角度单位为度。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-translate &lt;vector&gt;</code></td><td>在旋转前按指定向量平移。</td></tr><tr><td><code>-write-format &lt;type&gt;</code></td><td>指定输出格式；默认由文件扩展名判断。</td></tr><tr><td><code>-write-scale &lt;scalar | vector&gt;</code></td><td>对输出几何进行等比例或分方向缩放。</td></tr><tr><td><code>-yawPitchRoll &lt;vector&gt;</code></td><td>按 &#x27;(yaw pitch roll)&#x27; 指定偏航、俯仰、滚转角，单位为度。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceTransformPoints/surfaceTransformPoints.C">源码与说明</a> · <a href="/assets/command-help/surfacetransformpoints.txt">帮助文本</a></p>
