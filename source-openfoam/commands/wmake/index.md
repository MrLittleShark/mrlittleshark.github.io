---
title: "wmake"
layout: reference
description: "编译应用程序或用户库，读取 Make/files 与 Make/options。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>编译应用程序或用户库，读取 Make/files 与 Make/options。</p><h2>v2512 源码中的用途</h2><p>General, wrapped make system for multi-platform development. Intermediate object and dependency files retain the tree structure of the original source files, with its location depending on the build context. 1. Building within the OpenFOAM project: The tree is located under &#36;WM_PROJECT_DIR/build/&#36;WM_OPTIONS/ 2. Building applications or libraries outside the OpenFOAM project: The tree is located under its local Make/&#36;WM_OPTIONS/ The `wdep` script can be used to locate the dependency file corresponding to a given source file. When `wmake -all` is used, the following rules are applied: 1. If `Allwmake.override` exists, use it. 2. (OR) If `Allwmake` exists, use it. 3. (OR) descend into each sub-directory and repeat.</p><h2>使用入口</h2><pre><code class="language-bash">wmake</code></pre><h2>使用条件与核对</h2><p>编译应用程序或用户库，读取 Make/files 与 Make/options。 示例中的算例名、路径与主机名须按实际环境替换。
General, wrapped make system for multi-platform development. Intermediate object and dependency files retain the tree structure of the original source files, with its location depending on the build context. 1. Building within the OpenFOAM project: The tree is located under &#36;WM_PROJECT_DIR/build/&#36;WM_OPTIONS/ 2. Building applications or libraries outside the OpenFOAM project: The tree is located under its local Make/&#36;WM_OPTIONS/ The `wdep` script can be used to locate the dependency file corresponding to a given source file. When `wmake -all` is used, the following rules are applied: 1. If `Allwmake.override` exists, use it. 2. (OR) If `Allwmake` exists, use it. 3. (OR) descend into each sub-directory and repeat.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-a -all -build-info -build-root -check-dir -debug -debug-O -j -k -module-prefix -no-openfoam -no-openmp -no-scheduler -openmp -q -s -show-api -show-c -show-cflags -show-cflags-arch -show-compile-c -show-compile-cxx -show-cxx -show-cxxflags -show-cxxflags-arch -show-ext-so -show-mpi-compile -show-mpi-link -show-openmp-compile -show-openmp-link -show-path-c -show-path-cxx -strict -update -with-bear</p><p>关联配置：<a href="/dictionaries/make-files/">files</a> · <a href="/dictionaries/make-options/">options</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wmake.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wmake
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmake

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wmake [OPTION] [dir]
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
  lib libo libso    Libraries (.a .o .so)</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmake">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
