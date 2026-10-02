---
title: "foamConfigurePaths · 修改环境配置中的安装版本和硬编码路径"
layout: reference
description: "修改环境配置中的安装版本和硬编码路径。"
cms_slug: "command-foamconfigurepaths"
---

<p>修改环境配置中的安装版本和硬编码路径。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 此工具会改写 etc 配置文件。先复制配置到独立目录：configCopy=$(mktemp -d "$HOME/foam-etc.XXXXXX"); cp -a "$WM_PROJECT_DIR/etc/." "$configCopy/"。以下都用 -etc 指向副本。</p>
<h2>示例 1：选择双精度</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamConfigurePaths" -etc="$configCopy" -dp
</code></pre>
<p>修改副本 bashrc/cshrc 的默认浮点精度。</p>
<h2>示例 2：设置索引位宽</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamConfigurePaths" -etc="$configCopy" -int64
</code></pre>
<p>把默认 WM_LABEL_SIZE 改为 64，用于后续匹配构建。</p>
<h2>示例 3：采用系统 GCC</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamConfigurePaths" -etc="$configCopy" -system-compiler Gcc
</code></pre>
<p>同时设置编译器种类和来源为系统编译器。</p>
<h2>示例 4：选择系统 OpenMPI</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamConfigurePaths" -etc="$configCopy" -sys-openmpi
</code></pre>
<p>改写默认 WM_MPLIB；MPI 本身仍需安装。</p>
<h2>示例 5：指定 ParaView 位置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamConfigurePaths" -etc="$configCopy" -paraview-path /opt/ParaView
</code></pre>
<p>替换为真实可用安装路径，改变副本中的 ParaView_DIR 配置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-foamInstall DIR</code></td><td>已废弃的兼容选项。</td></tr><tr><td><code>-projectName NAME</code></td><td>已废弃的兼容选项。</td></tr><tr><td><code>-sigfpe|-no-sigfpe</code></td><td>此选项已废弃；改在 etc/controlDict 中设置。</td></tr><tr><td><code>-archOption 32|64</code></td><td>此选项已废弃；直接修改 WM_ARCH_OPTION。</td></tr><tr><td><code>-h | -help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr><tr><td><code>-etc=[DIR]</code></td><td>设置或清除 FOAM_CONFIG_ETC，以切换项目配置文件目录。</td></tr><tr><td><code>-project-path DIR</code></td><td>指定 WM_PROJECT_DIR，即 OpenFOAM 安装根目录。</td></tr><tr><td><code>-version VER</code></td><td>指定 OpenFOAM 版本。</td></tr><tr><td><code>-spdp | -SPDP</code></td><td>设置混合精度选项 WM_PRECISION_OPTION。</td></tr><tr><td><code>-int32 | -int64</code></td><td>设置整数编号位数 WM_LABEL_SIZE。</td></tr><tr><td><code>-third-compiler NAME</code></td><td>指定 ThirdParty 编译器，例如 Clang40。</td></tr><tr><td><code>-gcc VER</code></td><td>指定 ThirdParty 的 default_gcc_version。</td></tr><tr><td><code>-clang VER</code></td><td>指定 ThirdParty 的 default_clang_version。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（40 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-mpi=NAME</code></td><td>指定 WM_MPLIB 类型，例如 INTELMPI。</td></tr><tr><td><code>-openmpi[=VER]</code></td><td>使用 ThirdParty 的 OpenMPI，并按指定版本设置 FOAM_MPI。</td></tr><tr><td><code>-sys-openmpi[=MAJ]</code></td><td>使用系统 OpenMPI，可指定主版本号。</td></tr><tr><td><code>-adios VER</code></td><td>指定 adios2_version。</td></tr><tr><td><code>-boost VER</code></td><td>指定 boost_version。</td></tr><tr><td><code>-cgal VER</code></td><td>指定 cgal_version。</td></tr><tr><td><code>-cmake VER</code></td><td>指定 cmake_version。</td></tr><tr><td><code>-fftw VER</code></td><td>指定 FFTW 版本。</td></tr><tr><td><code>-hdf5 VER</code></td><td>指定 hdf5_version。</td></tr><tr><td><code>-kahip VER</code></td><td>指定 KAHIP_VERSION。</td></tr><tr><td><code>-metis VER</code></td><td>指定 METIS_VERSION。</td></tr><tr><td><code>-petsc VER</code></td><td>指定 petsc_version。</td></tr><tr><td><code>-scotch VER</code></td><td>指定 SCOTCH_VERSION。</td></tr><tr><td><code>-adios-path DIR</code></td><td>设置 ADIOS2_ARCH_PATH，优先于 -adios。</td></tr><tr><td><code>-boost-path DIR</code></td><td>设置 BOOST_ARCH_PATH，优先于 -boost。</td></tr><tr><td><code>-cgal-path DIR</code></td><td>设置 CGAL_ARCH_PATH，优先于 -cgal。</td></tr><tr><td><code>-cmake-path DIR</code></td><td>设置 CMAKE_ARCH_PATH，优先于 -cmake。</td></tr><tr><td><code>-fftw-path DIR</code></td><td>设置 FFTW_ARCH_PATH，优先于 -fftw。</td></tr><tr><td><code>-hdf5-path DIR</code></td><td>设置 HDF5_ARCH_PATH，优先于 -hdf5。</td></tr><tr><td><code>-kahip-path DIR</code></td><td>设置 KAHIP_ARCH_PATH，优先于 -kahip。</td></tr><tr><td><code>-metis-path DIR</code></td><td>设置 METIS_ARCH_PATH，优先于 -metis。</td></tr><tr><td><code>-petsc-path DIR</code></td><td>设置 PETSC_ARCH_PATH，优先于 -petsc。</td></tr><tr><td><code>-readline-path</code></td><td>设置 READLINE_ARCH_PATH。</td></tr><tr><td><code>-scotch-path DIR</code></td><td>设置 SCOTCH_ARCH_PATH，优先于 -scotch。</td></tr><tr><td><code>-gmp-path DIR</code></td><td>设置 CGAL 配置中的 GMP_ARCH_PATH。</td></tr><tr><td><code>-mpfr-path DIR</code></td><td>设置 CGAL 配置中的 MPFR_ARCH_PATH。</td></tr><tr><td><code>-with-homebrew</code></td><td>一次启用前面列出的全部 Homebrew 选项。</td></tr><tr><td><code>-gmp-brew</code></td><td>在 CGAL 配置中使用 Homebrew 提供的 GMP。</td></tr><tr><td><code>-mpfr-brew</code></td><td>在 CGAL 配置中使用 Homebrew 提供的 MPFR。</td></tr><tr><td><code>-petsc-brew</code></td><td>使用 Homebrew 提供的 PETSc。</td></tr><tr><td><code>-paraview VER</code></td><td>指定 ParaView_VERSION；可填具体版本或 system。</td></tr><tr><td><code>-paraview-qt VER</code></td><td>指定 ParaView_QT，例如 qt-system。</td></tr><tr><td><code>-paraview-path DIR</code></td><td>指定 ParaView_DIR 安装目录。</td></tr><tr><td><code>-llvm VER</code></td><td>指定 mesa_llvm。</td></tr><tr><td><code>-mesa VER</code></td><td>指定 mesa_version。</td></tr><tr><td><code>-vtk VER</code></td><td>指定 vtk_version。</td></tr><tr><td><code>-llvm-path DIR</code></td><td>设置 LLVM_ARCH_PATH，优先于 -llvm。</td></tr><tr><td><code>-mesa-path DIR</code></td><td>设置 MESA_ARCH_PATH，优先于 -mesa。</td></tr><tr><td><code>-vtk-path DIR</code></td><td>设置 VTK_DIR，优先于 -vtk。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamConfigurePaths">源码与说明</a> · <a href="/assets/command-help/foamconfigurepaths.txt">帮助文本</a></p>
