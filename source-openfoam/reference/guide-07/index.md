---
title: "第 7 章　求解器与运行控制"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>7.1 跑一个算例的标准流程</h4>
<pre><code>$ run                                     # 去工作目录
$ cp -r $FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily .
$ cd pitzDaily
$ blockMesh              &gt; log.blockMesh  2&gt;&amp;1    # ① 建网格
$ checkMesh              &gt; log.checkMesh  2&gt;&amp;1    # ② 查网格
$ simpleFoam             &gt; log.simpleFoam 2&gt;&amp;1 &amp;  # ③ 后台求解，日志落盘
$ tail -f log.simpleFoam                          # ④ 实时看进度（Ctrl+C 只退出查看，不影响计算）
$ foamLog log.simpleFoam                          # ⑤ 提取残差
$ paraFoam                                        # ⑥ 可视化</code></pre>
<p>重定向可保存标准输出与标准错误，便于记录运行过程和排查异常。2&gt;&amp;1 将标准错误合并到标准输出。foamLog 可从求解器日志提取残差数据；foamMonitor 可用于监视相应的数据文件。</p>
<p>为什么用 &amp; 放后台：前台运行时终端被占住，网络一断（尤其是 ssh 到服务器）进程就被杀。更稳的做法见第 20 章的 nohup 与 tmux。</p>
<h4>7.2 求解器名字的构词法</h4>
<p>不要死记两百个求解器名，先掌握构词规律：</p>
<div class="table-scroll"><table>
<tr><th>词缀</th><th>含义</th><th>例子</th></tr>
<tr><td>ico</td><td>incompressible，层流不可压</td><td>icoFoam</td></tr>
<tr><td>simple</td><td>用 SIMPLE 算法 → 稳态</td><td>simpleFoam、rhoSimpleFoam</td></tr>
<tr><td>piso / pimple</td><td>PISO / PIMPLE 算法 → 瞬态</td><td>pisoFoam、pimpleFoam</td></tr>
<tr><td>rho</td><td>可压缩（解密度）</td><td>rhoPimpleFoam、rhoCentralFoam</td></tr>
<tr><td>buoyant</td><td>含浮力（自然对流）</td><td>buoyantSimpleFoam</td></tr>
<tr><td>inter</td><td>两相 VOF（inter-face）</td><td>interFoam、interIsoFoam</td></tr>
<tr><td>multiphase</td><td>多于两相</td><td>multiphaseInterFoam</td></tr>
<tr><td>reacting</td><td>含化学反应</td><td>reactingFoam</td></tr>
<tr><td>cht</td><td>共轭传热（流固耦合传热）</td><td>chtMultiRegionFoam</td></tr>
<tr><td>over</td><td>重叠网格（overset）</td><td>overInterDyMFoam</td></tr>
<tr><td>DyM</td><td>动网格（v1706 后大多已并入主求解器）</td><td>pimpleFoam 直接支持动网格</td></tr>
<tr><td>Foam</td><td>后缀，无实义</td><td>——</td></tr>
</table></div>
<p>由此可以推断：想算”瞬态、可压、带反应”的问题，八成是 reactingFoam；“稳态、不可压、湍流”就是 simpleFoam。这个推断能力比背表有用。</p>
<h4>7.3 常用求解器速查</h4>
<p>基础</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>解什么</th><th>关键字典</th></tr>
<tr><td>laplacianFoam</td><td>纯扩散方程（导热）</td><td>transportProperties（DT）</td></tr>
<tr><td>scalarTransportFoam</td><td>给定流场下的标量输运</td><td>transportProperties</td></tr>
<tr><td>potentialFoam</td><td>势流。常用来给复杂算例造初场</td><td>——</td></tr>
</table></div>
<p>不可压缩</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用</th></tr>
<tr><td>icoFoam</td><td>层流、瞬态、牛顿流体。教学入门用</td></tr>
<tr><td>simpleFoam</td><td>稳态、湍流。外流绕流、管道，最常用</td></tr>
<tr><td>pimpleFoam</td><td>瞬态、湍流，允许大 Courant 数（LES/URANS 主力）</td></tr>
<tr><td>pisoFoam</td><td>瞬态、湍流，要求 \(\mathrm{Co} &lt; 1\)（做 LES 时精度更可控）</td></tr>
<tr><td>boundaryFoam</td><td>一维充分发展边界层，标定壁面函数用</td></tr>
<tr><td>adjointShapeOptimizationFoam</td><td>伴随法形状优化</td></tr>
</table></div>
<p>可压缩</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用</th></tr>
<tr><td>rhoSimpleFoam</td><td>稳态可压</td></tr>
<tr><td>rhoPimpleFoam</td><td>瞬态可压（亚声速到跨声速），基于压力</td></tr>
<tr><td>rhoCentralFoam</td><td>基于密度的中心格式，激波捕捉。超声速、激波管、爆炸问题首选</td></tr>
<tr><td>sonicFoam</td><td>瞬态跨/超声速（较老，多数场景已被上面两个取代）</td></tr>
</table></div>
<p>传热/浮力</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用</th></tr>
<tr><td>buoyantSimpleFoam / buoyantPimpleFoam</td><td>稳态/瞬态自然对流</td></tr>
<tr><td>chtMultiRegionFoam</td><td>流固共轭传热（多区域）</td></tr>
<tr><td>thermoFoam</td><td>冻结流场，只解能量方程</td></tr>
</table></div>
<p>多相</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用</th></tr>
<tr><td>interFoam</td><td>两相不可压 VOF（溃坝、自由液面）。多相入门必学</td></tr>
<tr><td>interIsoFoam</td><td>用 isoAdvector 几何界面重构，界面更锐利</td></tr>
<tr><td>compressibleInterFoam</td><td>两相且可压（空化、水下爆炸）</td></tr>
<tr><td>multiphaseInterFoam</td><td>三相及以上 VOF</td></tr>
<tr><td>interMixingFoam</td><td>两相 + 其中一相可混溶</td></tr>
<tr><td>cavitatingFoam</td><td>空化</td></tr>
<tr><td>driftFluxFoam</td><td>沉降/悬浮泥沙类</td></tr>
<tr><td>multiphaseEulerFoam</td><td>欧拉-欧拉多相（气泡塔、流化床）</td></tr>
<tr><td>potentialFreeSurfaceFoam</td><td>小变形自由液面（势流近似）</td></tr>
</table></div>
<p>颗粒 / 反应 / 其他</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用</th></tr>
<tr><td>DPMFoam / MPPICFoam</td><td>离散颗粒（稠密颗粒用 MPPIC）</td></tr>
<tr><td>icoUncoupledKinematicParcelFoam</td><td>单向耦合示踪颗粒</td></tr>
<tr><td>reactingFoam</td><td>燃烧/化学反应</td></tr>
<tr><td>XiFoam</td><td>预混燃烧</td></tr>
<tr><td>fireFoam</td><td>火灾（含辐射、热解）</td></tr>
<tr><td>sprayFoam</td><td>喷雾燃烧</td></tr>
<tr><td>chemFoam</td><td>零维化学反应器（验证机理用）</td></tr>
<tr><td>solidDisplacementFoam</td><td>线弹性固体应力</td></tr>
<tr><td>electrostaticFoam / mhdFoam / magneticFoam</td><td>静电 / 磁流体 / 静磁</td></tr>
<tr><td>overPimpleDyMFoam / overInterDyMFoam</td><td>重叠网格版本</td></tr>
</table></div>
<p>怎么确认本机到底有哪些：</p>
<pre><code>$ ls $FOAM_APPBIN | grep -i foam | sort | less
$ ls $FOAM_SOLVERS/*                      # 按类别看源码目录</code></pre>
<h4>7.4 求解器的运行选项</h4>
<pre><code>simpleFoam [-case &lt;dir&gt;] [-parallel] [-postProcess] [-dry-run] [-noFunctionObjects]
           [-fileHandler collated] [-libs &#x27;(&quot;libMyBC.so&quot;)&#x27;] [-region &lt;name&gt;]</code></pre>
<p>-postProcess：把求解器当后处理器用（非常重要的技巧）</p>
<pre><code># 用求解器自己的物理模型，对已有结果做后处理（例如算 yPlus 需要湍流模型信息）
$ simpleFoam -postProcess -func yPlus -latestTime
$ pimpleFoam -postProcess -func &quot;grad(p)&quot; -time &#x27;1:5&#x27;</code></pre>
<p>为什么要用 -postProcess 而不是 postProcess：postProcess 是通用工具，不知道你的湍流模型和物性；而 &lt;求解器&gt; -postProcess 会加载与求解时完全相同的模型，所以像 yPlus、wallShearStress、turbulenceFields 这类依赖模型的量必须用它。</p>
<p>-dry-run：开算前的语法体检</p>
<pre><code>$ interFoam -dry-run</code></pre>
<p>它会读完所有字典、建好场、然后退出。字典写错、边界条件名拼错、场文件缺失都会在这一步暴露——比跑 3 小时后崩掉划算得多。</p>
<h4>7.5 续算、中止与在线改参数</h4>
<p>续算（从上次结果接着算）</p>
<pre><code>// system/controlDict
startFrom       latestTime;    // 从最新时间目录接着算
endTime         10;            // 把结束时间改大
$ simpleFoam &gt;&gt; log.simpleFoam 2&gt;&amp;1 &amp;      # 用 &gt;&gt; 追加，保留之前的日志</code></pre>
<p>优雅地提前中止（不要直接 kill，否则最后一步结果没写完）</p>
<pre><code>// controlDict 里保证
runTimeModifiable  true;      // 允许运行中修改 controlDict</code></pre>
<p>然后在算例跑着的时候改 controlDict：</p>
<pre><code>$ foamDictionary system/controlDict -entry stopAt -set writeNow</code></pre>
<p>求解器会在当前时间步结束后写出结果再退出。这就是 runTimeModifiable 的价值：算到一半发现输出频率不合适、想提前停，都不用重来。</p>
<p>stopAt 的四个取值</p>
<div class="table-scroll"><table>
<tr><th>值</th><th>行为</th></tr>
<tr><td>endTime</td><td>算到 endTime（默认）</td></tr>
<tr><td>writeNow</td><td>立即写结果并退出</td></tr>
<tr><td>noWriteNow</td><td>立即退出，不写</td></tr>
<tr><td>nextWrite</td><td>到下一个输出时刻后退出</td></tr>
</table></div>
<h4>7.6 时间步长与 Courant 数</h4>
<p>瞬态算例几乎都会用自适应时间步：</p>
<pre><code>// system/controlDict
adjustTimeStep  yes;
maxCo           0.9;        // 全场最大 Courant 数
maxAlphaCo      0.9;        // VOF：界面处的 Courant 数（更严）
maxDeltaT       1e-3;       // 时间步上限，防止流速很低时步长失控变大</code></pre>
<p>为什么要控制 Courant 数：\(\mathrm{Co}=\frac{|\boldsymbol U|\Delta t}{\Delta x}\)，表示一个时间步内流体走过几个网格。显式格式 \(\mathrm{Co} &gt; 1\) 直接发散；隐式格式（PIMPLE）虽能容忍 \(\mathrm{Co} &gt; 1\)，但精度会掉。interFoam 这类界面追踪算法对界面处的 Co 尤其敏感，所以单列一个 maxAlphaCo。</p>
<p>日志里怎么看：</p>
<pre><code>Courant Number mean: 0.0132 max: 0.847
deltaT = 0.000123</code></pre>
<p>max 长期贴着你设的上限是正常的（说明自适应在起作用）；如果 deltaT 越缩越小到 1e-12，说明局部有问题（网格坏点或场发散），该去查网格而不是继续等。</p>
{% endraw %}