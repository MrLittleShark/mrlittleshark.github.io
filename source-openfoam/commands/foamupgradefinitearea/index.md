---
title: "foamUpgradeFiniteArea  迁移旧版有限面积文件"
layout: reference
description: "将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。</p><h2>v2512 源码中的用途</h2><p>Relocate finite-area files to new sub-directory locations</p><h2>使用入口</h2><pre><code class="language-bash">foamUpgradeFiniteArea -dry-run -case ./legacyCase</code></pre><h2>使用条件与核对</h2><p>将旧版文件调整为包含 finite-area 子目录的结构。-dry-run 预览迁移内容。 用法：foamUpgradeFiniteArea [选项] 示例：foamUpgradeFiniteArea -dry-run -case ./legacyCase
Relocate finite-area files to new sub-directory locations
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-case -dry-run -force -git -help -link-back -no-mesh -verbose</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamupgradefinitearea.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamUpgradeFiniteArea
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamUpgradeFiniteArea

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamUpgradeFiniteArea [OPTION]
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
  | -case=DIR  | -case DIR |</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamUpgradeFiniteArea">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
