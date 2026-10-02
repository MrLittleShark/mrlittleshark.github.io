---
title: "foamConfigurePaths · 修改环境配置中的安装版本和硬编码路径"
layout: reference
description: "修改环境配置中的安装版本和硬编码路径。"
cms_slug: "command-foamconfigurepaths"
---

<p>修改环境配置中的安装版本和硬编码路径。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamConfigurePaths&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-foamInstall DIR</td><td>[obsolete]</td></tr><tr><td>-projectName NAME</td><td>[obsolete]</td></tr><tr><td>-sigfpe|-no-sigfpe</td><td>[obsolete] now under etc/controlDict</td></tr><tr><td>-archOption 32|64</td><td>[obsolete] now edit WM_ARCH_OPTION manually</td></tr><tr><td>-version</td><td>--projectVersion | -foamVersion</td></tr><tr><td>-archOption</td><td>--archOption</td></tr><tr><td>-third</td><td>-ThirdParty</td></tr><tr><td>-paraview</td><td>--paraviewVersion | -paraviewVersion</td></tr><tr><td>-paraview-path</td><td>--paraviewInstall | -paraviewInstall</td></tr><tr><td>-scotch</td><td>--scotchVersion | -scotchVersion</td></tr><tr><td>-scotch-path</td><td>--scotchArchPath | -scotchArchPath</td></tr><tr><td>-system-compiler</td><td>-system</td></tr><tr><td>-third-compiler</td><td>-third</td></tr><tr><td>-sys-openmpi</td><td>-openmpi-system</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
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


usage: $0 options

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
for OpenFOAM.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamConfigurePaths">源码与说明</a> · <a href="/assets/command-help/foamconfigurepaths.txt">帮助文本</a></p>
