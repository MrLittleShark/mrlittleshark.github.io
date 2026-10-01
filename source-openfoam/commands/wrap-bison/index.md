---
title: "wrap-bison · 构建或开发辅助脚本"
layout: reference
description: "A wrapper to handle renaming/relocation of bison-generated files. When bison is used, it generates several output files. The names of the regular output files may not match our expectations. The skeleton files are always named the same, whi"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>A wrapper to handle renaming/relocation of bison-generated files. When bison is used, it generates several output files. The names of the regular output files may not match our expectations. The skeleton files are always named the same, which can cause file-name collisions in some cases. Input: - myFile.yy Output: &lt;myFile.yy&gt; - myFile.tab.hh - myFile.tab.cc - location.hh - position.hh - stack.hh Approach - call bison from within a local Make/some-name/ directory. - use sed to modify the #include contents and rename files. From location.hh -&gt; myFile.location.hh - place generated *.hh files directly into lnInclude/ - place generated *.cc file into the build/ directory When called with m4 wrapping, it sets the m4 -I include to have the following: - the directory of the parser. - include/ in the top-level source tree of the current target (eg, src/finiteVolume/include/ when compiling libfiniteVolume) - include/ from OpenFOAM</p><h2>v2512 源码中的用途</h2><p>A wrapper to handle renaming/relocation of bison-generated files. When bison is used, it generates several output files. The names of the regular output files may not match our expectations. The skeleton files are always named the same, which can cause file-name collisions in some cases. Input: - myFile.yy Output: &lt;myFile.yy&gt; - myFile.tab.hh - myFile.tab.cc - location.hh - position.hh - stack.hh Approach - call bison from within a local Make/some-name/ directory. - use sed to modify the #include contents and rename files. From location.hh -&gt; myFile.location.hh - place generated *.hh files directly into lnInclude/ - place generated *.cc file into the build/ directory When called with m4 wrapping, it sets the m4 -I include to have the following: - the directory of the parser. - include/ in the top-level source tree of the current target (eg, src/finiteVolume/include/ when compiling libfiniteVolume) - include/ from OpenFOAM</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/scripts/wrap-bison&quot;</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>
A wrapper to handle renaming/relocation of bison-generated files. When bison is used, it generates several output files. The names of the regular output files may not match our expectations. The skeleton files are always named the same, which can cause file-name collisions in some cases. Input: - myFile.yy Output: &lt;myFile.yy&gt; - myFile.tab.hh - myFile.tab.cc - location.hh - position.hh - stack.hh Approach - call bison from within a local Make/some-name/ directory. - use sed to modify the #include contents and rename files. From location.hh -&gt; myFile.location.hh - place generated *.hh files directly into lnInclude/ - place generated *.cc file into the build/ directory When called with m4 wrapping, it sets the m4 -I include to have the following: - the directory of the parser. - include/ in the top-level source tree of the current target (eg, src/finiteVolume/include/ when compiling libfiniteVolume) - include/ from OpenFOAM
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-dry-run -grammar -h -no-tmp -output</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wrap-bison.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wrap-bison
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-bison

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wrap-bison [options] [bison args/options]

options:
  -dry-run          Process m4 only (output on stdout)
  -grammar          Output grammar tables (ignored)
  -no-tmp           Do not retain temporary m4 processed files
  -output=NAME      Request renaming actions
  -h, -help         Print the usage

A bison wrapper with renaming of skeleton files</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-bison">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
