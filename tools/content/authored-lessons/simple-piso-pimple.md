不可压缩流动同时满足动量方程和连续性方程。压力梯度影响速度，速度又必须满足体积守恒。SIMPLE、PISO 和 PIMPLE 用不同的迭代方式协调这两个要求，是理解 `fvSolution` 中算法设置的基础。

## 压力为什么需要单独校正

对于密度恒定的流体，连续性方程为

\[
\nabla\cdot\mathbf U=0.
\]

它要求每个单元的流入与流出体积流量相平衡。动量方程则为

\[
\frac{\partial\mathbf U}{\partial t}
+\nabla\cdot(\mathbf U\mathbf U)
=-\nabla p+\nu\nabla^2\mathbf U.
\]

这里采用 `icoFoam` 的记法，$p$ 是运动压力，即物理压力除以密度，单位为 $\mathrm{m^2/s^2}$；$\nu$ 是运动黏度，单位为 $\mathrm{m^2/s}$。

给定当前压力后，可以求出一份速度，但这份速度通常还没有满足所有单元的流量平衡。程序据此构造压力方程，求出新的压力，再修正速度和面通量。反复进行这一过程，两个方程逐渐协调。

## 从动量方程得到压力方程

将离散动量方程简写成

\[
a_P\mathbf U_P=\mathbf H_P-\nabla p_P.
\]

$a_P$ 表示对角系数，$\mathbf H_P$ 汇总邻居单元和已知项。除以 $a_P$ 得

\[
\mathbf U=\mathbf H/a_P-(1/a_P)\nabla p.
\]

将其代入 $\nabla\cdot\mathbf U=0$，就得到压力方程的基本形式：

\[
\nabla\cdot\left(\frac{1}{a_P}\nabla p\right)
=\nabla\cdot\left(\frac{\mathbf H}{a_P}\right).
\]

右侧反映预测通量的散度，压力通过左侧的修正使最终通量满足连续性。在实际程序中，这些量还包含边界约束、面插值和瞬态一致性处理。

## SIMPLE：反复更新稳态场

SIMPLE 常用于稳态计算。一次外迭代的主要操作为：

1. 用已有速度、压力和物性组装动量方程，得到预测速度。
2. 根据预测通量建立并求解压力方程。
3. 修正压力、速度和面通量。
4. 更新湍流量等其他方程，开始下一轮迭代。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-simple-pressure-coupling.png" alt="SIMPLE 压力—速度迭代流程" loading="lazy"><figcaption><strong>SIMPLE 压力—速度迭代流程</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 90 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

随着外迭代进行，方程系数和流场同时更新。`simpleFoam` 的 `Time` 常用于标记迭代序号；例如输出目录 `500` 可以表示第 500 次迭代。

在稳态算例的 `system/fvSolution` 中可使用以下基本设置：

```foam
SIMPLE
{
    nNonOrthogonalCorrectors 0;
    residualControl
    {
        p                 1e-5;
        U                 1e-6;
        "(k|epsilon)"     1e-6;
    }
}
```

`residualControl` 根据外迭代残差控制结束条件。正则表达式 `"(k|epsilon)"` 同时匹配 $k$ 和 $\epsilon$，适用于求解这些场的模型。该处阈值影响整个 SIMPLE 迭代是否继续；`solvers` 中的 `tolerance` 则控制某一次线性系统求解。

配套 `pitzDaily` 原始设置还包含 `consistent yes`，启用一致性修正。它与普通 SIMPLE 在压力校正系数的处理上有差别。研究松弛和收敛时可以先保留该算例的完整原始设置，再单独比较这一选项。

## PISO：在一个时间步内多次校正压力

PISO 常用于瞬态计算。程序先前进一个时间步，组装动量方程，再进行多次压力—速度校正。`icoFoam/cavity` 中的设置为：

```foam
PISO
{
    nCorrectors               2;
    nNonOrthogonalCorrectors  0;
    pRefCell                  0;
    pRefValue                 0;
}
```

`nCorrectors 2` 表示每个时间步做两次压力校正；`nNonOrthogonalCorrectors 0` 表示每次压力校正只进行基础压力求解。若后者改为 1，每次压力校正中还会多做一次非正交修正求解。

