---
title: "files"
layout: reference
description: "Make/files 列出参与编译的源文件，并指定可执行程序 EXE 或共享库 LIB 的输出位置。"
dictionary: true
cms_slug: "dictionary-files"
---

<p>Make/files 列出参与编译的源文件，并指定可执行程序 EXE 或共享库 LIB 的输出位置。</p><p>位置：<code>Make/files</code></p><h2>配置实例</h2><pre><code class="language-bash"># Make/files
myScalarFoam.C

EXE = $(FOAM_USER_APPBIN)/myScalarFoam
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude

EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 <code>LIB = $(FOAM_USER_LIBBIN)/libMyModel</code>，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。</p><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · applications/utilities/postProcessing/noise/Make</summary><p>noise 的 Make/files 告诉 wmake 编译哪个源文件、把可执行程序放在哪里。</p>
<ul>
<li><code>noise.C</code> 是参与当前目标构建的源文件。</li>
<li><code>EXE = $(FOAM_APPBIN)/noise</code> 指定官方应用输出目录和程序名。</li>
<li>头文件搜索与链接库通常由相邻 Make/options 补充。</li>
</ul>
<p>创建自己的版本时可改程序名并输出到 FOAM_USER_APPBIN，随后通过 command -v 确认调用路径。</p>
<p><a href="/assets/examples/v2512/files/1-files.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/noise/Make/files">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/utilities/postProcessing/noise/Make">案例目录</a></p><pre><code class="language-foam">noise.C

EXE = $(FOAM_APPBIN)/noise</code></pre></details><details class="reference-example"><summary>示例 2 · applications/solvers/combustion/XiFoam/Make</summary><p>XiFoam 的构建入口由这个文件列出。</p>
<ul>
<li><code>XiFoam.C</code> 提供主程序源文件，其他实现可通过包含文件和链接库配合。</li>
<li><code>EXE = $(FOAM_APPBIN)/XiFoam</code> 将目标命名为 XiFoam。</li>
<li>增加独立编译的 .C 文件时需要加入源文件清单。</li>
</ul>
<p>学习修改时可复制为不同名称的用户应用，并同步检查 Make/options 所列依赖。</p>
<p><a href="/assets/examples/v2512/files/2-files.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/XiFoam/Make/files">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/solvers/combustion/XiFoam/Make">案例目录</a></p><pre><code class="language-foam">XiFoam.C

EXE = $(FOAM_APPBIN)/XiFoam</code></pre></details><details class="reference-example"><summary>示例 3 · applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make</summary><p>分子动力学求解器 mdFoam 的 Make/files 组织可执行程序构建。</p>
<ul>
<li><code>mdFoam.C</code> 是当前编译源文件。</li>
<li>输出目标为 <code>$(FOAM_APPBIN)/mdFoam</code>。</li>
<li>该文件管理源清单和目标位置，分子相互作用库等依赖由配套构建设置提供。</li>
</ul>
<p>扩展求解器时将新源文件纳入清单，并保持自己的目标名和输出目录清晰。</p>
<p><a href="/assets/examples/v2512/files/3-files.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make/files">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/applications/solvers/discreteMethods/molecularDynamics/mdFoam/Make">案例目录</a></p><pre><code class="language-foam">mdFoam.C

EXE = $(FOAM_APPBIN)/mdFoam</code></pre></details><h2>相关命令</h2><p><a href="/commands/wmake/">wmake</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到头文件</td><td>核对 EXE_INC、库 lnInclude 是否生成以及当前 WM_PROJECT_DIR。</td></tr><tr><td>链接时 undefined reference</td><td>核对 EXE_LIBS / LIB_LIBS、库名与链接顺序，并确认实现文件参与编译。</td></tr><tr><td>加载共享库失败</td><td>检查编译使用的 v2512 环境与运行时 ABI、库搜索路径和 controlDict 的 libs。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
