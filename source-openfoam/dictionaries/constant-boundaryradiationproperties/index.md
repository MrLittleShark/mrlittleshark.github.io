---
title: "boundaryRadiationProperties"
layout: reference
description: "按边界配置辐射发射率、吸收率或透射率的模型。"
dictionary: true
cms_slug: "dictionary-boundaryradiationproperties"
---

<p>按边界配置辐射发射率、吸收率或透射率的模型。</p><p>位置：<code>constant/boundaryRadiationProperties</code></p><h2>配置实例</h2><p>combustion/fireFoam/LES/simplePMMApanel 中的 boundaryRadiationProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      boundaryRadiationProperties;
}

&quot;.*&quot;
{
    type            lookup;
    emissivity      1.0;
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>emissivity</td><td>发射率或发射率模型输入；应与辐射模型和壁面物理条件一致。</td></tr><tr><td>absorptivity</td><td>吸收率或其模型输入。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · combustion/fireFoam/LES/simplePMMApanel</summary><p>PMMA 板燃烧计算需要壁面辐射性质。这个文件用统一参数匹配所有边界。</p>
<ul>
<li><code>".*"</code> 是匹配边界名称的正则表达式。</li>
<li><code>type lookup</code> 直接读取字典中的辐射参数。</li>
<li><code>emissivity 1</code> 将所匹配边界的发射率设为 1，对应黑体发射率上限。</li>
</ul>
<p>给不同材料赋值时可为材料边界分别建子字典；发射率由材料表面与温度条件确定，并与选用的辐射模型配套。</p>
<p><a href="/assets/examples/v2512/boundaryradiationproperties/1-boundaryRadiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel/constant/boundaryRadiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/fireFoam/LES/simplePMMApanel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1.0;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/reactingFoam/RAS/SandiaD_LTS</summary><p>Sandia D 火焰算例使用边界辐射参数来描述辐射与外部边界的交换。</p>
<ul>
<li><code>".*"</code> 将同一组参数用于所有匹配边界，<code>type lookup</code> 采用常数输入。</li>
<li><code>emissivity 1</code> 指定发射率为 1。</li>
<li><code>absorptivity 0</code> 将本配置中的吸收率设为 0，影响入射辐射的吸收处理。</li>
</ul>
<p>移植到受热固壁时，根据壁面材料及辐射边界条件重新设置发射率与吸收率，不能直接沿用开放火焰边界的组合。</p>
<p><a href="/assets/examples/v2512/boundaryradiationproperties/2-boundaryRadiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/boundaryRadiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1;
    absorptivity    0;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/buoyantSimpleFoam/hotRadiationRoom</summary><p>hotRadiationRoom 同时考虑温度变化与壁面辐射，这里把匹配边界设置为完全发射、完全吸收入射辐射的表面。</p>
<ul>
<li><code>type lookup</code> 从本字典读取参数，<code>".*"</code> 覆盖所有边界名称。</li>
<li><code>emissivity 1</code> 采用黑体发射率。</li>
<li><code>absorptivity 1</code> 使入射辐射全部按吸收处理；这两个值应结合壁面辐射边界条件理解。</li>
</ul>
<p>需要区分金属、涂层或其他表面时，为对应 patch 单独给出参数，并比较壁面辐射热流与温度变化。</p>
<p><a href="/assets/examples/v2512/boundaryradiationproperties/3-boundaryRadiationProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom/constant/boundaryRadiationProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/hotRadiationRoom">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      boundaryRadiationProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

&quot;.*&quot;
{
    type            lookup;
    emissivity      1.0;
    absorptivity    1.0;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/buoyantsimplefoam/">buoyantSimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
