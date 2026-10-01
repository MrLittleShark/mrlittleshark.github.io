---
title: "foamCopySettings  复制算例配置"
layout: reference
description: "采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。</p><h2>v2512 源码中的用途</h2><p>Usage: foamCopySettings srcDir dstDir Copy OpenFOAM settings from one case to another, without copying the mesh or results - requires rsync</p><h2>使用入口</h2><pre><code class="language-bash">foamCopySettings ../baseCase ./</code></pre><h2>使用条件与核对</h2><p>采用 rsync，按 foamCopySettings.rc 定义的规则复制，不包含网格和计算结果。 用法：foamCopySettings 源目录 目标目录 示例：foamCopySettings ../baseCase ./
Usage: foamCopySettings srcDir dstDir Copy OpenFOAM settings from one case to another, without copying the mesh or results - requires rsync
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcopysettings.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCopySettings
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCopySettings

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCopySettings srcDir dstDir

    Copy OpenFOAM settings from one case to another, without copying
    the mesh or results.
    - requires rsync

Note
    The foamCopySettings.rc (found via foamEtcFile) can be used to add any
    custom rsync options.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCopySettings">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
