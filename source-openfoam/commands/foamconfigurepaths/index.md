---
title: "foamConfigurePaths · 构建或开发辅助脚本"
layout: reference
description: "Adjust hardcoded installation versions and paths in etc/{bashrc,cshrc} and etc/config.{sh,csh}/ Requires - sed - bin/foamEtcFile"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Adjust hardcoded installation versions and paths in etc/{bashrc,cshrc} and etc/config.{sh,csh}/ Requires - sed - bin/foamEtcFile</p><h2>v2512 源码中的用途</h2><p>Adjust hardcoded installation versions and paths in etc/{bashrc,cshrc} and etc/config.{sh,csh}/ Requires - sed - bin/foamEtcFile</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/bin/tools/foamConfigurePaths&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
Adjust hardcoded installation versions and paths in etc/{bashrc,cshrc} and etc/config.{sh,csh}/ Requires - sed - bin/foamEtcFile
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-adios -adios-brew -adios-path -archOption -boost -boost-path -cgal -cgal-path -clang -cmake -cmake-path -dp -etc -fftw -fftw-path -foamInstall -gcc -gmp-brew -gmp-path -h -hdf5 -hdf5-brew -hdf5-path -help-compat -help-full -int32 -kahip -kahip-path -llvm -llvm-path -mesa -mesa-path -metis -metis-path -mpfr-brew -mpfr-path -mpi -openmpi -paraview -paraview-path -paraview-qt -petsc -petsc-brew -petsc-path -project-path -projectName -readline-path -scotch -scotch-path -sigfpe -sp -spdp -sys-openmpi -system-compiler -third -third-compiler -version -vtk -vtk-path -with-homebrew</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamconfigurepaths.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamConfigurePaths
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamConfigurePaths

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Obsolete options:
  -foamInstall DIR    [obsolete]
  -projectName NAME   [obsolete]
  -sigfpe|-no-sigfpe  [obsolete] now under etc/controlDict
  -archOption 32|64   [obsolete] now edit WM_ARCH_OPTION manually

Equivalent options:
  -version              --projectVersion | -foamVersion
  -archOption           --archOption
  -third                -ThirdParty
  -paraview             --paraviewVersion | -paraviewVersion
  -paraview-path        --paraviewInstall | -paraviewInstall
  -scotch               --scotchVersion | -scotchVersion
  -scotch-path          --scotchArchPath | -scotchArchPath
  -system-compiler      -system
  -third-compiler       -third
  -sys-openmpi          -openmpi-system
  -openmpi              -openmpi-third


usage: &#36;0 options

Options
  -h | -help          Display short help and exit
  -help-compat        Display compatibility options and exit
  -help-full          Display full help and exit

Basic
  -etc=[DIR]          set/unset FOAM_CONFIG_ETC for alternative project files
  -project-path DIR   specify &#x27;WM_PROJECT_DIR&#x27; (eg, /opt/openfoam1806-patch1)
  -version VER        specify project version (eg, v1806)
  -sp | -SP | -float32 single precision (WM_PRECISION_OPTION)
  -dp | -DP | -float64 double precision (WM_PRECISION_OPTION)
  -spdp | -SPDP       mixed precision (WM_PRECISION_OPTION)
  -int32 | -int64     label-size (WM_LABEL_SIZE)

Compiler
  -system-compiler NAME The &#x27;system&#x27; compiler to use (eg, Gcc, Clang, Icc,...)
  -third-compiler NAME  The &#x27;ThirdParty&#x27; compiler to use (eg, Clang40,...)
  -gcc VER            ThirdParty &#x27;default_gcc_version&#x27; (eg, gcc-7.5.0)
  -clang VER          ThirdParty &#x27;default_clang_version&#x27; (eg, llvm-10.0.0)
  gmp-VERSION         For ThirdParty gcc (gmp-system for system library)
  mpfr-VERSION        For ThirdParty gcc (mpfr-system for system library)
  mpc-VERSION         For ThirdParty gcc (mpc-system for system library)

MPI
  -mpi=NAME           Specify &#x27;WM_MPLIB&#x27; type (eg, INTELMPI, etc)
  -openmpi[=VER]      Use ThirdParty openmpi, with version for &#x27;FOAM_MPI&#x27;
  -sys-openmpi[=MAJ]  Use system openmpi, with specified major version

