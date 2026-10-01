---
title: "第 21 章　常见报错速查"
layout: reference
description: "OpenCFD v2512 常见报错速查；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>先学会读 OpenFOAM 的报错。它的格式是固定的：</p>
<pre><code class="language-plaintext">--&gt; FOAM FATAL ERROR: (openfoam-2512)
cannot find file "/home/chen/run/cavity/0/U"

    From ... in file db/regIOobject/regIOobjectRead.C at line 132.
FOAM exiting</code></pre>
<p>错误日志通常包含错误类型、具体说明以及相关文件或源码位置。FATAL IO ERROR 通常与文件读取或字典解析有关；FATAL ERROR 的原因范围更广。应保留完整错误上下文，依据具体说明定位，不能仅凭错误类别确定原因。</p>
<h2>21.1 环境与文件类</h2>
<div class="table-scroll"><table>
<tr><th>症状</th><th>原因</th><th>处理</th></tr>
<tr><td>blockMesh: command not found</td><td>没 source 环境</td><td>of2512（或 source .../etc/bashrc），再 foamVersion 确认</td></tr>
<tr><td>cannot find file ".../0/U"</td><td>缺场文件，或 0/ 被 Allclean 删了</td><td>cp -r 0.orig 0</td></tr>
<tr><td>keyword xxx is undefined in dictionary</td><td>字典里缺关键字</td><td>报错会给出字典路径，去补；不确定填什么就去 &#36;FOAM_TUTORIALS 找同类算例抄</td></tr>
<tr><td>Cannot find patchField entry for &lt;名字&gt;</td><td>0/ 里某个场漏了某个 patch</td><td>在该场的 boundaryField 里补上；或加 ".*" { type zeroGradient; } 兜底</td></tr>
<tr><td>ill defined primitiveEntry starting at ...</td><td>语法错：漏分号、括号不配对、有中文全角符号</td><td>从报错行往上找；从 PDF 复制的内容尤其要检查全角字符</td></tr>
<tr><td>incompatible dimensions for operation</td><td>量纲不匹配</td><td>检查 dimensions。最常见：不可压求解器里把 p 写成了 Pa 的量纲</td></tr>
<tr><td>Unknown patchField type xxx</td><td>边界条件名拼错，或该类型需要额外的库</td><td>foamHelp boundary -field U 看正确名字；或在 controlDict 里 libs 加载对应库</td></tr>
<tr><td>object of type ... not found</td><td>object 名与文件名不一致</td><td>改文件头里的 object</td></tr>
</table></div>
<h2>21.2 网格类</h2>
<div class="table-scroll"><table>
<tr><th>症状</th><th>原因</th><th>处理</th></tr>
<tr><td>Block ... has negative volume</td><td>blockMeshDict 顶点顺序错</td><td>按 15.2 的规则重排；用 paraFoam -block 看</td></tr>
<tr><td>***Number of severely non-orthogonal faces: N</td><td>网格质量差</td><td>fvSolution 加 nNonOrthogonalCorrectors 2；fvSchemes 改 limited corrected 0.33；根本办法是改网格</td></tr>
<tr><td>Zero or negative cell volume detected</td><td>网格坏</td><td>必须重建；checkMesh -writeSets vtk 定位坏单元</td></tr>
<tr><td>snappyHexMesh 跑完没有网格 / 只剩一点</td><td>locationInMesh 点在固体内或落在面上</td><td>挪到明确的流体区，坐标带零头（如 (0.501 0.301 0.201)）</td></tr>
<tr><td>加层几乎全失败（layer ratio &lt; 0.5）</td><td>几何尖角、层太厚、质量阈值太严</td><td>减 nSurfaceLayers、减 finalLayerThickness、minTetQuality 放宽到 -1e30</td></tr>
<tr><td>结果里壁面函数没起作用</td><td>patch 类型是 patch 而不是 wall</td><td>改 constant/polyMesh/boundary 里的 type，或用 createPatch</td></tr>
</table></div>
<h2>21.3 计算发散类（最常见）</h2>
<p>典型现象</p>
<pre><code class="language-plaintext">Courant Number mean: 1.2e+15 max: 3.4e+18
bounding k, min: -1.2e+03 max: 5.6e+05 average: 12.3
#0  Foam::error::printStack(...)
Floating point exception</code></pre>
<p>排查顺序（按这个顺序查，不要跳）</p>
<p>网格：checkMesh -allGeometry -allTopology 有没有 ***？非正交角多少？</p>
<p>边界条件：进出口是不是都定了？封闭腔体给了 pRefCell 吗？出口用 inletOutlet 了吗？</p>
<p>初场：初场是不是物理上不可能（比如压力给了负值、alpha 超出 [0,1]）？</p>
<p>时间步：maxCo 是不是太大？先降到 0.3 试试。</p>
<p>格式：把 divSchemes 全改成 Gauss upwind（一阶最稳），如果这样能跑说明是格式问题，再逐步换回二阶。</p>
<p>松弛因子：稳态算例把 p 降到 0.1、U 降到 0.3。</p>
<p>这个顺序的道理：从”不可能算对”的问题（网格、边界条件）查到”可能只是不稳”的问题（格式、松弛）。反过来查会浪费大量时间——网格有负体积时，你把松弛因子调到 0.01 也没用。</p>
<p>几个具体信号的含义</p>
<div class="table-scroll"><table>
<tr><th>日志里的话</th><th>含义</th><th>处理</th></tr>
<tr><td>bounding k / bounding epsilon 偶尔出现</td><td>湍流量被限幅（正常现象）</td><td>忽略；持续大量出现才是问题</td></tr>
<tr><td>bounding 每步都出现</td><td>湍流量在发散</td><td>检查入口湍流量估算、壁面函数、\(y^{+}\)</td></tr>
<tr><td>Continuity error 越来越大</td><td>连续性不满足</td><td>增加 nCorrectors、nNonOrthogonalCorrectors；检查 fixedFluxPressure</td></tr>
<tr><td>deltaT 一直缩小到 1e-12</td><td>局部有坏点或数值爆炸</td><td>用 ParaView 找 U 或 p 最大的位置，八成是网格坏点</td></tr>
<tr><td>Floating point exception</td><td>出现了 0/0 或 sqrt(负数)</td><td>开 <code>export FOAM_SIGFPE=true 重新计算</code>，定位第一次出错的位置</td></tr>
<tr><td>GAMG 求解器不收敛 / singular matrix</td><td>压力无基准</td><td>给 pRefCell/pRefValue（全封闭算例必需）</td></tr>
<tr><td>Maximum number of iterations exceeded</td><td>线性求解器达到上限</td><td>放宽 tolerance 或换求解器；也可能是矩阵已经坏了，先查上面几条</td></tr>
</table></div>
<h2>21.4 并行类</h2>
<div class="table-scroll"><table>
<tr><th>症状</th><th>原因</th><th>处理</th></tr>
<tr><td>结果错乱、日志重复 8 遍</td><td>漏了 -parallel</td><td>mpirun -np 8 solver -parallel</td></tr>
<tr><td>number of processor directories = 4 is not equal to the number of processors = 8</td><td>-np 与 numberOfSubdomains 不一致</td><td>改一致，或 decomposePar -force 重分</td></tr>
<tr><td>mpirun 报共享库错误</td><td>集群 MPI 与编译时的 MPI 不同</td><td>module load 与编译一致的 MPI，或重新编译</td></tr>
<tr><td>并行比串行还慢</td><td>每核网格太少</td><td>减核数，保证每核 \(\ge  5\) 万单元</td></tr>
<tr><td>大规模并行写文件极慢</td><td>小文件太多</td><td>加 -fileHandler collated</td></tr>
</table></div>
<h2>21.5 编译类</h2>
<div class="table-scroll"><table>
<tr><th>症状</th><th>原因</th><th>处理</th></tr>
<tr><td>xxx.H: No such file or directory</td><td>Make/options 里 EXE_INC 缺路径</td><td>加对应的 -I&#36;(LIB_SRC)/.../lnInclude</td></tr>
<tr><td>undefined reference to ...</td><td>EXE_LIBS 缺库</td><td>加对应的 -lxxx</td></tr>
<tr><td>编译成功但 command not found</td><td>装到了 &#36;FOAM_USER_APPBIN 但环境没刷新，或 Make/files 里 EXE 路径写错</td><td>wmake 后看输出路径；which 命令名</td></tr>
<tr><td>改了 codedFixedValue 不生效</td><td>dynamicCode/ 缓存</td><td>rm -rf dynamicCode</td></tr>
<tr><td>error: 'xxx' was not declared</td><td>版本 API 变了</td><td>去 &#36;FOAM_SRC 找同名新接口</td></tr>
</table></div>
<h2>21.6 无运行报错情况下的结果偏差</h2>
<p>这类问题没有报错信息，只能靠检查清单：</p>
<p>单位：STL 是毫米吗？transformPoints -scale 做了吗？</p>
<p>patch 类型：壁面是 wall 不是 patch 吗？</p>
<p>不可压里的压力：p 的单位是 \(m^{2}/s^{2}\)，算力时给 rhoInf 了吗？</p>
<p>重力方向：g 的方向与网格坐标系一致吗？</p>
<p>setFields 跑在干净的 0/ 上吗？（跑两次结果不同就是这个问题）</p>
<p>湍流模型开了吗：turbulenceProperties 里 turbulence on;？</p>
<p>统计平均的起始时间：fieldAverage 的 timeStart 是不是把初始瞬态也统计进去了？</p>
<p>收敛了吗：稳态算例残差降到 1e-4 以下了吗？监测量（如阻力系数）平了吗？残差降下来 \(\ne\) 收敛，还要看物理量不再变化。</p>
<p>网格无关性：加密一倍，结果变化超过 5% 吗？</p>
<p>养成一个习惯：任何一个新算例，先用你知道答案的简化工况验证一遍（层流管流对比 Hagen–Poiseuille、圆柱绕流对比 \(\mathrm{Re}=100\) 的 St 数）。这一步花半天，能省掉后面几周的怀疑。</p>
{% endraw %}
