---
title: "foamGrepExeTargets · 列出 Make/files 中的可执行文件目标，便于检查构建结果"
layout: reference
description: "列出 Make/files 中的可执行文件目标，便于检查构建结果。"
cms_slug: "command-foamgrepexetargets"
---

<p>列出 Make/files 中的可执行文件目标，便于检查构建结果。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-bin</td><td>List contents of \$FOAM_APPBIN (no git required)</td></tr><tr><td>-no-git</td><td>Disable use of git for obtaining information</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: foamGrepExeTargets
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamGrepExeTargets

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: foamGrepExeTargets
  -bin          List contents of \$FOAM_APPBIN (no git required)
  -no-git       Disable use of git for obtaining information
  -help         Print the usage

List exe targets (contains EXE). Uses git when possible</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamGrepExeTargets">源码与说明</a> · <a href="/assets/command-help/foamgrepexetargets.txt">帮助文本</a></p>
