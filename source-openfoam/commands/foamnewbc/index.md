---
title: "foamNewBC  生成自定义边界条件代码"
layout: reference
description: "在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。</p><h2>v2512 源码中的用途</h2><p>Create directory of source and compilation files for a new BC</p><h2>使用入口</h2><pre><code class="language-bash">foamNewBC fixedValue scalar myTemperature</code></pre><h2>使用条件与核对</h2><p>在生成目录运行 wmake libso，并在算例的 libs 中加载生成的库。 用法：foamNewBC 基类 场类型 名称 示例：foamNewBC fixedValue scalar myTemperature
Create directory of source and compilation files for a new BC
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-a -f -m -s -sphericalTensor -symmTensor -t -v</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamnewbc.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamNewBC
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewBC

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamNewBC [-h | -help] &lt;base&gt; &lt;type&gt; &lt;boundaryConditionName&gt;

* Create directory of source and compilation files for a new boundary condition
  &lt;boundaryConditionName&gt; (dir)
  - .C and .H source files
  - Make (dir)
    - files
    - options
  Compiles a library named lib&lt;boundaryConditionName&gt;.so in \&#36;FOAM_USER_LIBBIN:
  &#36;FOAM_USER_LIBBIN

&lt;base&gt; conditions:
-f | -fixedValue    | fixedValue
-m | -mixed         | mixed

&lt;type&gt; options:
-a | -all    | all  | template (creates a template class)
-s | -scalar | scalar
-v | -vector | vector
-t | -tensor | tensor
-symmTensor  | symmTensor
-sphericalTensor | sphericalTensor</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewBC">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
