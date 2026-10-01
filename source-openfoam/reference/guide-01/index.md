---
title: "第 1 章　OpenFOAM 分支与版本识别"
layout: reference
description: "OpenCFD v2512 OpenFOAM 分支与版本识别；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>使用其他发行分支的教程可能产生配置不兼容。应先确认分支、版本及配套教程。常用发行分支可按下表区分。</p>
<div class="table-scroll"><table>
<tr><th>分支</th><th>官网</th><th>版本标识</th><th>典型命令风格</th></tr>
<tr><td>OpenCFD 版（本手册）</td><td>openfoam.com</td><td>v2506、v2512（年份+月份）</td><td>simpleFoam、interFoam 等独立程序；物性文件由模型决定</td></tr>
<tr><td>Foundation 版</td><td>openfoam.org</td><td>11、12、13（整数）</td><td>较新版本采用模块化求解入口；物性和湍流配置接口需分别核对</td></tr>
</table></div>
<p>OpenCFD v2512 与 Foundation 发行版是不同的代码分支。较新的 Foundation 版本使用模块化求解器及不同配置接口；不能把其命令和字典名称直接移植到 v2512。本网站以 OpenCFD v2512 的实际程序、源码标签和教程为准，版本号外观只用于初步识别。</p>
<p>一条命令确认：</p>
<pre><code class="language-bash">printf '%s\n' "&#36;WM_PROJECT_VERSION"  # 版本变量不依赖交互式别名</code></pre><h2>环境函数与安装程序的区别</h2><p><code>foamVersion</code>、<code>tut</code>、<code>run</code> 等可由环境脚本定义为函数或别名，并非所有打包环境和非交互式 shell 都加载它们。<code>type foamVersion</code> 用于诊断当前 shell；查询版本可直接输出 <code>WM_PROJECT_VERSION</code>，查找实际程序用 <code>command -v blockMesh</code>。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">v2512 的函数与别名定义</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">foamExec 的位置和环境激活实现</a></p>
{% endraw %}
