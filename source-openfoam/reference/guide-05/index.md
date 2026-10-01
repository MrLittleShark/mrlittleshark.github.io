---
title: "第 5 章　系统与通用命令"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>5.1 所有命令都认的通用选项</h4>
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
<tr><td>-time &lt;范围&gt;</td><td>只处理指定时刻</td><td>如 -time &#x27;0.1:0.5&#x27;、-time 0.2</td></tr>
<tr><td>-latestTime</td><td>只处理最后一个时刻</td><td>后处理时最常用</td></tr>
<tr><td>-noZero / -withZero</td><td>排除 / 包含 0 时刻</td><td>后处理时避免把初始场算进去</td></tr>
<tr><td>-constant</td><td>包含 constant 目录</td><td>处理网格类数据时</td></tr>
<tr><td>-noFunctionObjects</td><td>关闭 controlDict 里的 functionObject</td><td>只想重新计算求解、不想重复采样时</td></tr>
<tr><td>-fileHandler &lt;类型&gt;</td><td>文件读写方式：uncollated/collated/masterUncollated</td><td>大规模并行时防止小文件把文件系统拖垮</td></tr>
<tr><td>-libs &#x27;(&quot;libX.so&quot;)&#x27;</td><td>运行时额外加载库</td><td>用自己写的边界条件/模型而不改求解器</td></tr>
<tr><td>-dry-run</td><td>只做初始化不真正求解</td><td>快速检查设置文件有没有语法错</td></tr>
<tr><td>-listFunctionObjects</td><td>列出本机所有可用 functionObject</td><td>找后处理功能名</td></tr>
<tr><td>-listScalarBCs / -listVectorBCs</td><td>列出可用的标量/矢量边界条件</td><td>忘了边界条件叫什么</td></tr>
<tr><td>-listSwitches</td><td>列出所有调试/优化开关</td><td>高级调试</td></tr>
</table></div>
<p>示例</p>
<pre><code>$ simpleFoam -help                       # 看这个求解器有哪些选项
$ blockMesh -help-full | less            # 看全部选项
$ simpleFoam -case ../pitzDaily          # 算另一个目录里的算例
$ interFoam -dry-run                     # 只检查设置，不真算
$ simpleFoam -listFunctionObjects | head -40
$ pimpleFoam -listVectorBCs | grep -i inlet</code></pre>
<h4>5.2 foamVersion —— 确认版本</h4>
<pre><code>$ foamVersion
OpenFOAM-v2512 (www.openfoam.com) version v2512</code></pre>
<p>用途：任何求助、任何报错帖，第一句都该是版本号。它也是检查 source 有没有生效的最快方法。</p>
<h4>5.3 foamHelp —— 内置的”查手册”命令</h4>
<p>是什么：OpenFOAM 自带的帮助工具，能查边界条件、求解器、functionObject 的可用类型和参数。</p>
<p>为什么需要它：初学者最大的困惑是”这个场能填什么边界条件”。网上教程给的是别人算例里的写法，foamHelp 给的是你这个版本真正支持的全集。</p>
<p>用法</p>
<pre><code>foamHelp boundary [-field &lt;场名&gt;] [-constraint] [-browse &lt;类型名&gt;]
foamHelp solver   [-browse &lt;求解器名&gt;]
foamHelp functionObject [-browse &lt;名字&gt;]</code></pre>
<p>示例</p>
<pre><code># ① 列出 U 场所有可用边界条件（数量很多，建议接 less）
$ foamHelp boundary -field U | less

# ② 只看&quot;约束型&quot;边界条件（empty、cyclic、symmetry 这类）
$ foamHelp boundary -constraint

