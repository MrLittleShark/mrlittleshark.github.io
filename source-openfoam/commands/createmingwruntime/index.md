---
title: "createMingwRuntime · 将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录"
layout: reference
description: "将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录。"
cms_slug: "command-createmingwruntime"
---

<p>将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/createMingwRuntime&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-name=NAME</td><td>Stem for tar-file (default: auto)</td></tr><tr><td>-output=DIR</td><td>Output directory (default: &quot;.&quot;)</td></tr><tr><td>-prefix=NAME</td><td>Prefix directory within tar-file (default: auto)</td></tr><tr><td>-no-tutorials</td><td>Exclude tutorials</td></tr><tr><td>-no-patch</td><td>Ignore &#x27;_patch&#x27; number for output tar-file</td></tr><tr><td>-no-prefix</td><td>Do not prefix subdirectory</td></tr><tr><td>-no-compress</td><td>Disable compression</td></tr><tr><td>-compress=TYPE</td><td>Use specified compression type</td></tr><tr><td>-sep=SEP</td><td>Change version/patch separator from &#x27;_&#x27; to SEP</td></tr><tr><td>-with-api=NUM</td><td>Specify alternative api value for packaging</td></tr><tr><td>-with-testbin</td><td>Include any Test-* files from user appbin (expert option)</td></tr><tr><td>-tgz, -xz, -zip</td><td>Alias for -compress=tgz, -compress=xz, -compress=zip</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: createMingwRuntime
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/createMingwRuntime

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: createMingwRuntime [OPTION]
options:
  -name=NAME        Stem for tar-file (default: auto)
  -output=DIR       Output directory (default: &quot;.&quot;)
  -prefix=NAME      Prefix directory within tar-file (default: auto)
  -no-tutorials     Exclude tutorials
  -no-patch         Ignore &#x27;_patch&#x27; number for output tar-file
  -no-prefix        Do not prefix subdirectory
  -no-compress      Disable compression
  -compress=TYPE    Use specified compression type
  -sep=SEP          Change version/patch separator from &#x27;_&#x27; to SEP
  -with-api=NUM     Specify alternative api value for packaging
  -with-testbin     Include any Test-* files from user appbin (expert option)
  -tgz, -xz, -zip   Alias for -compress=tgz, -compress=xz, -compress=zip
  -help             Print help

Pack OpenFOAM cross-compiled linux64Mingw -&gt; win64Mingw (run-time)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/createMingwRuntime">源码与说明</a> · <a href="/assets/command-help/createmingwruntime.txt">帮助文本</a></p>
