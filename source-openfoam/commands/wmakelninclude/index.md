---
title: "wmakeLnInclude · OpenFOAM 官方脚本"
layout: reference
description: "Link header/template files from specified dir(s) into their respective lnInclude directories Header files : .h .H .hh .hpp .hxx Source files : .c .C .cc .cpp .cxx Template files : -- .C .tcc .tpp .txx"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Link header/template files from specified dir(s) into their respective lnInclude directories Header files : .h .H .hh .hpp .hxx Source files : .c .C .cc .cpp .cxx Template files : -- .C .tcc .tpp .txx</p><h2>v2512 源码中的用途</h2><p>Link header/template files from specified dir(s) into their respective lnInclude directories Header files : .h .H .hh .hpp .hxx Source files : .c .C .cc .cpp .cxx Template files : -- .C .tcc .tpp .txx</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/wmakeLnInclude&quot;</code></pre><h2>使用条件与核对</h2><p>
Link header/template files from specified dir(s) into their respective lnInclude directories Header files : .h .H .hh .hpp .hxx Source files : .c .C .cc .cpp .cxx Template files : -- .C .tcc .tpp .txx
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-extra -f -help -no-extra -pwd -s -u</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wmakelninclude.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wmakeLnInclude
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnInclude

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wmakeLnInclude [OPTION] [-pwd | dir [.. dirN]]

options:
  -f | -force       Force remove of existing lnInclude/ before recreating
  -u | -update      Update existing lnInclude directories
  -s | -silent      Silent mode (do not echo command)
  -extra            Also include all source files in lnInclude/
  -no-extra         Do not include all source files in lnInclude/ [default]
  -pwd              Locate root directory containing Make/ directory
  -help             Print the usage

Link header/template files from specified dir(s) into their respective
lnInclude/ directories. With &#x27;-update&#x27;, items are relinked with &#x27;ln -sf&#x27;</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnInclude">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