# ③ 打开某个边界条件的源码文档，看它需要哪些参数
$ foamHelp boundary -browse inletOutlet</code></pre>
<p>提示 foamHelp boundary 必须在一个算例目录里运行（它需要读网格和场信息）。在空目录里跑会报错。</p>
<h4>5.4 foamGet —— 把官方模板抓到手边</h4>
<p>是什么：从 $FOAM_ETC/caseDicts 里把官方字典模板复制到当前算例。</p>
<p>为什么需要它：写 functionObject、写 sample 配置时，从零手敲很容易漏关键字。官方模板是”填空题”，比”问答题”容易得多。</p>
<p>用法与示例</p>
<pre><code>$ foamGet -list                 # 列出所有可取的模板
$ foamGet singleGraph           # 把沿线取样模板拷进 system/
$ foamGet -case ../run1 probes  # 拷到别的算例目录</code></pre>
<p>如果你的版本没有这个命令（which foamGet 查不到），等价的手动做法是直接复制：</p>
<pre><code>$ cp $FOAM_ETC/caseDicts/postProcessing/graphs/singleGraph system/
$ ls $FOAM_ETC/caseDicts/postProcessing/     # 先看看有哪些模板</code></pre>
<h4>5.5 foamEtcFile —— 定位配置文件</h4>
<p>是什么：按 OpenFOAM 的查找顺序（用户 → 站点 → 安装）找出某个配置文件的真实路径。</p>
<pre><code>$ foamEtcFile -list             # 列出配置文件的搜索路径
$ foamEtcFile controlDict       # 全局默认 controlDict 在哪
$ foamEtcFile -all bashrc       # 所有同名文件都列出来</code></pre>
<p>为什么需要它：OpenFOAM 的配置是分层覆盖的（你的 ~/.OpenFOAM/v2512/ 里的设置会盖掉安装目录的）。当”我明明改了配置却没生效”时，用它确认程序实际读的是哪一个文件。</p>
<h4>5.6 foamCloneCase —— 干净地复制算例</h4>
<p>是什么：只复制 0/、constant/、system/，不复制计算结果。</p>
<p>为什么不用 cp -r：cp -r 会把几十 GB 的时间目录一起拷过去，既慢又占地方，而且新算例里混着旧结果，latestTime 会读到不该读的东西。</p>
<pre><code>$ foamCloneCase pitzDaily pitzDaily_fine
$ foamCloneCase -latestTime oldCase newCase   # 用旧算例最后时刻做新算例的初场</code></pre>
<h4>5.7 foamListTimes —— 列出/删除时间目录</h4>
<pre><code>$ foamListTimes                 # 列出所有时间目录
$ foamListTimes -latestTime     # 只打印最后一个时刻
$ foamListTimes -rm             # ★删除全部时间目录（保留 0/），即&quot;清算例&quot;
$ foamListTimes -rm -processor  # 并行算例：连 processor*/ 里的一起删</code></pre>
<p>为什么常用：调参阶段一天要重新计算十几次，每次都得先清掉上一次的结果，否则 startFrom latestTime 会从旧结果续算，你以为改了参数其实没从头算。</p>
<h4>5.8 foamDictionary —— 在命令行读写字典</h4>
<p>是什么：不打开编辑器，直接查询或修改字典文件里的某一项。</p>
<p>为什么需要它：写批量脚本时（参数扫描、网格无关性验证）必须靠它。手动改 20 次 endTime 既慢又容易改错。</p>
<p>用法</p>
<pre><code>foamDictionary &lt;文件&gt; -entry &lt;关键字路径&gt; [-set &lt;值&gt;] [-add &lt;值&gt;] [-remove] [-value] [-keywords] [-expand]</code></pre>
<p>示例</p>
<pre><code># ① 查看 endTime
$ foamDictionary system/controlDict -entry endTime
endTime         0.5;

# ② 只要值，不要关键字（脚本里好用）
$ foamDictionary system/controlDict -entry endTime -value
0.5

# ③ 修改：把 endTime 改成 5
$ foamDictionary system/controlDict -entry endTime -set 5

# ④ 修改嵌套项：p 方程的容差（关键字路径用 / 分隔）
$ foamDictionary system/fvSolution -entry solvers/p/tolerance -set 1e-8

# ⑤ 改边界条件的值
$ foamDictionary 0/U -entry boundaryField/inlet/value -set &quot;uniform (5 0 0)&quot;

# ⑥ 列出某一层有哪些关键字
$ foamDictionary system/fvSolution -entry solvers -keywords

# ⑦ 展开所有 #include、宏和计算，看&quot;程序最终读到的&quot;是什么
$ foamDictionary system/controlDict -expand</code></pre>
<p>第 ⑦ 条在排查”我用了 #include 结果不对”时是决定性的：它把所有包含、变量替换、#calc 全部算完再打印，你看到的就是求解器看到的。</p>
<p>批量脚本示例（网格无关性验证）</p>
<pre><code>for N in 20 40 80 160; do
    foamCloneCase base mesh_$N
    foamDictionary mesh_$N/system/blockMeshDict -entry blocks \
        -set &quot;( hex (0 1 2 3 4 5 6 7) ($N $N 1) simpleGrading (1 1 1) )&quot;
    ( cd mesh_$N &amp;&amp; blockMesh &gt; log.blockMesh &amp;&amp; simpleFoam &gt; log.simpleFoam )
done</code></pre>
<h4>5.9 foamSearch —— 在教程库里搜关键字的取值</h4>
<p>是什么：在一堆算例里搜索某个字典关键字，并把出现过的不同取值汇总去重。</p>
<p>为什么需要它：回答”这个参数别人一般填多少”这类问题。比 grep 强在会去重、按取值归类。</p>
<pre><code># 看官方教程里 p 方程都用过哪些线性求解器
$ foamSearch $FOAM_TUTORIALS fvSolution solvers/p/solver

