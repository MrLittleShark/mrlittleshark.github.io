---
title: "foamExec"
layout: reference
description: "使用安装目录中提供的环境包装脚本运行应用。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>使用安装目录中提供的环境包装脚本运行应用。</p><h2>v2512 源码中的用途</h2><p>Runs an application (with arguments) after first sourcing the OpenFOAM etc/bashrc file from the project directory Can useful for parallel runs. For example, mpirun -n &lt;nProcs&gt; \ projectDir/bin/tools/foamExec &lt;simpleFoam&gt; ... -parallel</p><h2>使用入口</h2><pre><code class="language-bash">&quot;&#36;WM_PROJECT_DIR/bin/tools/foamExec&quot; icoFoam -help</code></pre><p>该条属于内部构建或开发辅助入口，可能依赖调用方预先设置变量、工作目录和参数。正常使用应优先从 wmake、Allwmake 或相应公开脚本进入。</p><h2>使用条件与核对</h2><p>使用安装目录中提供的环境包装脚本运行应用。 示例中的算例名、路径与主机名须按实际环境替换。
Runs an application (with arguments) after first sourcing the OpenFOAM etc/bashrc file from the project directory Can useful for parallel runs. For example, mpirun -n &lt;nProcs&gt; \ projectDir/bin/tools/foamExec &lt;simpleFoam&gt; ... -parallel
辅助脚本不一定加入 PATH；不要把内部调用接口当作稳定的用户命令。
源码帮助选项：-help</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamexec.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamExec
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamExec [OPTION] &lt;application&gt; ...

options:
  -help             Print the usage

Run an application (with arguments) after first sourcing
the OpenFOAM etc/bashrc file from the project directory:
(&#36;projectDir)</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
