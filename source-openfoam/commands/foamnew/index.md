---
title: "foamNew  生成源码或模板文件"
layout: reference
description: "示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。</p><h2>v2512 源码中的用途</h2><p>Create a new standard OpenFOAM source or template file</p><h2>使用入口</h2><pre><code class="language-bash">foamNew source H MyModel</code></pre><h2>使用条件与核对</h2><p>示例生成 MyModel.H。C、H、I、IO 和 App 等模板由 foamNewSource 配套提供。 用法：foamNew source 文件类型 类名 示例：foamNew source H MyModel
Create a new standard OpenFOAM source or template file
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-s -t</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamnew.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamNew
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNew

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamNew &lt;type&gt; {args}

* create a new standard OpenFOAM source or template file

type:
    -s | -source | source
    -t | -template | template</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNew">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
