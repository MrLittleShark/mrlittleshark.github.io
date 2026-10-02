---
title: "mapFields · 将一个案例的场映射到当前目标案例"
layout: reference
description: "将一个案例的场映射到当前目标案例。"
cms_slug: "command-mapfields"
---

<p>将一个案例的场映射到当前目标案例。</p><h2>开始前</h2>
<p>源案例已有结果，目标案例已有网格和相容字段；非一致边界映射需要system/mapFieldsDict。</p>
<h2>示例 1：同几何案例之间映射</h2>
<pre><code class="language-bash">mapFields ../sourceCase -consistent
</code></pre>
<p>在目标案例目录执行；源、目标几何及边界对应一致时使用-consistent，映射源场作为目标初值。</p>
<h2>示例 2：明确源结果时间</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceTime 5 -consistent
</code></pre>
<p>读取源时间5，避免由默认时间选择引入混淆；目标写入时刻由目标controlDict确定。</p>
<h2>示例 3：使用最新源场</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceTime latestTime
</code></pre>
<p>源案例已有最新结果且目标配置mapFieldsDict；将源最终场映射到目标网格。</p>
<h2>示例 4：映射两个命名区域</h2>
<pre><code class="language-bash">mapFields ../sourceCase -sourceRegion fluid -targetRegion gas -sourceTime 5
</code></pre>
<p>源fluid映射到目标gas；两区域字段和边界映射已准备，用于区域名称不同的案例迁移。</p>
<h2>示例 5：从分区结果映射到目标</h2>
<pre><code class="language-bash">mapFields ../sourceCase -parallelSource -sourceTime latestTime
</code></pre>
<p>源结果位于processor目录时启用-parallelSource；工具从分区源数据读取，写目标案例字段。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-consistent</code></td><td>用于源与目标的几何、边界条件完全一致的映射。</td></tr><tr><td><code>-mapMethod &lt;word&gt;</code></td><td>指定映射方法。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallelSource</code></td><td>源算例已经过并行分解。</td></tr><tr><td><code>-parallelTarget</code></td><td>目标算例已经过并行分解。</td></tr><tr><td><code>-sourceDecomposeParDict &lt;file&gt;</code></td><td>从指定位置读取 decomposeParDict。</td></tr><tr><td><code>-sourceRegion &lt;word&gt;</code></td><td>指定源网格区域。</td></tr><tr><td><code>-sourceTime &lt;scalar|&#x27;latestTime&#x27;&gt;</code></td><td>指定源算例时刻；latestTime 表示最新时刻。</td></tr><tr><td><code>-subtract</code></td><td>从目标场中减去映射后的源场。</td></tr><tr><td><code>-targetDecomposeParDict &lt;file&gt;</code></td><td>从指定位置读取 decomposeParDict。</td></tr><tr><td><code>-targetRegion &lt;word&gt;</code></td><td>指定目标网格区域。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-mapfieldsdict/">mapFieldsDict</a></p><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mapFields/mapLagrangian.C">源码与说明</a> · <a href="/assets/command-help/mapfields.txt">帮助文本</a></p>
