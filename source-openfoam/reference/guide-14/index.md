---
title: "第 14 章　system/fvSolution（线性求解器与算法控制）"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>它管什么：每个方程用什么线性代数求解器、迭代到什么精度、外层算法（SIMPLE/PISO/PIMPLE）怎么循环、松弛因子多少。</p>
<h4>14.1 solvers 子字典</h4>
<pre><code>solvers
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
        $p;                                // 继承 p 的所有设置
        relTol          0;                 // 最后一次外迭代要求解到底
    }

    &quot;(U|k|epsilon|omega)&quot;
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
<p>为什么压力方程要特殊对待：不可压 N-S 里压力方程是椭圆型的，信息瞬间传遍全场，是最难解也最耗时的一个（通常占总时间 60%–80%）。GAMG（几何-代数多重网格）通过在粗网格上快速消除长波误差来加速，因此成为标配。</p>
<p>relTol 在瞬态里为什么设成 0.01 而不是 0：瞬态每个时间步都要解好几次，中间步骤解得太精确是浪费——反正下一次外迭代还会改。只有最后一次（pFinal）才要求解到底（relTol 0）。这个”中间松、最后紧”的策略能省下大量时间。</p>
<h4>14.2 SIMPLE / PISO / PIMPLE 控制</h4>
<p>稳态 SIMPLE</p>
<pre><code>SIMPLE
{
    nNonOrthogonalCorrectors 1;     // 非正交修正次数，按 checkMesh 结果定
    consistent               yes;   // 用 SIMPLEC：可以把松弛因子放大，收敛更快
    residualControl                 // 收敛判据：都低于阈值就提前结束
    {
        p       1e-4;
        U       1e-4;
        &quot;(k|omega|epsilon)&quot; 1e-4;
    }
}</code></pre>
<p>瞬态 PISO</p>
<pre><code>PISO
{
    nCorrectors              2;     // 压力修正次数
    nNonOrthogonalCorrectors 1;
    pRefCell                 0;     // 全封闭区域必须给参考压力
    pRefValue                0;
}</code></pre>
<p>瞬态 PIMPLE</p>
<pre><code>PIMPLE
{
    nOuterCorrectors         2;     // ★ =1 时退化为 PISO；&gt;1 才是真 PIMPLE
    nCorrectors              2;
    nNonOrthogonalCorrectors 1;
    momentumPredictor        yes;   // 低速/多相有时关掉更稳
    turbOnFinalIterOnly      yes;
}</code></pre>
<p>PIMPLE 的意义：PISO 要求 \(\mathrm{Co} &lt; 1\)；PIMPLE 在每个时间步内做多次外迭代（相当于把稳态 SIMPLE 嵌进每个时间步），因此可以用 \(\mathrm{Co} \gg  1\) 的大时间步。代价是每步更贵，所以 nOuterCorrectors 一般取 2–3，配合 \(\mathrm{Co} \approx  5\text{–}10\) 才划算。</p>
<p>pRefCell / pRefValue 什么时候必须给：当边界条件里没有任何一处给定压力值（全是 zeroGradient，例如封闭腔体、全 wall 的算例）时，压力场只能定到相差一个常数，矩阵奇异。这两个参数的作用就是”指定参考单元的压力值”。忘了给，日志里会看到压力越漂越大或直接不收敛。</p>
<h4>14.3 relaxationFactors（松弛因子）</h4>
<pre><code>relaxationFactors
{
    fields
    {
        p               0.3;
    }
    equations
    {
        U               0.7;
        &quot;(k|omega|epsilon)&quot; 0.7;
    }
}</code></pre>
<p>为什么稳态需要松弛：SIMPLE 的每步更新如果全量采纳，会左右横跳发散。松弛因子 \(\alpha\) 表示”只采纳 \(\alpha\) 那么多”。经验值 p 用 0.3、其他用 0.7（两者之和约为 1 是经典配比）。</p>
<p>收敛太慢怎么办：开 consistent yes（SIMPLEC），此时可以把 p 放到 0.7–0.9、U 放到 0.9，通常能省一半迭代步。发散怎么办：把所有因子减半（p 0.1、U 0.3），先算出一个不发散的解，再逐步放大。</p>
<p>瞬态 PIMPLE 里通常只对非最终迭代松弛：</p>
<pre><code>relaxationFactors
{
    equations
    {
        &quot;.*&quot;        1;         // 最终迭代不松弛，保证时间精度
        &quot;U.*&quot;       0.9;
    }
}</code></pre>
<h4>14.4 cache 与其他</h4>
<pre><code>cache { grad(U); }        // 缓存梯度，省重复计算</code></pre>
{% endraw %}