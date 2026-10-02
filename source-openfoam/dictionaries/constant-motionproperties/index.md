---
title: "motionProperties"
layout: reference
description: "多相溃坝教程保留的专用文件，示例只含 movingFvMesh staticFvMesh。"
dictionary: true
cms_slug: "dictionary-motionproperties"
---

<p>多相溃坝教程保留的专用文件，示例只含 movingFvMesh staticFvMesh。</p><p>位置：<code>constant/motionProperties</code></p><h2>配置实例</h2><p>multiphase/multiphaseEulerFoam/damBreak4phase 中的 motionProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      motionProperties;
}

movingFvMesh    staticFvMesh;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>movingFvMesh</td><td>示例保留的旧式网格类型关键字。不要与 current dynamicFvMesh 名称混用；须检查实际求解器读取情况。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/multiphaseEulerFoam/damBreak4phase</summary><p>damBreak4phase 的 motionProperties 通过网格运动接口选择静止网格，四相体积分数与流场在固定单元上推进。</p>
<ul>
<li><code>movingFvMesh staticFvMesh</code> 指定网格点位置与拓扑保持固定。</li>
<li>四相界面的变化由相输运方程计算，网格选择与相的运动分别处理。</li>
</ul>
<p>扩展到带运动边界的问题时，除选择相应网格运动模型，还需给出位移或运动参数，并配置运动边界上的场条件。</p>
<p><a href="/assets/examples/v2512/motionproperties/1-motionProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/multiphaseEulerFoam/damBreak4phase/constant/motionProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/multiphaseEulerFoam/damBreak4phase">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      motionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

movingFvMesh    staticFvMesh;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/foamdictionary/">foamDictionary</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
