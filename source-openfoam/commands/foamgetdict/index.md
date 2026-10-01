---
title: "foamGetDict  复制配置字典模板"
layout: reference
description: "默认写入 system，*Properties 通常写入 constant。-target 指定目标目录，-force 覆盖已有文件。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认写入 system，*Properties 通常写入 constant。-target 指定目标目录，-force 覆盖已有文件。</p><h2>v2512 源码中的用途</h2><p>Find an OpenFOAM dictionary file from OpenFOAM/etc/caseDicts/ or {user,site} locations and copy it into the case directory.</p><h2>使用入口</h2><pre><code class="language-bash">foamGetDict decomposeParDict</code></pre><h2>使用条件与核对</h2><p>默认写入 system，*Properties 通常写入 constant。-target 指定目标目录，-force 覆盖已有文件。 用法：foamGetDict [选项] 文件名 示例：foamGetDict decomposeParDict
Find an OpenFOAM dictionary file from OpenFOAM/etc/caseDicts/ or {user,site} locations and copy it into the case directory.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-case -cfg -ext -f -help -no-ext -target -with-api</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamgetdict.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamGetDict
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamGetDict

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamGetDict [OPTIONS] &lt;file&gt;
options:
  -case &lt;dir&gt;       Alternative case directory, default is the cwd
  -ext  &lt;ext&gt;       File extension
  -cfg              Same as &#x27;-ext cfg&#x27; for &#x27;.cfg&#x27; files
  -f | -force       Force overwrite of existing files
  -no-ext           Files without extension
  -target &lt;dir&gt;     Target directory (default: system, or auto-detected)
  -with-api=NUM     Alternative api value for searching
  -help             Display short help and exit

Find an OpenFOAM dictionary file from etc/caseDicts/ or {user,site} locations
and copy it into the case directory. For example,

    foamGetDict decomposeParDict
    foamGetDict extrudeMeshDict
    foamGetDict createPatchDict
    foamGetDict surfaces</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamGetDict">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
