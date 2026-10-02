---
title: "addr2line · 源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具"
layout: reference
description: "源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。"
cms_slug: "command-addr2line"
---

<p>源码包提供 macOS 兼容实现；Linux 通常使用 GNU Binutils 同名工具。地址解析需具备调试符号。</p><h2>用法</h2><pre><code class="language-bash">addr2line -e mySolver 0x1234</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-a --addresses</td><td>Show addresses</td></tr><tr><td>-b --target=&lt;bfdname&gt;</td><td>Set the binary file format</td></tr><tr><td>-e --exe=&lt;executable&gt;</td><td>Set the input file name (default is a.out)</td></tr><tr><td>-i --inlines</td><td>Unwind inlined functions</td></tr><tr><td>-j --section=&lt;name&gt;</td><td>Read section-relative offsets instead of addresses</td></tr><tr><td>-p --pretty-print</td><td>Make the output easier to read for humans</td></tr><tr><td>-s --basenames</td><td>Strip directory names</td></tr><tr><td>-f --functions</td><td>Show function names</td></tr><tr><td>-C --demangle[=style]</td><td>Demangle function names</td></tr><tr><td>-R --recurse-limit</td><td>Enable a limit on recursion whilst demangling.  [Default]</td></tr><tr><td>-r --no-recurse-limit</td><td>Disable a limit on recursion whilst demangling</td></tr><tr><td>-h --help</td><td>Display this information</td></tr><tr><td>-v --version</td><td>Display the program&#x27;s version</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: /usr/bin/addr2line [option(s)] [addr(s)]
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
Report bugs to &lt;https://sourceware.org/bugzilla/&gt;</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/OSspecific/addr2line/Make/files">源码与说明</a> · <a href="/assets/command-help/addr2line.txt">帮助文本</a></p>