# 看 ddtSchemes 都有哪些用法
$ foamSearch $FOAM_TUTORIALS fvSchemes ddtSchemes/default</code></pre>
<p>若提示参数顺序不对，敲一次 foamSearch -h 看本机用法。</p>
<h4>5.10 foamLog —— 把日志里的残差拆成可画图的数据</h4>
<p>是什么：解析求解器日志，把每个方程的初始残差、迭代次数、连续性误差等提取成一列列数据文件，放进 logs/ 目录。</p>
<p>为什么需要它：判断算例收敛没有，靠肉眼滚屏是不行的，必须画残差曲线。</p>
<pre><code>$ simpleFoam &gt; log.simpleFoam 2&gt;&amp;1        # 先把日志存下来（这是必须养成的习惯）
$ foamLog log.simpleFoam
$ ls logs/
Ux_0  Uy_0  p_0  contCumulative_0  contGlobal_0  ...
$ gnuplot -p -e &quot;set logscale y; plot &#x27;logs/p_0&#x27; w l, &#x27;logs/Ux_0&#x27; w l&quot;</code></pre>
<h4>5.11 foamMonitor —— 边算边画</h4>
<pre><code>$ foamMonitor -l postProcessing/residuals/0/residuals.dat</code></pre>
<p>-l 表示 y 轴取对数。需要系统装了 gnuplot。这条命令在另一个终端里跑，实时刷新残差曲线。</p>
<h4>5.12 foamJob / foamExec —— 后台运行与环境包装</h4>
<pre><code>$ foamJob simpleFoam                # 后台运行，日志写到 log
$ foamJob -s simpleFoam             # 同时输出到屏幕（screen）
$ foamJob -p -s interFoam           # 并行 + 屏幕输出
$ foamExec simpleFoam -help         # 在正确环境下执行（集群脚本里常用）</code></pre>
<p>为什么需要 foamExec：集群提交作业时，计算节点上的 shell 可能没有 source 过 OpenFOAM 环境，foamExec 会先补上环境再执行。</p>
<h4>5.13 foamSystemCheck / foamInstallationTest</h4>
<pre><code>$ foamSystemCheck        # 编译前：检查 gcc/mpi/flex 等基础环境
$ foamInstallationTest   # 安装后：检查路径、库、命令是否都正常</code></pre>
<p>装完或者环境出问题时先跑这两个，能省掉大量瞎猜。</p>
<h4>5.14 foamCleanTutorials / 清理类命令</h4>
<pre><code>$ foamCleanTutorials       # 递归清理当前目录下所有算例（调用各自的 Allclean）
$ ./Allclean               # 清理单个算例（官方算例大多自带这个脚本）
$ foamListTimes -rm        # 只删时间目录
$ rm -rf processor*        # 删并行分区数据</code></pre>
<h4>5.15 foamNew* —— 生成代码骨架（二次开发用）</h4>
<pre><code>$ foamNewApp myApp                    # 新建一个应用程序骨架
$ foamNewSource app myApp             # 新建源文件模板
$ foamNewBC -f myBC                   # 新建边界条件骨架
$ foamNewFunctionObject myFO          # 新建 functionObject 骨架</code></pre>
<p>为什么用它而不是手写：OpenFOAM 的类要能被运行时选择（RTS），必须有一整套宏、Make/files、Make/options 配套。骨架生成器把这些样板都写好了，你只需要填物理逻辑。具体见第 10 章。</p>
<h4>5.16 Allrun / Allclean 与 RunFunctions</h4>
<p>官方算例里几乎都有 Allrun、Allclean（有的还有 Allmesh、Allpost）。它们是普通 shell 脚本，开头都会 source 两个函数库：</p>
<pre><code>#!/bin/sh
cd &quot;${0%/*}&quot; || exit                                # 切到脚本所在目录
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
<p>0.orig/ 是什么、为什么要有它：setFields 这类命令会就地修改 0/ 里的场。跑第二遍时 0/ 已经被改过了，再 setFields 一次结果就错了。所以官方做法是把干净的初始场存在 0.orig/，每次运行前先 restore0Dir 拷贝一份出来。你自己的算例也应该照这个习惯做。</p>
<p>一个完整的 Allrun 示例（interFoam 溃坝）</p>
<pre><code>#!/bin/sh
cd &quot;${0%/*}&quot; || exit
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions

restore0Dir
runApplication blockMesh
runApplication setFields
runApplication $(getApplication)</code></pre>
<p>CleanFunctions 提供的函数：cleanCase（删时间目录、日志、processor*）、cleanCase0（再把 0/ 也删掉，配合 0.orig 用）、cleanTimeDirectories、cleanPostProcessing、cleanDynamicCode（清 dynamicCode/，改了 codedFixedValue 却不生效时必须清）。</p>
{% endraw %}