---
title: "addr2line  将程序地址映射到源码行"
layout: reference
description: "源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。</p><h2>使用入口</h2><pre><code class="language-bash">addr2line -e mySolver 0x1234</code></pre><h2>使用条件与核对</h2><p>源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。 用法：addr2line -e 可执行文件 地址 示例：addr2line -e mySolver 0x1234
源码说明：
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-C -R -a -b -e -f -h -i -j -p -r -s -v</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/addr2line.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: addr2line
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/OSspecific/addr2line/Make/files

Usage: /usr/bin/addr2line [option(s)] [addr(s)]
 Convert addresses into line number/file name pairs.
 If no addresses are specified on the command line, they will be read from stdin
 The options are:
  @&lt;file&gt;                Read options from &lt;file&gt;
  -a --addresses         Show addresses
  -b --target=&lt;bfdname&gt;  Set the binary file format
  -e --exe=&lt;executable&gt;  Set the input file name (default is a.out)
  -i --inlines           Unwind inlined functions
  -j --section=&lt;name&gt;    Read section-relative offsets instead of addresses
  -p --pretty-print      Make the output easier to read for humans
  -s --basenames         Strip directory names
  -f --functions         Show function names
  -C --demangle[=style]  Demangle function names
  -R --recurse-limit     Enable a limit on recursion whilst demangling.  [Default]
  -r --no-recurse-limit  Disable a limit on recursion whilst demangling
  -h --help              Display this information
  -v --version           Display the program&#x27;s version

/usr/bin/addr2line: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big pe-bigobj-x86-64 pe-i386 pe-bigobj-i386 pdb srec symbolsrec verilog tekhex binary ihex plugin
Report bugs to &lt;https://sourceware.org/bugzilla/&gt;</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/OSspecific/addr2line/Make/files">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/OSspecific/addr2line/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
