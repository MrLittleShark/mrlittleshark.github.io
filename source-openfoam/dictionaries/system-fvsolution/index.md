---
title: "system/fvSolution"
layout: "reference"
description: "SIMPLE、PISO 和 PIMPLE 分别采用对应的算法子字典。SIMPLE 常用 nNonOrthogonalCorrectors、consistent、residualControl 和 pRefCell/pRefValue；PISO 通过 nCorrectors 控制校正次数；PIMPLE"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/fvSolution</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>solvers</code> · <code>solver</code> · <code>tolerance</code> · <code>relTol</code> · <code>preconditioner</code> · <code>smoother</code> · <code>PISO</code> · <code>PIMPLE</code> · <code>SIMPLE</code> · <code>nCorrectors</code> · <code>nOuterCorrectors</code> · <code>nNonOrthogonalCorrectors</code> · <code>relaxationFactors</code> · <code>residualControl</code> · <code>pRefCell</code> · <code>pRefValue</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/fvSolution -keywords
icoFoam -help</code></pre><h2>8.3 system/fvSolution</h2><pre><code>FoamFile
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
<pre><code>// SIMPLE 片段：稳态算例
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
<h2>第 14 章　system/fvSolution（线性求解器与算法控制）</h2><p>它管什么：每个方程用什么线性代数求解器、迭代到什么精度、外层算法（SIMPLE/PISO/PIMPLE）怎么循环、松弛因子多少。</p>
{% endraw %}