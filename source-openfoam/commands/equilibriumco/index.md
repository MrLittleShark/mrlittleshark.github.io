---
title: "equilibriumCO · 输出四个气相解离反应在固定温压下的平衡常数 Kc"
layout: reference
description: "输出四个气相解离反应在固定温压下的平衡常数 Kc。"
cms_slug: "command-equilibriumco"
---

<p>输出四个气相解离反应在固定温压下的平衡常数 Kc。</p><h2>开始前</h2>
<p>v2512源码固定P=1e5Pa、T=3000K，读取constant/thermoData；默认工具输出反应平衡常数，所需物种包括CO2、CO、O2、O、H2O、H2、H、OH、N2。</p>
<h2>示例 1：准备最小热化学案例</h2>
<pre><code class="language-bash">mkdir -p coCase/constant coCase/system
cat &gt; coCase/system/controlDict &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object controlDict; }
application equilibriumCO;
startFrom startTime;
startTime 0;
stopAt endTime;
endTime 1;
deltaT 1;
writeControl timeStep;
writeInterval 1;
EOF
cat &gt; coCase/constant/thermoData &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object thermoData; }
#includeEtc "thermoData/thermoData"
EOF
equilibriumCO -case coCase
</code></pre>
<p>通过includeEtc引用安装版热物性库，运行后输出4个Kc，依次对应CO2、O2和两条H2O解离反应。</p>
<h2>示例 2：给输出标明反应</h2>
<pre><code class="language-bash">equilibriumCO -case coCase | awk 'BEGIN {split("CO2_to_CO O2_to_O H2O_to_H2 H2O_to_H_OH",r," ")} /Kc\(EQreactions\)/ {i++; print r[i],$NF}'
</code></pre>
<p>把每个Kc与源码中的反应顺序对应，方便制作温度依赖表或检查反向反应关系。</p>
<h2>示例 3：编译2000K的个人版本</h2>
<pre><code class="language-bash">cp -r "$WM_PROJECT_DIR/applications/utilities/thermophysical/equilibriumCO" equilibriumCOStudy-src
sed -i 's/const scalar T = 3000.0;/const scalar T = 2000.0;/' equilibriumCOStudy-src/equilibriumCO.C
sed -i 's@$(FOAM_APPBIN)/equilibriumCO@$(FOAM_USER_APPBIN)/equilibriumCOStudy@' equilibriumCOStudy-src/Make/files
(cd equilibriumCOStudy-src &amp;&amp; wmake)
equilibriumCOStudy -case coCase
</code></pre>
<p>只修改个人源码副本的温度，编译为新程序名；与基准3000K的4个Kc比较，原安装程序保持原参数。</p>
<h2>示例 4：在个人版本修改压力</h2>
<pre><code class="language-bash">sed -i 's/const scalar P = 1e5;/const scalar P = 1e6;/' equilibriumCOStudy-src/equilibriumCO.C
(cd equilibriumCOStudy-src &amp;&amp; wmake)
equilibriumCOStudy -case coCase
</code></pre>
<p>将个人版本输入压力设为1MPa并重新编译；观察所用理想气体热力学中Kc的压力依赖，和实际平衡组成的压力响应分别讨论。</p>
<h2>示例 5：增加一个反向反应</h2>
<pre><code class="language-bash">sed -i '/for (const thermo&amp; react : EQreactions)/i\    EQreactions.emplace_back((H2 + 0.5*O2 == H2O));' equilibriumCOStudy-src/equilibriumCO.C
(cd equilibriumCOStudy-src &amp;&amp; wmake)
equilibriumCOStudy -case coCase
</code></pre>
<p>在循环前增加水生成反应，输出变为5个Kc；新增反应与原第三条互为逆反应，可检查相同温压下平衡常数的倒数关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/equilibriumCO/equilibriumCO.C">源码与说明</a> · <a href="/assets/command-help/equilibriumco.txt">帮助文本</a></p>
