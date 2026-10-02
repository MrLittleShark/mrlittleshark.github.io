---
title: "06 常见文件与字典语法"
layout: reference
description: "常见文件与字典语法：用法与配置实例。"
cms_slug: "reference-manual-06"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>配置示例依据 v2512 源码、etc/caseDicts 和 tutorials 编写，参见 S2、S3。独立文件包含 FoamFile 文件头；配置片段应嵌入指定的父字典。几何尺寸、物性和数值参数按具体算例确定。</p>
<h3>6.1 目录结构与文件用途</h3>
<div class="table-scroll"><table>
<tr><th>路径</th><th>主要作用</th><th>使用阶段</th></tr>
<tr><td>0/ 或起始时间目录</td><td>U、p、T、湍流量、相分数等场的初值与边界条件</td><td>初始化和边界设置</td></tr>
<tr><td>0.orig/</td><td>教程约定的初始场备份目录</td><td>配合 restore0Dir 恢复</td></tr>
<tr><td>constant/polyMesh/</td><td>points、faces、owner、neighbour、boundary 及可选 zones</td><td>通常由网格工具生成</td></tr>
<tr><td>constant/triSurface/</td><td>STL、OBJ、eMesh 等几何与特征线</td><td>网格前处理</td></tr>
<tr><td>constant/</td><td>物性、湍流、重力、旋转、动网格等配置</td><td>物理模型设置</td></tr>
<tr><td>system/</td><td>controlDict、fvSchemes、fvSolution、网格工具字典</td><td>时间、离散、求解和工具控制</td></tr>
<tr><td>constant/区域名 和 system/区域名</td><td>分别保存各区域的网格、物性和数值配置</td><td>共轭传热等</td></tr>
<tr><td>system/finite-area/ 和 constant/finite-area/</td><td>有限面积配置与网格；多区域按名称分层</td><td>有限面积模型</td></tr>
<tr><td>processor0/ 等</td><td>分散式并行网格和场；collated 采用对应目录结构</td><td>decomposePar 等生成</td></tr>
<tr><td>postProcessing/</td><td>函数对象的采样、积分与统计结果</td><td>运行时或事后处理</td></tr>
<tr><td>时间目录/polyMesh/</td><td>移动网格点坐标及更新后的拓扑</td><td>动网格结果</td></tr>
<tr><td>Allrun、Allclean</td><td>约定的算例运行与清理脚本</td><td>算例批处理</td></tr>
</table></div>
<h3>6.2 文件头与字典语法</h3>
<p>字典采用“关键字 值;”的形式定义条目，以花括号组织子字典、圆括号定义列表、方括号表示量纲。单行和多行注释分别使用 // 和 /* ... */。文件名、关键字及模型名称区分大小写。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0;
    format ascii;
    class dictionary;
    object controlDict;
}</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置方法</th></tr>
<tr><td>version</td><td>OpenFOAM 文件格式版本</td><td>通常设为 2.0</td></tr>
<tr><td>format</td><td>存储方式</td><td>ascii 可读；binary 更紧凑</td></tr>
<tr><td>class</td><td>数据类型</td><td>dictionary、volScalarField、volVectorField 等</td></tr>
<tr><td>object</td><td>对象名</td><td>通常与文件名一致</td></tr>
<tr><td>location</td><td>可选存储位置说明</td><td>如 "0" 或 "system"，用于描述存储位置</td></tr>
<tr><td>dimensions</td><td>七个 SI 基本量纲指数</td><td>顺序为质量、长度、时间、温度、物质的量、电流、发光强度</td></tr>
<tr><td>uniform 与 nonuniform</td><td>统一赋值或按对象逐项赋值</td><td>非均匀列表数量须与网格对象数量匹配</td></tr>
<tr><td>true/false、on/off、yes/no</td><td>常见开关表示</td><td>同一文件采用一致的开关写法</td></tr>
</table></div>
<p>速度 U 的量纲为 [0 1 -1 0 0 0 0]，温度 T 为 [0 0 0 1 0 0 0]，运动黏度为 [0 2 -1 0 0 0 0]。压力场需区分运动学压力 [0 2 -2 0 0 0 0] 与以 Pa 表示的压力 [1 -1 -2 0 0 0 0]，具体定义见求解器及场文件的 dimensions。</p>
<h3>6.3 引用和预处理关键字</h3>
<div class="table-scroll"><table>
<tr><th>关键字</th><th>作用</th><th>示例</th></tr>
<tr><td>$名称</td><td>引用当前或可见作用域中的字典条目</td><td>pFinal { $p; relTol 0; }</td></tr>
<tr><td>${名称}</td><td>限定变量名称范围，支持环境变量展开</td><td>#include "${FOAM_CASE}/system/commonSettings"</td></tr>
<tr><td>$../名称</td><td>访问父字典作用域</td><td>a $../referenceValue;</td></tr>
<tr><td>$!名称</td><td>从顶层字典查找</td><td>a $!referenceValue;</td></tr>
<tr><td>#include</td><td>读取指定文件</td><td>#include "commonSettings"</td></tr>
<tr><td>#includeIfPresent</td><td>仅在文件存在时包含</td><td>#includeIfPresent "localOverrides"</td></tr>
<tr><td>#includeEtc</td><td>从 OpenFOAM 配置搜索路径引入文件</td><td>#includeEtc "caseDicts/meshQualityDict"</td></tr>
<tr><td>#includeFunc</td><td>加入预配置函数对象</td><td>#includeFunc solverInfo</td></tr>
<tr><td>#inputMode</td><td>控制重复键合并方式</td><td>#inputMode merge</td></tr>
<tr><td>#remove</td><td>删除已有条目，支持正则表达式</td><td>#remove "obsolete.*"</td></tr>
<tr><td>#calc</td><td>由动态编译表达式生成值</td><td>length 2; halfLength #calc "$length/2.0";</td></tr>
<tr><td>#eval</td><td>采用表达式求值</td><td>a #eval "sqrt(2.0)";</td></tr>
<tr><td>#codeStream</td><td>编译执行 C++ 并写回字典内容</td><td>见第 9.13 节</td></tr>
</table></div>
<p>OpenFOAM 字典引用与 Bash 变量展开分别由各自的解析器处理。使用 shell 生成含 $p 的字典时，采用带引号的 here-document 定界符，如 &lt;&lt;'EOF'，可保留引用原文。</p>
<p>foamDictionary system/fvSolution -expand 可查看展开后的配置。#calc 和 #codeStream 会编译并执行代码，使用时需具备相应编译环境。</p><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>
