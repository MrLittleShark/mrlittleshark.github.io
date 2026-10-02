---
title: "foamUpgradeFiniteArea · 将旧版文件调整为包含 finite-area 子目录的结构"
layout: reference
description: "将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。"
cms_slug: "command-foamupgradefinitearea"
---

<p>将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在个人工作目录中准备 caseA 算例副本。新目标目录使用未占用的名称。 用于旧有限面积文件位置的迁移，目标是新的 finite-area 子目录结构。</p>
<h2>示例 1：先预览迁移</h2>
<pre><code class="language-bash">foamUpgradeFiniteArea -dry-run -case caseA
</code></pre>
<p>只报告移动计划，不改变文件。</p>
<h2>示例 2：迁移一个算例</h2>
<pre><code class="language-bash">foamUpgradeFiniteArea -case caseA
</code></pre>
<p>将识别到的有限面积输入与网格迁移到对应新位置。</p>
<h2>示例 3：显示完整动作</h2>
<pre><code class="language-bash">foamUpgradeFiniteArea -verbose -case caseA
</code></pre>
<p>详细打印迁移信息，便于检查哪些文件发生变化。</p>
<h2>示例 4：保留旧路径链接</h2>
<pre><code class="language-bash">foamUpgradeFiniteArea -link-back -case caseA
</code></pre>
<p>迁移后创建回指新位置的链接，供仍引用旧路径的工作流使用。</p>
<h2>示例 5：在版本库中迁移</h2>
<pre><code class="language-bash">foamUpgradeFiniteArea -git -case caseA
git -C caseA diff --stat
</code></pre>
<p>算例须在 Git 工作树中，-git 使用 git mv，随后查看变更范围。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case=DIR</code></td><td>Specify starting directory, default is cwd</td></tr><tr><td><code>-dry-run | -n</code></td><td>Test without performing actions</td></tr><tr><td><code>-verbose | -v</code></td><td>Additional verbosity</td></tr><tr><td><code>-force</code></td><td>(currently ignored)</td></tr><tr><td><code>-link-back</code></td><td>Link back from new finite-area/ to old locations</td></tr><tr><td><code>-no-mesh</code></td><td>Do not move system/faMeshDefinition</td></tr><tr><td><code>-git</code></td><td>Use &#x27;git mv&#x27; when making changes</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamUpgradeFiniteArea [OPTION]
options:
  -case=DIR         Specify starting directory, default is cwd
  -dry-run | -n     Test without performing actions
  -verbose | -v     Additional verbosity
  -force            (currently ignored)
  -link-back        Link back from new finite-area/ to old locations
  -no-mesh          Do not move system/faMeshDefinition
  -git              Use &#x27;git mv&#x27; when making changes
  -help             Print help and exit

Relocate finite-area files to new sub-directory locations

Equivalent options:
  | -case=DIR  | -case DIR |</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamUpgradeFiniteArea">源码与说明</a> · <a href="/assets/command-help/foamupgradefinitearea.txt">帮助文本</a></p>
