---
title: "第 22 章　附录"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>附录 A　一页速查表（打印出来贴在桌上）</h4>
<p>环境</p>
<pre><code>of2512                          # 激活环境（自定义别名）
foamVersion                     # 确认版本
tut / run / sol / util / src    # 跳转到 教程 / 工作目录 / 求解器 / 工具 / 源码
echo $FOAM_TUTORIALS            # 看变量</code></pre>
<p>一个算例的完整生命周期</p>
<pre><code>cp -r $FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily $FOAM_RUN/
cd $FOAM_RUN/pitzDaily
blockMesh          &gt; log.blockMesh   2&gt;&amp;1      # 建网格
checkMesh          &gt; log.checkMesh   2&gt;&amp;1      # 查网格
setFields          &gt; log.setFields   2&gt;&amp;1      # 初场（需要时）
decomposePar       &gt; log.decomposePar 2&gt;&amp;1     # 分区（并行时）
mpirun -np 8 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1 &amp;
tail -f log.simpleFoam                          # 盯进度
reconstructPar -latestTime                      # 合并
foamLog log.simpleFoam                          # 残差数据
paraFoam                                        # 看结果
foamListTimes -rm                               # 清理重来</code></pre>
<p>查询</p>
<pre><code>命令名 -help  /  -help-full        # 命令用法
foamHelp boundary -field U         # 可用边界条件
postProcess -list                  # 可用后处理功能
simpleFoam -listFunctionObjects    # 可用 functionObject
ls $FOAM_APPBIN                    # 本机所有命令
grep -r &quot;关键字&quot; $FOAM_TUTORIALS   # 别人怎么写的
foamDictionary &lt;文件&gt; -expand      # 字典最终展开成什么</code></pre>
<p>改设置</p>
<pre><code>foamDictionary system/controlDict -entry endTime -set 5
foamDictionary system/fvSolution  -entry solvers/p/tolerance -set 1e-8
foamDictionary 0/U -entry boundaryField/inlet/value -set &quot;uniform (5 0 0)&quot;</code></pre>
<p>排错</p>
<pre><code>checkMesh -allGeometry -allTopology     # 网格
solver -dry-run                         # 设置语法
export FOAM_SIGFPE=true                 # 定位第一次浮点异常
grep -A5 &quot;FOAM FATAL&quot; log.xxx           # 抓错误
diff -r caseA/system caseB/system       # 和能跑的算例对比</code></pre>
<h4>附录 B　各文件”必填项”清单</h4>
<div class="table-scroll"><table>
<tr><th>文件</th><th>必须有的关键字</th></tr>
<tr><td>system/controlDict</td><td>application、startFrom、startTime、stopAt、endTime、deltaT、writeControl、writeInterval</td></tr>
<tr><td>system/fvSchemes</td><td>ddtSchemes、gradSchemes、divSchemes、laplacianSchemes、interpolationSchemes、snGradSchemes</td></tr>
<tr><td>system/fvSolution</td><td>solvers；瞬态还要 PISO/PIMPLE，稳态还要 SIMPLE + relaxationFactors</td></tr>
<tr><td>system/blockMeshDict</td><td>scale、vertices、blocks、edges、boundary、mergePatchPairs</td></tr>
<tr><td>system/decomposeParDict</td><td>numberOfSubdomains、method</td></tr>
<tr><td>constant/transportProperties</td><td>transportModel、nu（多相时按相分组 + sigma）</td></tr>
<tr><td>constant/turbulenceProperties</td><td>simulationType（RAS/LES 时还要对应子字典）</td></tr>
<tr><td>0/&lt;场&gt;</td><td>dimensions、internalField、boundaryField（覆盖全部 patch）</td></tr>
</table></div>
<h4>附录 C　ESI 版与 Foundation 版的主要差异</h4>
<div class="table-scroll"><table>
<tr><th>项目</th><th>ESI（v2512，本手册）</th><th>Foundation（v13）</th></tr>
<tr><td>版本号</td><td>v2506、v2512</td><td>11、12、13</td></tr>
<tr><td>求解器</td><td>simpleFoam、interFoam 等独立可执行文件</td><td>统一为 foamRun -solver &lt;模块&gt;</td></tr>
<tr><td>物性文件</td><td>transportProperties、thermophysicalProperties</td><td>physicalProperties</td></tr>
<tr><td>湍流文件</td><td>turbulenceProperties</td><td>momentumTransport</td></tr>
<tr><td>网格工具</td><td>surfaceFeatureExtract</td><td>surfaceFeatures</td></tr>
<tr><td>官网</td><td>openfoam.com</td><td>openfoam.org</td></tr>
</table></div>
<p>遇到教程时先看它是哪个分支：文中出现 foamRun 或 momentumTransport 就是 .org 的，不要照抄。</p>
<h4>附录 D　学习路径建议</h4>
<p>第一阶段（能跑）：cavity（icoFoam）→ pitzDaily（simpleFoam）→ damBreak（interFoam）。目标是把”复制算例 → 建网格 → 检查 → 求解 → 可视化 → 清理”这条链路走顺，能看懂日志。</p>
<p>第二阶段（能改）：改网格密度看结果变化；改边界条件；改湍流模型；改离散格式。目标是理解每个字典的每一项改了会发生什么——这一步必须自己动手试，看书没用。</p>
<p>第三阶段（能验证）：做一个有解析解或有实验数据的算例（Poiseuille 流、\(\mathrm{Re}=100\) 圆柱绕流的 St 数、后台阶再附着长度），把误差算出来。目标是建立”我的结果可信吗”的判断力。</p>
<p>第四阶段（能开发）：从 icoFoam 出发加一个标量输运方程；写一个 codedFixedValue 边界条件；写一个自己的 functionObject。目标是能读懂 $FOAM_SOLVERS 里的代码。</p>
<h4>附录 E　资源</h4>
<div class="table-scroll"><table>
<tr><th>资源</th><th>地址 / 位置</th></tr>
<tr><td>官方教程库（最重要）</td><td>$FOAM_TUTORIALS</td></tr>
<tr><td>官方用户手册</td><td>doc.openfoam.com</td></tr>
<tr><td>源码文档（Doxygen）</td><td>openfoam.com/documentation/guides/latest/api</td></tr>
<tr><td>官方源码仓库（v2512 起）</td><td>gitlab.com/openfoam/core/openfoam</td></tr>
<tr><td>CFD Online 论坛 OpenFOAM 版</td><td>cfd-online.com/Forums/openfoam</td></tr>
<tr><td>各版本发布说明</td><td>openfoam.com/news</td></tr>
</table></div>
<p>一条最有用的建议：遇到问题时，先在 $FOAM_TUTORIALS 里搜有没有类似的官方算例。官方算例是被验证过、能成功执行的，比论坛帖子和博客可靠得多。grep -rl 加上一个关键字，通常十秒钟就能找到。</p>
{% endraw %}