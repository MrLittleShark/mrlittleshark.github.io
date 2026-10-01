---
title: "第 4 章　环境变量参考（$WM_* 与 $FOAM_*）"
layout: reference
description: "OpenCFD v2512 环境变量参考（$WM_* 与 $FOAM_*）；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>4.1 先理解：这些变量是干什么的</h2>
<p>source etc/bashrc 之后，你的终端里会多出上百个变量。它们分两类：</p>
<p>WM_ 开头（WM = wmake）：编译期用的。决定用哪个编译器、什么精度、装在哪儿。改了它们要重新编译才生效。</p>
<p>FOAM_ 开头：使用期用的。基本都是路径，让你不用记一长串目录就能跳过去。</p>
<p>环境变量提供稳定的安装、教程和用户工作目录入口。使用 FOAM_TUTORIALS、FOAM_RUN、FOAM_USER_LIBBIN 等变量，可以减少脚本对个人绝对路径的依赖；首次使用仍需确认变量已定义且指向预期版本。</p>
<p>查看方法：</p>
<pre><code class="language-bash">echo &#36;FOAM_TUTORIALS              # 看单个变量
env | grep FOAM_ | sort           # 看所有 FOAM_ 变量
env | grep WM_ | sort             # 看所有 WM_ 变量</code></pre>
<h2>4.2 FOAM_*：路径类（最常用）</h2>
<div class="table-scroll"><table>
<tr><th>变量</th><th>指向</th><th>典型用途</th></tr>
<tr><td>&#36;FOAM_TUTORIALS</td><td>官方算例库</td><td>最常用。找相似算例照抄设置</td></tr>
<tr><td>&#36;FOAM_RUN</td><td>&#36;HOME/OpenFOAM/&lt;用户名&gt;-v2512/run</td><td>你自己的工作目录，算例都放这</td></tr>
<tr><td>&#36;FOAM_SRC</td><td>src/ 核心库源码</td><td>查边界条件、湍流模型怎么实现的</td></tr>
<tr><td>&#36;FOAM_APP</td><td>applications/</td><td>求解器和工具的源码总目录</td></tr>
<tr><td>&#36;FOAM_SOLVERS</td><td>applications/solvers/</td><td>查某个求解器解了哪几个方程</td></tr>
<tr><td>&#36;FOAM_UTILITIES</td><td>applications/utilities/</td><td>查某个工具的源码与默认字典</td></tr>
<tr><td>&#36;FOAM_APPBIN</td><td>可执行文件目录</td><td>ls &#36;FOAM_APPBIN 列出本机所有命令</td></tr>
<tr><td>&#36;FOAM_LIBBIN</td><td>动态库目录</td><td>排查 “cannot open shared object file”</td></tr>
<tr><td>&#36;FOAM_ETC</td><td>etc/</td><td>官方字典模板都在 &#36;FOAM_ETC/caseDicts</td></tr>
<tr><td>&#36;FOAM_USER_APPBIN</td><td>你自己编译的可执行文件</td><td>自写求解器编译后进这里</td></tr>
<tr><td>&#36;FOAM_USER_LIBBIN</td><td>你自己编译的库</td><td>自写边界条件/模型编译后进这里</td></tr>
<tr><td>&#36;FOAM_SITE_APPBIN</td><td>全站共享（多用户集群用）</td><td>单机基本用不到</td></tr>
<tr><td>&#36;FOAM_MPI</td><td>当前 MPI 实现的名字</td><td>如 openmpi-system，排查并行问题时看</td></tr>
<tr><td>&#36;FOAM_API</td><td>2512</td><td>脚本里判断版本用</td></tr>
<tr><td>&#36;FOAM_JOB_DIR</td><td>foamJob 的日志目录</td><td>集群批量作业时用</td></tr>
<tr><td>&#36;WM_PROJECT_USER_DIR</td><td>&#36;HOME/OpenFOAM/&lt;用户名&gt;-v2512</td><td>你的私有开发目录（源码放这，见第 10 章）</td></tr>
</table></div>
<p>四个”调试开关”型变量（不是路径，是行为控制，排错时极有用）：</p>
<div class="table-scroll"><table>
<tr><th>变量</th><th>作用</th><th>怎么用</th></tr>
<tr><td>FOAM_SIGFPE</td><td>捕获浮点异常（除零、NaN）并立即中止 + 打印调用栈</td><td><code>export FOAM_SIGFPE=true</code></td></tr>
<tr><td>FOAM_SETNAN</td><td>把新分配的内存初始化成 NaN，让”用了未初始化变量”立刻暴露</td><td><code>export FOAM_SETNAN=true</code></td></tr>
<tr><td>FOAM_ABORT</td><td>让 FatalError 触发 abort 并生成 core dump，方便 gdb 调试</td><td><code>export FOAM_ABORT=true</code></td></tr>
<tr><td>FOAM_CODE_TEMPLATES</td><td>codedFixedValue 等动态编译功能的模板目录</td><td>自定义模板时改</td></tr>
</table></div>
<p>FOAM_SIGFPE 用于启用浮点异常捕获。在运行环境支持的情况下，它可帮助定位除零、无效浮点运算等异常。异常位置仍需结合调用栈、初始场、边界条件及离散设置分析。</p>
<h2>4.3 WM_*：编译类</h2>
<div class="table-scroll"><table>
<tr><th>变量</th><th>典型值</th><th>含义</th></tr>
<tr><td>&#36;WM_PROJECT</td><td>OpenFOAM</td><td>项目名</td></tr>
<tr><td>&#36;WM_PROJECT_VERSION</td><td>v2512</td><td>版本</td></tr>
<tr><td>&#36;WM_PROJECT_DIR</td><td>~/OpenFOAM/OpenFOAM-v2512</td><td>安装根目录</td></tr>
<tr><td>&#36;WM_OPTIONS</td><td>linux64GccDPInt32Opt</td><td>平台串，platforms/ 下的子目录名</td></tr>
<tr><td>&#36;WM_ARCH</td><td>linux64</td><td>系统架构</td></tr>
<tr><td>&#36;WM_COMPILER</td><td>Gcc / Clang</td><td>编译器</td></tr>
<tr><td>&#36;WM_COMPILER_TYPE</td><td>system / ThirdParty</td><td>用系统编译器还是自带的</td></tr>
<tr><td>&#36;WM_COMPILE_OPTION</td><td>Opt / Debug / Prof</td><td>优化 / 调试 / 性能剖析</td></tr>
<tr><td>&#36;WM_PRECISION_OPTION</td><td>DP / SP / SPDP</td><td>双精度 / 单精度 / 混合</td></tr>
<tr><td>&#36;WM_LABEL_SIZE</td><td>32 / 64</td><td>网格标签整型位宽。超过 20 亿网格才需要 64</td></tr>
<tr><td>&#36;WM_MPLIB</td><td>SYSTEMOPENMPI</td><td>用哪个 MPI</td></tr>
<tr><td>&#36;WM_NCOMPPROCS</td><td>8</td><td>编译时并行核数</td></tr>
<tr><td>&#36;WM_THIRD_PARTY_DIR</td><td>~/OpenFOAM/ThirdParty-v2512</td><td>第三方库目录</td></tr>
<tr><td>&#36;WM_DIR</td><td>&#36;WM_PROJECT_DIR/wmake</td><td>编译系统所在</td></tr>
<tr><td>&#36;WM_PROJECT_SITE</td><td>（常为空）</td><td>多用户站点共享目录</td></tr>
</table></div>
<p>用得上的场景：合作者说”我这儿能跑你那儿不能”，第一件事就是对比双方的 echo &#36;WM_OPTIONS——精度不同（DP vs SP）、标签位宽不同（Int32 vs Int64）编译出来的库互不兼容。</p>
<h2>4.4 快捷别名：tut、sol、run……</h2>
<p>etc/config.sh/aliases 里预定义了一批别名，全是”跳目录”和”改编译选项”的：</p>
<div class="table-scroll"><table>
<tr><th>别名</th><th>等价于</th><th>说明</th></tr>
<tr><td>foam</td><td>cd &#36;WM_PROJECT_DIR</td><td>回安装根目录</td></tr>
<tr><td>run</td><td>cd &#36;FOAM_RUN</td><td>回你的工作目录</td></tr>
<tr><td>tut</td><td>cd &#36;FOAM_TUTORIALS</td><td>去官方算例库</td></tr>
<tr><td>src</td><td>cd &#36;FOAM_SRC</td><td>去核心库源码</td></tr>
<tr><td>app</td><td>cd &#36;FOAM_APP</td><td>去应用源码</td></tr>
<tr><td>sol</td><td>cd &#36;FOAM_SOLVERS</td><td>去求解器源码</td></tr>
<tr><td>util</td><td>cd &#36;FOAM_UTILITIES</td><td>去工具源码</td></tr>
<tr><td>lib</td><td>cd &#36;FOAM_LIBBIN</td><td>去库目录</td></tr>
<tr><td>wmSet</td><td>重新 source etc/bashrc</td><td>改完编译选项后刷新环境</td></tr>
<tr><td>wmUnset</td><td>清除全部 OpenFOAM 环境变量</td><td>切版本前用</td></tr>
<tr><td>wmRefresh</td><td>清环境 + 重新 source</td><td>相当于 wmUnset; wmSet</td></tr>
<tr><td>wmDP / wmSP</td><td>切双精度 / 单精度</td><td>切完要重新编译</td></tr>
<tr><td>wmInt32 / wmInt64</td><td>切标签位宽</td><td>同上</td></tr>
<tr><td>wmSchedOn / wmSchedOff</td><td>开/关分布式编译调度</td><td>集群编译用</td></tr>
</table></div>
<p>查看你这台机器上实际有哪些别名（不同版本略有出入，以本机为准）：</p>
<pre><code class="language-plaintext">alias | grep -E 'cd \$(FOAM|WM)'</code></pre>
<p>示例：别名到底省了多少事</p>
<pre><code class="language-bash">tut                                    # 一步跳到教程库
cd incompressible/simpleFoam/pitzDaily # 打开经典的后台阶算例
run                                    # 一步跳回工作目录
cp -r &#36;FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily .   # 复制到工作目录</code></pre>
<h2>4.5 常用”找东西”套路（把变量真正用起来）</h2>
<pre><code class="language-plaintext"># ① 本机所有可执行命令（求解器 + 工具），约 200 多个
ls &#36;FOAM_APPBIN | sort | less

# ② 所有 foam 开头的脚本类命令
ls &#36;WM_PROJECT_DIR/bin

# ③ 找出所有可压缩求解器
ls &#36;FOAM_SOLVERS/compressible

# ④ 哪些教程用了 interFoam（找相似算例）
grep -rl "application *interFoam" &#36;FOAM_TUTORIALS --include=controlDict

# ⑤ 别人的 fvSolution 里 p 用什么线性求解器（学习别人的参数选择）
grep -rA3 "^ *p$" &#36;FOAM_TUTORIALS/incompressible/simpleFoam/*/system/fvSolution | grep solver

# ⑥ 某个边界条件的源码在哪、有哪些可选参数
find &#36;FOAM_SRC -name "*inletOutlet*"

# ⑦ 官方字典模板（functionObject 模板全在这）
ls &#36;FOAM_ETC/caseDicts/postProcessing/</code></pre>
<p>第 ④⑤ 条是这一章最值钱的东西：遇到不会设的参数，不要凭空猜，去 &#36;FOAM_TUTORIALS 里找一个物理上最接近的官方算例照抄。官方算例是被验证过的，你猜的不是。</p>
<h2>第二部分　命令参考</h2><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>
{% endraw %}
