---
title: "第 14 章　system/fvSolution（线性求解器与算法控制）"
layout: reference
description: "OpenCFD v2512 system/fvSolution（线性求解器与算法控制）；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>它管什么：每个方程用什么线性代数求解器、迭代到什么精度、外层算法（SIMPLE/PISO/PIMPLE）怎么循环、松弛因子多少。</p>
<h2>14.1 solvers 子字典</h2>
<pre><code class="language-openfoam">solvers
{
    p
    {
        solver          GAMG;              // 压力方程用多重网格
        tolerance       1e-6;              // 绝对残差
        relTol          0.01;              // 相对残差（本步残差降到初始的 1%）
        smoother        GaussSeidel;
        nCellsInCoarsestLevel 20;
    }

    pFinal
    {
        &#36;p;                                // 继承 p 的所有设置
        relTol          0;                 // 最后一次外迭代要求解到底
    }

    "(U|k|epsilon|omega)"
    {
        solver          smoothSolver;
        smoother        symGaussSeidel;
        tolerance       1e-8;
        relTol          0.1;
    }
}</code></pre>
<p>线性求解器怎么选</p>
<div class="table-scroll"><table>
<tr><th>求解器</th><th>适用矩阵</th><th>场景</th></tr>
<tr><td>GAMG</td><td>对称</td><td>压力方程首选，大网格上比 PCG 快数倍</td></tr>
<tr><td>PCG</td><td>对称</td><td>压力，配 preconditioner DIC</td></tr>
<tr><td>PBiCGStab</td><td>非对称</td><td>U、k、epsilon 等</td></tr>
<tr><td>smoothSolver</td><td>通用</td><td>U 与湍流量，简单快速</td></tr>
<tr><td>diagonal</td><td>对角阵</td><td>显式方程（如 rhoCentralFoam 里的密度）</td></tr>
</table></div>
<div class="table-scroll"><table>
<tr><th>预处理/光顺器</th><th>用于</th></tr>
<tr><td>DIC</td><td>对称矩阵（配 PCG）</td></tr>
<tr><td>DILU</td><td>非对称矩阵（配 PBiCGStab）</td></tr>
<tr><td>GaussSeidel / symGaussSeidel</td><td>GAMG、smoothSolver 的光顺器</td></tr>
<tr><td>DICGaussSeidel</td><td>GAMG 用，收敛更快但每步更贵</td></tr>
</table></div>
<p>压力方程的长波误差可能使迭代收敛较慢。GAMG 通过网格聚合与多层修正加速误差消除，但性能依赖矩阵、聚合参数、平滑器和并行划分。应比较实际迭代次数与求解耗时，不采用固定的耗时比例判断。</p>
<p>tolerance 是绝对残差阈值，relTol 是相对初始残差的下降阈值。可以对中间修正与最终修正采用不同精度，但需确认求解器会选择 pFinal 等配置；relTol 0 表示关闭相对提前停止，并不要求残差等于零。</p>
<h2>14.2 SIMPLE / PISO / PIMPLE 控制</h2>
<p>稳态 SIMPLE</p>
<pre><code class="language-plaintext">SIMPLE
{
    nNonOrthogonalCorrectors 1;     // 非正交修正次数，按 checkMesh 结果定
    consistent               yes;   // 用 SIMPLEC：可以把松弛因子放大，收敛更快
    residualControl                 // 收敛判据：都低于阈值就提前结束
    {
        p       1e-4;
        U       1e-4;
        "(k|omega|epsilon)" 1e-4;
    }
}</code></pre>
<p>瞬态 PISO</p>
<pre><code class="language-plaintext">PISO
{
    nCorrectors              2;     // 压力修正次数
    nNonOrthogonalCorrectors 1;
    pRefCell                 0;     // 全封闭区域必须给参考压力
    pRefValue                0;
}</code></pre>
<p>瞬态 PIMPLE</p>
<pre><code class="language-plaintext">PIMPLE
{
    nOuterCorrectors         2;     // ★ =1 时退化为 PISO；&gt;1 才是真 PIMPLE
    nCorrectors              2;
    nNonOrthogonalCorrectors 1;
    momentumPredictor        yes;   // 低速/多相有时关掉更稳
    turbOnFinalIterOnly      yes;
}</code></pre>
<p>PIMPLE 的意义：PISO 要求 \(\mathrm{Co} &lt; 1\)；PIMPLE 在每个时间步内做多次外迭代（相当于把稳态 SIMPLE 嵌进每个时间步），因此可以用 \(\mathrm{Co} \gg  1\) 的大时间步。代价是每步更贵，所以 nOuterCorrectors 一般取 2–3，配合 \(\mathrm{Co} \approx  5\text{–}10\) 才划算。</p>
<p>pRefCell / pRefValue 什么时候必须给：当边界条件里没有任何一处给定压力值（全是 zeroGradient，例如封闭腔体、全 wall 的算例）时，压力场只能定到相差一个常数，矩阵奇异。这两个参数的作用就是”指定参考单元的压力值”。忘了给，日志里会看到压力越漂越大或直接不收敛。</p>
<h2>14.3 relaxationFactors（松弛因子）</h2>
<pre><code class="language-plaintext">relaxationFactors
{
    fields
    {
        p               0.3;
    }
    equations
    {
        U               0.7;
        "(k|omega|epsilon)" 0.7;
    }
}</code></pre>
<p>SIMPLE 等外迭代可使用场松弛或方程松弛降低更新幅度，提高某些非线性耦合问题的稳健性。松弛因子 \(\alpha\) 应结合收敛表现调整；压力与速度的松弛因子没有“相加应等于 1”的通用条件。</p>
<p>收敛太慢怎么办：开 consistent yes（SIMPLEC），此时可以把 p 放到 0.7–0.9、U 放到 0.9，通常能省一半迭代步。发散怎么办：把所有因子减半（p 0.1、U 0.3），先算出一个不发散的解，再逐步放大。</p>
<p>瞬态 PIMPLE 里通常只对非最终迭代松弛：</p>
<pre><code class="language-plaintext">relaxationFactors
{
    equations
    {
        ".*"        1;         // 最终迭代不松弛，保证时间精度
        "U.*"       0.9;
    }
}</code></pre>
<h2>14.4 cache 与其他</h2>
<pre><code class="language-plaintext">cache { grad(U); }        // 缓存梯度，省重复计算</code></pre>
{% endraw %}
