---
title: "smapToFoam · 把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场"
layout: reference
description: "把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场。"
cms_slug: "command-smaptofoam"
---

<p>把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场。</p><h2>开始前</h2>
<p>已有与SMAP数据对应的网格、当前时间目录中的目标场文件；支持SU→U、P→p、T→T等固定名称映射。</p>
<h2>示例 1：导入已有SMAP结果</h2>
<pre><code class="language-bash">smapToFoam results.smap
</code></pre>
<p>位置参数是SMAP文件；程序根据当前目录已有字段读取对应数据并重写字段内部值。</p>
<h2>示例 2：导入到指定案例</h2>
<pre><code class="language-bash">smapToFoam -case ./convertedCase results.smap
</code></pre>
<p>convertedCase已建立相同几何对应网格和目标场；-case决定结果写入的案例。</p>
<h2>示例 3：把SMAP结果作为重启初值</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set startTime
foamDictionary system/controlDict -entry startTime -set 0
smapToFoam steady.smap
</code></pre>
<p>把当前实例明确设为0，导入数据到已准备的0/U、0/p等文件，供后续求解器从此状态启动。</p>
<h2>示例 4：仅导入已有目标标量</h2>
<pre><code class="language-bash">smapToFoam -case ./temperatureImport thermal.smap
</code></pre>
<p>temperatureImport当前时间只准备需要的T等目标字段时，工具按已有文件建立名称映射；检查SMAP内相应列与目标单位。</p>
<h2>示例 5：导入后可视化核对</h2>
<pre><code class="language-bash">smapToFoam results.smap
foamToVTK -time 0 -fields '(U p T)' -name VTK-smap
</code></pre>
<p>本案例当前实例为0并已有U、p、T；导出导入后的字段，检查空间分布、速度方向和数量级。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/smapToFoam/smapToFoam.C">源码与说明</a> · <a href="/assets/command-help/smaptofoam.txt">帮助文本</a></p>
