---
title: "thermalProperties"
layout: reference
description: "专用固体或热弹性求解器的热物性与热应力开关。"
dictionary: true
cms_slug: "dictionary-thermalproperties"
---

<p>专用固体或热弹性求解器的热物性与热应力开关。</p><p>位置：<code>constant/thermalProperties</code></p><h2>配置实例</h2><p>stressAnalysis/solidDisplacementFoam/plateHole 中的 thermalProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      thermalProperties;
}

C
{
    type        uniform;
    value       434;
}

k
{
    type        uniform;
    value       60.5;
}

alpha
{
    type        uniform;
    value       1.1e-05;
}

thermalStress   no;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>C</td><td>固体比热容，可通过 uniform/value 方式指定。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>k</td><td>固体热导率，此处不是湍动能。</td></tr><tr><td>alpha</td><td>固体线膨胀系数，此处不是多相流体积分数。</td></tr><tr><td>thermalStress</td><td>是否启用温度变化引起的热应力。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · stressAnalysis/solidDisplacementFoam/plateHole</summary><p>plateHole 的 thermalProperties 提供热传导和热膨胀所需常数，并决定是否把温度变化耦合到应力。</p>
<ul>
<li><code>C/value 434</code> 为比热容，单位 J/(kg·K)。</li>
<li><code>k/value 60.5</code> 为热导率，单位 W/(m·K)。</li>
<li><code>alpha/value 1.1e-5</code> 是线膨胀系数，单位 K⁻¹，用于把温差转换为热应变。</li>
<li><code>thermalStress no</code> 在当前计算中关闭热应力耦合。</li>
</ul>
<p>研究受热板的变形时开启热应力，并同时给出温度初值、热边界条件以及对应参考温度设置。</p>
<p><a href="/assets/examples/v2512/thermalproperties/1-thermalProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole/constant/thermalProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/stressAnalysis/solidDisplacementFoam/plateHole">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      thermalProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

C
{
    type        uniform;
    value       434;
}

k
{
    type        uniform;
    value       60.5;
}

alpha
{
    type        uniform;
    value       1.1e-05;
}

thermalStress   no;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/soliddisplacementfoam/">solidDisplacementFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
