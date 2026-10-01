---
title: "Make/files · files"
layout: reference
description: "在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 LIB = $(FOAM_USER_LIBBIN)/libMyModel，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 LIB = &#36;(FOAM_USER_LIBBIN)/libMyModel，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 &#36;(FOAM_USER_APPBIN) 形式，Bash 变量采用 &#36;{FOAM_USER_APPBIN} 形式。</p><figure><img src="/assets/diagrams/reference-9.svg" alt="编译配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>Make/files</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>EXE</code> · <code>LIB</code> · <code>FOAM_USER_APPBIN</code> · <code>FOAM_USER_LIBBIN</code></p><h2>关联命令</h2><p><a href="/commands/?q=wmake">wmake</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
cat Make/files
wmake -help</code></pre><h2>9.14 Make/files 与 Make/options</h2><pre><code class="language-bash"># Make/files
myScalarFoam.C

EXE = $(FOAM_USER_APPBIN)/myScalarFoam
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude

EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 <code>LIB = $(FOAM_USER_LIBBIN)/libMyModel</code>，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。</p><h2>从真实配置理解关键条目</h2><p>该专用配置的字段由对应程序决定。阅读下面完整文件时，应把同一层的大括号块作为一个模型实例，并从 Allrun 和 #include 追踪输入关系；本页不为缺少直接证据的键杜撰默认值。</p><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · applications/utilities/postProcessing/noise/Make</h3><p>原始路径：<code>applications/utilities/postProcessing/noise/Make/files</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/noise/Make/files">查看固定版本源码</a> · <a href="/assets/examples/v2512/files/1-files.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/utilities/postProcessing/noise/Make">查看配套目录</a></p><pre><code class="language-makefile">noise.C

EXE = &#36;(FOAM_APPBIN)/noise</code></pre><h3>示例 2 · applications/solvers/combustion/XiFoam/Make</h3><p>原始路径：<code>applications/solvers/combustion/XiFoam/Make/files</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/XiFoam/Make/files">查看固定版本源码</a> · <a href="/assets/examples/v2512/files/2-files.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/solvers/combustion/XiFoam/Make">查看配套目录</a></p><pre><code class="language-makefile">XiFoam.C

EXE = &#36;(FOAM_APPBIN)/XiFoam</code></pre><h3>示例 3 · applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make</h3><p>原始路径：<code>applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make/files</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make/files">查看固定版本源码</a> · <a href="/assets/examples/v2512/files/3-files.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make">查看配套目录</a></p><pre><code class="language-makefile">mdFoam.C

EXE = &#36;(FOAM_APPBIN)/mdFoam</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/wmake/">wmake</a></p><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到头文件</td><td>核对 EXE_INC、库 lnInclude 是否生成以及当前 WM_PROJECT_DIR。</td></tr><tr><td>链接时 undefined reference</td><td>核对 EXE_LIBS / LIB_LIBS、库名与链接顺序，并确认实现文件参与编译。</td></tr><tr><td>加载共享库失败</td><td>检查编译使用的 v2512 环境与运行时 ABI、库搜索路径和 controlDict 的 libs。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
