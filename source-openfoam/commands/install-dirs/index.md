---
title: "install-dirs · 构建或开发辅助脚本"
layout: reference
description: "Simple installer to copy architecture-independent directories."
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Simple installer to copy architecture-independent directories.</p><h2>v2512 源码中的用途</h2><p>Simple installer to copy architecture-independent directories.</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/bin/tools/install-dirs&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
Simple installer to copy architecture-independent directories.
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-collate -collate-doc -collate-tut -core -default -dry-run -foam-mpi -force -help -no-app -no-src -no-wmake -platform -prefix -source -verbose</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/install-dirs.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: install-dirs
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/install-dirs

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: install-dirs [OPTION]

input options:
  -source=SOURCE          Source directory
                          [\&#36;WM_PROJECT_DIR &#36;{WM_PROJECT_DIR:-&#x27;&#x27;}]
  -platform=PLATFORM      OpenFOAM platform name [\&#36;WM_OPTIONS &#36;{WM_OPTIONS:-&#x27;&#x27;}]
  -foam-mpi=FOAM_MPI      OpenFOAM mpi name [\&#36;FOAM_MPI &#36;{FOAM_MPI:-&#x27;&#x27;}]

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
    install-dirs -prefix=/opt/openfoamVER</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/install-dirs">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
