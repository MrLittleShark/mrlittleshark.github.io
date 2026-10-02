---
title: "fvSolution"
layout: reference
description: "设置线性方程求解器、收敛容差、压力速度耦合和欠松弛。"
dictionary: true
cms_slug: "dictionary-fvsolution"
---

<p>设置线性方程求解器、收敛容差、压力速度耦合和欠松弛。</p><p>位置：<code>system/fvSolution</code></p><figure class="wolf-figure"><img src="/assets/wolf/wolf-pimple-pressure-coupling.png" alt="PIMPLE 外校正与 PISO 内校正" loading="lazy"><figcaption><strong>PIMPLE 外校正与 PISO 内校正</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 96 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure><h2>fvSolution 控制代数求解和压力校正</h2>
<p><code>system/fvSolution</code> 主要包含三类内容：各场的线性求解器、压力—速度耦合算法，以及需要时使用的松弛因子。下面是一份适用于 <code>icoFoam</code> 方腔的主体配置，放在 <code>FoamFile</code> 文件头之后：</p>
<pre><code class="language-foam">solvers
{
    p
    {
        solver PCG;
        preconditioner DIC;
        tolerance 1e-6;
        relTol 0.05;
    }
    pFinal
    {
        $p;
        relTol 0;
    }
    U
    {
        solver smoothSolver;
        smoother symGaussSeidel;
        tolerance 1e-5;
        relTol 0;
    }
}
PISO
{
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    pRefCell 0;
    pRefValue 0;
}
</code></pre>
<h3>每次线性求解何时结束</h3>
<p><code>solver</code> 选择算法，<code>preconditioner</code> 选择预条件器，<code>smoother</code> 选择平滑方法。PCG 适用于相应的对称正定系统；有对流项的非对称系统可使用 <code>PBiCGStab</code> 等算法。</p>
<p><code>tolerance</code> 是归一化残差的绝对阈值，<code>relTol</code> 是相对本次初始残差的比例。初始残差为 0.01 时，<code>relTol 0.05</code> 对应 0.0005。满足相应停止条件后，本次线性求解结束；还可用 <code>maxIter</code> 限制最大迭代次数。</p>
<p><code>pFinal</code> 先通过 <code>$p;</code> 继承压力配置，再关闭相对提前停止条件。最终校正采用更严格的压力求解，前面的校正可以较快完成。它使用同一个压力场。</p>
<h3>校正次数怎么理解</h3>
<p><code>nCorrectors 2</code> 表示每步做两次压力校正。<code>nNonOrthogonalCorrectors 0</code> 表示每次压力校正只做基础求解；取 1 则再增加一次非正交修正。封闭方腔需要压力基准，<code>pRefCell</code> 与 <code>pRefValue</code> 给出参考单元和参考压力。</p>
<p>对于 <code>simpleFoam</code>，使用 <code>SIMPLE</code> 子字典；对于 <code>pimpleFoam</code>，使用 <code>PIMPLE</code>。以下片段替换算法控制部分，用在完整 <code>pimpleFoam</code> 算例中：</p>
<pre><code class="language-foam">PIMPLE
{
    momentumPredictor yes;
    nOuterCorrectors 3;
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
}
</code></pre>
<p>每个时间步做三轮外校正，每轮做两次压力校正。外循环允许动量系数与模型重复更新，适合需要更充分非线性耦合的情况。</p>
<h3>稳态松弛</h3>
<p>稳态 SIMPLE 算例常在文件末尾加入：</p>
<pre><code class="language-foam">relaxationFactors
{
    fields
    {
        p 0.3;
    }
    equations
    {
        U 0.7;
        "(k|epsilon)" 0.7;
    }
}
</code></pre>
<p><code>fields</code> 控制求解后场值的更新，<code>equations</code> 控制求解前矩阵的松弛。较小因子一般使更新更平缓，也可能增加迭代次数。正则键应匹配实际模型的场名。比较松弛因子时，观察达到相同目标量精度所需的耗时。</p>
<p><code>residualControl</code> 用于 SIMPLE 或 PIMPLE 的外层收敛判断，<code>solvers</code> 的容差用于内层线性求解。二者放在不同层次，分别影响耦合迭代与每次矩阵求解。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p><code>icoFoam</code> 在每个时间步使用 PISO 修正压力和速度。这里同时规定线性方程的求解方式和一次时间步内的校正次数。</p>
<ul>
<li>压力 <code>p</code> 使用 <code>PCG</code>、<code>DIC</code>，绝对容差 <code>1e-6</code>，相对容差 <code>0.05</code>。普通压力求解可以在残差降到初始值的 5% 时结束，也可以因达到绝对容差而结束。</li>
<li><code>pFinal</code> 通过 <code>$p</code> 继承压力设置，再令 <code>relTol 0</code>，使最后一次压力求解以绝对容差作为停止要求。</li>
<li>速度 <code>U</code> 使用 <code>smoothSolver</code>、<code>symGaussSeidel</code>，容差为 <code>1e-5</code>，<code>relTol 0</code>。</li>
<li><code>PISO/nCorrectors 2</code> 在每个时间步执行两次压力校正；<code>nNonOrthogonalCorrectors 0</code> 适用于配套正交网格，无额外非正交校正。</li>
<li>方腔压力边界均为梯度条件，<code>pRefCell 0</code>、<code>pRefValue 0</code> 固定一个压力参考，消除任意常数。</li>
</ul>
<p>网格改变后先检查非正交性，再决定额外校正次数。<code>tolerance</code> 是线性残差的停止阈值，<code>writePrecision</code> 是文件输出位数，二者由不同字典管理。</p>
<p><a href="/assets/examples/v2512/fvsolution/1-fvSolution.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/fvSolution">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSolution;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solvers
{
    p
    {
        solver          PCG;
        preconditioner  DIC;
        tolerance       1e-06;
        relTol          0.05;
    }

    pFinal
    {
        $p;
        relTol          0;
    }

    U
    {
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-05;
        relTol          0;
    }
}

