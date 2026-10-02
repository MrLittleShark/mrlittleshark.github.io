---
title: "install-platform · 安装已编译的 bin 和 lib 平台目录"
layout: reference
description: "安装已编译的 bin 和 lib 平台目录。"
cms_slug: "command-install-platform"
---

<p>安装已编译的 bin 和 lib 平台目录。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 源安装需已有对应平台二进制；prefix 仅使用新建的个人打包目标，先检查 dry-run 输出。</p>
<h2>示例 1：预览当前平台安装</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-platform" -dry-run -prefix="$HOME/foam-binary-package"
</code></pre>
<p>使用 WM_OPTIONS，计划复制 bin、lib 和 MPI 相关库。</p>
<h2>示例 2：只复制应用</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-platform" -dry-run -no-lib -no-mpi -prefix="$HOME/foam-app-package"
</code></pre>
<p>排除普通和 MPI 库目录，预览应用部分。</p>
<h2>示例 3：只复制库</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-platform" -dry-run -no-bin -prefix="$HOME/foam-lib-package"
</code></pre>
<p>应用程序不复制，保留库安装步骤。</p>
<h2>示例 4：只更新 MPI 库目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-platform" -dry-run -mpi-only -prefix="$HOME/foam-mpi-package"
</code></pre>
<p>限定于当前 FOAM_MPI 对应的并行库。</p>
<h2>示例 5：设置独立二进制布局</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-platform" -dry-run -bindir="$HOME/package/bin" -libdir="$HOME/package/lib" -mpi-libdir="$HOME/package/lib/mpi"
</code></pre>
<p>分别指定三类目标目录，便于制作其他布局的发行包。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-source=SOURCE</code></td><td>Source directory [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]</td></tr><tr><td><code>-platform=PLATFORM</code></td><td>OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]</td></tr><tr><td><code>-foam-mpi=FOAM_MPI</code></td><td>OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]</td></tr><tr><td><code>-prefix=PREFIX</code></td><td>Top-level installation directory in PREFIX [&#x27;&#x27;]</td></tr><tr><td><code>-exec-prefix=EPREFIX</code></td><td>Architecture-dependent in EPREFIX [PREFIX/platforms/PLATFORM]</td></tr><tr><td><code>-bindir=DIR</code></td><td>bin directory [EPREFIX/bin]</td></tr><tr><td><code>-libdir=DIR</code></td><td>lib directory [EPREFIX/lib]</td></tr><tr><td><code>-mpi-libdir=DIR</code></td><td>mpi libdir [&lt;libdir&gt;/FOAM_MPI]</td></tr><tr><td><code>-no-bin</code></td><td>Do not install bin directory</td></tr><tr><td><code>-no-lib</code></td><td>Do not install lib directory</td></tr><tr><td><code>-no-mpi</code></td><td>Do not install mpi lib directory</td></tr><tr><td><code>-mpi-only</code></td><td>Only install mpi lib directory</td></tr><tr><td><code>-mpi-mkdir</code></td><td>Create foam-mpi directory within libdir</td></tr><tr><td><code>-dry-run, -n</code></td><td>Do not perform any operations</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: install-platform [OPTION]

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
