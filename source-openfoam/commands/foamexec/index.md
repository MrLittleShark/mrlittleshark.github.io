---
title: "foamExec · 使用安装目录中提供的环境包装脚本运行应用"
layout: reference
description: "使用安装目录中提供的环境包装脚本运行应用。"
cms_slug: "command-foamexec"
---

<p>使用安装目录中提供的环境包装脚本运行应用。</p><h2>用法</h2><pre><code class="language-bash">&quot;$WM_PROJECT_DIR/bin/tools/foamExec&quot; icoFoam -help</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamExec [OPTION] &lt;application&gt; ...

options:
  -help             Print the usage

Run an application (with arguments) after first sourcing
the OpenFOAM etc/bashrc file from the project directory:
($projectDir)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">源码与说明</a> · <a href="/assets/command-help/foamexec.txt">帮助文本</a></p>
