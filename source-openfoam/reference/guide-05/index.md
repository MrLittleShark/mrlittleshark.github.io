---
title: "第 5 章　系统与通用命令"
layout: reference
description: "系统与通用命令：用法与配置实例。"
cms_slug: "reference-guide-05"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>5.1 所有命令都认的通用选项</h2>
<p>OpenFOAM 的可执行文件都继承同一套命令行解析器，所以下面这些选项几乎每个命令都能用。先学这一组，等于一次性学会了两百个命令的用法。</p>
<div class="table-scroll"><table>
<tr><th>选项</th><th>作用</th><th>为什么需要它</th></tr>
<tr><td>-help</td><td>简要帮助</td><td>忘了选项时第一反应</td></tr>
<tr><td>-help-full</td><td>完整帮助（含不常用选项）</td><td>-help 里没有的高级选项在这</td></tr>
<tr><td>-help-man</td><td>man 手册格式</td><td>配合 \| less 慢慢读</td></tr>
<tr><td>-doc</td><td>打开该程序的在线 Doxygen 文档</td><td>想知道背后的方程</td></tr>
<tr><td>-srcDoc</td><td>打开源码文档</td><td>读实现细节</td></tr>
<tr><td>-case &lt;dir&gt;</td><td>指定算例目录</td><td>不用先 cd 进去；写脚本时必备</td></tr>
<tr><td>-parallel</td><td>并行运行</td><td>必须与 mpirun 一起用</td></tr>
<tr><td>-region &lt;name&gt;</td><td>指定网格区域</td><td>多区域（如共轭传热）算例</td></tr>
<tr><td>-time &lt;范围&gt;</td><td>只处理指定时刻</td><td>如 -time '0.1:0.5'、-time 0.2</td></tr>
<tr><td>-latestTime</td><td>只处理最后一个时刻</td><td>后处理时最常用</td></tr>
<tr><td>-noZero / -withZero</td><td>排除 / 包含 0 时刻</td><td>后处理时避免把初始场算进去</td></tr>
<tr><td>-constant</td><td>包含 constant 目录</td><td>处理网格类数据时</td></tr>
<tr><td>-noFunctionObjects</td><td>关闭 controlDict 里的 functionObject</td><td>只想重新计算求解、不想重复采样时</td></tr>
<tr><td>-fileHandler &lt;类型&gt;</td><td>文件读写方式：uncollated/collated/masterUncollated</td><td>大规模并行时防止小文件把文件系统拖垮</td></tr>
<tr><td>-libs '("libX.so")'</td><td>运行时额外加载库</td><td>用自己写的边界条件/模型而不改求解器</td></tr>
<tr><td>-dry-run</td><td>只做初始化不真正求解</td><td>快速检查设置文件有没有语法错</td></tr>
<tr><td>-listFunctionObjects</td><td>列出本机所有可用 functionObject</td><td>找后处理功能名</td></tr>
<tr><td>-listScalarBCs / -listVectorBCs</td><td>列出可用的标量/矢量边界条件</td><td>忘了边界条件叫什么</td></tr>
<tr><td>-listSwitches</td><td>列出所有调试/优化开关</td><td>高级调试</td></tr>
</table></div>
<p>示例</p>
<pre><code class="language-bash">simpleFoam -help                       # 看这个求解器有哪些选项
blockMesh -help-full | less            # 看全部选项
simpleFoam -case ../pitzDaily          # 算另一个目录里的算例
interFoam -dry-run                     # 只检查设置，不真算
simpleFoam -listFunctionObjects | head -40
pimpleFoam -listVectorBCs | grep -i inlet</code></pre>
<h2>5.2 foamVersion —— 确认版本</h2>
<pre><code class="language-bash">printf '%s\n' "$WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名</code></pre>
<p>用途：任何求助、任何报错帖，第一句都该是版本号。它也是检查 source 有没有生效的最快方法。</p>
<h2>5.3 foamHelp —— 内置的”查手册”命令</h2>
<p>是什么：OpenFOAM 自带的帮助工具，能查边界条件、求解器、functionObject 的可用类型和参数。</p>
<p>边界条件类型取决于场类型、已加载的库和当前版本。foamHelp 能查询当前安装注册的类型；查询结果仍需结合对应模型的必需条目与物理适用条件。</p>
<p>用法</p>
<pre><code class="language-bash">foamHelp boundary [-field &lt;场名&gt;] [-constraint] [-browse &lt;类型名&gt;]
foamHelp solver   [-browse &lt;求解器名&gt;]
foamHelp functionObject [-browse &lt;名字&gt;]</code></pre>
<p>示例</p>
<pre><code class="language-bash"># ① 列出 U 场所有可用边界条件（数量很多，建议接 less）
foamHelp boundary -field U | less

