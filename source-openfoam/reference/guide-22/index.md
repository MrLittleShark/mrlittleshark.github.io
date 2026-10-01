---
title: "第 22 章　附录"
layout: reference
description: "OpenCFD v2512 附录；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>附录 A　一页速查表（打印出来贴在桌上）</h2>
<p>环境</p>
<pre><code class="language-bash">of2512                          # 激活环境（自定义别名）
printf '%s\n' "&#36;WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名
tut / run / sol / util / src    # 跳转到 教程 / 工作目录 / 求解器 / 工具 / 源码
echo &#36;FOAM_TUTORIALS            # 看变量</code></pre>
<p>一个算例的完整生命周期</p>
<pre><code class="language-bash">cp -r &#36;FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily &#36;FOAM_RUN/
cd &#36;FOAM_RUN/pitzDaily
blockMesh          &gt; log.blockMesh   2&gt;&amp;1      # 建网格
checkMesh          &gt; log.checkMesh   2&gt;&amp;1      # 查网格
setFields          &gt; log.setFields   2&gt;&amp;1      # 初场（需要时）
decomposePar       &gt; log.decomposePar 2&gt;&amp;1     # 分区（并行时）
mpirun -np 8 simpleFoam -parallel &gt; log.simpleFoam 2&gt;&amp;1 &amp;
tail -f log.simpleFoam                          # 盯进度
reconstructPar -latestTime                      # 合并
foamLog log.simpleFoam                          # 残差数据
paraFoam                                        # 看结果
foamListTimes                                   # 先列出时间目录
# 确认保留需求后，才按帮助选择 -rm 删除结果</code></pre>
<p>查询</p>
<pre><code class="language-bash">命令名 -help  /  -help-full        # 命令用法
foamHelp boundary -field U         # 可用边界条件
postProcess -list                  # 可用后处理功能
simpleFoam -listFunctionObjects    # 可用 functionObject
ls &#36;FOAM_APPBIN                    # 本机所有命令
grep -r "关键字" &#36;FOAM_TUTORIALS   # 别人怎么写的
foamDictionary &lt;文件&gt; -expand      # 字典最终展开成什么</code></pre>
<p>改设置</p>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 5
foamDictionary system/fvSolution  -entry solvers/p/tolerance -set 1e-8
foamDictionary 0/U -entry boundaryField/inlet/value -set "uniform (5 0 0)"</code></pre>
<p>排错</p>
<pre><code class="language-bash">checkMesh -allGeometry -allTopology     # 网格
solver -dry-run                         # 设置语法
export FOAM_SIGFPE=true                 # 定位第一次浮点异常
grep -A5 "FOAM FATAL" log.xxx           # 抓错误
diff -r caseA/system caseB/system       # 和能跑的算例对比</code></pre>
<h2>附录 B　各文件”必填项”清单</h2>
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
<h2>附录 C　ESI 版与 Foundation 版的主要差异</h2>
<div class="table-scroll"><table>
<tr><th>项目</th><th>ESI（v2512，本手册）</th><th>Foundation（v13）</th></tr>
<tr><td>版本号</td><td>v2506、v2512</td><td>11、12、13</td></tr>
<tr><td>求解器</td><td>simpleFoam、interFoam 等独立可执行文件</td><td>较新版本提供 foamRun -solver &lt;模块&gt; 等入口</td></tr>
<tr><td>物性文件</td><td>transportProperties、thermophysicalProperties</td><td>physicalProperties</td></tr>
<tr><td>湍流文件</td><td>turbulenceProperties</td><td>momentumTransport</td></tr>
<tr><td>网格工具</td><td>surfaceFeatureExtract</td><td>surfaceFeatures</td></tr>
<tr><td>官网</td><td>openfoam.com</td><td>openfoam.org</td></tr>
</table></div>
<p>foamRun、momentumTransport 等名称可作为分支差异的线索，但最终应检查教程来源、版本和实际读取接口。迁移时逐项核对求解器、物性、湍流、源项和边界类型，而不是只替换文件名。</p>
<h2>附录 D　学习路径建议</h2>
<p>第一阶段（能跑）：cavity（icoFoam）→ pitzDaily（simpleFoam）→ damBreak（interFoam）。目标是把”复制算例 → 建网格 → 检查 → 求解 → 可视化 → 清理”这条链路走顺，能看懂日志。</p>
<p>第二阶段（能改）：改网格密度看结果变化；改边界条件；改湍流模型；改离散格式。目标是理解每个字典的每一项改了会发生什么——这一步必须自己动手试，看书没用。</p>
<p>第三阶段（能验证）：做一个有解析解或有实验数据的算例（Poiseuille 流、\(\mathrm{Re}=100\) 圆柱绕流的 St 数、后台阶再附着长度），把误差算出来。目标是建立”我的结果可信吗”的判断力。</p>
<p>第四阶段（能开发）：从 icoFoam 出发加一个标量输运方程；写一个 codedFixedValue 边界条件；写一个自己的 functionObject。目标是能读懂 &#36;FOAM_SOLVERS 里的代码。</p>
<h2>附录 E　资源</h2>
<div class="table-scroll"><table>
<tr><th>资源</th><th>地址 / 位置</th></tr>
<tr><td>官方教程库（最重要）</td><td>&#36;FOAM_TUTORIALS</td></tr>
<tr><td>官方用户手册</td><td>doc.openfoam.com</td></tr>
<tr><td>源码文档（Doxygen）</td><td>openfoam.com/documentation/guides/latest/api</td></tr>
<tr><td>官方源码仓库（v2512 起）</td><td>gitlab.com/openfoam/core/openfoam</td></tr>
<tr><td>CFD Online 论坛 OpenFOAM 版</td><td>cfd-online.com/Forums/openfoam</td></tr>
<tr><td>各版本发布说明</td><td>openfoam.com/news</td></tr>
</table></div>
<p>一条最有用的建议：遇到问题时，先在 &#36;FOAM_TUTORIALS 里搜有没有类似的官方算例。官方算例是被验证过、能成功执行的，比论坛帖子和博客可靠得多。grep -rl 加上一个关键字，通常十秒钟就能找到。</p><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>
{% endraw %}
