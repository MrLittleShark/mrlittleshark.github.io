---
title: "createMingwRuntime · 将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录"
layout: reference
description: "将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录。"
cms_slug: "command-createmingwruntime"
---

<p>将交叉编译的 MinGW 程序、DLL 和公共文件打包为 Windows 运行目录。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 面向已经在 Linux 上完成 Mingw 交叉编译的 win64 运行环境，需要对应 DLL/EXE 产物与归档工具；不是把 Linux 程序自动转换成 Windows 程序。先 mkdir -p packages。</p>
<h2>示例 1：生成默认运行包</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/createMingwRuntime" -output=packages
</code></pre>
<p>从交叉编译产物打包运行环境，名称按 API 和平台生成。</p>
<h2>示例 2：生成 ZIP 包</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/createMingwRuntime" -zip -output=packages -name=foam-windows
</code></pre>
<p>-zip 选择 ZIP 压缩，-name 指定包名主体。</p>
<h2>示例 3：只分发运行环境</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/createMingwRuntime" -no-tutorials -output=packages -name=foam-runtime
</code></pre>
<p>不包含教程，减少分发尺寸。</p>
<h2>示例 4：设定包内顶层目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/createMingwRuntime" -prefix=OpenFOAM-v2512 -output=packages -name=foam-prefixed
</code></pre>
<p>归档内采用明确的顶层目录，便于解包整理。</p>
<h2>示例 5：生成未压缩归档</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/createMingwRuntime" -no-compress -output=packages -name=foam-uncompressed
</code></pre>
<p>跳过压缩步骤，适合随后由其他打包流程压缩。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-name=NAME</code></td><td>指定归档文件的基本名称，默认自动生成。</td></tr><tr><td><code>-output=DIR</code></td><td>指定输出目录，默认为当前目录。</td></tr><tr><td><code>-prefix=NAME</code></td><td>指定归档内部的顶层目录名，默认自动生成。</td></tr><tr><td><code>-no-tutorials</code></td><td>打包时排除教程。</td></tr><tr><td><code>-no-patch</code></td><td>输出归档名称中省略 _patch 补丁编号。</td></tr><tr><td><code>-no-prefix</code></td><td>打包时省略顶层子目录前缀。</td></tr><tr><td><code>-no-compress</code></td><td>生成未压缩归档。</td></tr><tr><td><code>-compress=TYPE</code></td><td>指定压缩格式。</td></tr><tr><td><code>-sep=SEP</code></td><td>将版本号与补丁号之间的分隔符从下划线改为指定字符。</td></tr><tr><td><code>-with-api=NUM</code></td><td>指定打包使用的 API 版本值。</td></tr><tr><td><code>-with-testbin</code></td><td>同时打包用户应用目录中的 Test-* 程序，适用于开发测试。</td></tr><tr><td><code>-tgz, -xz, -zip</code></td><td>分别等同于 -compress=tgz、-compress=xz、-compress=zip。</td></tr><tr><td><code>-help</code></td><td>显示帮助。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/createMingwRuntime">源码与说明</a> · <a href="/assets/command-help/createmingwruntime.txt">帮助文本</a></p>