# ② 只看"约束型"边界条件（empty、cyclic、symmetry 这类）
foamHelp boundary -constraint

# ③ 打开某个边界条件的源码文档，看它需要哪些参数
foamHelp boundary -browse inletOutlet</code></pre>
<p>提示 foamHelp boundary 必须在一个算例目录里运行（它需要读网格和场信息）。在空目录里跑会报错。</p>
<h2>5.4 foamGet —— 把官方模板抓到手边</h2>
<p>是什么：从 $FOAM_ETC/caseDicts 里把官方字典模板复制到当前算例。</p>
<p>从 v2512 自带模板开始配置，可以保留必要的库和参数结构。模板中的场名、patch 名、坐标与物性仍需根据具体算例修改，模板存在也不代表任意求解器都能使用它。</p>
<p>用法与示例</p>
<pre><code class="language-bash">foamGetDict -list                 # 列出所有可取的模板
foamGetDict singleGraph           # 把沿线取样模板拷进 system/
foamGetDict -case ../run1 probes  # 拷到别的算例目录</code></pre>
<p>先用 command -v foamGetDict 检查当前环境。若安装未提供该脚本，可从正确的 etc/caseDicts 子目录复制对应模板；模板仍可能通过 #includeEtc 引用其他文件。</p>
<pre><code class="language-bash">cp $FOAM_ETC/caseDicts/postProcessing/graphs/singleGraph system/
ls $FOAM_ETC/caseDicts/postProcessing/     # 先看看有哪些模板</code></pre>
<h2>5.5 foamEtcFile —— 定位配置文件</h2>
<p>是什么：按 OpenFOAM 的查找顺序（用户 → 站点 → 安装）找出某个配置文件的真实路径。</p>
<pre><code class="language-bash">foamEtcFile -list             # 列出配置文件的搜索路径
foamEtcFile controlDict       # 全局默认 controlDict 在哪
foamEtcFile -all bashrc       # 所有同名文件都列出来</code></pre>
<p>配置查找可能经过用户、站点与安装目录。foamEtcFile 可用于查看匹配文件及搜索层级；诊断覆盖关系时，应同时检查环境变量与实际展开的字典。</p>
<h2>5.6 foamCloneCase —— 干净地复制算例</h2>
<p>是什么：只复制 0/、constant/、system/，不复制计算结果。</p>
<p>复制已有计算时，应明确是否需要网格、初始场和结果。foamCloneCase 可以按选项选择复制范围，减少把旧时间目录带入新算例的情况。普通 cp 也可以使用，但应检查目标目录和 startFrom 设置。</p>
<pre><code class="language-bash">foamCloneCase pitzDaily pitzDaily_fine
foamCloneCase -latestTime oldCase newCase   # 选择并复制最后时间目录；不会自动改名为 0</code></pre>
<h2>5.7 foamListTimes —— 列出/删除时间目录</h2>
<pre><code class="language-bash">foamListTimes                 # 列出所有时间目录
foamListTimes -latestTime     # 只打印最后一个时刻
foamListTimes -rm             # ★删除全部时间目录（保留 0/），即"清算例"
foamListTimes -rm -processor  # 并行算例：连 processor*/ 里的一起删</code></pre>
<p>重复计算前要确定目标是从初始状态重新运行，还是从已有结果续算。清理命令会删除相应生成文件；先保留需要的结果，再检查时间目录与 startFrom，避免无意从旧时刻启动。</p>
<h2>5.8 foamDictionary —— 在命令行读写字典</h2>
<p>是什么：不打开编辑器，直接查询或修改字典文件里的某一项。</p>
<p>foamDictionary 可按条目路径读取或修改字典，适合参数扫描和批量算例设置。脚本应记录修改前后的值，并在运行前检查字典语法和参数量纲。</p>
<p>用法</p>
<pre><code class="language-bash">foamDictionary &lt;文件&gt; -entry &lt;关键字路径&gt; [-set &lt;值&gt;] [-add &lt;值&gt;] [-remove] [-value] [-keywords] [-expand]</code></pre>
<p>示例</p>
<pre><code class="language-bash"># ① 查看 endTime
foamDictionary system/controlDict -entry endTime
# 输出示例：endTime 0.5;

