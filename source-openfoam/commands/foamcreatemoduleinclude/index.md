---
title: "foamCreateModuleInclude · 生成供环境模块系统使用的设置草稿"
layout: reference
description: "生成供环境模块系统使用的设置草稿。"
cms_slug: "command-foamcreatemoduleinclude"
---

<p>生成供环境模块系统使用的设置草稿。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 用于集群 Environment Modules 配置生成，需要能够加载目标安装。输出是模块片段，供完整 modulefile 引用。</p>
<h2>示例 1：生成 Tcl 模块片段</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -output=ModuleInclude.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>默认 Tcl 格式，记录加载该安装所需的环境变化。</p>
<h2>示例 2：生成 shell 设置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -sh -output=ModuleInclude.sh "$WM_PROJECT_DIR"
</code></pre>
<p>-sh 输出 shell 格式，可供脚本检查或加载。</p>
<h2>示例 3：加载指定偏好文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -prefs="$HOME/.OpenFOAM/prefs.sh" -output=ModulePrefs.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>使用已经准备好的偏好文件生成相应编译配置。</p>
<h2>示例 4：保留 ParaView 环境</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -paraview -output=ModuleParaView.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>让片段包含 ParaView 相关路径设置。</p>
<h2>示例 5：指定构建临时目录</h2>
<pre><code class="language-bash">mkdir -p module-tmp
"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -tmpdir="$PWD/module-tmp" -debug -output=ModuleDebug.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>使用独立临时目录，-debug 保留中间文件供比较环境变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-output=file</code></td><td>The output name (default: ModuleInclude.tcl)</td></tr><tr><td><code>-prefs=file</code></td><td>A preferences file (OpenFOAM) to load.</td></tr><tr><td><code>-preload=file</code></td><td>Specify a shell file to preload. Can use multiple times</td></tr><tr><td><code>-tmpdir=file</code></td><td>The tmp directory to use.</td></tr><tr><td><code>-aliases</code></td><td>Output aliases (use with caution)</td></tr><tr><td><code>-paraview</code></td><td>Retain paraview elements</td></tr><tr><td><code>-sh | -tcl</code></td><td>Output flavour (default: -tcl)</td></tr><tr><td><code>-debug</code></td><td>Retain intermediate files for debugging purposes</td></tr><tr><td><code>-reduce=NUM</code></td><td>Environment reduction level (experimental)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: foamCreateModuleInclude
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateModuleInclude

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: foamCreateModuleInclude [OPTION] projectDir
options:
  -output=file      The output name (default: ModuleInclude.tcl)
  -prefs=file       A preferences file (OpenFOAM) to load.
  -preload=file     Specify a shell file to preload. Can use multiple times
  -tmpdir=file      The tmp directory to use.
  -aliases          Output aliases (use with caution)
  -paraview         Retain paraview elements
  -sh | -tcl        Output flavour (default: -tcl)
  -debug            Retain intermediate files for debugging purposes
  -reduce=NUM       Environment reduction level (experimental)
  -help             Print the usage

Create module settings for inclusion in a top-level openfoam module.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateModuleInclude">源码与说明</a> · <a href="/assets/command-help/foamcreatemoduleinclude.txt">帮助文本</a></p>