方腔全部封闭，压力边界主要给出法向梯度，压力整体加一个常数不会改变速度。`pRefCell 0` 与 `pRefValue 0` 因而选定一个参考单元及其运动压力值，使压力系统具有确定的基准。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-piso-pressure-coupling.png" alt="PISO 时间步与压力校正循环" loading="lazy"><figcaption><strong>PISO 时间步与压力校正循环</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 93 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

对这组静止网格方腔设置，每步通常能看到速度分量求解记录和两次压力求解记录。最后一次压力求解可以使用 `pFinal` 中更严格的容差，前面的校正采用普通 `p` 设置。

## PIMPLE：在时间步内再加外循环

PIMPLE 在 PISO 的时间步内部加入外循环。每轮外循环可以重新组装动量方程、校正压力和速度，并按设置更新相关模型，因此适合需要更充分非线性耦合的瞬态问题。

```foam
PIMPLE
{
    momentumPredictor         yes;
    nOuterCorrectors          3;
    nCorrectors               2;
    nNonOrthogonalCorrectors  0;
}
```

这段配置用于完整的 `pimpleFoam` 算例。`momentumPredictor yes` 启用动量预测；`nOuterCorrectors 3` 表示每步三轮外校正；每轮再做两次压力校正。在没有提前停止和其他附加循环时，每步共进行六次基础压力求解。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-pimple-pressure-coupling.png" alt="PIMPLE 外校正与 PISO 内校正" loading="lazy"><figcaption><strong>PIMPLE 外校正与 PISO 内校正</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 96 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

三类循环的关系可以写成：时间步 → 外校正 → 压力校正 → 非正交校正。增加外校正次数主要减少同一时间步内的耦合误差，减小时间步主要减少时间离散误差。两种操作可以分别比较效果和成本。

当 `nOuterCorrectors` 为 1 时，`pimpleFoam` 工作在 PISO 模式。对于较大的外校正上限，还可用 `residualControl` 让满足条件的时间步提前结束外循环：

```foam
residualControl
{
    p
    {
        tolerance 1e-5;
        relTol    0;
    }
    U
    {
        tolerance 1e-6;
        relTol    0;
    }
}
```

这个子字典放在 `PIMPLE` 内。`relTol 0` 关闭相对变化条件，按绝对阈值判断。选择阈值时，同时观察目标量随外校正次数的变化，找到足够准确且成本合适的设置。

## 对照 icoFoam 的核心代码

下列片段来自压力校正内部。前面已构造 `rAU`、`HbyA` 和预测面通量 `phiHbyA`：

```cpp
fvScalarMatrix pEqn
(
    fvm::laplacian(rAU, p) == fvc::div(phiHbyA)
);

pEqn.setReference(pRefCell, pRefValue);
pEqn.solve(p.select(piso.finalInnerIter()));

if (piso.finalNonOrthogonalIter())
{
    phi = phiHbyA - pEqn.flux();
}

U = HbyA - rAU*fvc::grad(p);
U.correctBoundaryConditions();
```

`rAU` 对应动量矩阵对角系数的倒数。`fvc::div(phiHbyA)` 计算预测通量的不平衡，作为压力方程右侧。`pEqn.flux()` 提供压力造成的面通量修正，并在最终非正交循环中更新 `phi`。最后两行由新压力修正单元速度，再更新速度边界。

`p.select(...)` 根据迭代位置选择 `p` 或 `pFinal` 的线性求解设置。求解器直接维护面通量，是因为连续性在网格面上离散；单元速度与面通量通过离散公式保持配合。

## 运行并观察校正次数

在原始方腔的两份副本中，分别设置 `nCorrectors 1` 和 `2`，保持其他输入相同。每份运行并保存日志：

```bash
icoFoam > log.icoFoam 2>&1
grep -E 'Time =|Solving for p|continuity errors' log.icoFoam
```

第一行保存标准输出和错误信息；第二行筛出物理时间、压力求解和连续性误差，便于按时间步阅读。比较两份日志中每步压力求解次数，再比较相同时刻的中心线速度。

若增加校正次数后场值变化很小而成本上升，原来的耦合精度对这一目标量可能已足够。若变化仍明显，可以继续增加校正或减小时间步，并分开记录两种影响。对于本身持续非定常的流动，使用瞬态计算分析其周期或统计平均也更合适。

源码位置：`$FOAM_SOLVERS/incompressible/icoFoam/icoFoam.C`，以及 `simpleFoam`、`pimpleFoam` 下的 `UEqn.H`、`pEqn.H`。算法名由求解器中的控制对象决定，字典名称与所选求解器对应。
