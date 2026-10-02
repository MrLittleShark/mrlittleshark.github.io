---
title: "foamPackRelease · 生成打包 OpenFOAM 源码和子模块的脚本"
layout: reference
description: "生成打包 OpenFOAM 源码和子模块的脚本。"
cms_slug: "command-foampackrelease"
---

<p>生成打包 OpenFOAM 源码和子模块的脚本。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 需要完整 Git 仓库与有效 commit-ish，例如 HEAD。脚本输出的是打包脚本；先保存并阅读，再显式执行。工作区未提交内容不属于指定提交。</p>
<h2>示例 1：生成默认打包脚本</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" HEAD &gt; pack-head.sh
less pack-head.sh
</code></pre>
<p>检查将归档的提交、模块及输出路径。</p>
<h2>示例 2：指定名称和输出目录</h2>
<pre><code class="language-bash">mkdir -p releases
"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -name=foamlab-source -output=releases HEAD &gt; pack-named.sh
</code></pre>
<p>将包名主体和存放位置写入脚本。</p>
<h2>示例 3：只打包核心源码</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -no-extras -name=core-only HEAD &gt; pack-core.sh
</code></pre>
<p>排除 modules/plugins 等附加内容。</p>
<h2>示例 4：选择压缩方式</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -xz -name=source-xz HEAD &gt; pack-xz.sh
</code></pre>
<p>生成采用 xz 的打包脚本。</p>
<h2>示例 5：使用另一份仓库</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -gitbase="$HOME/src/OpenFOAM-v2512" -name=source-copy HEAD &gt; pack-copy.sh
bash pack-copy.sh
</code></pre>
<p>输入目录必须是真实 Git 仓库；审核脚本后执行，生成该提交的源码包。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-name=NAME</code></td><td>Stem for tar-file (default: auto)</td></tr><tr><td><code>-output=DIR</code></td><td>Output directory (default: &quot;.&quot;)</td></tr><tr><td><code>-prefix=NAME</code></td><td>Prefix directory within tar-file (default: auto)</td></tr><tr><td><code>-pkg-modules</code></td><td>Package &#x27;modules&#x27; exclusively (no OpenFOAM)</td></tr><tr><td><code>-pkg-plugins</code></td><td>Package &#x27;plugins&#x27; exclusively (no OpenFOAM)</td></tr><tr><td><code>-no-extras</code></td><td>Exclude &#x27;modules, plugins,...&#x27; from source pack</td></tr><tr><td><code>-no-modules</code></td><td>Exclude &#x27;modules&#x27; from source pack (default: off)</td></tr><tr><td><code>-no-plugins</code></td><td>Exclude &#x27;plugins&#x27; from source pack (default: on)</td></tr><tr><td><code>-all-extras</code></td><td>Include &#x27;modules, plugins,...&#x27; into source pack</td></tr><tr><td><code>-with-modules</code></td><td>Include &#x27;modules&#x27; into source pack (default: on)</td></tr><tr><td><code>-with-plugins</code></td><td>Include &#x27;plugins&#x27; into source pack (default: off)</td></tr><tr><td><code>-no-patch</code></td><td>Ignore &#x27;_patch&#x27; number for output tar-file</td></tr><tr><td><code>-no-prefix</code></td><td>Do not prefix subdirectory</td></tr><tr><td><code>-no-compress</code></td><td>Disable compression</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamPackRelease [OPTION] commit-ish
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
