---
title: "system/potentialDict · potentialDict"
layout: reference
description: "分子动力学势函数配置，定义粒子间相互作用、截断距离等。截断与平滑方式会影响能量守恒和压力估计，应与采用的分子模型文献和教程配套。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>分子动力学势函数配置，定义粒子间相互作用、截断距离等。截断与平滑方式会影响能量守恒和压力估计，应与采用的分子模型文献和教程配套。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>sigma</td><td>常见为表面张力系数，但在电磁模型中可表示电导率；以模型与量纲为准。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>removalOrder</td><td>Not all types need to be present, a molecule that is not present is automatically less valuable than any on the list.  For molecules of the same type there is no control over which is removed.</td></tr><tr><td>potentialEnergyLimit</td><td>Potential Energy Limit Maximum permissible pair energy allowed at startup.  Used to remove overlapping molecules created during preprocessing.</td></tr><tr><td>pair</td><td>Pair potentials are specified by the combination of their ids, for MOLA and MOLB, &quot;MOLA-MOLB&quot; OR &quot;MOLB-MOLA&quot; is acceptable (strictly OR, both or neither will throw an error)</td></tr><tr><td>tether</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Tethering Potentials</td></tr><tr><td>external</td><td>External Forces Bulk external forces (namely gravity) will be specified as forces rather than potentials to allow their direction to be controlled.</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/potentialDict</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater/system/potentialDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/potentialdict/1-potentialDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeWater">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon</h3><p>原始路径：<code>tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/potentialDict</code>；求解器：<code>mdEquilibrationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon/system/potentialDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/potentialdict/2-potentialDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/discreteMethods/molecularDynamics/mdEquilibrationFoam/periodicCubeArgon">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/mdfoam/">mdFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/potentialDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/potentialDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