# ② 只要值，不要关键字（脚本里好用）
foamDictionary system/controlDict -entry endTime -value
# 输出示例：0.5

# ③ 修改：把 endTime 改成 5
foamDictionary system/controlDict -entry endTime -set 5

# ④ 修改嵌套项：p 方程的容差（关键字路径用 / 分隔）
foamDictionary system/fvSolution -entry solvers/p/tolerance -set 1e-8

# ⑤ 改边界条件的值
foamDictionary 0/U -entry boundaryField/inlet/value -set "uniform (5 0 0)"

# ⑥ 列出某一层有哪些关键字
foamDictionary system/fvSolution -entry solvers -keywords

# ⑦ 展开所有 #include、宏和计算，看"程序最终读到的"是什么
foamDictionary system/controlDict -expand</code></pre>
<p>第 ⑦ 条在排查”我用了 #include 结果不对”时是决定性的：它把所有包含、变量替换、#calc 全部算完再打印，你看到的就是求解器看到的。</p>
<p>批量脚本示例（网格无关性验证）</p>
<pre><code class="language-plaintext">for N in 20 40 80 160; do
    foamCloneCase base mesh_$N
    foamDictionary mesh_$N/system/blockMeshDict -entry blocks \
        -set "( hex (0 1 2 3 4 5 6 7) ($N $N 1) simpleGrading (1 1 1) )"
    ( cd mesh_$N &amp;&amp; blockMesh &gt; log.blockMesh &amp;&amp; simpleFoam &gt; log.simpleFoam )
done</code></pre>
<h2>5.9 foamSearch —— 在教程库里搜关键字的取值</h2>
<p>是什么：在一堆算例里搜索某个字典关键字，并把出现过的不同取值汇总去重。</p>
<p>foamSearch 用于比较多个算例中特定条目的取值。其他教程的参数提供实例，不能替代本算例的模型选择、量纲分析和敏感性检查。</p>
<pre><code class="language-bash"># 看官方教程里 p 方程都用过哪些线性求解器
foamSearch "$FOAM_TUTORIALS" solvers.p.solver fvSolution

# 看 ddtSchemes 都有哪些用法
foamSearch "$FOAM_TUTORIALS" ddtSchemes.default fvSchemes</code></pre>
<p>若提示参数顺序不对，敲一次 foamSearch -h 看本机用法。</p>
<h2>5.10 foamLog —— 把日志里的残差拆成可画图的数据</h2>
<p>是什么：解析求解器日志，把每个方程的初始残差、迭代次数、连续性误差等提取成一列列数据文件，放进 logs/ 目录。</p>
<p>残差曲线有助于识别迭代停滞、周期性变化和发散。收敛判断还应包括质量与能量守恒、关注目标量以及适当的网格和时间步检查。</p>
<pre><code class="language-bash">simpleFoam &gt; log.simpleFoam 2&gt;&amp;1        # 先把日志存下来（保存标准输出与错误输出）
foamLog log.simpleFoam
ls logs/
# 输出示例：Ux_0 Uy_0 p_0 contCumulative_0 contGlobal_0 ...
gnuplot -p -e "set logscale y; plot 'logs/p_0' w l, 'logs/Ux_0' w l"</code></pre>
<h2>5.11 foamMonitor —— 边算边画</h2>
<pre><code class="language-bash">foamLog log.simpleFoam
foamMonitor -l logs/p_0</code></pre>
<p>-l 表示 y 轴取对数。需要系统装了 gnuplot。这条命令在另一个终端里跑，实时刷新残差曲线。</p>
<h2>5.12 foamJob / foamExec —— 后台运行与环境包装</h2>
<pre><code class="language-bash">foamJob simpleFoam                # 后台运行，日志写到 log
foamJob -s simpleFoam             # 同时输出到屏幕（screen）
foamJob -p -s interFoam           # 并行 + 屏幕输出
"/usr/lib/openfoam/openfoam2512/bin/tools/foamExec" simpleFoam -help         # 在正确环境下执行（集群脚本里常用）</code></pre>
<p>foamExec 位于安装目录的 bin/tools，通常不会作为独立命令加入 PATH。它根据自身路径定位安装并激活 etc/bashrc，再执行传入程序；作业脚本通常也可以直接 source 已知安装的 bashrc。</p>
<h2>5.13 foamSystemCheck / foamInstallationTest</h2>
<pre><code class="language-bash">foamSystemCheck        # 编译前：检查 gcc/mpi/flex 等基础环境
foamInstallationTest   # 安装后：检查路径、库、命令是否都正常</code></pre>
<p>装完或者环境出问题时先跑这两个，能省掉大量瞎猜。</p>
<h2>5.14 foamCleanTutorials / 清理类命令</h2>
<pre><code class="language-bash">foamCleanTutorials       # 递归清理当前目录下所有算例（调用各自的 Allclean）
./Allclean               # 清理单个算例（官方算例大多自带这个脚本）
foamListTimes -rm        # 只删时间目录
rm -rf processor*        # 删并行分区数据</code></pre>
<h2>5.15 foamNew* —— 生成代码骨架（二次开发用）</h2>
<pre><code class="language-bash">foamNewApp myApp                    # 新建一个应用程序骨架
foamNew source H MyClass             # 新建源文件模板
foamNewBC fixedValue vector myBC                   # 新建边界条件骨架
foamNewFunctionObject myFO          # 新建 functionObject 骨架</code></pre>
<p>代码生成工具可以建立与 OpenFOAM 运行时选择机制相配套的类结构和 Make 配置。生成后仍需实现物理逻辑，检查基类接口、库依赖和边界更新条件，并通过小算例验证。</p>
<h2>5.16 Allrun / Allclean 与 RunFunctions</h2>
<p>官方算例里几乎都有 Allrun、Allclean（有的还有 Allmesh、Allpost）。它们是普通 shell 脚本，开头都会 source 两个函数库：</p>
<pre><code class="language-bash">#!/bin/sh
cd "${0%/*}" || exit                                # 切到脚本所在目录
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions        # 运行相关函数
. ${WM_PROJECT_DIR:?}/bin/tools/CleanFunctions      # 清理相关函数

