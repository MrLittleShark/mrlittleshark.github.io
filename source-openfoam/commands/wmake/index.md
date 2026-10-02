---
title: "wmake · 读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库"
layout: reference
description: "读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。"
cms_slug: "command-wmake"
---

<p>读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。</p><h2>开始前</h2>
<p>加载 v2512 编译环境。myUtility 与 myLibrary 是个人可写源码目录，各自具有 Make/files 和 Make/options；输出位置由 EXE 或 LIB 指定。</p>
<h2>示例 1：构建可执行程序</h2>
<pre><code class="language-bash">wmake myUtility
</code></pre>
<p>读取目标目录 Make 配置，生成可执行文件。</p>
<h2>示例 2：使用四个编译任务</h2>
<pre><code class="language-bash">wmake -j 4 myUtility
</code></pre>
<p>限制同时编译的任务数，减少大型项目构建耗时。</p>
<h2>示例 3：构建动态库</h2>
<pre><code class="language-bash">wmake libso myLibrary
</code></pre>
<p>按 LIB 目标生成共享库，供求解器或运行时选择机制加载。</p>
<h2>示例 4：只生成依赖</h2>
<pre><code class="language-bash">wmake dep myUtility
</code></pre>
<p>创建 lnInclude 和依赖信息，不完成最终链接。</p>
<h2>示例 5：为调试增加信息</h2>
<pre><code class="language-bash">wmake -debug-O0 myUtility
</code></pre>
<p>加调试符号、FULLDEBUG 并关闭优化，便于逐行调试当前应用。</p>
<h2>示例 6：编译整个用户项目树</h2>
<pre><code class="language-bash">wmake -all "$WM_PROJECT_USER_DIR/applications"
</code></pre>
<p>递归处理子目录；遇到 Allwmake 时按其流程构建。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-s | -silent</code></td><td>Silent mode (do not echo commands)</td></tr><tr><td><code>-a | -all</code></td><td>wmake all sub-directories, runs Allwmake if present</td></tr><tr><td><code>-q | -queue</code></td><td>Collect as single Makefile, runs Allwmake if present</td></tr><tr><td><code>-k | -keep-going</code></td><td>Keep going even when errors occur (-non-stop)</td></tr><tr><td><code>-j | -jN | -j N</code></td><td>Compile using all or specified N cores/hyperthreads</td></tr><tr><td><code>-update</code></td><td>Update lnInclude, dep files, remove deprecated files/dirs</td></tr><tr><td><code>-all=FILE</code></td><td>Runs specified file (in pwd) instead of Allwmake</td></tr><tr><td><code>-debug</code></td><td>Add &#x27;-g -DFULLDEBUG&#x27; flags</td></tr><tr><td><code>-debug-O[g0123]</code></td><td>Add &#x27;-g -DFULLDEBUG&#x27; flags and optimization level</td></tr><tr><td><code>-strict</code></td><td>More deprecation warnings (&#x27;+strict&#x27; WM_COMPILE_CONTROL)</td></tr><tr><td><code>-build-root=PATH</code></td><td>Specify FOAM_BUILDROOT for compilation intermediates</td></tr><tr><td><code>-module-prefix=PATH</code></td><td>Specify FOAM_MODULE_PREFIX as absolute/relative path</td></tr><tr><td><code>-module-prefix=TYPE</code></td><td>Specify FOAM_MODULE_PREFIX as predefined type (u,user | g,group | o,openfoam)</td></tr><tr><td><code>-no-openfoam</code></td><td>Disable OpenFOAM linking (&#x27;~openfoam&#x27; WM_COMPILE_CONTROL)</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/make-files/">files</a> · <a href="/dictionaries/make-options/">options</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake [OPTION] [dir]
       wmake [OPTION] target [dir [MakeDir]]
       wmake -subcommand ...

options:
  -s | -silent      Silent mode (do not echo commands)
  -a | -all         wmake all sub-directories, runs Allwmake if present
  -q | -queue       Collect as single Makefile, runs Allwmake if present
  -k | -keep-going  Keep going even when errors occur (-non-stop)
  -j | -jN | -j N   Compile using all or specified N cores/hyperthreads
  -update           Update lnInclude, dep files, remove deprecated files/dirs

  -all=FILE         Runs specified file (in pwd) instead of Allwmake
  -debug            Add &#x27;-g -DFULLDEBUG&#x27; flags
  -debug-O[g0123]   Add &#x27;-g -DFULLDEBUG&#x27; flags and optimization level
  -strict           More deprecation warnings (&#x27;+strict&#x27; WM_COMPILE_CONTROL)
  -build-root=PATH      Specify FOAM_BUILDROOT for compilation intermediates
  -module-prefix=PATH   Specify FOAM_MODULE_PREFIX as absolute/relative path
  -module-prefix=TYPE   Specify FOAM_MODULE_PREFIX as predefined type
                        (u,user | g,group | o,openfoam)
  -no-openfoam      Disable OpenFOAM linking (&#x27;~openfoam&#x27; WM_COMPILE_CONTROL)
  -openmp           Compile/link with openmp (&#x27;+openmp&#x27; WM_COMPILE_CONTROL)
  -no-openmp        Disable openmp (&#x27;~openmp&#x27; WM_COMPILE_CONTROL)

  -no-scheduler     Disable scheduled parallel compilation

  -show-api         Print api value (from Make rules)
  -show-ext-so      Print shared library extension (with &#x27;.&#x27; separator)
  -show-c           Print C compiler value
  -show-cflags      Print C compiler flags
  -show-cxx         Print C++ compiler value
  -show-cxxflags    Print C++ compiler flags
  -show-cflags-arch     The C compiler arch flag (eg, -m64 etc)
  -show-cxxflags-arch   The C++ compiler arch flag (eg, -m64 etc)
  -show-compile-c   Same as &#x27;-show-c -show-cflags&#x27;
  -show-compile-cxx Same as &#x27;-show-cxx -show-cxxflags&#x27;
  -show-path-c      Print path to C compiler
  -show-path-cxx    Print path to C++ compiler
  -show-mpi-compile Print mpi-related flags used when compiling
  -show-mpi-link    Print mpi-related flags used when linking
  -show-openmp-compile  Print openmp flags used when compiling
  -show-openmp-link     Print openmp flags used when compiling

  -build-info       Query/manage status of {api,branch,build} information
  -check-dir        Check directory equality
  -with-bear        Call wmake via &#x27;bear&#x27; to create json output

  -build-info -check-dir -with-bear


General, wrapped make system for multi-platform development.


Makefile targets:   platforms/linux64GccDPInt32Opt/.../fvMesh.o (for example)
Special targets:
  all | queue       Same as -all | -queue options
  exe               Create executable
  lib               Create statically linked archive lib (.a)
  libo              Create statically linked lib (.o)
  libso             Create dynamically linked lib (.so)
  dep               Create lnInclude and dependencies only
  updatedep         Create dependencies only (in case of broken dependencies)
  objects           Compile but not link

Environment
  FOAM_BUILDROOT
  FOAM_EXTRA_CFLAGS FOAM_EXTRA_CXXFLAGS FOAM_EXTRA_LDFLAGS
  FOAM_MODULE_PREFIX


Some special targets (see -help-full for details):
  all | queue       Same as -all | -queue options
  exe               Executable
  lib libo libso    Libraries (.a .o .so)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmake">源码与说明</a> · <a href="/assets/command-help/wmake.txt">帮助文本</a></p>
