---
title: "potentialDict"
layout: reference
description: "分子动力学势函数配置，定义粒子间相互作用、截断距离等。"
dictionary: true
cms_slug: "dictionary-potentialdict"
---

<p>分子动力学势函数配置，定义粒子间相互作用、截断距离等。</p><p>位置：<code>system/potentialDict</code></p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</summary><p>周期水分子体系使用分子间势计算相互作用，potentialDict 把短程作用与静电作用分别配置。</p>
<ul>
<li>氧位点之间采用 Lennard–Jones 势，<code>sigma 3.154e-10</code> m 给出长度尺度，<code>epsilon 1.07690722e-21</code> J 给出能量尺度。</li>
<li><code>rCut 1e-9</code> 将这组作用截断在 1 nm，<code>rMin</code>、<code>dr</code> 控制查表区间和分辨率，<code>writeTables yes</code> 输出势能表。</li>
<li>静电部分使用 dampedCoulomb，<code>alpha 2e9</code> 控制阻尼，<code>shiftedForce</code> 处理截断处的力连续性。</li>
<li><code>potentialEnergyLimit 1e-18</code> 配合 removalOrder 处理初始化时能量过高的分子重叠。</li>
<li>tether 中为 O 定义弹簧参数，只有被标记为系留位点的分子才使用该约束；外加重力为零。</li>
</ul>
<p>修改势参数后先检查导出的势能及力曲线，再比较平衡密度、温度和能量波动。</p>
<p><a href="/assets/examples/v2512/potentialdict/1-potentialDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/potentialDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      potentialDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Subdictionaries specifying types of intermolecular potential.
// Sub-sub dictionaries specify the potentials themselves.

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Removal order

// This is the order in which to remove overlapping pairs if more than one
// type of molecule is present.  The most valuable molecule type is at the
// right hand end, the molecule that will be removed 1st is 1st on the list.
// Not all types need to be present, a molecule that is not present is
// automatically less valuable than any on the list.  For molecules of the
// same type there is no control over which is removed.

removalOrder ( water );

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Potential Energy Limit

// Maximum permissible pair energy allowed at startup.  Used to remove
// overlapping molecules created during preprocessing.

potentialEnergyLimit 1e-18;

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Pair potentials

// If a pair are not present here it is assumed that they do not interact.

// Electrostatic pair interactions are not listed here - they are handled
// separately.

// If there are r different type of molecules, and a pair force is required
// between all combinations, then there are C = r(r+1)/2 combinations,
// i.e. for r = {1,2,3,4}, C = {1,3,6,10} (sum of triangular numbers).

// Pair potentials are specified by the combination of their ids,
// for MOLA and MOLB, &quot;MOLA-MOLB&quot; OR &quot;MOLB-MOLA&quot; is acceptable
// (strictly OR, both or neither will throw an error)

pair
{
    O-O
    {
        pairPotential   lennardJones;
        rCut            1.0e-9;
        rMin            0.1e-9;
        dr              1e-13;
        lennardJonesCoeffs
        {
            sigma       3.154e-10;
            epsilon     1.07690722e-21;
        }
        energyScalingFunction   noScaling;
        writeTables     yes;
    }

    electrostatic
    {
        pairPotential   dampedCoulomb;
        rCut            1e-9;
        rMin            2e-11;
        dr              2e-12;
        dampedCoulombCoeffs
        {
            alpha       2e9;
        }
        energyScalingFunction   shiftedForce;
        writeTables     yes;
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Tethering Potentials

tether
{
    O
    {
        tetherPotential restrainedHarmonicSpring;
        restrainedHarmonicSpringCoeffs
        {
            springConstant  0.277;
            rR              1.2e-9;
        }
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// External Forces

// Bulk external forces (namely gravity) will be specified as forces rather
// than potentials to allow their direction to be controlled.

external
{
    gravity             (0 0 0);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</summary><p>氩原子算例以 Ar–Ar 对势描述分子间作用，并输出查表结果供检查。</p>
<ul>
<li><code>pairPotential maitlandSmith</code> 选择 Maitland–Smith 势，<code>m 13</code>、<code>gamma 7.5</code> 控制势形状。</li>
<li><code>rm 0.3756e-9</code> m 和 <code>epsilon 1.990108438e-21</code> J 设置长度与能量尺度。</li>
<li><code>rCut 1e-9</code>、<code>rMin 0.15e-9</code>、<code>dr 5e-14</code> 给出势表范围与步长；doubleSigmoid 用 0.9 nm、0.97 nm 附近的过渡平滑处理截断。</li>
<li>本算例 Ar 电荷为零，文件中保留的静电配置对这些中性粒子的库仑作用为零；tether/O 也只有对应的系留位点才使用。</li>
</ul>
<p><code>gravity (0 0 0)</code> 关闭外重力。改变势参数前后可比较势阱位置、势阱深度和体系平衡状态。</p>
<p><a href="/assets/examples/v2512/potentialdict/2-potentialDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/potentialDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
n|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      potentialDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Subdictionaries specifying types of intermolecular potential.
// Sub-sub dictionaries specify the potentials themselves.

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Removal order

// This is the order in which to remove overlapping pairs if more than one
// type of molecule is present.  The most valuable molecule type is at the
// right hand end, the molecule that will be removed 1st is 1st on the list.
// Not all types need to be present, a molecule that is not present is
// automatically less valuable than any on the list.  For molecules of the
// same type there is no control over which is removed.

removalOrder ( Ar );

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Potential Energy Limit

// Maximum permissible pair energy allowed at startup.  Used to remove
// overlapping molecules created during preprocessing.

potentialEnergyLimit 1e-18;

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Pair potentials

// If there are r different type of molecules, and a pair force is required
// between all combinations, then there are C = r(r+1)/2 combinations,
// i.e. for r = {1,2,3,4}, C = {1,3,6,10} (sum of triangular numbers).

// Pair potentials are specified by the combination of their ids,
// for MOLA and MOLB, &quot;MOLA-MOLB&quot; OR &quot;MOLB-MOLA&quot; is acceptable
// (strictly OR, both or neither is an error)

pair
{
    Ar-Ar
    {
        pairPotential   maitlandSmith;
        rCut            1.0e-9;
        rMin            0.15e-9;
        dr              5e-14;
        maitlandSmithCoeffs
        {
            m           13.0;
            gamma       7.5;
            rm          0.3756e-9;
            epsilon     1.990108438e-21;
        }
        energyScalingFunction   doubleSigmoid;
        doubleSigmoidCoeffs
        {
            shift1      0.9e-9;
            scale1      0.3e11;
            shift2      0.97e-9;
            scale2      1.2e11;
        }
        writeTables     yes;
    }

    electrostatic
    {
        pairPotential   dampedCoulomb;
        rCut            1.0e-9;
        rMin            0.1e-9;
        dr              2e-12;
        dampedCoulombCoeffs
        {
            alpha       2e9;
        }
        energyScalingFunction   shiftedForce;
        writeTables     yes;
    }
}

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// Tethering Potentials

tether
{
    O
    {
        tetherPotential restrainedHarmonicSpring;
        restrainedHarmonicSpringCoeffs
        {
            springConstant  0.277;
            rR              1.2e-9;
        }
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
// External Forces

// Bulk external forces (namely gravity) will be specified as forces rather
// than potentials to allow their direction to be controlled.

external
{
    gravity             (0 0 0);
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mdfoam/">mdFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
