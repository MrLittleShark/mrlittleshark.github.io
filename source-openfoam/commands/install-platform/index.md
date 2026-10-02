---
title: "install-platform · 安装已编译的 bin 和 lib 平台目录"
layout: reference
description: "安装已编译的 bin 和 lib 平台目录。"
cms_slug: "command-install-platform"
---

<p>安装已编译的 bin 和 lib 平台目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/install-platform&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-source=SOURCE</td><td>Source directory [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]</td></tr><tr><td>-platform=PLATFORM</td><td>OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]</td></tr><tr><td>-foam-mpi=FOAM_MPI</td><td>OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]</td></tr><tr><td>-prefix=PREFIX</td><td>Top-level installation directory in PREFIX [&#x27;&#x27;]</td></tr><tr><td>-exec-prefix=EPREFIX</td><td>Architecture-dependent in EPREFIX [PREFIX/platforms/PLATFORM]</td></tr><tr><td>-bindir=DIR</td><td>bin directory [EPREFIX/bin]</td></tr><tr><td>-libdir=DIR</td><td>lib directory [EPREFIX/lib]</td></tr><tr><td>-mpi-libdir=DIR</td><td>mpi libdir [&lt;libdir&gt;/FOAM_MPI]</td></tr><tr><td>-no-bin</td><td>Do not install bin directory</td></tr><tr><td>-no-lib</td><td>Do not install lib directory</td></tr><tr><td>-no-mpi</td><td>Do not install mpi lib directory</td></tr><tr><td>-mpi-only</td><td>Only install mpi lib directory</td></tr><tr><td>-mpi-mkdir</td><td>Create foam-mpi directory within libdir</td></tr><tr><td>-dry-run, -n</td><td>Do not perform any operations</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: install-platform [OPTION]

input options:
  -source=SOURCE          Source directory
                          [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]
  -platform=PLATFORM      OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]
  -foam-mpi=FOAM_MPI      OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]

target options:
  -prefix=PREFIX          Top-level installation directory in PREFIX [&#x27;&#x27;]
  -exec-prefix=EPREFIX    Architecture-dependent in EPREFIX
                          [PREFIX/platforms/PLATFORM]
  -bindir=DIR             bin directory [EPREFIX/bin]
  -libdir=DIR             lib directory [EPREFIX/lib]
  -mpi-libdir=DIR         mpi libdir [&lt;libdir&gt;/FOAM_MPI]

tuning options:
  -no-bin                 Do not install bin directory
  -no-lib                 Do not install lib directory
  -no-mpi                 Do not install mpi lib directory
  -mpi-only               Only install mpi lib directory
  -mpi-mkdir              Create foam-mpi directory within libdir

general options:
  -dry-run, -n            Do not perform any operations
  -force, -f              Ignored
  -verbose, -v            Additional verbosity
  -help                   Print the help and exit


Simple installer to copy OpenFOAM binary bin/, lib/ (platforms) directories.

Example,
    install-platform -prefix=/opt/openfoamVER</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/install-platform">源码与说明</a> · <a href="/assets/command-help/install-platform.txt">帮助文本</a></p>
