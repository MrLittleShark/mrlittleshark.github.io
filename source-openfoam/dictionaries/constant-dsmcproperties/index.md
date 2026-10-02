---
title: "dsmcProperties"
layout: reference
description: "DSMC 模拟的分子物种、碰撞和壁面相互作用模型。"
dictionary: true
cms_slug: "dictionary-dsmcproperties"
---

<p>DSMC 模拟的分子物种、碰撞和壁面相互作用模型。</p><p>位置：<code>constant/dsmcProperties</code></p><h2>配置实例</h2><p>discreteMethods/dsmcFoam/supersonicCorner 中的 dsmcProperties：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      dsmcProperties;
}

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
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/dsmcFoam/supersonicCorner</summary><p><code>supersonicCorner</code> 的工作气体为单原子氩。这个文件定义模拟粒子的统计权重、分子碰撞规律以及壁面与入口模型。</p>
<ul>
<li><code>nEquivalentParticles 1.2e12</code> 使一个计算粒子代表 \(1.2\times10^{12}\) 个氩原子；降低该值会增加抽样粒子数量。</li>
<li><code>VariableHardSphere</code> 使用可变硬球碰撞模型，<code>Tref 273</code> 是碰撞参考温度；<code>omega 0.81</code> 控制碰撞截面随相对速度变化的规律。</li>
<li><code>mass 66.3e-27</code> kg 与 <code>diameter 4.17e-10</code> m 描述氩原子的质量和参考碰撞直径。<code>internalDegreesOfFreedom 0</code> 与单原子气体相符。</li>
<li><code>MaxwellianThermal</code> 按壁面温度重新抽样反射速度，体现与壁面热交换；墙温来自配套边界场。</li>
<li><code>FreeStream</code> 配合 <code>Ar 1e20</code> 持续补充来流，和初始化文件中的物种及数密度一致。</li>
</ul>
<p>要比较壁面热适应效应，可与镜面反射模型对照；要降低统计噪声，可增加粒子数和采样时长。改变碰撞直径后，平均自由程会随之改变，网格尺度也应重新检查。</p>
<p><a href="/assets/examples/v2512/dsmcproperties/1-dsmcProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner/constant/dsmcProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/supersonicCorner">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/dsmcFoam/freeSpacePeriodic</summary><p><code>freeSpacePeriodic</code> 使用氮氧双原子混合气，在周期区域中观察碰撞与能量分配。</p>
<ul>
<li><code>nEquivalentParticles 1e12</code> 给出统计权重；<code>typeIdList (N2 O2)</code> 定义可出现的两种分子。</li>
<li>两种分子的 <code>internalDegreesOfFreedom</code> 均为 2，对应这里采用的转动内能自由度。质量分别为 <code>46.5e-27</code>、<code>53.12e-27</code> kg。</li>
<li><code>LarsenBorgnakkeVariableHardSphere</code> 在可变硬球碰撞基础上加入平动与内能再分配。<code>relaxationCollisionNumber 5.0</code> 对应模型中 \(1/5\) 的内能再分配抽样概率。</li>
<li><code>Tref 273</code>、氮气 <code>omega 0.74</code> 和氧气 <code>omega 0.77</code> 决定各物种的碰撞温度依赖。</li>
<li><code>InflowBoundaryModel none</code> 与周期体系配合；<code>SpecularReflection</code> 是遇到实体壁面时使用的镜面反射模型，周期面继续按周期拓扑处理。</li>
</ul>
<p>可改变 <code>relaxationCollisionNumber</code> 比较内能向平衡状态靠近的速度。调整模拟粒子权重时，保持真实数密度和分子物性不变，以单独评估统计分辨率。</p>
<p><a href="/assets/examples/v2512/dsmcproperties/2-dsmcProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic/constant/dsmcProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpacePeriodic">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · discreteMethods/dsmcFoam/freeSpaceStream</summary><p><code>freeSpaceStream</code> 把氮氧混合气持续送入计算域，适合检查入口统计与下游流场是否保持一致。</p>
<ul>
<li><code>FreeStreamCoeffs/numberDensities</code> 给出氮气 <code>0.777e20</code>、氧气 <code>0.223e20</code> m⁻³；入口速度和温度还需与配套边界场一致。</li>
<li><code>nEquivalentParticles 1e12</code> 将真实分子流率转化为有限数量的模拟粒子注入事件。</li>
<li><code>LarsenBorgnakkeVariableHardSphere</code> 处理碰撞及内能交换，<code>relaxationCollisionNumber 5.0</code> 设置内能交换的统计频率。</li>
<li><code>internalDegreesOfFreedom 2</code> 给两种双原子分子分配转动自由度。<code>mass</code>、<code>diameter</code>、<code>omega</code> 分别控制惯性、参考碰撞尺度和速度依赖。</li>
<li><code>MaxwellianThermal</code> 指定实体壁面的热反射处理。开放入口与出口由对应边界类型决定。</li>
</ul>
<p>增大入口数密度后，应同时比较入口与出口的分子数流率。延长统计时段可减小抽样噪声；提高流速后则应重新选择粒子跟踪时间步。</p>
<p><a href="/assets/examples/v2512/dsmcproperties/3-dsmcProperties.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpaceStream/constant/dsmcProperties">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/dsmcFoam/freeSpaceStream">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/dsmcfoam/">dsmcFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>模型或类型名称未识别：<code>Unknown model / Unknown type</code></td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
