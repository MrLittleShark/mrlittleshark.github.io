---
title: "foamPackRelease · 生成打包 OpenFOAM 源码和子模块的脚本"
layout: reference
description: "生成打包 OpenFOAM 源码和子模块的脚本。"
cms_slug: "command-foampackrelease"
---

<p>生成打包 OpenFOAM 源码和子模块的脚本。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamPackRelease&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-name=NAME</td><td>Stem for tar-file (default: auto)</td></tr><tr><td>-output=DIR</td><td>Output directory (default: &quot;.&quot;)</td></tr><tr><td>-prefix=NAME</td><td>Prefix directory within tar-file (default: auto)</td></tr><tr><td>-pkg-modules</td><td>Package &#x27;modules&#x27; exclusively (no OpenFOAM)</td></tr><tr><td>-pkg-plugins</td><td>Package &#x27;plugins&#x27; exclusively (no OpenFOAM)</td></tr><tr><td>-no-extras</td><td>Exclude &#x27;modules, plugins,...&#x27; from source pack</td></tr><tr><td>-no-modules</td><td>Exclude &#x27;modules&#x27; from source pack (default: off)</td></tr><tr><td>-no-plugins</td><td>Exclude &#x27;plugins&#x27; from source pack (default: on)</td></tr><tr><td>-all-extras</td><td>Include &#x27;modules, plugins,...&#x27; into source pack</td></tr><tr><td>-with-modules</td><td>Include &#x27;modules&#x27; into source pack (default: on)</td></tr><tr><td>-with-plugins</td><td>Include &#x27;plugins&#x27; into source pack (default: off)</td></tr><tr><td>-no-patch</td><td>Ignore &#x27;_patch&#x27; number for output tar-file</td></tr><tr><td>-no-prefix</td><td>Do not prefix subdirectory</td></tr><tr><td>-no-compress</td><td>Disable compression</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamPackRelease [OPTION] commit-ish
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

    foamPackRelease -tgz origin/master | bash</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamPackRelease">源码与说明</a> · <a href="/assets/command-help/foampackrelease.txt">帮助文本</a></p>
