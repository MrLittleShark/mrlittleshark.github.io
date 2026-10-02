---
title: "install-dirs · 安装与处理器架构无关的公共目录"
layout: reference
description: "安装与处理器架构无关的公共目录。"
cms_slug: "command-install-dirs"
---

<p>安装与处理器架构无关的公共目录。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 这是非二进制目录的复制安装器。示例先用 -dry-run 预览，prefix 指向个人打包目录，避免覆盖已有安装。</p>
<h2>示例 1：预览标准安装布局</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-dirs" -dry-run -default -prefix="$HOME/foam-package"
</code></pre>
<p>default 选择公共配置、开发源码、文档与教程，输出复制计划。</p>
<h2>示例 2：只准备运行配置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-dirs" -dry-run -common -prefix="$HOME/foam-runtime-package"
</code></pre>
<p>仅选择 bin、etc 和 META-INFO；二进制需由 install-platform 处理。</p>
<h2>示例 3：准备开发资料</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-dirs" -dry-run -devel -prefix="$HOME/foam-devel-package"
</code></pre>
<p>选择 applications、src 与 wmake。</p>
<h2>示例 4：单独分发教程</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-dirs" -dry-run -tut -collate-tut -prefix="$HOME/foam-tutorial-package"
</code></pre>
<p>收录教程并按选项汇集模块教程。</p>
<h2>示例 5：复制到新的打包目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/install-dirs" -common -devel -prefix="$HOME/foam-package-new"
</code></pre>
<p>确认新目录用途后省略 dry-run，实际复制公共和开发文件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-source=SOURCE</code></td><td>Source directory [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]</td></tr><tr><td><code>-platform=PLATFORM</code></td><td>OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]</td></tr><tr><td><code>-foam-mpi=FOAM_MPI</code></td><td>OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]</td></tr><tr><td><code>-prefix=PREFIX</code></td><td>Top-level installation directory in PREFIX [&#x27;&#x27;]</td></tr><tr><td><code>-no-app, -no-apps</code></td><td>do not install (applications)</td></tr><tr><td><code>-no-src</code></td><td>do not install (src)</td></tr><tr><td><code>-no-wmake</code></td><td>do not install (wmake)</td></tr><tr><td><code>-core</code></td><td>Select: -common -devel</td></tr><tr><td><code>-default</code></td><td>Select: -common -devel -doc -tut</td></tr><tr><td><code>-collate</code></td><td>Collate modules (doc, tutorials)</td></tr><tr><td><code>-collate-doc</code></td><td>Collate modules (doc) into doc/modules</td></tr><tr><td><code>-collate-tut</code></td><td>Collate modules (tutorials) into tutorials/modules</td></tr><tr><td><code>-dry-run, -n</code></td><td>Do not perform any operations</td></tr><tr><td><code>-force, -f</code></td><td>Ignored</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: install-dirs [OPTION]

input options:
  -source=SOURCE          Source directory
                          [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]
  -platform=PLATFORM      OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]
  -foam-mpi=FOAM_MPI      OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]

target options:
  -prefix=PREFIX          Top-level installation directory in PREFIX [&#x27;&#x27;]

selections:
  -[no-]common            [do not] install (bin, etc, META-INFO)
  -[no-]devel             [do not] install (applications, src, wmake)
  -[no-]doc               [do not] install (doc)
  -[no-]tut               [do not] install (tutorials)
  -no-app, -no-apps       do not install (applications)
  -no-src                 do not install (src)
  -no-wmake               do not install (wmake)

bundled selections:
  -core                   Select: -common -devel
  -default                Select: -common -devel -doc -tut

tuning options:
  -collate                Collate modules (doc, tutorials)
  -collate-doc            Collate modules (doc) into doc/modules
  -collate-tut            Collate modules (tutorials) into tutorials/modules

general options:
  -dry-run, -n            Do not perform any operations
  -force, -f              Ignored
  -verbose, -v            Additional verbosity
  -help                   Print the help and exit


Simple installer to copy OpenFOAM non-binary directories.

Example,
    install-dirs -prefix=/opt/openfoamVER</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/install-dirs">源码与说明</a> · <a href="/assets/command-help/install-dirs.txt">帮助文本</a></p>
