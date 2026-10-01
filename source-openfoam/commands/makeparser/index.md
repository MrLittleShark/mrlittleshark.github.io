---
title: "makeParser · 构建或开发辅助脚本"
layout: reference
description: "Pregenerate ragel code and/or lemon parser headers"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Pregenerate ragel code and/or lemon parser headers</p><h2>v2512 源码中的用途</h2><p>Pregenerate ragel code and/or lemon parser headers</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/scripts/makeParser&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
Pregenerate ragel code and/or lemon parser headers
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-code -dry-run -grammar -h -header -no-lines -no-tmp -parser -prefix -remove -scanner</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/makeparser.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: makeParser
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeParser

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: makeParser [options]

options:
  -prefix=NAME      Common prefix for parser and scanner
  -parser=FILE      Generate lemon parser header
  -scanner=FILE     Generate ragel scanner code
  -code             Generate parser code, not header
  -header           Generate parser header, not code (default)
  -grammar          Output grammar tables (if supported)
  -dry-run          Process m4 only (output on stdout)
  -no-lines         Suppress generation of #line directives
  -no-tmp           Do not retain temporary m4 processed files
  -remove           Remove generated code
  -h, -help         Print the usage

Pregenerate ragel code and/or lemon parser headers</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeParser">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
