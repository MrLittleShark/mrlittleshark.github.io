---
title: "11 环境变量与编译工具"
layout: reference
description: "环境变量与编译工具：用法与配置实例。"
cms_slug: "reference-manual-11"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>11.1 环境加载与检查</h3>
<p>以下命令在 Linux 或 WSL 的 Bash 环境中执行。加载路径按实际安装位置设置，环境配置见 etc/bashrc、etc/config.sh/settings 和 aliases，编译配置见 wmake。</p>
<pre><code class="language-bash">source /实际安装路径/OpenFOAM-v2512/etc/bashrc
printf '%s\n' "$WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名
echo "$WM_PROJECT_VERSION"
echo "$WM_PROJECT_DIR"
type foam tut sol foamVersion
command -v blockMesh
blockMesh -help</code></pre>
<p>source 在当前 shell 中加载环境；通过 bash 启动的脚本仅设置子进程环境。将正确的 source 命令写入 ~/.bashrc，可在新终端中自动加载。非交互脚本通常采用 cd "$FOAM_TUTORIALS" 等路径命令，避免依赖未展开的别名。</p>
<h3>11.2 FOAM 系列变量</h3>
<p>使用 printf '%s\n' "$变量名" 查询变量值。下表按默认源码安装环境说明路径关系，软件包安装的目录前缀以实际环境为准。</p>
<div class="table-scroll"><table>
<tr><th>变量</th><th>含义</th><th>用法示例</th></tr>
<tr><td>FOAM_API</td><td>数值 API 版本，本手册为 2512</td><td>echo "$FOAM_API"</td></tr>
<tr><td>FOAM_TUTORIALS</td><td>官方教程根目录</td><td>find "$FOAM_TUTORIALS" -name controlDict</td></tr>
<tr><td>FOAM_RUN</td><td>用户算例工作目录</td><td>mkdir -p "$FOAM_RUN"</td></tr>
<tr><td>FOAM_SRC</td><td>源码库目录</td><td>cd "$FOAM_SRC/finiteVolume"</td></tr>
<tr><td>FOAM_APP</td><td>应用源码目录</td><td>ls "$FOAM_APP"</td></tr>
<tr><td>FOAM_SOLVERS</td><td>求解器源码目录</td><td>find "$FOAM_SOLVERS" -name '*.C'</td></tr>
<tr><td>FOAM_UTILITIES</td><td>工具源码目录</td><td>ls "$FOAM_UTILITIES/mesh"</td></tr>
<tr><td>FOAM_ETC</td><td>安装配置目录</td><td>ls "$FOAM_ETC/caseDicts"</td></tr>
<tr><td>FOAM_APPBIN</td><td>当前构建的官方可执行程序目录</td><td>ls "$FOAM_APPBIN"</td></tr>
<tr><td>FOAM_LIBBIN</td><td>当前构建的官方共享库目录</td><td>ls "$FOAM_LIBBIN"</td></tr>
<tr><td>FOAM_USER_APPBIN</td><td>用户编译应用输出目录</td><td>ls "$FOAM_USER_APPBIN"</td></tr>
<tr><td>FOAM_USER_LIBBIN</td><td>用户编译共享库输出目录</td><td>ls "$FOAM_USER_LIBBIN"</td></tr>
<tr><td>FOAM_SITE_APPBIN、FOAM_SITE_LIBBIN</td><td>站点构建输出目录</td><td>echo "$FOAM_SITE_LIBBIN"</td></tr>
<tr><td>FOAM_MPI、FOAM_MPI_LIBBIN</td><td>MPI 配置及相应库目录</td><td>echo "$FOAM_MPI"</td></tr>
<tr><td>FOAM_CONFIG_ETC</td><td>可定制的配置查找位置</td><td>echo "$FOAM_CONFIG_ETC"；foamEtcFile -list</td></tr>
<tr><td>FOAM_SETTINGS</td><td>当前环境加载设置记录</td><td>echo "$FOAM_SETTINGS"</td></tr>
<tr><td>FOAM_FILEHANDLER</td><td>默认 IO 文件处理器</td><td><code>export FOAM_FILEHANDLER=collated</code></td></tr>
<tr><td>FOAM_SIGFPE</td><td>是否捕获浮点异常</td><td><code>export FOAM_SIGFPE=true</code></td></tr>
<tr><td>FOAM_SETNAN</td><td>将部分新分配内存初始化为 NaN，辅助排错</td><td><code>export FOAM_SETNAN=true</code></td></tr>
<tr><td>FOAM_ABORT</td><td>发生错误时调用 abort</td><td><code>export FOAM_ABORT=1</code>，用于调试</td></tr>
<tr><td>FOAM_JOB_DIR</td><td>启用作业记录时的目录</td><td>echo "$FOAM_JOB_DIR"；未配置时可能为空</td></tr>
<tr><td>FOAM_CASE</td><td>当前应用运行中的算例绝对路径</td><td>字典中 #include "${FOAM_CASE}/system/common"</td></tr>
<tr><td>FOAM_CASENAME</td><td>当前应用运行中的算例名称</td><td>用于该进程的环境或字典展开</td></tr>
</table></div>
<p>FOAM_CASE 和 FOAM_CASENAME 由 OpenFOAM 应用在运行进程中设置，可供该进程内的字典展开使用。教程目录变量为 FOAM_TUTORIALS。</p>
<h3>11.3 WM 系列变量与编译配置</h3>
<div class="table-scroll"><table>
<tr><th>变量</th><th>含义</th><th>示例与说明</th></tr>
<tr><td>WM_PROJECT</td><td>项目名</td><td>通常 OpenFOAM</td></tr>
<tr><td>WM_PROJECT_VERSION</td><td>带 v 的版本字符串</td><td>v2512</td></tr>
<tr><td>WM_PROJECT_DIR</td><td>安装或源码根目录</td><td>cd "$WM_PROJECT_DIR"</td></tr>
<tr><td>WM_PROJECT_USER_DIR</td><td>用户开发根目录</td><td>mkdir -p "$WM_PROJECT_USER_DIR/applications"</td></tr>
<tr><td>WM_PROJECT_SITE</td><td>站点配置和扩展目录</td><td>未配置站点时可为空</td></tr>
<tr><td>WM_THIRD_PARTY_DIR</td><td>第三方依赖源码目录</td><td>用于源码构建，软件包安装按实际提供情况确定</td></tr>
<tr><td>WM_DIR</td><td>wmake 所在目录</td><td>ls "$WM_DIR"</td></tr>
<tr><td>WM_ARCH</td><td>平台架构标识</td><td>例如 linux64，由环境检测</td></tr>
<tr><td>WM_ARCH_OPTION</td><td>32 或 64 位平台配置</td><td>与硬件和构建一致</td></tr>
<tr><td>WM_COMPILER_TYPE</td><td>编译器来源</td><td>如 system</td></tr>
<tr><td>WM_COMPILER</td><td>编译器工具链</td><td>如 Gcc 或 Clang</td></tr>
<tr><td>WM_PRECISION_OPTION</td><td>标量精度</td><td>DP、SP、SPDP，须有匹配的已编译库</td></tr>
<tr><td>WM_LABEL_SIZE</td><td>label 整数位宽</td><td>32 或 64</td></tr>
<tr><td>WM_LABEL_OPTION</td><td>派生 label 标识</td><td>如 Int32</td></tr>
<tr><td>WM_COMPILE_OPTION</td><td>构建模式</td><td>Opt、Debug、Prof 等可用模式</td></tr>
<tr><td>WM_OPTIONS</td><td>由平台编译配置组合的目录标识</td><td>例如 linux64GccDPInt32Opt</td></tr>
<tr><td>WM_MPLIB</td><td>MPI 选择</td><td>如 SYSTEMOPENMPI</td></tr>
<tr><td>WM_NCOMPPROCS</td><td>编译并发数</td><td><code>export WM_NCOMPPROCS=4</code>，设置编译并发数</td></tr>
<tr><td>MPI_ARCH_PATH</td><td>MPI 安装前缀</td><td>用于核对编译和运行阶段的 MPI 路径</td></tr>
<tr><td>PATH</td><td>可执行文件搜索路径</td><td>command -v simpleFoam 查询实际程序路径</td></tr>
<tr><td>LD_LIBRARY_PATH</td><td>Linux 共享库搜索路径</td><td>echo "$LD_LIBRARY_PATH" 查询库搜索路径</td></tr>
</table></div>
<p>旧版变量 WM_PROJECT_INST_DIR 在当前环境中可未定义。精度和整数位宽切换后，需使用对应配置编译的可执行程序及库。用户应用、第三方库和 OpenFOAM 核心应保持 ABI 兼容。</p>
<h3>11.4 目录别名</h3>
<p>目录别名定义于 etc/config.sh/aliases，直接输入名称即可切换目录。进入下级目录时另用 cd，例如执行 sol 后再执行 cd incompressible/icoFoam。</p>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义</th><th>操作示例</th></tr>
<tr><td>foam</td><td>进入 WM_PROJECT_DIR</td><td>foam；pwd</td></tr>
<tr><td>src</td><td>进入核心库源码目录</td><td>src；ls</td></tr>
<tr><td>lib</td><td>进入 FOAM_LIBBIN</td><td>lib；ls libfiniteVolume*</td></tr>
<tr><td>app</td><td>进入 applications</td><td>app；ls</td></tr>
<tr><td>sol</td><td>进入 applications/solvers</td><td>sol；cd incompressible/icoFoam</td></tr>
<tr><td>util</td><td>进入 applications/utilities</td><td>util；cd mesh/generation/blockMesh</td></tr>
<tr><td>tut</td><td>进入 FOAM_TUTORIALS</td><td>tut；cd incompressible/icoFoam/cavity/cavity</td></tr>
<tr><td>run</td><td>进入 FOAM_RUN</td><td>mkdir -p "$FOAM_RUN"；run</td></tr>
<tr><td>ufoam</td><td>进入用户开发根目录</td><td>ufoam；pwd</td></tr>
<tr><td>uapp</td><td>进入用户 applications 目录</td><td>建立用户 applications 目录后执行 uapp</td></tr>
<tr><td>usol</td><td>进入用户 applications/solvers</td><td>建立用户 applications/solvers 目录后执行 usol</td></tr>
<tr><td>uutil</td><td>进入用户 applications/utilities</td><td>建立用户 applications/utilities 目录后执行 uutil</td></tr>
</table></div>
<h3>11.5 环境查询与切换</h3>
<div class="table-scroll"><table>
<tr><th>命令</th><th>含义</th><th>用法和示例</th></tr>
<tr><td>foamVersion</td><td>查询当前版本，或切换到同级已安装版本</td><td>foamVersion；foamVersion v2512</td></tr>
<tr><td>foamPwd</td><td>以环境变量缩写显示当前路径</td><td>foamPwd</td></tr>
<tr><td>foamPV</td><td>切换或刷新 ParaView 环境</td><td>foamPV；已安装对应版本时执行 foamPV 5.12.1</td></tr>
<tr><td>wmSet</td><td>重新加载 bashrc 并应用指定设置</td><td><code>wmSet WM_COMPILE_OPTION=Debug</code></td></tr>
<tr><td>wmRefresh</td><td>按已有设置清除并刷新环境</td><td>wmRefresh</td></tr>
<tr><td>wmUnset</td><td>移除当前 OpenFOAM 环境</td><td>wmUnset</td></tr>
<tr><td>wmInt32</td><td>切换到 32 位 label 配置</td><td>wmInt32，使用对应配置的程序和库</td></tr>
<tr><td>wmInt64</td><td>切换到 64 位 label 配置</td><td>wmInt64，使用对应配置的程序和库</td></tr>
<tr><td>wmDP</td><td>切换双精度配置</td><td>wmDP</td></tr>
<tr><td>wmSP</td><td>切换单精度配置</td><td>wmSP</td></tr>
<tr><td>wmSPDP</td><td>切换混合精度配置</td><td>wmSPDP</td></tr>
</table></div>
<p>foamVersion 按同级 OpenFOAM-版本目录查找并切换环境。type foamVersion 可查看当前实际生效的函数定义。</p>
<h3>11.6 编译工具与运行函数</h3>
<div class="table-scroll"><table>
<tr><th>命令或函数</th><th>含义</th><th>具体用法与示例</th></tr>
<tr><td>wmake</td><td>按 Make 配置构建应用或库</td><td>wmake；wmake -j 4；wmake libso</td></tr>
<tr><td>wclean</td><td>清理当前应用或库构建产物</td><td>wclean；wclean libso</td></tr>
<tr><td>wmakeLnInclude</td><td>创建头文件 lnInclude 链接目录</td><td>在库源码目录执行 wmakeLnInclude .</td></tr>
<tr><td>Allwmake</td><td>工程提供的批量构建脚本</td><td>./Allwmake -j 4；参数以该脚本为准</td></tr>
<tr><td>getApplication</td><td>读取 controlDict 中的 application</td><td>加载 RunFunctions 后执行 getApplication</td></tr>
<tr><td>getNumberOfProcessors</td><td>读取分区数量</td><td>加载 RunFunctions 后执行 getNumberOfProcessors</td></tr>
<tr><td>runApplication</td><td>执行应用并保存 log.应用名</td><td>runApplication blockMesh，默认按已有日志判断是否跳过</td></tr>
<tr><td>runParallel</td><td>按分区设置执行 MPI 应用</td><td>执行 decomposePar 后运行 runParallel simpleFoam</td></tr>
<tr><td>restore0Dir</td><td>从 0.orig 恢复初始场</td><td>restore0Dir，重建初始场目录</td></tr>
<tr><td>cleanCase</td><td>清理计算结果和工作文件</td><td>加载 CleanFunctions 后执行 cleanCase</td></tr>
</table></div>
<pre><code class="language-plaintext">. "$WM_PROJECT_DIR/bin/tools/RunFunctions"
getApplication
runApplication blockMesh
runApplication checkMesh
runApplication "$(getApplication)"</code></pre>
<p>RunFunctions 和 CleanFunctions 为 shell 函数库，使用前通过 source 加载。runApplication 检测到已有日志时会跳过执行；重新计算时可采用其覆盖选项，或移除对应日志后运行。</p><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>