Components versions (ThirdParty)
  -adios VER          specify &#x27;adios2_version&#x27;
  -boost VER          specify &#x27;boost_version&#x27;
  -cgal VER           specify &#x27;cgal_version&#x27;
  -cmake VER          specify &#x27;cmake_version&#x27;
  -fftw VER           specify &#x27;fffw_version&#x27;
  -hdf5 VER           specify &#x27;hdf5_version&#x27;
  -kahip VER          specify &#x27;KAHIP_VERSION&#x27;
  -metis VER          specify &#x27;METIS_VERSION&#x27;
  -petsc VER          specify &#x27;petsc_version&#x27;
  -scotch VER         specify &#x27;SCOTCH_VERSION&#x27; (eg, scotch_6.0.4)

Components specified by absolute path
  -adios-path DIR     Path for &#x27;ADIOS2_ARCH_PATH&#x27; (overrides -adios)
  -boost-path DIR     Path for &#x27;BOOST_ARCH_PATH&#x27;  (overrides -boost)
  -cgal-path DIR      Path for &#x27;CGAL_ARCH_PATH&#x27;   (overrides -cgal)
  -cmake-path DIR     Path for &#x27;CMAKE_ARCH_PATH&#x27;  (overrides -cmake)
  -fftw-path DIR      Path for &#x27;FFTW_ARCH_PATH&#x27;   (overrides -fftw)
  -hdf5-path DIR      Path for &#x27;HDF5_ARCH_PATH&#x27;   (overrides -hdf5)
  -kahip-path DIR     Path for &#x27;KAHIP_ARCH_PATH&#x27;  (overrides -kahip)
  -metis-path DIR     Path for &#x27;METIS_ARCH_PATH&#x27;  (overrides -metis)
  -petsc-path DIR     Path for &#x27;PETSC_ARCH_PATH&#x27;  (overrides -petsc)
  -readline-path      Path for &#x27;READLINE_ARCH_PATH&#x27;
  -scotch-path DIR    Path for &#x27;SCOTCH_ARCH_PATH&#x27; (overrides -scotch)

  -gmp-path DIR       Path for &#x27;GMP_ARCH_PATH&#x27;    (in cgal config)
  -mpfr-path DIR      Path for &#x27;MPFR_ARCH_PATH&#x27;   (in cgal config)

Components specified by homebrew (treat like system locations)
Sets version as system, path from brew --prefix
  -adios-brew, -adios2-brew, -boost-brew, -cgal-brew, -fftw-brew,
  -hdf5-brew, -kahip-brew, -metis-brew, -readline-brew -scotch-brew

  -with-homebrew      Shortcut for selecting all the above

  -gmp-brew           Homebrew for &#x27;GMP_ARCH_PATH&#x27;    (in cgal config)
  -mpfr-brew          Homebrew for &#x27;MPFR_ARCH_PATH&#x27;   (in cgal config)
  -petsc-brew         Homebrew for petsc

Graphics
  -paraview VER       specify &#x27;ParaView_VERSION&#x27; (eg, 5.9.0 or system)
  -paraview-qt VER    specify &#x27;ParaView_QT&#x27; (eg, qt-system)
  -paraview-path DIR  specify &#x27;ParaView_DIR&#x27; (eg, /opt/ParaView-5.9.0)
  -llvm VER           specify &#x27;mesa_llvm&#x27;
  -mesa VER           specify &#x27;mesa_version&#x27; (eg, mesa-13.0.1)
  -vtk  VER           specify &#x27;vtk_version&#x27; (eg, VTK-9.0.0)
  -llvm-path DIR      Path for &#x27;LLVM_ARCH_PATH&#x27;   (overrides -llvm)
  -mesa-path DIR      Path for &#x27;MESA_ARCH_PATH&#x27;   (overrides -mesa)
  -vtk-path DIR       Path for &#x27;VTK_DIR&#x27;          (overrides -vtk)

Adjusts hardcoded versions and installation paths (POSIX and C-shell)
for OpenFOAM.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamConfigurePaths">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
