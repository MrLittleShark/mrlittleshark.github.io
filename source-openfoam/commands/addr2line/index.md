---
title: "addr2line · 把二进制地址解析为函数名和源文件行号"
layout: reference
description: "把二进制地址解析为函数名和源文件行号。"
cms_slug: "command-addr2line"
---

<p>把二进制地址解析为函数名和源文件行号。</p><h2>开始前</h2>
<p>此处对应Linux GNU addr2line；需要带调试符号的可执行文件或库，以及该模块内的地址/偏移。示例0x1234应替换为实际值。</p>
<h2>示例 1：定位可执行文件地址</h2>
<pre><code class="language-bash">addr2line -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-e指定产生堆栈的可执行文件，地址替换为模块内地址；输出源文件和行号。</p>
<h2>示例 2：同时显示C++函数名</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-f增加函数名，-C还原C++修饰名称，便于把崩溃位置对应到类成员函数。</p>
<h2>示例 3：一次解析多个地址</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_APPBIN/mySolver" 0x1234 0x2345 0x3456
</code></pre>
<p>依次解析同一模块中的多个堆栈地址，输出相应调用位置。</p>
<h2>示例 4：定位共享库中的错误</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_LIBBIN/libmyBoundary.so" 0x1234
</code></pre>
<p>崩溃位于自定义边界库时选择该.so，并使用其模块内偏移，定位库源码而非主求解器。</p>
<h2>示例 5：展开内联调用链</h2>
<pre><code class="language-bash">addr2line -C -f -i -p -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-i展开内联函数，-p用更紧凑的单行形式输出；适合优化编译后一个地址对应多层内联代码的情况。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-a --addresses</code></td><td>Show addresses</td></tr><tr><td><code>-b --target=&lt;bfdname&gt;</code></td><td>Set the binary file format</td></tr><tr><td><code>-e --exe=&lt;executable&gt;</code></td><td>Set the input file name (default is a.out)</td></tr><tr><td><code>-i --inlines</code></td><td>Unwind inlined functions</td></tr><tr><td><code>-j --section=&lt;name&gt;</code></td><td>Read section-relative offsets instead of addresses</td></tr><tr><td><code>-p --pretty-print</code></td><td>Make the output easier to read for humans</td></tr><tr><td><code>-s --basenames</code></td><td>Strip directory names</td></tr><tr><td><code>-f --functions</code></td><td>Show function names</td></tr><tr><td><code>-C --demangle[=style]</code></td><td>Demangle function names</td></tr><tr><td><code>-R --recurse-limit</code></td><td>Enable a limit on recursion whilst demangling.  [Default]</td></tr><tr><td><code>-r --no-recurse-limit</code></td><td>Disable a limit on recursion whilst demangling</td></tr><tr><td><code>-h --help</code></td><td>Display this information</td></tr><tr><td><code>-v --version</code></td><td>Display the program&#x27;s version</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: /usr/bin/addr2line [option(s)] [addr(s)]
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
