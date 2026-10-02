顶盖驱动方腔是一种经典流动：方形腔体充满流体，上壁以恒定速度向右运动，其余壁面静止。顶盖通过黏性剪切带动流体，在封闭腔体内形成回流。几何简单、边界明确，适合用来熟悉完整的计算过程。

## 算例的物理设置

![顶盖驱动方腔](/assets/diagrams/core-cavity.svg)

本课采用官方基础方腔，参数如下：

| 参数 | 数值 | 所在文件 |
| --- | --- | --- |
| 腔体边长 $L$ | $0.1\,\mathrm{m}$ | `system/blockMeshDict` |
| 顶盖速度 $U_{\mathrm{lid}}$ | $1\,\mathrm{m/s}$ | `0/U` |
| 运动黏度 $\nu$ | $0.01\,\mathrm{m^2/s}$ | `constant/transportProperties` |
| 网格 | $20\times20\times1$ | `system/blockMeshDict` |
| 时间步长 $\Delta t$ | $0.005\,\mathrm{s}$ | `system/controlDict` |
| 结束时间 | $0.5\,\mathrm{s}$ | `system/controlDict` |

雷诺数表示惯性作用与黏性作用的相对大小：

$$
Re=\frac{U_{\mathrm{lid}}L}{\nu}
=\frac{1\times0.1}{0.01}=10.
$$

在这个低雷诺数设置下，黏性对流动影响显著，采用层流模型。网格在厚度方向只有一个单元，前后面使用 `empty`，计算的是二维流动。

求解器 `icoFoam` 求解不可压缩连续性方程与动量方程：

$$
\nabla\cdot\mathbf U=0,
$$

$$
\frac{\partial\mathbf U}{\partial t}
+\nabla\cdot(\mathbf U\mathbf U)
=-\nabla p+\nu\nabla^2\mathbf U.
$$

动量方程依次包含非定常变化、对流、压力梯度和黏性扩散。这里的 $p$ 是运动学压力，单位为 $\mathrm{m^2/s^2}$。求解器通过 PISO 压力校正，使更新后的速度满足连续性方程。

## 准备算例

