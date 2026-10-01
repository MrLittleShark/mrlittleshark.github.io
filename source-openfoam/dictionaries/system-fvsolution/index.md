---
title: "system/fvSolution · fvSolution"
layout: reference
description: "SIMPLE、PISO 和 PIMPLE 分别采用对应的算法子字典。SIMPLE 常用 nNonOrthogonalCorrectors、consistent、residualControl 和 pRefCell/pRefValue；PISO 通过 nCorrectors 控制校正次数；PIMPLE 另设 nOuterCorrectors 控制外迭代。压力方程需要参考值且求解器采用该机制时，设置 pRefCell 和 pRefValue。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>SIMPLE、PISO 和 PIMPLE 分别采用对应的算法子字典。SIMPLE 常用 nNonOrthogonalCorrectors、consistent、residualControl 和 pRefCell/pRefValue；PISO 通过 nCorrectors 控制校正次数；PIMPLE 另设 nOuterCorrectors 控制外迭代。压力方程需要参考值且求解器采用该机制时，设置 pRefCell 和 pRefValue。</p><figure><img src="/assets/diagrams/reference-4.svg" alt="数值方法配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/fvSolution</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>solvers</code> · <code>solver</code> · <code>tolerance</code> · <code>relTol</code> · <code>preconditioner</code> · <code>smoother</code> · <code>PISO</code> · <code>PIMPLE</code> · <code>SIMPLE</code> · <code>nCorrectors</code> · <code>nOuterCorrectors</code> · <code>nNonOrthogonalCorrectors</code> · <code>relaxationFactors</code> · <code>residualControl</code> · <code>pRefCell</code> · <code>pRefValue</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/fvSolution -keywords
icoFoam -help</code></pre><h2>8.3 system/fvSolution</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvSolution;
}
solvers
{
    p
    {
        solver GAMG;
        tolerance 1e-7;
        relTol 0.05;
        smoother GaussSeidel;
    }
    pFinal { $p; relTol 0; }
    U
    {
        solver smoothSolver;
        smoother symGaussSeidel;
        tolerance 1e-8;
        relTol 0;
    }
}
PIMPLE
{
    nOuterCorrectors 2;
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    momentumPredictor yes;
    pRefCell 0;
    pRefValue 0;
}
relaxationFactors
{
    equations { U 1; }
}</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置原则</th></tr>
<tr><td>solver</td><td>线性代数求解器</td><td>PCG 适于相容的对称矩阵；PBiCGStab 可处理非对称矩阵；GAMG 为多重网格</td></tr>
<tr><td>preconditioner</td><td>预条件器</td><td>DIC、DILU 等须与矩阵和 solver 相容</td></tr>
<tr><td>smoother</td><td>平滑器</td><td>如 GaussSeidel、symGaussSeidel、DICGaussSeidel</td></tr>
<tr><td>tolerance</td><td>绝对残差停止阈值</td><td>控制线性方程残差的停止条件</td></tr>
<tr><td>relTol</td><td>相对本次求解初始残差的停止阈值</td><td>0 表示关闭相对阈值，常用于最终校正</td></tr>
<tr><td>minIter、maxIter</td><td>线性迭代上下限</td><td>达到 maxIter 时结合残差判断收敛状态</td></tr>
<tr><td>nSweeps</td><td>每组平滑扫描次数</td><td>仅适用求解器使用</td></tr>
<tr><td>cacheAgglomeration</td><td>缓存 GAMG 聚合</td><td>静态网格可复用聚合结果</td></tr>
<tr><td>nCellsInCoarsestLevel</td><td>GAMG 最粗层目标单元数</td><td>结合并行分区和收敛情况调整</td></tr>
<tr><td>pFinal、UFinal 等</td><td>最后一次校正的专用设置</td><td>是否使用由求解器控制</td></tr>
<tr><td>正则字段名</td><td>共享线性求解配置</td><td>如 &quot;(U|k|omega)&quot;，采用引号包围正则表达式</td></tr>
<tr><td>relaxationFactors/fields</td><td>场松弛</td><td>如稳态 p 0.3</td></tr>
<tr><td>relaxationFactors/equations</td><td>方程松弛</td><td>如稳态 U 0.7；较小因子降低更新幅度</td></tr>
</table></div>
<p>SIMPLE、PISO 和 PIMPLE 分别采用对应的算法子字典。SIMPLE 常用 nNonOrthogonalCorrectors、consistent、residualControl 和 pRefCell/pRefValue；PISO 通过 nCorrectors 控制校正次数；PIMPLE 另设 nOuterCorrectors 控制外迭代。压力方程需要参考值且求解器采用该机制时，设置 pRefCell 和 pRefValue。</p>
<pre><code class="language-openfoam">// SIMPLE 片段：稳态算例
SIMPLE
{
    nNonOrthogonalCorrectors 0;
    residualControl
    {
        p 1e-5;
        U 1e-6;
        &quot;(k|omega)&quot; 1e-6;
    }
}
relaxationFactors
{
    fields { p 0.3; }
    equations { U 0.7; k 0.7; omega 0.7; }
}</code></pre>
<p>residualControl 的结构由算法接口确定，部分 PIMPLE 控制采用 tolerance/relTol 子字典。收敛判定应同时考察残差、质量守恒及力、流量、温度等目标量的稳定性。</p>
<h2>补充说明</h2><p>它管什么：每个方程用什么线性代数求解器、迭代到什么精度、外层算法（SIMPLE/PISO/PIMPLE）怎么循环、松弛因子多少。</p><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>solvers</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/system/fvSolution</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/fvSolution">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvsolution/1-fvSolution.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
        &#36;p;
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


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/system/fvSolution</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/fvSolution">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvsolution/2-fvSolution.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSolution</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/fvSolution">查看固定版本源码</a> · <a href="/assets/examples/v2512/fvsolution/3-fvSolution.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
        &#36;p_rgh;
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/fvSolution&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/fvSolution&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>找不到离散项或场求解器</td><td>把错误中的完整键名与 fvSchemes / fvSolution 对照，注意 div(phi,U) 等键的精确拼写。</td></tr><tr><td>残差下降但目标量漂移</td><td>同时监测守恒误差、力或流量，并分别检查时间步与网格敏感性。</td></tr><tr><td>非正交修正导致成本增加</td><td>优先改善网格；增加修正次数不是无条件提高精度的办法。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
