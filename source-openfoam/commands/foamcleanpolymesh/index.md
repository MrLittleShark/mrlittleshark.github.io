---
title: "foamCleanPolyMesh  清理体网格文件"
layout: reference
description: "-dry-run 预览清理范围，移除该选项后执行删除。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-dry-run 预览清理范围，移除该选项后执行删除。</p><h2>v2512 源码中的用途</h2><p>Remove the contents of the constant/polyMesh directory as per the Foam::polyMesh::removeFiles() method.</p><h2>使用入口</h2><pre><code class="language-bash">foamCleanPolyMesh -dry-run</code></pre><h2>使用条件与核对</h2><p>-dry-run 预览清理范围，移除该选项后执行删除。 用法：foamCleanPolyMesh [-case 目录] [-dry-run] 示例：foamCleanPolyMesh -dry-run
Remove the contents of the constant/polyMesh directory as per the Foam::polyMesh::removeFiles() method.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-allRegions -case -dry-run -help -region</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcleanpolymesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCleanPolyMesh
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPolyMesh

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCleanPolyMesh [OPTION]
options:
  -case &lt;dir&gt;           case directory, default is the cwd
  -allRegions           all mesh regions
  -region &lt;name&gt;        mesh region
  -dry-run | -n         report actions but do not remove
  -help                 print the usage

Remove the contents of the constant/polyMesh directory as per the
Foam::polyMesh::removeFiles() method.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPolyMesh">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
