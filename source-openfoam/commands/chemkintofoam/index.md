---
title: "chemkinToFoam · 把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典"
layout: reference
description: "把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典。"
cms_slug: "command-chemkintofoam"
---

<p>把 CHEMKIN 机理、热力学和输运数据转换成 OpenFOAM 字典。</p><h2>开始前</h2>
<p>准备同一机理对应的CHEMKIN反应文件、热力学文件和输运文件；五个位置参数最后两项是输出化学与热物性字典。</p>
<h2>示例 1：转换一套完整机理</h2>
<pre><code class="language-bash">chemkinToFoam chem.inp therm.dat tran.dat reactions thermodynamics
</code></pre>
<p>前三个文件提供反应、JANAF热物性和输运信息，结果写为reactions与thermodynamics。</p>
<h2>示例 2：直接放入案例constant目录</h2>
<pre><code class="language-bash">mkdir -p constant
chemkinToFoam mechanism/chem.inp mechanism/therm.dat mechanism/tran.dat constant/reactions constant/thermo.compressibleGas
</code></pre>
<p>集中从mechanism读取输入，生成案例中可引用的两个字典；thermophysicalProperties应指向相应文件。</p>
<h2>示例 3：读取新版热力学格式</h2>
<pre><code class="language-bash">chemkinToFoam -newFormat chem.inp therm-new.dat tran.dat reactions-new thermodynamics-new
</code></pre>
<p>热力学文件采用该解析器支持的newFormat时启用选项，输出使用不同文件名便于比较。</p>
<h2>示例 4：转换后检查物种清单</h2>
<pre><code class="language-bash">chemkinToFoam chem.inp therm.dat tran.dat constant/reactions constant/thermo.compressibleGas
foamDictionary constant/reactions -entry species -value
</code></pre>
<p>列出转换后注册的物种，核对后续组分初始场的名称、大小写和机理中的物种是否一致。</p>
<h2>示例 5：比较简化机理与详细机理</h2>
<pre><code class="language-bash">mkdir -p converted/detailed converted/reduced
chemkinToFoam detailed/chem.inp detailed/therm.dat detailed/tran.dat converted/detailed/reactions converted/detailed/thermo
chemkinToFoam reduced/chem.inp reduced/therm.dat reduced/tran.dat converted/reduced/reactions converted/reduced/thermo
</code></pre>
<p>两套机理各用自身配套热物性、输运文件，输出分开保存，再比较物种数、反应数和目标工况的计算成本。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-newFormat</code></td><td>按新格式读取 Chemkin 热物性文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/chemkinToFoam/chemkinToFoam.C">源码与说明</a> · <a href="/assets/command-help/chemkintofoam.txt">帮助文本</a></p>