PISO
{
    nCorrectors     2;
    nNonOrthogonalCorrectors 0;
    pRefCell        0;
    pRefValue       0;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p>后台阶算例用 SIMPLE 外迭代求稳态流动；每轮外迭代内部还要求解压力、速度和湍流方程。</p>
<ul>
<li>压力使用 <code>GAMG</code> 多重网格求解，<code>tolerance 1e-6</code>、<code>relTol 0.1</code>，允许单轮线性求解先降到初始残差的十分之一。</li>
<li><code>"(U|k|epsilon|omega|f|v2)"</code> 用一个正则表达式共用求解器设置，实际被读取的字段由所选湍流模型决定。</li>
<li><code>SIMPLE/consistent yes</code> 开启一致性压力速度修正，即 SIMPLEC 风格处理；<code>nNonOrthogonalCorrectors 0</code> 表示没有额外非正交校正。</li>
<li><code>residualControl</code> 把外迭代停止阈值设为压力 <code>1e-2</code>、速度和湍流变量 <code>1e-3</code>。它们与上面每次线性求解的 <code>tolerance</code> 分别控制不同层次。</li>
<li><code>relaxationFactors/equations</code> 中 <code>U 0.9</code> 和 <code>".*" 0.9</code> 对方程进行欠松弛，减缓相邻外迭代的变化。</li>
</ul>
<p>如果回流区随迭代持续变化，可减小松弛系数并检查边界和网格。达到残差停止条件后，还应看回流长度、压降等目标量是否稳定，以决定阈值是否足够。</p>
<p><a href="/assets/examples/v2512/fvsolution/2-fvSolution.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/fvSolution">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSolution;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solvers
{
    p
    {
        solver          GAMG;
        tolerance       1e-06;
        relTol          0.1;
        smoother        GaussSeidel;
    }

    &quot;(U|k|epsilon|omega|f|v2)&quot;
    {
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-05;
        relTol          0.1;
    }
}

SIMPLE
{
    nNonOrthogonalCorrectors 0;
    consistent      yes;

    residualControl
    {
        p               1e-2;
        U               1e-3;
        &quot;(k|epsilon|omega|f|v2)&quot; 1e-3;
    }
}

relaxationFactors
{
    equations
    {
        U               0.9; // 0.9 is more stable but 0.95 more convergent
        &quot;.*&quot;            0.9; // 0.9 is more stable but 0.95 more convergent
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</summary><p>水柱塌落时需要同时更新体积分数、压力和速度。这个 <code>fvSolution</code> 使用一轮 PIMPLE 外校正，并在其中安排界面与压力校正。</p>
<ul>
<li><code>"alpha.water.*"</code> 匹配水体积分数相关求解条目。<code>nAlphaCorr 2</code> 执行两次相分数校正，<code>nAlphaSubCycles 1</code> 表示不把主时间步再拆成多个相分数子步。</li>
<li><code>cAlpha 1</code> 设置界面压缩系数，<code>MULESCorr yes</code> 使用 MULES 修正，<code>nLimiterIter 5</code> 控制限制器迭代次数。它们共同影响界面锐度与有界性。</li>
<li><code>p_rgh</code> 的容差为 <code>1e-7</code>、<code>relTol 0.05</code>；<code>p_rghFinal</code> 继承后将 <code>relTol</code> 设为 0，用较严格的最后一次压力求解收尾。</li>
<li><code>PIMPLE/nOuterCorrectors 1</code> 每步一轮外校正，<code>nCorrectors 3</code> 为该轮设置三次压力校正，<code>nNonOrthogonalCorrectors 0</code> 不增加额外非正交求解。</li>
<li><code>momentumPredictor no</code> 跳过单独的动量预测求解步骤，速度仍在压力速度耦合过程中更新。<code>relaxationFactors/equations/".*" 1</code> 不再通过小于 1 的系数增强欠松弛；方程松弛仍会检查和修正对角占优性。</li>
</ul>
<p>时间步增大后，可比较增加外校正次数对耦合误差的影响；相分数子循环主要细化界面输运时间步。改变这些设置时，同时比较水体积、前沿位置与每步成本。</p>
<p><a href="/assets/examples/v2512/fvsolution/3-fvSolution.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSolution">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvSolution;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

solvers
{
    &quot;alpha.water.*&quot;
    {
        nAlphaCorr      2;
        nAlphaSubCycles 1;
        cAlpha          1;

        MULESCorr       yes;
        nLimiterIter    5;

        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-8;
        relTol          0;
    }

    &quot;pcorr.*&quot;
    {
        solver          PCG;
        preconditioner  DIC;
        tolerance       1e-5;
        relTol          0;
    }

    p_rgh
    {
        solver          PCG;
        preconditioner  DIC;
        tolerance       1e-07;
        relTol          0.05;
    }

    p_rghFinal
    {
        $p_rgh;
        relTol          0;
    }

    U
    {
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-06;
        relTol          0;
    }
}

PIMPLE
{
    momentumPredictor   no;
    nOuterCorrectors    1;
    nCorrectors         3;
    nNonOrthogonalCorrectors 0;
}

relaxationFactors
{
    equations
    {
        &quot;.*&quot; 1;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数其作用随网格质量和解的光滑程度变化，可通过细化对比评估。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
