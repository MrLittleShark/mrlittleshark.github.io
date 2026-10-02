---
title: "pre-commit-hook · 在 Git 提交前检查源码中的制表符和行宽"
layout: reference
description: "在 Git 提交前检查源码中的制表符和行宽。"
cms_slug: "command-pre-commit-hook"
---

<p>在 Git 提交前检查源码中的制表符和行宽。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 在自己的 Git 练习仓库使用，待检查内容先 git add。手动路径参数决定文件集合，实际检查的源码仍是暂存区版本。</p>
<h2>示例 1：检查待提交变更</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/pre-commit-hook"
</code></pre>
<p>无参数检查此次暂存文件，检测制表符、行长及不合规范的代码模式。</p>
<h2>示例 2：检查一个实现文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/pre-commit-hook" myModel.C
</code></pre>
<p>只选择被 Git 跟踪的 myModel.C，检查其暂存版本。</p>
<h2>示例 3：检查整个模块</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/pre-commit-hook" src/myModel
</code></pre>
<p>按路径筛选已跟踪文件，适合提交一个模块前执行。</p>
<h2>示例 4：一次报告更多问题</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/pre-commit-hook" -all myModel.C myModel.H
</code></pre>
<p>-all 尽量完成多类检查；Git 的基础空白检查仍可能先结束流程。</p>
<h2>示例 5：修正后再次检查</h2>
<pre><code class="language-bash">${EDITOR:-vi} myModel.C
git add myModel.C
"$WM_PROJECT_DIR/bin/tools/pre-commit-hook" myModel.C
</code></pre>
<p>修正并重新暂存后重跑，避免一直检查旧暂存内容。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/pre-commit-hook">源码与说明</a> · <a href="/assets/command-help/pre-commit-hook.txt">帮助文本</a></p>
