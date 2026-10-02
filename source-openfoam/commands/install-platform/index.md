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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-source=SOURCE</code></td><td>指定源码目录，默认使用 $WM_PROJECT_DIR。</td></tr><tr><td><code>-platform=PLATFORM</code></td><td>指定 OpenFOAM 构建平台名称，默认使用 $WM_OPTIONS。</td></tr><tr><td><code>-foam-mpi=FOAM_MPI</code></td><td>指定 OpenFOAM MPI 名称，默认使用 $FOAM_MPI。</td></tr><tr><td><code>-prefix=PREFIX</code></td><td>指定顶层安装前缀，默认为空。</td></tr><tr><td><code>-exec-prefix=EPREFIX</code></td><td>指定与架构相关的安装目录，默认为 PREFIX/platforms/PLATFORM。</td></tr><tr><td><code>-bindir=DIR</code></td><td>指定可执行文件目录，默认为 EPREFIX/bin。</td></tr><tr><td><code>-libdir=DIR</code></td><td>指定库目录，默认为 EPREFIX/lib。</td></tr><tr><td><code>-mpi-libdir=DIR</code></td><td>指定 MPI 库目录，默认为库目录下的 FOAM_MPI 子目录。</td></tr><tr><td><code>-no-bin</code></td><td>安装时排除 bin 目录。</td></tr><tr><td><code>-no-lib</code></td><td>安装时排除 lib 目录。</td></tr><tr><td><code>-no-mpi</code></td><td>安装时排除 MPI 库目录。</td></tr><tr><td><code>-mpi-only</code></td><td>仅安装 MPI 库目录。</td></tr><tr><td><code>-mpi-mkdir</code></td><td>在库目录中创建 foam-mpi 子目录。</td></tr><tr><td><code>-dry-run, -n</code></td><td>仅预览操作。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（3 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-force, -f</code></td><td>为兼容性保留的选项，当前会被忽略。</td></tr><tr><td><code>-verbose, -v</code></td><td>显示更详细的输出。</td></tr><tr><td><code>-help</code></td><td>显示帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/install-platform">源码与说明</a> · <a href="/assets/command-help/install-platform.txt">帮助文本</a></p>
