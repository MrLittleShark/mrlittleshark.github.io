---
title: "constant/mechanicalProperties · mechanicalProperties"
layout: reference
description: "固体力学中的密度、弹性模量与泊松比等材料参数。平面应力和平面应变代表不同约束；检查位移场量纲、载荷方向及刚体运动约束。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>固体力学中的密度、弹性模量与泊松比等材料参数。平面应力和平面应变代表不同约束；检查位移场量纲、载荷方向及刚体运动约束。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>rho</td><td>固体密度，示例可以通过 uniform/value 子字典指定。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>nu</td><td>此文件中 nu 表示泊松比，不是流体运动黏度。</td></tr><tr><td>E</td><td>杨氏模量，压力单位。</td></tr><tr><td>planeStress</td><td>平面应力开关；关闭时的二维约束应结合求解器与几何解释。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · stressAnalysis/solidDisplacementFoam/plateHole</h3><p>原始路径：<code>tutorials/stressAnalysis/solidDisplacementFoam/plateHole/constant/mechanicalProperties</code>；求解器：<code>solidDisplacementFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole/constant/mechanicalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/mechanicalproperties/1-mechanicalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mechanicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rho
{
    type        uniform;
    value       7854;
}

nu
{
    type        uniform;
    value       0.3;
}

E
{
    type        uniform;
    value       2e+11;
}

planeStress     yes;


// ************************************************************************* //</code></pre><h3>示例 2 · stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad</h3><p>原始路径：<code>tutorials/stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad/constant/mechanicalProperties</code>；求解器：<code>solidEquilibriumDisplacementFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad/constant/mechanicalProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/mechanicalproperties/2-mechanicalProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/stressAnalysis/solidEquilibriumDisplacementFoam/beamEndLoad">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mechanicalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rho
{
    type        uniform;
    value       7854;
}

nu
{
    type        uniform;
    value       0.0;
}

E
{
    type        uniform;
    value       2e+11;
}

planeStress     yes;


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/soliddisplacementfoam/">solidDisplacementFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/mechanicalProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/mechanicalProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
