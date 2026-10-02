---
title: "01 版本说明与使用方法"
layout: reference
description: "版本说明与使用方法：用法与配置实例。"
cms_slug: "reference-manual-01"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>OpenFOAM v2512 属于 OpenCFD 发行分支。该分支与 OpenFOAM Foundation 发行版在命令、配置文件和模型接口方面存在差异，算例配置应采用对应分支的教程和文档。版本资料见 S1，源码见 S2。</p>
<div class="table-scroll"><table>
<tr><th>名称</th><th>v2512 定义</th><th>调用或配置示例</th></tr>
<tr><td>foam</td><td>切换至安装根目录的别名</td><td>foam</td></tr>
<tr><td>foamGet</td><td>官方核心发行包采用 foamGetDict</td><td>foamGetDict decomposeParDict</td></tr>
<tr><td>foamHelp</td><td>按 boundary、functionObject、solver 类别查询</td><td>foamHelp boundary -field U</td></tr>
<tr><td>ControlDict、SetFieldsDict</td><td>文件名区分大小写，采用小写首字母</td><td>system/controlDict、system/setFieldsDict</td></tr>
<tr><td>$FOAM_TOTORIAL</td><td>教程目录变量应为 $FOAM_TUTORIALS</td><td>cd "$FOAM_TUTORIALS"</td></tr>
<tr><td>tut、sol</td><td>分别切换至教程和求解器源码目录</td><td>tut 进入教程；sol 进入求解器源码</td></tr>
<tr><td>fvModels、momentumTransport</td><td>其他发行分支的配置文件名</td><td>v2512 常用 fvOptions 和 turbulenceProperties</td></tr>
<tr><td>yPlus、Q、forces</td><td>函数对象类型或 -func 预配置名称</td><td>simpleFoam -postProcess -func yPlus</td></tr>
</table></div>
<h3>1.1 命令语法约定</h3>
<p>命令语法中，方括号表示可选参数，中文名称表示待替换的参数。未指定 -case 时，程序通常读取当前算例目录。示例中的文件名、边界名称和区域名称应与算例数据对应。</p>
<p>各求解器条目给出功能和启动方式，所需网格、场文件及物理模型由对应算例提供。应用目录统计不含测试程序、第三方插件和用户自行编译的程序。</p>
<h3>1.2 常用命令选项</h3>
<div class="table-scroll"><table>
<tr><th>选项</th><th>含义</th><th>示例</th></tr>
<tr><td>-help、-help-full</td><td>简要帮助与完整帮助</td><td>blockMesh -help-full</td></tr>
<tr><td>-case 路径</td><td>指定算例目录</td><td>checkMesh -case ./caseA</td></tr>
<tr><td>-dict 文件</td><td>指定替代配置字典</td><td>topoSet -dict system/topoSetDict.alt</td></tr>
<tr><td>-parallel</td><td>启用并行模式，由 MPI 启动各进程</td><td>mpirun -np 4 simpleFoam -parallel</td></tr>
<tr><td>-region 名称</td><td>选择计算区域</td><td>checkMesh -region fluid</td></tr>
<tr><td>-time 范围</td><td>选择时刻</td><td>postProcess -time "0.1:0.5"</td></tr>
<tr><td>-latestTime</td><td>选择最后时刻</td><td>foamToVTK -latestTime</td></tr>
<tr><td>-constant、-withZero、-noZero</td><td>包含 constant、包含 0 或排除 0</td><td>foamListTimes -noZero</td></tr>
<tr><td>-overwrite</td><td>覆盖当前网格或相应输出</td><td>snappyHexMesh -overwrite</td></tr>
<tr><td>-fileHandler 类型</td><td>选择文件处理器</td><td>simpleFoam -fileHandler collated</td></tr>
<tr><td>-noFunctionObjects</td><td>关闭函数对象</td><td>simpleFoam -noFunctionObjects</td></tr>
<tr><td>-doc、-srcDoc</td><td>打开程序文档或源码文档</td><td>blockMesh -doc</td></tr>
</table></div>
<p>各程序支持的选项可通过 -help 或 -help-full 查询。Shell 脚本与编译程序分别解析参数，具体接口见相应命令条目。</p>
