---
title: "install-dirs · 安装与处理器架构无关的公共目录"
layout: reference
description: "安装与处理器架构无关的公共目录。"
cms_slug: "command-install-dirs"
---

<p>安装与处理器架构无关的公共目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/install-dirs&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-source=SOURCE</td><td>Source directory [\$WM_PROJECT_DIR ${WM_PROJECT_DIR:-&#x27;&#x27;}]</td></tr><tr><td>-platform=PLATFORM</td><td>OpenFOAM platform name [\$WM_OPTIONS ${WM_OPTIONS:-&#x27;&#x27;}]</td></tr><tr><td>-foam-mpi=FOAM_MPI</td><td>OpenFOAM mpi name [\$FOAM_MPI ${FOAM_MPI:-&#x27;&#x27;}]</td></tr><tr><td>-prefix=PREFIX</td><td>Top-level installation directory in PREFIX [&#x27;&#x27;]</td></tr><tr><td>-no-app, -no-apps</td><td>do not install (applications)</td></tr><tr><td>-no-src</td><td>do not install (src)</td></tr><tr><td>-no-wmake</td><td>do not install (wmake)</td></tr><tr><td>-core</td><td>Select: -common -devel</td></tr><tr><td>-default</td><td>Select: -common -devel -doc -tut</td></tr><tr><td>-collate</td><td>Collate modules (doc, tutorials)</td></tr><tr><td>-collate-doc</td><td>Collate modules (doc) into doc/modules</td></tr><tr><td>-collate-tut</td><td>Collate modules (tutorials) into tutorials/modules</td></tr><tr><td>-dry-run, -n</td><td>Do not perform any operations</td></tr><tr><td>-force, -f</td><td>Ignored</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: install-dirs [OPTION]

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
