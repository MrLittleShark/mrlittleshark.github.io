---
title: "foamNewBC · 在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库"
layout: reference
description: "在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。"
cms_slug: "command-foamnewbc"
---

<p>在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。</p><h2>用法</h2><pre><code class="language-bash">foamNewBC fixedValue scalar myTemperature</code></pre><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamNewBC [-h | -help] &lt;base&gt; &lt;type&gt; &lt;boundaryConditionName&gt;

* Create directory of source and compilation files for a new boundary condition
  &lt;boundaryConditionName&gt; (dir)
  - .C and .H source files
  - Make (dir)
    - files
    - options
  Compiles a library named lib&lt;boundaryConditionName&gt;.so in \$FOAM_USER_LIBBIN:
  $FOAM_USER_LIBBIN

&lt;base&gt; conditions:
-f | -fixedValue    | fixedValue
-m | -mixed         | mixed

&lt;type&gt; options:
-a | -all    | all  | template (creates a template class)
-s | -scalar | scalar
-v | -vector | vector
-t | -tensor | tensor
-symmTensor  | symmTensor
-sphericalTensor | sphericalTensor</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewBC">源码与说明</a> · <a href="/assets/command-help/foamnewbc.txt">帮助文本</a></p>
