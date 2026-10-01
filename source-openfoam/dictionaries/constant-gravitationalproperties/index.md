---
title: "constant/gravitationalProperties · gravitationalProperties"
layout: reference
description: "shallowWaterFoam 浅水教程中的重力与旋转参数。g 给出重力向量，rotating 控制旋转效应，Omega 给出旋转角速度向量。常规浮力或 VOF 流动通常使用 constant/g，这两种文件结构不可直接互换。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>shallowWaterFoam 浅水教程中的重力与旋转参数。g 给出重力向量，rotating 控制旋转效应，Omega 给出旋转角速度向量。常规浮力或 VOF 流动通常使用 constant/g，这两种文件结构不可直接互换。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>g</td><td>含显式量纲的重力加速度向量，垂向方向由其符号与坐标共同确定。</td></tr><tr><td>rotating</td><td>是否在浅水方程中考虑旋转效应。</td></tr><tr><td>Omega</td><td>旋转角速度向量，量纲为时间的负一次方；并非湍流比耗散率 omega。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>g</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · incompressible/shallowWaterFoam/squareBump</h3><p>原始路径：<code>tutorials/incompressible/shallowWaterFoam/squareBump/constant/gravitationalProperties</code>；求解器：<code>shallowWaterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/shallowWaterFoam/squareBump/constant/gravitationalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/gravitationalproperties/1-gravitationalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/shallowWaterFoam/squareBump">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      gravitationalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

g            g           [0 1 -2 0 0 0 0]  (0 0 -9.81);
rotating     true;
Omega        Omega       [0 0 -1 0 0 0 0]  (0 0 7.292e-5);


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/shallowwaterfoam/">shallowWaterFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/gravitationalProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/gravitationalProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
