---
title: "system/optimisationDict · optimisationDict"
layout: reference
description: "定义伴随优化的目标函数、设计变量、优化器与更新策略。一个优化迭代通常包含正问题、伴随问题和设计更新；减少单次残差并不等同于目标函数改善。结合算例的 Allrun 与目标函数输出理解优化循环。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>定义伴随优化的目标函数、设计变量、优化器与更新策略。一个优化迭代通常包含正问题、伴随问题和设计更新；减少单次残差并不等同于目标函数改善。结合算例的 Allrun 与目标函数输出理解优化循环。</p><figure><img src="/assets/diagrams/reference-4.svg" alt="数值方法配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>optimisationManager</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>objectives</td><td>manage objectives</td></tr><tr><td>ATCModel</td><td>ATC treatment</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/optimisationDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/optimisationDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/optimisationdict/1-optimisationDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      optimisationDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

optimisationManager singleRun;

primalSolvers
{
    op1
    {
        active                 true;
        type                   incompressible;
        solver                 simple;
        solutionControls
        {
            nIters 3000;
            residualControl
            {
                &quot;p.*&quot;       5.e-7;
                &quot;U.*&quot;       5.e-7;
            }
        }
    }
}

adjointManagers
{
    adjManager1
    {
        primalSolver             op1;
        adjointSolvers
        {
            as1
            {
                // choose adjoint solver
                //----------------------
                active                 false;
                type                   incompressible;
                solver                 adjointSimple;
                computeSensitivities   false;
                // manage objectives
                //------------------
                objectives
                {
                    type  incompressible;
                    objectiveNames
                    {
                        losses
                        {
                            weight          1.; 
                            type            PtLosses;
                            patches         (inlet &quot;outlet.*&quot;);
                            normalise       true;
                        }
                    }
                }
                // ATC treatment
                //--------------
                ATCModel
                {
                    ATCModel        standard;
                }
                // solution control
                //------------------
                solutionControls
                {
                    nIters 300;
                    residualControl
                    {
                        &quot;pa.*&quot;       5.e-7;
                        &quot;Ua.*&quot;       5.e-7;
                    }
                }
            }
        }
    }
}

// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar/system/optimisationDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar/system/optimisationDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/optimisationdict/2-optimisationDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      optimisationDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

optimisationManager     singleRun;

primalSolvers
{
    p1
    {
        active                 true;
        type                   incompressible;
        solver                 simple;
        solutionControls
        {
            nIters 3000;
            residualControl
            {
                &quot;p.*&quot;       1.e-7;
                &quot;U.*&quot;       1.e-7;
            }
        }
    }
}

adjointManagers
{
    am1
    {
        primalSolver             p1;
        adjointSolvers
        {
            as1
            {
                // choose adjoint solver
                //----------------------
                active                 true;
                type                   incompressible;
                solver                 adjointSimple;

                // manage objectives
                //------------------
                objectives
                {
                    type                incompressible;
                    objectiveNames
                    {
                        losses
                        {
                            weight          1;
                            type            PtLosses;
                            patches         (Inlet Outlet);
                        }
                    }
                }

                // ATC treatment
                //--------------
                ATCModel
                {
                    ATCModel        standard;
                }

                // solution control
                //------------------
                solutionControls
                {
                    nIters 3000;
                    residualControl
                    {
                        &quot;pa.*&quot;       1.e-7;
                        &quot;Ua.*&quot;       1.e-7;
                    }
                }
            }
        }
    }
}

optimisation
{
    designVariables
    {
        sensitivityType surfacePoints;
        patches         (lower upper);
    }
}

// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD</h3><p>原始路径：<code>tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD/system/optimisationDict</code>；求解器：<code>adjointOptimisationFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD/system/optimisationDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/optimisationdict/3-optimisationDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      optimisationDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

optimisationManager     steadyOptimisation;

primalSolvers
{
    p1
    {
        active                 true;
        type                   incompressible;
        solver                 simple;
        solutionControls
        {
            nIters 3000;
            residualControl
            {
                &quot;p.*&quot;       1.e-7;
                &quot;U.*&quot;       1.e-7;
            }
        }
    }
}

adjointManagers
{
    am1
    {
        primalSolver             p1;
        adjointSolvers
        {
            as1
            {
                // choose adjoint solver
                //----------------------
                active                 true;
                type                   incompressible;
                solver                 adjointSimple;

                // manage objectives
                //------------------
                objectives
                {
                    type                incompressible;
                    objectiveNames
                    {
                        losses
                        {
                            weight          1;
                            type            PtLosses;
                        }
                    }
                }

                // ATC treatment
                //--------------
                ATCModel
                {
                    ATCModel        standard;
                }

                // solution control
                //------------------
                solutionControls
                {
                    nIters 3000;
                    residualControl
                    {
                        &quot;pa.*&quot;       1.e-7;
                        &quot;Ua.*&quot;       1.e-7;
                    }
                }
            }
        }
    }
}

optimisation
{
    designVariables
    {
        type            shape;
        shapeType       volumetricBSplines;
        sensitivityType shapeFI;
        patches         (lower upper);
        maxInitChange   2.e-3;
    }
    updateMethod
    {
        method  steepestDescent;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/adjointoptimisationfoam/">adjointOptimisationFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/optimisationDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/optimisationDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数不是无条件提高精度的办法。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
