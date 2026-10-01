---
title: "cleanOptimisation · 已加载脚本中的 shell 函数"
layout: reference
description: "定义于 bin/tools/CleanFunctions；需要先 source 对应脚本。它不是独立的 OpenFOAM 可执行程序。"
---
{% raw %}
<div class="source-note">源码中定义；未执行函数。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>定义于 bin/tools/CleanFunctions；需要先 source 对应脚本。它不是独立的 OpenFOAM 可执行程序。</p><h2>使用入口</h2><pre><code class="language-bash">. &quot;&#36;WM_PROJECT_DIR/bin/tools/CleanFunctions&quot;
type cleanOptimisation</code></pre><h2>使用条件与核对</h2><p>这是 v2512 源码中的函数入口。用途、位置参数和副作用应以函数定义及调用处为准。清理函数会删除指定算例的生成文件，应先保存需要保留的数据。</p><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/CleanFunctions">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
