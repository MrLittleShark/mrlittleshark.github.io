---
title: "optimisationDict"
layout: reference
description: "定义伴随优化的目标函数、设计变量、优化器与更新策略。"
dictionary: true
cms_slug: "dictionary-optimisationdict"
---

<p>定义伴随优化的目标函数、设计变量、优化器与更新策略。</p><p>位置：<code>system/optimisationDict</code></p><h2>配置实例</h2><p>incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval 中的 optimisationDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      optimisationDict;
}

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
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>method</td><td>所采用的分区、插值或模型方法；含义由该字典的读取程序决定。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval</summary><p>topology/reEval 用已有设计重新计算原始流场，重点是评估该几何下的总压损失。</p>
<ul>
<li><code>optimisationManager singleRun</code> 执行一次计算流程，原始求解器 op1 使用不可压缩 SIMPLE。</li>
<li><code>nIters 3000</code> 限定最大原始迭代次数，p、U 的 residualControl 均为 <code>5e-7</code>。</li>
<li>伴随求解器 as1 的 <code>active false</code> 和 <code>computeSensitivities false</code> 关闭伴随求解与敏感度计算。</li>
<li>目标 <code>PtLosses</code> 在 inlet 与匹配 outlet.* 的出口之间计算总压损失，<code>normalise true</code> 采用归一化目标。</li>
</ul>
<p>重新比较两个设计时保持入口工况和目标定义一致，并确认各自原始流场已经达到所设残差要求。</p>
<p><a href="/assets/examples/v2512/optimisationdict/1-optimisationDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval/system/optimisationDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/1_Inlet_2_Outlet/levelSet/R_05x_NB_01x/reEval">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar</summary><p>S 形弯管的 sensitivityMaps 算例求解原始流场和伴随场，并在上下壁面输出总压损失的形状敏感度。</p>
<ul>
<li><code>singleRun</code> 执行一次原始—伴随流程；原始 simple 与伴随 adjointSimple 都允许最多 3000 次迭代。</li>
<li>两组 residualControl 均设为 <code>1e-7</code>，分别控制 p、U 和 pa、Ua 的停止要求。</li>
<li><code>PtLosses</code> 的 <code>patches (Inlet Outlet)</code> 指定测量总压损失的边界，名称大小写需与网格一致。</li>
<li><code>sensitivityType surfacePoints</code>、<code>patches (lower upper)</code> 把设计敏感度输出到上下壁面点。</li>
</ul>
<p>阅读结果时将敏感度符号与采用的表面法向、目标函数方向对应起来，再决定局部壁面移动方向。</p>
<p><a href="/assets/examples/v2512/optimisationdict/2-optimisationDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar/system/optimisationDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/sensitivityMaps/sbend/laminar">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD</summary><p>losses_sD 将 S 形弯管的总压损失作为优化目标，通过 B 样条参数控制上下壁面的形状。</p>
<ul>
<li><code>optimisationManager steadyOptimisation</code> 开启多轮稳态优化，每轮需要原始与伴随流场。</li>
<li>simple 和 adjointSimple 的 <code>nIters 3000</code>、残差阈值 <code>1e-7</code> 控制每轮方程求解。</li>
<li><code>type shape</code>、<code>shapeType volumetricBSplines</code> 以体积 B 样条控制点描述网格变形，<code>patches (lower upper)</code> 指定可调整壁面。</li>
<li><code>sensitivityType shapeFI</code> 选择形状敏感度计算方法，<code>maxInitChange 2e-3</code> 限制初始设计改变量尺度。</li>
<li><code>method steepestDescent</code> 沿目标梯度的下降方向更新设计。</li>
</ul>
<p>优化步长影响目标下降与网格质量。出现明显网格畸变时，先减小允许的形状改变量，再比较每轮目标值与最差网格指标。</p>
<p><a href="/assets/examples/v2512/optimisationdict/3-optimisationDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD/system/optimisationDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/shapeOptimisation/sbend/laminar/opt/unconstrained/losses/SD">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/adjointoptimisationfoam/">adjointOptimisationFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数其作用随网格质量和解的光滑程度变化，可通过细化对比评估。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
