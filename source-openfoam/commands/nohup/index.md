---
title: "nohup"
layout: reference
description: "使程序忽略挂断信号并重定向日志。"
---
{% raw %}
<div class="source-note">配套命令说明；不计入 278 个核心编译目标。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>使程序忽略挂断信号并重定向日志。</p><h2>使用入口</h2><pre><code class="language-bash">nohup interFoam &gt; log.interFoam 2&gt;&amp;1 &amp;</code></pre><h2>使用条件与核对</h2><p>使程序忽略挂断信号并重定向日志。 示例中的算例名、路径与主机名须按实际环境替换。</p><h2>来源与版本边界</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
