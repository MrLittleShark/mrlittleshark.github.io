---
title: "foamCreateModuleInclude · 生成供环境模块系统使用的设置草稿"
layout: reference
description: "生成供环境模块系统使用的设置草稿。"
cms_slug: "command-foamcreatemoduleinclude"
---

<p>生成供环境模块系统使用的设置草稿。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-output=file</td><td>The output name (default: ModuleInclude.tcl)</td></tr><tr><td>-prefs=file</td><td>A preferences file (OpenFOAM) to load.</td></tr><tr><td>-preload=file</td><td>Specify a shell file to preload. Can use multiple times</td></tr><tr><td>-tmpdir=file</td><td>The tmp directory to use.</td></tr><tr><td>-aliases</td><td>Output aliases (use with caution)</td></tr><tr><td>-paraview</td><td>Retain paraview elements</td></tr><tr><td>-sh | -tcl</td><td>Output flavour (default: -tcl)</td></tr><tr><td>-debug</td><td>Retain intermediate files for debugging purposes</td></tr><tr><td>-reduce=NUM</td><td>Environment reduction level (experimental)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
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
