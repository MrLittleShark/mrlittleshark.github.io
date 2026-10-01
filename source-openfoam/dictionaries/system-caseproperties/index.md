---
title: "system/caseProperties · caseProperties"
layout: reference
description: "createZeroDirectory 使用的算例描述文件，指定初始值、边界类别、模板选项与区域。工具根据求解器、湍流模型和模板生成 0/ 场；它不是求解器每一步读取的时间控制字典。多区域时每个区域可有独立的 caseProperties。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>createZeroDirectory 使用的算例描述文件，指定初始值、边界类别、模板选项与区域。工具根据求解器、湍流模型和模板生成 0/ 场；它不是求解器每一步读取的时间控制字典。多区域时每个区域可有独立的 caseProperties。</p><figure><img src="/assets/diagrams/reference-3.svg" alt="计算控制配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>initialConditions</td><td>生成初始场时使用的变量和值，常写作 p uniform 100000 或 U uniform (0 0 0)。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>boundaryConditions</td><td>以逻辑边界组组织模板；每组再通过 patches 对应实际网格边界。</td></tr><tr><td>category</td><td>边界模板类别，例如 wall 或 inlet，影响可选择的模板类型。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>options</td><td>热传递、流动等边界模板选项；由所用模板库定义。</td></tr><tr><td>values</td><td>传给模板的字段或数值，示例通过 &#36;/initialConditions 引用根字典中的默认值。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>initialConditions</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · preProcessing/createZeroDirectory/snappyMultiRegionHeater</h3><p>原始路径：<code>tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/leftSolid/caseProperties</code>；求解器：<code>chtMultiRegionFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater/system/leftSolid/caseProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/caseproperties/1-caseProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/snappyMultiRegionHeater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
            &#36;/initialConditions;
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
            &#36;/initialConditions;
        }
    }
}


// ************************************************************************* //</code></pre><h3>示例 2 · preProcessing/createZeroDirectory/cavity</h3><p>原始路径：<code>tutorials/preProcessing/createZeroDirectory/cavity/system/caseProperties</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/cavity/system/caseProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/caseproperties/2-caseProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · preProcessing/createZeroDirectory/motorBike</h3><p>原始路径：<code>tutorials/preProcessing/createZeroDirectory/motorBike/system/caseProperties</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/motorBike/system/caseProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/caseproperties/3-caseProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/createZeroDirectory/motorBike">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
            &#36;/initialConditions;
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
            &#36;/initialConditions;
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
            &#36;/initialConditions;
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
            &#36;/initialConditions;
        }
    }

    upperWall
    {
        category        wall;
        type            slip;
        patches         (upperWall);
        values
        {
            &#36;/initialConditions;
        }
    }

    frontAndBack
    {
        category        wall;
        type            slip;
        patches         (frontAndBack);
        values
        {
            &#36;/initialConditions;
        }
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/createzerodirectory/">createZeroDirectory</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/leftSolid/caseProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/leftSolid/caseProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>重启时刻不符合预期</td><td>核对 startFrom、startTime 与已存在的时间目录，避免旧结果影响首次运行。</td></tr><tr><td>时间目录增长过快</td><td>结合 writeControl、writeInterval、purgeWrite 与函数对象输出，先估计磁盘占用。</td></tr><tr><td>开启 adjustTimeStep 仍不生效</td><td>确认求解器确实实现对应时间步控制；字典可解析不代表每个键被使用。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
