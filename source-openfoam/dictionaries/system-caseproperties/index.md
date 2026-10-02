---
title: "caseProperties"
layout: reference
description: "createZeroDirectory 使用的算例描述文件，指定初始值、边界类别、模板选项与区域。"
dictionary: true
cms_slug: "dictionary-caseproperties"
---

<p>createZeroDirectory 使用的算例描述文件，指定初始值、边界类别、模板选项与区域。</p><p>位置：<code>system/caseProperties</code></p><h2>配置实例</h2><p>preProcessing/createZeroDirectory/snappyMultiRegionHeater 中的 caseProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      caseProperties;
}

initialConditions
{
    p       uniform 100000;
    rho     uniform 8000;
    T       uniform 300;
}

boundaryConditions
{
    thermalWalls
    {
        category    wall;
        type        thermal;
        patches     (minX minZ maxZ);
        options
        {
            heatTransfer adiabatic;
        }
        values
        {
            $/initialConditions;
        }
    }
    thermalCoupledWalls
    {
        category    wall;
        type        thermal;
        patches     (&quot;.*_to_.*&quot;);
        options
        {
            heatTransfer thermalCoupled;
        }
        values
        {
            $/initialConditions;
        }
    }
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>initialConditions</td><td>生成初始场时使用的变量和值，常写作 p uniform 100000 或 U uniform (0 0 0)。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>boundaryConditions</td><td>以逻辑边界组组织模板；每组再通过 patches 对应实际网格边界。</td></tr><tr><td>category</td><td>边界模板类别，例如 wall 或 inlet，影响可选择的模板类型。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>options</td><td>热传递、流动等边界模板选项；由所用模板库定义。</td></tr><tr><td>values</td><td>传给模板的字段或数值，示例通过 $/initialConditions 引用根字典中的默认值。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · preProcessing/createZeroDirectory/snappyMultiRegionHeater</summary><p>createZeroDirectory 使用 caseProperties 中的物理角色生成初始场。这里配置多区域加热器的 leftSolid 固体区域。</p>
<ul>
<li><code>initialConditions</code> 设 p=100000 Pa、rho=8000 kg/m³、T=300 K，供后面的边界模板引用。</li>
<li>thermalWalls 覆盖 minX、minZ、maxZ，<code>heatTransfer adiabatic</code> 指定绝热处理。</li>
<li>thermalCoupledWalls 用 <code>".*_to_.*"</code> 匹配区域间界面，<code>heatTransfer thermalCoupled</code> 生成热耦合设置。</li>
<li><code>values $/initialConditions</code> 从顶层初始条件引用参数，避免在各边界重复维护数值。</li>
</ul>
<p>给固体换材料时修改密度及相应热物性；生成后检查界面两侧的边界名称与温度耦合关系。</p>
<p><a href="/assets/examples/v2512/caseproperties/1-caseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/leftSolid/caseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      caseProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

initialConditions
{
    p       uniform 100000;
    rho     uniform 8000;
    T       uniform 300;
}


boundaryConditions
{
    thermalWalls
    {
        category    wall;
        type        thermal;
        patches     (minX minZ maxZ);
        options
        {
            heatTransfer adiabatic;
        }
        values
        {
            $/initialConditions;
        }
    }
    thermalCoupledWalls
    {
        category    wall;
        type        thermal;
        patches     (&quot;.*_to_.*&quot;);
        options
        {
            heatTransfer thermalCoupled;
        }
        values
        {
            $/initialConditions;
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · preProcessing/createZeroDirectory/cavity</summary><p>方腔的 caseProperties 将“运动顶壁、静止固壁”等物理角色转换为具体的 U、p 边界配置。</p>
<ul>
<li>初始 <code>U (0 0 0)</code> 表示静止流体，<code>p 0</code> 给出压力初值。</li>
<li>topWall 对应 movingWall，<code>motion moving</code> 和 <code>U (1 0 0)</code> 让顶壁沿 x 方向以 1 m/s 运动。</li>
<li>walls 对应 fixedWalls，<code>motion stationary</code> 生成静止无滑移壁面条件。</li>
<li>两组壁面都采用 <code>type noSlip</code>；运动壁面的无滑移速度等于壁面自身速度。模板中其他通用选项由生成器按所选模型处理。</li>
</ul>
<p>改变顶盖速度时修改 topWall 的 U，再重新生成初始场；可用生成后的 0/U 检查方向与数值。</p>
<p><a href="/assets/examples/v2512/caseproperties/2-caseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/cavity/system/caseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      caseProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

initialConditions
{
    U           uniform (0 0 0);
    p           uniform 0;
}

boundaryConditions
{
    topWall
    {
        category        wall;
        patches         (movingWall);
        type            noSlip;
        options
        {
            wallFunction    highReynolds;
            motion          moving;
        };
        values
        {
            U           uniform (1 0 0);
        }
    }

    walls
    {
        category        wall;
        patches         (fixedWalls);
        type            noSlip;
        options
        {
            wallFunction    highReynolds;
            motion          stationary;
        };
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · preProcessing/createZeroDirectory/motorBike</summary><p>motorBike 的 caseProperties 用于创建外流计算的初始场和边界条件。它把车体、地面、入口、出口分别描述为物理边界。</p>
<ul>
<li>初始 <code>U (20 0 0)</code> 设来流速度 20 m/s，<code>k 0.24</code>、<code>omega 1.78</code> 给出湍流初值。</li>
<li>motorBikeGroup 采用静止无滑移壁面和 highReynolds 壁面处理；地面 lowerWall 同样为无滑移壁面。</li>
<li>inlet 的 <code>subSonic</code>、<code>fixedVelocity</code> 使用给定入口速度，outlet 的 <code>returnFlow default</code> 为可能的回流提供模板处理。</li>
<li>upperWall 和 frontAndBack 使用 slip，减少外围边界对切向速度的约束。</li>
</ul>
<p>改变来流工况时同时检查湍流入口值和车体首层网格；若模拟移动地面，应更新地面运动选项及速度。</p>
<p><a href="/assets/examples/v2512/caseproperties/3-caseProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/motorBike/system/caseProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/motorBike">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      caseProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

initialConditions
{
    U           uniform (20 0 0);
    p           uniform 0;
    k           uniform 0.24;
    omega       uniform 1.78;
    nut         uniform 0;
}

boundaryConditions
{
    motorbike
    {
        category        wall;
        type            noSlip;
        patches         (motorBikeGroup);
        options
        {
            wallFunction    highReynolds;
            motion          stationary;
        }
        values
        {
            $/initialConditions;
        }
    }

    inlet
    {
        category        inlet;
        type            subSonic;
        patches         (inlet);
        options
        {
            flowSpecification fixedVelocity;
        }
        values
        {
            $/initialConditions;
        }
    }

    lowerWall
    {
        category        wall;
        type            noSlip;
        patches         (lowerWall);
        options
        {
            wallFunction    highReynolds;
            motion          stationary;
        }
        values
        {
            $/initialConditions;
        }
    }

    outlet
    {
        category        outlet;
        type            subSonic;
        patches         (outlet);
        options
        {
            returnFlow      default;
        }
        values
        {
            $/initialConditions;
        }
    }

    upperWall
    {
        category        wall;
        type            slip;
        patches         (upperWall);
        values
        {
            $/initialConditions;
        }
    }

    frontAndBack
    {
        category        wall;
        type            slip;
        patches         (frontAndBack);
        values
        {
            $/initialConditions;
        }
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/createzerodirectory/">createZeroDirectory</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>重启时刻不符合预期</td><td>核对 startFrom、startTime 与已存在的时间目录，避免旧结果影响首次运行。</td></tr><tr><td>时间目录增长过快</td><td>结合 writeControl、writeInterval、purgeWrite 与函数对象输出，先估计磁盘占用。</td></tr><tr><td>开启 adjustTimeStep 仍不生效</td><td>确认求解器确实实现对应时间步控制；检查当前求解器是否读取该参数。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
