---
title: "第 7 章　求解器与运行控制"
layout: reference
description: "OpenCFD v2512 求解器与运行控制；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>7.1 跑一个算例的标准流程</h2>
<pre><code class="language-bash">run                                     # 去工作目录
cp -r &#36;FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily .
cd pitzDaily
blockMesh              &gt; log.blockMesh  2&gt;&amp;1    # ① 建网格
checkMesh              &gt; log.checkMesh  2&gt;&amp;1    # ② 查网格
simpleFoam             &gt; log.simpleFoam 2&gt;&amp;1 &amp;  # ③ 后台求解，日志落盘
tail -f log.simpleFoam                          # ④ 实时看进度（Ctrl+C 只退出查看，不影响计算）
foamLog log.simpleFoam                          # ⑤ 提取残差
paraFoam                                        # ⑥ 可视化</code></pre>
<p>重定向可保存标准输出与标准错误，便于记录运行过程和排查异常。2&gt;&amp;1 将标准错误合并到标准输出。foamLog 可从求解器日志提取残差数据；foamMonitor 可用于监视相应的数据文件。</p>
<p>末尾的 &amp; 使任务在当前 shell 后台运行，并不保证 SSH 断开后任务仍继续。长任务应采用作业调度器、tmux 或按环境配置的 nohup，并明确日志与退出状态的保存方式。</p>
<h2>7.2 求解器名字的构词法</h2>
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
<h2>7.3 常用求解器速查</h2>
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
<pre><code class="language-plaintext">ls &#36;FOAM_APPBIN | grep -i foam | sort | less
ls &#36;FOAM_SOLVERS/*                      # 按类别看源码目录</code></pre>
<h2>7.4 求解器的运行选项</h2>
<pre><code class="language-bash">simpleFoam [-case &lt;dir&gt;] [-parallel] [-postProcess] [-dry-run] [-noFunctionObjects]
           [-fileHandler collated] [-libs '("libMyBC.so")'] [-region &lt;name&gt;]</code></pre>
<p>-postProcess：把求解器当后处理器用（非常重要的技巧）</p>
<pre><code class="language-bash"># 用求解器自己的物理模型，对已有结果做后处理（例如算 yPlus 需要湍流模型信息）
simpleFoam -postProcess -func yPlus -latestTime
pimpleFoam -postProcess -func "grad(p)" -time '1:5'</code></pre>
<p>通用 postProcess 与求解器的 -postProcess 模式创建的模型对象可能不同。yPlus、壁面剪切应力等量需要湍流或输运模型；应按函数对象要求选择能构建这些对象的入口，而不是假定只要已有 U、p 就足够。</p>
<p>-dry-run：开算前的语法体检</p>
<pre><code class="language-bash">interFoam -dry-run</code></pre>
<p>它会读完所有字典、建好场、然后退出。字典写错、边界条件名拼错、场文件缺失都会在这一步暴露——比跑 3 小时后崩掉划算得多。</p>
<h2>7.5 续算、中止与在线改参数</h2>
<p>续算（从上次结果接着算）</p>
<pre><code class="language-bash">// system/controlDict
startFrom       latestTime;    // 从最新时间目录接着算
endTime         10;            // 把结束时间改大
simpleFoam &gt;&gt; log.simpleFoam 2&gt;&amp;1 &amp;      # 用 &gt;&gt; 追加，保留之前的日志</code></pre>
<p>优雅地提前中止（不要直接 kill，否则最后一步结果没写完）</p>
<pre><code class="language-plaintext">// controlDict 里保证
runTimeModifiable  true;      // 允许运行中修改 controlDict</code></pre>
<p>然后在算例跑着的时候改 controlDict：</p>
<pre><code class="language-bash">foamDictionary system/controlDict -entry stopAt -set writeNow</code></pre>
<p>求解器会在当前时间步结束后写出结果再退出。这就是 runTimeModifiable 的价值：算到一半发现输出频率不合适、想提前停，都不用重来。</p>
<p>stopAt 的四个取值</p>
<div class="table-scroll"><table>
<tr><th>值</th><th>行为</th></tr>
<tr><td>endTime</td><td>算到 endTime（默认）</td></tr>
<tr><td>writeNow</td><td>立即写结果并退出</td></tr>
<tr><td>noWriteNow</td><td>立即退出，不写</td></tr>
<tr><td>nextWrite</td><td>到下一个输出时刻后退出</td></tr>
</table></div>
<h2>7.6 时间步长与 Courant 数</h2>
<p>瞬态算例几乎都会用自适应时间步：</p>
<pre><code class="language-plaintext">// system/controlDict
adjustTimeStep  yes;
maxCo           0.9;        // 全场最大 Courant 数
maxAlphaCo      0.9;        // VOF：界面处的 Courant 数（更严）
maxDeltaT       1e-3;       // 时间步上限，防止流速很低时步长失控变大</code></pre>
<p>Courant 数衡量单步输运相对于网格尺度的大小，简单一维估计为 \(\mathrm{Co}=|U|\Delta t/\Delta x\)。稳定性限制取决于时间积分、空间离散和多维通量；不能把 Co 大于 1 一概视为必然发散。隐式方法允许较大时间步也不代表时间精度足够。VOF 计算还应检查界面输运的时间步限制。</p>
<p>日志里怎么看：</p>
<pre><code class="language-plaintext">Courant Number mean: 0.0132 max: 0.847
deltaT = 0.000123</code></pre>
<p>max 长期贴着你设的上限是正常的（说明自适应在起作用）；如果 deltaT 越缩越小到 1e-12，说明局部有问题（网格坏点或场发散），该去查网格而不是继续等。</p>
{% endraw %}
