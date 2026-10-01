---
title: "第 1 章　OpenFOAM 分支与版本识别"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>使用其他发行分支的教程可能产生配置不兼容。应先确认分支、版本及配套教程。常用发行分支可按下表区分。</p>
<div class="table-scroll"><table>
<tr><th>分支</th><th>官网</th><th>版本号长相</th><th>典型命令风格</th></tr>
<tr><td>ESI / OpenCFD 版（本手册）</td><td>openfoam.com</td><td>v2506、v2512（年份+月份）</td><td>simpleFoam、interFoam，物性文件叫 transportProperties</td></tr>
<tr><td>Foundation 版</td><td>openfoam.org</td><td>11、12、13（整数）</td><td>foamRun -solver ...，物性文件叫 physicalProperties、momentumTransport</td></tr>
</table></div>
<p>为什么必须先分清：Foundation 从版本 11 起把几十个求解器合并成了一个 foamRun，字典文件也改了名。你如果装的是 ESI v2512，却照着 openfoam.org 的教程敲 foamRun，会得到 command not found；反过来在 .org 版里敲 simpleFoam 同样找不到。先看版本号长相：带 v 和四位年月的是 ESI 版。</p>
<p>一条命令确认：</p>
<pre><code>$ foamVersion
OpenFOAM-v2512 (www.openfoam.com) version v2512</code></pre>
{% endraw %}