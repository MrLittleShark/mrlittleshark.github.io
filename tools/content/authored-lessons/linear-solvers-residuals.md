每次求解速度、压力或温度，OpenFOAM 都要处理一组离散代数方程。`fvSolution/solvers` 规定这些方程用什么方法求解、达到什么条件停止；日志中的残差和迭代次数则记录本次求解的进展。

## 残差怎样计算

离散方程写成 $A\mathbf x=\mathbf b$。对于当前近似值 $\mathbf x$，残差为

\[
\mathbf r=\mathbf b-A\mathbf x.
\]

例如方程 $2x=6$，当前取 $x=2.8$，残差是 $6-2\times2.8=0.4$；准确解为 3，解误差是 0.2。二者通过方程系数联系起来。在多变量系统中，有 $A\mathbf e=\mathbf r$，矩阵性质会影响小残差对应多大的解误差。

OpenFOAM 日志通常输出归一化残差，便于观察下降程度。其数值与方程缩放、初始场和矩阵有关，所以压力残差和速度残差适合各自跟踪，不能直接按相同物理单位比较。

## 读懂一行求解日志

下面是一行格式示例，数字用于说明各列：

```text
DICPCG: Solving for p, Initial residual = 0.01,
Final residual = 0.0004, No Iterations 12
```

`DICPCG` 是求解方法与预条件器组合，`p` 是正在求解的场。初始残差在这次线性求解开始时计算，最终残差在结束时计算，`12` 是内部迭代次数。

同一个物理时间步可能有多次压力校正，因此可以看到多行 `Solving for p`。下一行的初始残差对应新的压力系统或校正阶段，其数值会随右侧、系数和已有解变化。

## tolerance 与 relTol

方腔的 `system/fvSolution` 中有如下压力配置：

```foam
solvers
{
    p
    {
        solver          PCG;
        preconditioner  DIC;
        tolerance       1e-6;
        relTol          0.05;
    }
    pFinal
    {
        $p;
        relTol          0;
    }
}
```

`tolerance` 指定本次归一化残差的绝对阈值。`relTol` 指定相对于本次初始残差的下降比例。若初始残差为 0.01，`relTol 0.05` 对应 $0.01\times0.05=0.0005$。上面日志示例的 0.0004 已达到这个相对条件，即使尚未达到 $10^{-6}$，也可以结束本次线性求解。

`$p;` 将 `p` 中的配置复制到 `pFinal`，再用 `relTol 0` 覆盖相对阈值。最终校正因此继续追求绝对容差。`pFinal` 是一组求解配置，压力场本身仍然是 `p`。

还可显式设置最大迭代次数：

```foam
maxIter 1000;
```

它放在某个场的求解器子字典中。达到上限也会结束该次线性迭代；此时应结合最终残差判断是否满足要求。频繁达到上限时，检查矩阵、网格和预条件器通常比单纯提高上限更有价值。

## 根据方程选择线性算法

扩散和压力方程常形成对称矩阵；对流项通常使矩阵非对称。算法应与矩阵性质和规模匹配。

| 设置 | 常见用途 | 主要特点 |
| --- | --- | --- |
| `PCG` + `DIC` | 对称正定的压力或扩散系统 | 共轭梯度配合不完全 Cholesky 预条件 |
| `PBiCGStab` + `DILU` | 含对流的非对称系统 | 稳定化双共轭梯度，适用范围较广 |
| `smoothSolver` | 速度及部分标量方程 | 通过选定平滑器迭代 |
| `GAMG` | 较大规模的椭圆型系统 | 利用粗细多层网格消除不同尺度误差 |

预条件器对线性系统做一种近似变换，使迭代更容易收敛；它与空间离散格式各司其职。下列是被动标量输运例子的配置：

```foam
T
{
    solver          PBiCGStab;
    preconditioner  DILU;
    tolerance       1e-12;
    relTol          0;
}
```