在加载 OpenFOAM 环境的 Linux 终端中，复制一份新的基础方腔：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-run
cd cavity-run
```

若 `cavity-run` 已存在，可换一个目录名，以便分别保留每次练习的设置。课程下载包中的同名官方算例也可直接使用。

先读取三个关键参数：

```bash
foamDictionary 0/U -entry boundaryField/movingWall/value -value
foamDictionary constant/transportProperties -entry nu -value
foamDictionary system/controlDict -entry endTime -value
```

基础设置应分别得到 `uniform (1 0 0)`、`0.01` 和 `0.5`。如果上一课已修改过参数，使用这里的新副本即可恢复原始设置。

## 生成并检查网格

```bash
blockMesh > log.blockMesh 2>&1
tail -n 20 log.blockMesh
```

`blockMesh` 读取顶点、块划分和边界面，生成 `constant/polyMesh`。日志正常结束后，检查网格：

```bash
checkMesh > log.checkMesh 2>&1
cat log.checkMesh
```

基础网格应有 400 个单元，包围盒为 $(0,0,0)$ 到 $(0.1,0.1,0.01)$。厚度 $0.01\,\mathrm{m}$ 来自 `blockMeshDict` 中的几何缩放。日志中的几何方向和求解方向应与二维设置一致。

网格检查通过后再运行求解器。如果日志报告边界定义、负体积或拓扑错误，先按报错修改网格输入并重新生成；这些错误会直接影响后面的方程离散。

## 运行 icoFoam

```bash
icoFoam > log.icoFoam 2>&1
tail -n 30 log.icoFoam
```

程序从 `0/U` 和 `0/p` 读取初场，然后以 $0.005\,\mathrm{s}$ 的步长推进，直到 $0.5\,\mathrm{s}$。一共推进 100 步，每 20 步写出一次结果，因此通常会看到 `0.1`、`0.2`、`0.3`、`0.4`、`0.5` 这些结果目录。

日志主要包含以下信息：

| 日志内容 | 含义 | 阅读重点 |
| --- | --- | --- |
| `Time = ...` | 当前物理时间 | 是否推进到设定的结束时间 |
| `Courant Number mean: ... max: ...` | 平均与最大 Courant 数 | 时间步相对于局部输运时间尺度的大小 |
| `Solving for Ux`、`Uy` | 速度分量方程的线性求解 | 初始残差、最终残差、迭代次数 |
| `Solving for p` | 压力校正方程的线性求解 | 同一时间步内会出现多次 |
| `time step continuity errors` | 离散连续性误差 | 局部和全局误差是否异常增长 |
| `ExecutionTime`、`ClockTime` | CPU 时间与实际经过时间 | 计算成本 |

一次线性求解的残差减小，表示当前矩阵方程求解得更充分。流动是否接近稳定，还要比较不同时间的速度和压力。例如顶盖启动后，早期与后期的中心线速度会变化；这种变化属于真实的瞬态过程。

## 在 ParaView 中查看结果

在算例根目录创建一个读取入口：

```bash
touch cavity.foam
```

用 ParaView 打开 `cavity.foam`，选择 OpenFOAM Reader，再按以下顺序操作：

1. 在 `Properties` 中勾选 `internalMesh`，以及需要查看的 `U`、`p`，点击 `Apply`。
2. 将时间切换到 `0.5`，显示方式选择 `Surface With Edges`，先看清网格。
3. 颜色变量选择 `U`，分量选择 `Magnitude`，显示速度大小。
4. 点击重新缩放色标，使颜色范围对应当前数据。

![方腔速度大小，20×20×1 网格，t=0.5 s](/assets/science/cavity-velocity.png)

上图是该设置的速度大小结果。顶盖附近速度较大，内部出现主回流。固定壁面上满足无滑移条件，因此壁面速度为零；紧邻壁面的单元中心具有有限距离，其速度值通常与壁面值不同。

如果将颜色分量改为 `U_X`，负值表示流体沿 $x$ 负方向运动；`Magnitude` 始终非负。比较不同算例时，应使用相同的变量、时间和色标范围。

## 提取中心线速度

云图可以显示整体结构，中心线曲线更适合比较数值变化。在 ParaView 中选中算例，添加 `Plot Over Line`：

| 曲线 | 起点 | 终点 | 查看分量 |
| --- | --- | --- | --- |
| 竖直中心线 | `(0.05 0 0.005)` | `(0.05 0.1 0.005)` | 水平速度 $U_x$ |
| 水平中心线 | `(0 0.05 0.005)` | `(0.1 0.05 0.005)` | 竖直速度 $U_y$ |

竖直中心线上，下部通常存在向左的回流，上部受顶盖驱动向右。水平中心线上的竖直速度则反映两侧回流方向。将数据导出为 CSV，后续可以与细网格结果比较。

文献中的方腔数据常采用其他雷诺数。比较前将本例与参考数据的 $Re$、边界条件、无量纲坐标和时间状态对应起来；不同 $Re$ 的剖面本来就会不同。

## 改变顶盖速度

再从官方目录复制一份 `cavity-slow`，将 `0/U` 中顶盖的 `value` 改为：

```foam
value uniform (0.5 0 0);
```

其余条件保持相同时，新的雷诺数为 $Re=5$。运行网格、检查和求解后，对比相同时间的速度场与中心线曲线。速度尺度随顶盖速度降低，但无量纲剖面也可能因雷诺数改变而变化。

若希望改变速度后仍保持 $Re=10$，应同时按比例改变运动黏度：

```foam
nu 0.005;
```

相同雷诺数的两个算例，比较瞬态过程时还要匹配无量纲时间 $t^*=tU_{\mathrm{lid}}/L$。速度减半后，相同的物理时间对应不同的 $t^*$；要比较相同发展阶段，可以把结束时间增加一倍。

## 常见问题

| 现象 | 原因与处理 |
| --- | --- |
| 求解器找不到网格 | 确认已在当前算例运行 `blockMesh`，检查 `constant/polyMesh` |
| `cannot find patchField entry` | `0/U` 或 `0/p` 的边界名称与网格不一致 |
| ParaView 只显示方框 | 检查 `internalMesh` 是否选中、是否点击 `Apply`，并重置相机 |
| 计算结束但没有每一步的目录 | 写出频率由 `writeControl` 与 `writeInterval` 决定 |
| 改完速度仍看到原来的结果 | 在新算例重新求解，并在 ParaView 打开对应文件、选择正确时间 |

继续细化到 $40\times40\times1$ 时，可以使用相同方法比较中心线曲线。网格加密、时间步缩小和计算时间延长分别检验不同误差来源，后续章节会逐项展开。
