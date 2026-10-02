---
title: "compileApplication · 通过 wmake 编译指定目录中的应用程序"
layout: reference
description: "通过 wmake 编译指定目录中的应用程序。"
cms_slug: "command-compileapplication"
---

<p>通过 wmake 编译指定目录中的应用程序。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 函数把第一个参数作为目录传给 wmake；源码目录需有完整 Make/files 与 Make/options，路径使用不含空格的名称。</p>
<h2>示例 1：编译一个工具</h2>
<pre><code class="language-bash">compileApplication fieldStats
</code></pre>
<p>调用 wmake fieldStats，终端显示编译命令，输出位置由 Make/files 决定。</p>
<h2>示例 2：编译生成的应用骨架</h2>
<pre><code class="language-bash">foamNewApp inspectCase
compileApplication inspectCase
</code></pre>
<p>先生成应用和 Make 文件，再构建到 FOAM_USER_APPBIN。</p>
<h2>示例 3：编译指定源码目录</h2>
<pre><code class="language-bash">compileApplication "$WM_PROJECT_USER_DIR/applications/utilities/fieldStats"
</code></pre>
<p>完整路径消除当前目录对查找的影响，输入仍为同一编译单元。</p>
<h2>示例 4：批量编译两个项目</h2>
<pre><code class="language-bash">for appDir in fieldStats meshReport; do compileApplication "$appDir" || break; done
</code></pre>
<p>依次编译已准备的工具；失败后停止，方便从当前终端定位第一处错误。</p>
<h2>示例 5：编译后运行</h2>
<pre><code class="language-bash">compileApplication fieldStats &amp;&amp; fieldStats -case caseA
</code></pre>
<p>工具参数以其实现为准；仅在编译成功后运行，避免误用旧二进制。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
