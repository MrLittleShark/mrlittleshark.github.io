---
title: "vscode-settings · 输出 OpenFOAM 的 VS Code 工作区设置"
layout: reference
description: "输出 OpenFOAM 的 VS Code 工作区设置。"
cms_slug: "command-vscode-settings"
---

<p>输出 OpenFOAM 的 VS Code 工作区设置。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 生成的是旧版面向 ccls 的 .code-workspace 模板，含关闭 Microsoft C/C++ 补全的设置。先输出新文件阅读，再按自己的语言服务器调整；compileCommands 应指向真实编译数据库文件。</p>
<h2>示例 1：生成工作区模板</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/vscode-settings" &gt; openfoam.code-workspace
</code></pre>
<p>输出包含源码目录和 ccls 缓存位置的 JSON 工作区。</p>
<h2>示例 2：分离诊断信息</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/vscode-settings" &gt; openfoam-review.code-workspace 2&gt; workspace-generation.log
</code></pre>
<p>JSON 写到工作区文件，项目路径诊断写到另一文件。</p>
<h2>示例 3：检查 JSON 格式</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/vscode-settings" &gt; workspace-check.code-workspace
python3 -m json.tool workspace-check.code-workspace
</code></pre>
<p>用 Python 解析后格式化显示，检查生成文件是否完整。</p>
<h2>示例 4：为另一编译配置生成模板</h2>
<pre><code class="language-bash">(source "$WM_PROJECT_DIR/etc/bashrc" WM_LABEL_SIZE=64; "$WM_PROJECT_DIR/bin/tools/vscode-settings") &gt; openfoam-int64.code-workspace
</code></pre>
<p>缓存位置随 WM_OPTIONS 变化，区分不同编译配置。</p>
<h2>示例 5：配合编译数据库使用</h2>
<pre><code class="language-bash">wmake -with-bear -bear-output-dir="$PWD/compile-db" myUtility
"$WM_PROJECT_DIR/bin/tools/vscode-settings" &gt; utility-review.code-workspace
</code></pre>
<p>先生成 compile_commands.json，再把模板中语言服务器的数据库路径改为该真实文件或目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: vscode-settings [OPTIONS]

options:
    -help           Print the usage

Emit some settings for Visual Studio Code + OpenFOAM

For example,
    bin/tools/vscode-settings &gt; openfoam.code-workspace</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/vscode-settings">源码与说明</a> · <a href="/assets/command-help/vscode-settings.txt">帮助文本</a></p>
