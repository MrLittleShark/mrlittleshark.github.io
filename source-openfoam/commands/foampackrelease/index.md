---
title: "foamPackRelease · 构建或开发辅助脚本"
layout: reference
description: "Script generator for packing OpenFOAM sources and submodules. The generated script can be further edited as required, or used directly. Examples Direct call foamPackRelease -tgz origin/master | bash Modules-only packaging with different api"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Script generator for packing OpenFOAM sources and submodules. The generated script can be further edited as required, or used directly. Examples Direct call foamPackRelease -tgz origin/master | bash Modules-only packaging with different api foamPackRelease -with-api=1912 -pkg-modules origin/develop Debian-style, without OpenFOAM sub-directory foamPackRelease -debian origin/develop == -debian=openfoam_{version} == -name=openfoam_{api}.{patch} -no-prefix</p><h2>v2512 源码中的用途</h2><p>Script generator for packing OpenFOAM sources and submodules. The generated script can be further edited as required, or used directly. Examples Direct call foamPackRelease -tgz origin/master | bash Modules-only packaging with different api foamPackRelease -with-api=1912 -pkg-modules origin/develop Debian-style, without OpenFOAM sub-directory foamPackRelease -debian origin/develop == -debian=openfoam_{version} == -name=openfoam_{api}.{patch} -no-prefix</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/bin/tools/foamPackRelease&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
Script generator for packing OpenFOAM sources and submodules. The generated script can be further edited as required, or used directly. Examples Direct call foamPackRelease -tgz origin/master | bash Modules-only packaging with different api foamPackRelease -with-api=1912 -pkg-modules origin/develop Debian-style, without OpenFOAM sub-directory foamPackRelease -debian origin/develop == -debian=openfoam_{version} == -name=openfoam_{api}.{patch} -no-prefix
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-all-extras -compress -debian -gitbase -help -modules -name -no-compress -no-extras -no-modules -no-patch -no-plugins -no-prefix -output -pkg-modules -pkg-plugins -plugins -prefix -sep -tgz -with-api -with-modules -with-plugins</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foampackrelease.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamPackRelease
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamPackRelease

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamPackRelease [OPTION] commit-ish
options:
  -name=NAME        Stem for tar-file (default: auto)
  -output=DIR       Output directory (default: &quot;.&quot;)
  -prefix=NAME      Prefix directory within tar-file (default: auto)
  -pkg-modules      Package &#x27;modules&#x27; exclusively (no OpenFOAM)
  -pkg-plugins      Package &#x27;plugins&#x27; exclusively (no OpenFOAM)
  -no-extras        Exclude &#x27;modules, plugins,...&#x27; from source pack
  -no-modules       Exclude &#x27;modules&#x27; from source pack (default: off)
  -no-plugins       Exclude &#x27;plugins&#x27; from source pack (default: on)
  -all-extras       Include &#x27;modules, plugins,...&#x27; into source pack
  -with-modules     Include &#x27;modules&#x27; into source pack (default: on)
  -with-plugins     Include &#x27;plugins&#x27; into source pack (default: off)
  -modules=name1,.. Include specifed &#x27;modules&#x27; into source pack
  -plugins=name1,.. Include specifed &#x27;plugins&#x27; into source pack
  -no-patch         Ignore &#x27;_patch&#x27; number for output tar-file
  -no-prefix        Do not prefix subdirectory
  -no-compress      Disable compression
  -compress=TYPE    Use specified compression type
  -sep=SEP          Change version/patch separator from &#x27;_&#x27; to SEP
  -gitbase=DIR      Alternative repository location
  -with-api=NUM     Specify alternative api value for packaging
  -tgz, -xz, -zstd  Alias for -compress=tgz, -compress=xz, -compress=zstd
  -debian           Auto (debian) naming with -no-prefix, -xz
  -debian=NUM       Auto (debian) naming with specified debian patch value
  -debian=NAME      Short-cut for -name=NAME.orig, -no-prefix, -xz
  -help             Print help

Script generator for packing OpenFOAM sources and submodules.
Eg,

    foamPackRelease -output=some-dir origin/master &gt; create-tar-file
    bash ./create-tar-file

    foamPackRelease -tgz origin/master | bash</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamPackRelease">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