runApplication blockMesh
runApplication decomposePar
runParallel $(getApplication)
runApplication reconstructPar</code></pre>
<p>RunFunctions 提供的函数</p>
<div class="table-scroll"><table>
<tr><th>函数</th><th>作用</th></tr>
<tr><td>runApplication &lt;cmd&gt;</td><td>串行运行并把输出写到 log.&lt;cmd&gt;；如果 log 已存在会跳过（防止重复跑）</td></tr>
<tr><td>runParallel &lt;cmd&gt;</td><td>并行运行，自动读 decomposeParDict 里的核数，自动加 -parallel</td></tr>
<tr><td>getApplication</td><td>从 controlDict 里读出 application 的值</td></tr>
<tr><td>getNumberOfProcessors</td><td>从 decomposeParDict 读出核数</td></tr>
<tr><td>cloneCase &lt;src&gt; &lt;dst&gt;</td><td>复制算例（不含结果）</td></tr>
<tr><td>restore0Dir</td><td>把 0.orig/ 复制成 0/</td></tr>
</table></div>
<p>0.orig 常用来保存可重复恢复的初始场模板。setFields 等工具可能修改工作目录中的场；restore0Dir 从保留模板恢复初始条件，有助于避免连续多次操作的相互影响。重复运行 setFields 是否改变结果，取决于其默认值与区域赋值方式，不能一概认为第二次运行必然错误。</p>
<p>一个完整的 Allrun 示例（interFoam 溃坝）</p>
<pre><code class="language-bash">#!/bin/sh
cd "${0%/*}" || exit
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions

restore0Dir
runApplication blockMesh
runApplication setFields
runApplication $(getApplication)</code></pre>
<p>CleanFunctions 提供的函数：cleanCase（删时间目录、日志、processor*）、cleanCase0（再把 0/ 也删掉，配合 0.orig 用）、cleanTimeDirectories、cleanPostProcessing、cleanDynamicCode（清 dynamicCode/，改了 codedFixedValue 却不生效时必须清）。</p><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p><h2>未安装的官方目标</h2><p><code>foamCalc</code> 与 <code>foamExprParserInfo</code> 存在于 v2512 的 applications/tools，但当前虚拟机安装没有找到其可执行文件。请先用 command -v 核对，不能把源码中存在的程序等同于已安装程序。</p><p><code>foamHelp boundary -field U</code> 需要能够读取相应网格和字段的算例。源码工具中的浏览器文档功能还依赖可用的文档索引及浏览器设置。</p>
