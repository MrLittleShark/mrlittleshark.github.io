---
title: "vscode-settings · 输出 OpenFOAM 的 VS Code 工作区设置"
layout: reference
description: "输出 OpenFOAM 的 VS Code 工作区设置。"
cms_slug: "command-vscode-settings"
---

<p>输出 OpenFOAM 的 VS Code 工作区设置。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/vscode-settings&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: vscode-settings [OPTIONS]

options:
    -help           Print the usage

Emit some settings for Visual Studio Code + OpenFOAM

For example,
    bin/tools/vscode-settings &gt; openfoam.code-workspace</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/vscode-settings">源码与说明</a> · <a href="/assets/command-help/vscode-settings.txt">帮助文本</a></p>
