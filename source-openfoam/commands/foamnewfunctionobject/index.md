---
title: "foamNewFunctionObject · 在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象"
layout: reference
description: "在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象。"
cms_slug: "command-foamnewfunctionobject"
---

<p>在生成目录运行 wmake libso，随后在 functions 中配置并加载该对象。</p><h2>用法</h2><pre><code class="language-bash">foamNewFunctionObject myProbe</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewFunctionObject [-h | -help] &lt;functionObjectName&gt;

* Create directory with source and compilation files for a new function object
  &lt;functionObjectName&gt; (dir)
  - &lt;functionObjectName&gt;.H
  - &lt;functionObjectName&gt;.C
  - IO&lt;functionObjectName&gt;.H
  - Make (dir)
    - files
    - options
  Compiles a library named lib&lt;functionObjectName&gt;FunctionObject.so in
  \$FOAM_USER_LIBBIN:
  $FOAM_USER_LIBBIN</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewFunctionObject">源码与说明</a> · <a href="/assets/command-help/foamnewfunctionobject.txt">帮助文本</a></p>
