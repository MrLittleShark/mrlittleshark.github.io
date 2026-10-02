---
title: "foamUpgradeFiniteArea · 将旧版文件调整为包含 finite-area 子目录的结构"
layout: reference
description: "将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。"
cms_slug: "command-foamupgradefinitearea"
---

<p>将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。</p><h2>用法</h2><pre><code class="language-bash">foamUpgradeFiniteArea -dry-run -case ./legacyCase</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case=DIR</td><td>Specify starting directory, default is cwd</td></tr><tr><td>-dry-run | -n</td><td>Test without performing actions</td></tr><tr><td>-verbose | -v</td><td>Additional verbosity</td></tr><tr><td>-force</td><td>(currently ignored)</td></tr><tr><td>-link-back</td><td>Link back from new finite-area/ to old locations</td></tr><tr><td>-no-mesh</td><td>Do not move system/faMeshDefinition</td></tr><tr><td>-git</td><td>Use &#x27;git mv&#x27; when making changes</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamUpgradeFiniteArea [OPTION]
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
