---
title: "options"
layout: reference
description: "Make/options 设置头文件搜索路径和链接库，供 wmake 编译应用程序或共享库。"
dictionary: true
cms_slug: "dictionary-options"
---

<p>Make/options 设置头文件搜索路径和链接库，供 wmake 编译应用程序或共享库。</p><p>位置：<code>Make/options</code></p><h2>配置实例</h2><pre><code class="language-bash"># Make/files
myScalarFoam.C

EXE = $(FOAM_USER_APPBIN)/myScalarFoam
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude

EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 <code>LIB = $(FOAM_USER_LIBBIN)/libMyModel</code>，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · applications/test/predicates/Make</summary><p>predicates 测试的 Make/options 为空，表示这里没有额外声明本地头文件路径或链接选项。</p>
<ul>
<li>编译仍使用 wmake 的通用规则与环境配置。</li>
<li>源文件和目标名在相邻 Make/files 中声明。</li>
<li>新增外部头文件或库时再添加相应 EXE_INC、EXE_LIBS。</li>
</ul>
<p>出现头文件或链接错误时，分别检查搜索路径和链接依赖。</p>
<p><a href="/assets/examples/v2512/options/1-options.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/test/predicates/Make/options">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/test/predicates/Make">案例目录</a></p><pre><code class="language-foam">/**/</code></pre></details><details class="reference-example"><summary>示例 2 · applications/test/codeStream/Make</summary><p>codeStream 测试显式保留了一个空的 EXE_INC 入口。</p>
<ul>
<li><code>EXE_INC =</code> 没有附加自定义 include 目录。</li>
<li>源代码可继续使用构建环境已经提供的头文件搜索路径。</li>
<li>新增本地头文件目录时使用 <code>-I路径</code> 写在这个变量中。</li>
</ul>
<p>涉及新库时还需配置链接项，头文件可见与符号可链接是构建的两个步骤。</p>
<p><a href="/assets/examples/v2512/options/2-options.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/test/codeStream/Make/options">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/test/codeStream/Make">案例目录</a></p><pre><code class="language-foam">EXE_INC =</code></pre></details><details class="reference-example"><summary>示例 3 · applications/test/MathFunctions/Make</summary><p>MathFunctions 测试复用相邻 TestTools 目录中的测试辅助头文件。</p>
<ul>
<li><code>EXE_INC = -I../TestTools</code> 将相对目录加入头文件搜索。</li>
<li><code>..</code> 相对于当前应用构建目录解释，因此目录层级影响能否找到文件。</li>
<li>当前文件没有额外列出 EXE_LIBS。</li>
</ul>
<p>移动测试代码时同步更新 include 路径，并根据新增调用检查链接依赖。</p>
<p><a href="/assets/examples/v2512/options/3-options.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/test/MathFunctions/Make/options">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/test/MathFunctions/Make">案例目录</a></p><pre><code class="language-foam">EXE_INC = -I../TestTools</code></pre></details><h2>相关命令</h2><p><a href="/commands/wmake/">wmake</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到头文件</td><td>核对 EXE_INC、库 lnInclude 是否生成以及当前 WM_PROJECT_DIR。</td></tr><tr><td>链接时 undefined reference</td><td>核对 EXE_LIBS / LIB_LIBS、库名与链接顺序，并确认实现文件参与编译。</td></tr><tr><td>加载共享库失败</td><td>检查编译使用的 v2512 环境与运行时 ABI、库搜索路径和 controlDict 的 libs。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
