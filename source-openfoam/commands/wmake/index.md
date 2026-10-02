---
title: "wmake · 读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库"
layout: reference
description: "读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。"
cms_slug: "command-wmake"
---

<p>读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。</p><h2>编译应用程序</h2>
<pre><code class="language-bash">wmake
</code></pre>
<p>在含 <code>Make</code> 目录的源码目录执行。<code>Make/files</code> 的 <code>EXE</code> 决定程序输出位置，<code>Make/options</code> 提供头文件路径和链接库。</p>
<h2>编译共享库</h2>
<pre><code class="language-bash">wmake libso
</code></pre>
<p><code>Make/files</code> 使用 <code>LIB</code> 指定目标，<code>Make/options</code> 使用 <code>LIB_LIBS</code> 指定依赖。计算时通过 <code>controlDict/libs</code> 或程序链接加载生成的库。</p>
<h2>并行编译</h2>
<pre><code class="language-bash">wmake -j 4
</code></pre>
<p>最多并行执行 4 个编译任务。源码修改后再次执行 wmake，会根据依赖重新编译受影响的文件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-s | -silent</td><td>Silent mode (do not echo commands)</td></tr><tr><td>-a | -all</td><td>wmake all sub-directories, runs Allwmake if present</td></tr><tr><td>-q | -queue</td><td>Collect as single Makefile, runs Allwmake if present</td></tr><tr><td>-k | -keep-going</td><td>Keep going even when errors occur (-non-stop)</td></tr><tr><td>-j | -jN | -j N</td><td>Compile using all or specified N cores/hyperthreads</td></tr><tr><td>-update</td><td>Update lnInclude, dep files, remove deprecated files/dirs</td></tr><tr><td>-all=FILE</td><td>Runs specified file (in pwd) instead of Allwmake</td></tr><tr><td>-debug</td><td>Add &#x27;-g -DFULLDEBUG&#x27; flags</td></tr><tr><td>-debug-O[g0123]</td><td>Add &#x27;-g -DFULLDEBUG&#x27; flags and optimization level</td></tr><tr><td>-strict</td><td>More deprecation warnings (&#x27;+strict&#x27; WM_COMPILE_CONTROL)</td></tr><tr><td>-build-root=PATH</td><td>Specify FOAM_BUILDROOT for compilation intermediates</td></tr><tr><td>-module-prefix=PATH</td><td>Specify FOAM_MODULE_PREFIX as absolute/relative path</td></tr><tr><td>-module-prefix=TYPE</td><td>Specify FOAM_MODULE_PREFIX as predefined type (u,user | g,group | o,openfoam)</td></tr><tr><td>-no-openfoam</td><td>Disable OpenFOAM linking (&#x27;~openfoam&#x27; WM_COMPILE_CONTROL)</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/make-files/">files</a> · <a href="/dictionaries/make-options/">options</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wmake [OPTION] [dir]
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
