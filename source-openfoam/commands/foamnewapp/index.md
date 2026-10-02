---
title: "foamNewApp · 生成应用源码和 Make 文件"
layout: reference
description: "生成应用源码和 Make 文件。在生成目录运行 wmake，程序通常输出至 FOAM_USER_APPBIN。"
cms_slug: "command-foamnewapp"
---

<p>生成应用源码和 Make 文件。在生成目录运行 wmake，程序通常输出至 FOAM_USER_APPBIN。</p><h2>用法</h2><pre><code class="language-bash">foamNewApp myScalarFoam</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewApp [-h | -help] &lt;applicationName&gt;

* Create directory with source and compilation files for a new application
  &lt;applicationName&gt; (dir)
  - &lt;applicationName&gt;.C
  - Make (dir)
    - files
    - options
  Compiles an executable named &lt;applicationName&gt; in \$FOAM_USER_APPBIN:
  $FOAM_USER_APPBIN</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewApp">源码与说明</a> · <a href="/assets/command-help/foamnewapp.txt">帮助文本</a></p>
