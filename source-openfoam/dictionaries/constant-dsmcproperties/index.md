---
title: "constant/dsmcProperties · dsmcProperties"
layout: reference
description: "DSMC 模拟的分子物种、碰撞和壁面相互作用模型。DSMC 的统计粒子数、单元尺寸和时间步需与平均自由程、碰撞时间及统计误差一起评估；它不是连续介质湍流模型。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>DSMC 模拟的分子物种、碰撞和壁面相互作用模型。DSMC 的统计粒子数、单元尺寸和时间步需与平均自由程、碰撞时间及统计误差一起评估；它不是连续介质湍流模型。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>nEquivalentParticles</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // General Properties ~~~~~~~~~~~~~~~~~~</td></tr><tr><td>WallInteractionModel</td><td>Wall Interaction Model ~~~~~~~~~~~~~~~~~~~~~~</td></tr><tr><td>BinaryCollisionModel</td><td>Binary Collision Model ~~~~~~~~~~~~~~~~~~~~~~</td></tr><tr><td>InflowBoundaryModel</td><td>Inflow Boundary Model ~~~~~~~~~~~~~~~~~~~~~</td></tr><tr><td>typeIdList</td><td>Molecular species ~~~~~~~~~~~~~~~~~</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · discreteMethods/dsmcFoam/supersonicCorner</h3><p>原始路径：<code>tutorials/discreteMethods/dsmcFoam/supersonicCorner/constant/dsmcProperties</code>；求解器：<code>dsmcFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner/constant/dsmcProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/dsmcproperties/1-dsmcProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


// General Properties
// ~~~~~~~~~~~~~~~~~~

nEquivalentParticles            1.2e12;


// Wall Interaction Model
// ~~~~~~~~~~~~~~~~~~~~~~

WallInteractionModel            MaxwellianThermal;


// Binary Collision Model
// ~~~~~~~~~~~~~~~~~~~~~~

BinaryCollisionModel            VariableHardSphere;

VariableHardSphereCoeffs
{
    Tref        273;
}


// Inflow Boundary Model
// ~~~~~~~~~~~~~~~~~~~~~

InflowBoundaryModel             FreeStream;

FreeStreamCoeffs
{
    numberDensities
    {
        Ar      1.0e20;
    };
}


// Molecular species
// ~~~~~~~~~~~~~~~~~

typeIdList                      (Ar);

moleculeProperties
{
    Ar
    {
        mass                            66.3e-27;
        diameter                        4.17e-10;
        internalDegreesOfFreedom        0;
        omega                           0.81;
    }
}


// ************************************************************************* //</code></pre><h3>示例 2 · discreteMethods/dsmcFoam/freeSpacePeriodic</h3><p>原始路径：<code>tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic/constant/dsmcProperties</code>；求解器：<code>dsmcFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic/constant/dsmcProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/dsmcproperties/2-dsmcProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


// General Properties
// ~~~~~~~~~~~~~~~~~~

nEquivalentParticles            1e12;


// Wall Interaction Model
// ~~~~~~~~~~~~~~~~~~~~~~

WallInteractionModel            SpecularReflection;


// Binary Collision Model
// ~~~~~~~~~~~~~~~~~~~~~~

BinaryCollisionModel            LarsenBorgnakkeVariableHardSphere;

LarsenBorgnakkeVariableHardSphereCoeffs
{
    Tref                        273;
    relaxationCollisionNumber   5.0;
}


// Inflow Boundary Model
// ~~~~~~~~~~~~~~~~~~~~~
InflowBoundaryModel             none;


// Molecular species
// ~~~~~~~~~~~~~~~~~

typeIdList                      (N2 O2);

moleculeProperties
{
    N2
    {
        mass                            46.5e-27;
        diameter                        4.17e-10;
        internalDegreesOfFreedom        2;
        omega                           0.74;
    }

    O2
    {
        mass                            53.12e-27;
        diameter                        4.07e-10;
        internalDegreesOfFreedom        2;
        omega                           0.77;
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · discreteMethods/dsmcFoam/freeSpaceStream</h3><p>原始路径：<code>tutorials/discreteMethods/dsmcFoam/freeSpaceStream/constant/dsmcProperties</code>；求解器：<code>dsmcFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpaceStream/constant/dsmcProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/dsmcproperties/3-dsmcProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpaceStream">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      dsmcProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //


// General Properties
// ~~~~~~~~~~~~~~~~~~

nEquivalentParticles            1e12;


// Wall Interaction Model
// ~~~~~~~~~~~~~~~~~~~~~~

WallInteractionModel            MaxwellianThermal;


// Binary Collision Model
// ~~~~~~~~~~~~~~~~~~~~~~

BinaryCollisionModel            LarsenBorgnakkeVariableHardSphere;

LarsenBorgnakkeVariableHardSphereCoeffs
{
    Tref                        273;
    relaxationCollisionNumber   5.0;
}


// Inflow Boundary Model
// ~~~~~~~~~~~~~~~~~~~~~

InflowBoundaryModel             FreeStream;

FreeStreamCoeffs
{
    numberDensities
    {
        N2      0.777e20;
        O2      0.223e20;
    };
}


// Molecular species
// ~~~~~~~~~~~~~~~~~

typeIdList                      (N2 O2);

moleculeProperties
{
    N2
    {
        mass                            46.5e-27;
        diameter                        4.17e-10;
        internalDegreesOfFreedom        2;
        omega                           0.74;
    }

    O2
    {
        mass                            53.12e-27;
        diameter                        4.07e-10;
        internalDegreesOfFreedom        2;
        omega                           0.77;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/dsmcfoam/">dsmcFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/dsmcProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/dsmcProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