它放在 `solvers` 内。对流使温度矩阵非对称，因此使用 `PBiCGStab`。较紧的容差使一维练习的代数误差较小，便于研究空间和时间误差；大型工程算例可以通过容差敏感性比较，选择成本合适的阈值。

## GAMG 为什么能加快压力求解

局部平滑器容易消除网格尺度上的高频误差，却可能较慢地消除跨越整个区域的平滑误差。GAMG 将问题转移到粗层，使这些大尺度误差在粗层上更容易处理，再把修正传回细层。

`pitzDaily` 的压力设置为：

```foam
p
{
    solver      GAMG;
    tolerance   1e-6;
    relTol      0.1;
    smoother    GaussSeidel;
}
```

`smoother` 指定各层上的平滑方法。实际性能受网格连接、长宽比和并行分区影响。比较 GAMG 与 PCG 时，应记录相同收敛要求下的总耗时；不同算法的一次迭代所做工作不同，单看迭代次数容易误判。

## 将残差保存成表格

在 `system/controlDict` 的 `functions` 内加入：

```foam
solverHistory
{
    type                 solverInfo;
    libs                 (utilityFunctionObjects);
    fields               (p U);
    executeControl       timeStep;
    executeInterval      1;
    writeResidualFields  false;
}
```

`fields` 选择压力和速度。`executeInterval 1` 让函数对象每步记录一次求解信息。`writeResidualFields false` 保留表格输出，避免额外保存逐单元残差场。表格通常写入 `postProcessing/solverHistory/0/solverInfo.dat`，起始目录会随运行起点变化。

`solverInfo` 在执行阶段读取求解信息，表头给出每列的场名和含义。需要逐次查看每一轮内部压力校正时，完整日志保留了更细的顺序信息。可另用

```bash
icoFoam > log.icoFoam 2>&1
foamLog log.icoFoam
```

第一条运行方腔并保存日志，第二条提取残差等曲线数据到 `logs` 目录。同一时间步内出现多次求解时，输出文件会区分相应序号。

## 给残差配一个物理监测量

求解误差以外，流场还可能受外迭代、时间分辨率、网格和模型影响。最实用的做法是同时监测一个实际关注的量，例如中心点速度、入口出口压差或壁面受力。

在 0.1 m 方腔中，可将以下对象也放入 `functions`：

```foam
centreProbe
{
    type              probes;
    libs              (sampling);
    fields            (U p);
    writeControl      timeStep;
    writeInterval     1;
    probeLocations    ((0.05 0.05 0.005));
}
```

坐标单位为 m，取在方腔中心和薄层厚度中间。程序会在 `postProcessing/centreProbe` 下保存速度、压力的时间记录。向量速度包含三个分量，二维方腔主要观察 $U_x$ 与 $U_y$。默认采样采用所在单元的值；需要更准确的点值比较时，可明确指定插值方式并在各算例中保持一致。

![残差与物理量的变化](/assets/diagrams/core-residual.svg)

稳态计算中，可以同时看初始残差是否降低、流量收支是否平衡、目标量是否趋于稳定。瞬态计算的目标量可以持续变化，此时关注每个时间步内的求解是否充分，以及波形对时间步和校正次数是否敏感。

## 练习：容差收紧后变化多大

从相同方腔输入建立两份副本。第一份保留压力 `tolerance 1e-6`，第二份将 `p` 和最终继承设置对应的绝对容差收紧到 `1e-8`；其余参数相同，比较同一物理时刻的中心点速度与总耗时。

若速度变化已经远小于关心的精度，而求解耗时明显上升，可以保持较宽松的设置，将计算资源用于细化网格或减小时间步。若速度仍明显变化，应继续检查压力校正和连续性误差，确认代数误差是否已经足够小。

对于长期计算，监测量应在启动前配置。最终场文件保存的是最后状态；完整残差历史来自运行日志和函数对象记录。
