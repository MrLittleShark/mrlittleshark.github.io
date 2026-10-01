---
title: "foamNewCase  按应用模板创建算例"
layout: reference
description: "模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。</p><h2>v2512 源码中的用途</h2><p>Create a new case from a template for particular applications - requires rsync</p><h2>使用入口</h2><pre><code class="language-bash">foamNewCase -list</code></pre><h2>使用条件与核对</h2><p>模板来自用户或站点配置。-list 列出可用模板；创建命令为 foamNewCase -app simpleFoam -case newCase。 用法：foamNewCase [-app 应用] [-case 目录] 示例：foamNewCase -list
Create a new case from a template for particular applications - requires rsync
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-app -case -help -list -version -with-api</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamnewcase.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamNewCase
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewCase

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamNewCase [OPTION]
options:
  -app NAME         specify the application to use
  -case DIR         specify alternative case directory, default is the cwd
  -list             list the applications available
  -with-api=NUM     specify alternative api to use (default: \&#36;FOAM_API)
  -version VER      [obsolete]
  -help             Print the usage

clone initial application settings to the specified case from
    &#36;userDir/&#36;templateDir/{&#36;projectApi,}/APP
    &#36;groupDir/&#36;templateDir/{&#36;projectApi,}/APP</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewCase">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
