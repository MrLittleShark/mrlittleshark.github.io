顶盖驱动方腔是 CFD 最经典的入门算例：一个充满流体的方形腔体，上壁以恒定速度向右运动，其余三面静止。顶盖靠黏性剪切带动流体，在腔内形成回流。它几何简单、边界明确，很适合用来走一遍完整的计算流程。

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

雷诺数这么低，黏性占主导，用层流模型即可。网格在厚度方向只有一层单元，前后面设为 `empty`，所以算的是二维流动。

求解器 `icoFoam` 求解不可压缩连续性方程与动量方程：

$$
\nabla\cdot\mathbf U=0,
$$

$$
\frac{\partial\mathbf U}{\partial t}
+\nabla\cdot(\mathbf U\mathbf U)
=-\nabla p+\nu\nabla^2\mathbf U.
$$

动量方程的四项依次是：随时间的变化、对流、压力梯度和黏性扩散。这里的 $p$ 是运动学压力（压力除以密度），单位为 $\mathrm{m^2/s^2}$。icoFoam 用 PISO 算法做压力校正，让每一步更新后的速度满足连续性方程。

## 准备算例

在已加载 OpenFOAM 环境的终端里，复制一份新的方腔算例：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-run
cd cavity-run
```

如果 `cavity-run` 已经存在，换个目录名即可，这样每次练习的设置都能各自保留。也可以直接使用课程下载包里的同名算例。

先查看三个关键参数：

```bash
foamDictionary 0/U -entry boundaryField/movingWall/value -value
foamDictionary constant/transportProperties -entry nu -value
foamDictionary system/controlDict -entry endTime -value
```

输出应依次是 `uniform (1 0 0)`、`0.01` 和 `0.5`。如果上一课改过参数，用这份新副本就能回到原始设置。

## 生成并检查网格

```bash
blockMesh > log.blockMesh 2>&1
tail -n 20 log.blockMesh
```

`blockMesh` 读取顶点、块划分和边界面，生成 `constant/polyMesh`。日志正常结束后，再检查网格：

```bash
checkMesh > log.checkMesh 2>&1
cat log.checkMesh
```

网格应有 400 个单元，包围盒从 $(0,0,0)$ 到 $(0.1,0.1,0.01)$，其中厚度 $0.01\,\mathrm{m}$ 来自 `blockMeshDict` 的缩放系数。日志还会报告网格的求解方向为 `(1 1 0)`，说明这是二维网格。

网格检查通过后再运行求解器。如果日志报告边界定义、负体积或拓扑错误，先按提示修改网格输入、重新生成——这些错误会直接影响方程的离散。

## 运行 icoFoam

```bash
icoFoam > log.icoFoam 2>&1
tail -n 30 log.icoFoam
```

程序先从 `0/U` 和 `0/p` 读入初始场，再以 $0.005\,\mathrm{s}$ 的步长推进到 $0.5\,\mathrm{s}$，共 100 步。每 20 步写出一次结果，所以算完会看到 `0.1`、`0.2`、`0.3`、`0.4`、`0.5` 五个时间目录。

日志里主要有这些信息：

| 日志内容 | 含义 | 阅读重点 |
| --- | --- | --- |
| `Time = ...` | 当前物理时间 | 是否推进到设定的结束时间 |
| `Courant Number mean: ... max: ...` | 平均与最大 Courant 数 | 时间步是否过大 |
| `Solving for Ux`、`Uy` | 速度分量方程的线性求解 | 初始残差、最终残差、迭代次数 |
| `Solving for p` | 压力校正方程的线性求解 | 同一时间步内会出现多次 |
| `time step continuity errors` | 离散连续性误差 | 局部和全局误差是否异常增长 |
| `ExecutionTime`、`ClockTime` | CPU 时间与实际经过时间 | 计算成本 |

残差变小，只说明这一步的矩阵方程解得更准了；流动是否趋于稳定，要比较不同时刻的速度和压力。比如顶盖刚启动时和计算后期，中心线速度并不一样——这是真实的瞬态过程，不是误差。

## 在 ParaView 中查看结果

在算例根目录创建一个空文件，作为 ParaView 的读取入口：

```bash
touch cavity.foam
```

用 ParaView 打开 `cavity.foam`，读取器选择 OpenFOAM Reader，然后：

1. 在 `Properties` 中勾选 `internalMesh`，以及需要查看的 `U`、`p`，点击 `Apply`。
2. 将时间切换到 `0.5`，显示方式选择 `Surface With Edges`，先看清网格。
3. 颜色变量选择 `U`，分量选择 `Magnitude`，显示速度大小。
4. 点击 `Rescale to Data Range`，让色标范围与当前数据一致。

![方腔速度大小，20×20×1 网格，t=0.5 s](/assets/science/cavity-velocity.png)

上图就是这组设置下的速度大小。顶盖附近速度最大，腔内形成一个主回流。固定壁面满足无滑移条件，壁面上速度为零；但紧邻壁面的单元中心离壁面还有一段距离，所以那里的速度一般不为零。

如果把分量改成 `U_X`，负值表示流体沿 $x$ 负方向运动；`Magnitude` 则始终非负。比较不同算例时，要用相同的变量、时刻和色标范围。

## 提取中心线速度

云图适合看整体结构，要比较具体数值，中心线曲线更合适。在 ParaView 中选中算例，添加 `Plot Over Line`：

| 曲线 | 起点 | 终点 | 查看分量 |
| --- | --- | --- | --- |
| 竖直中心线 | `(0.05 0 0.005)` | `(0.05 0.1 0.005)` | 水平速度 $U_x$ |
| 水平中心线 | `(0 0.05 0.005)` | `(0.1 0.05 0.005)` | 竖直速度 $U_y$ |

竖直中心线上，上部被顶盖带着向右，下部是向左的回流；水平中心线上的竖直速度则反映两侧回流的方向。把数据导出为 CSV，以后可以和细网格的结果对比。

文献中的方腔数据大多是其他雷诺数下的。和参考数据比较前，先确认 $Re$、边界条件、无量纲坐标和时间状态都对得上——$Re$ 不同，剖面本来就不一样。

## 改变顶盖速度

再从官方目录复制一份 `cavity-slow`，将 `0/U` 中顶盖的 `value` 改为：

```foam
value uniform (0.5 0 0);
```

其他条件不变，雷诺数就变成 $Re=5$。重新生成网格、检查并求解，然后对比同一时刻的速度场和中心线曲线。速度整体变小是显然的；但雷诺数变了，无量纲剖面也可能跟着改变。

如果想在降低速度的同时保持 $Re=10$，就要按同样比例减小运动黏度：

```foam
nu 0.005;
```

即使雷诺数相同，比较瞬态过程时还要对齐无量纲时间 $t^*=tU_{\mathrm{lid}}/L$。速度减半后，同一物理时刻对应的 $t^*$ 也减半；要比较相同的发展阶段，应把结束时间加倍。

## 常见问题

| 现象 | 原因与处理 |
| --- | --- |
| 求解器找不到网格 | 确认已在当前算例运行 `blockMesh`，检查 `constant/polyMesh` |
| `cannot find patchField entry` | `0/U` 或 `0/p` 的边界名称与网格不一致 |
| ParaView 只显示方框 | 检查 `internalMesh` 是否选中、是否点击 `Apply`，并重置相机 |
| 计算结束但没有每一步的目录 | 写出频率由 `writeControl` 与 `writeInterval` 决定 |
| 改完速度仍看到原来的结果 | 在新算例重新求解，并在 ParaView 打开对应文件、选择正确时间 |

把网格加密到 $40\times40\times1$，用同样的方法比较中心线曲线。加密网格、缩小时间步、延长计算时间，分别检验不同的误差来源，后面的章节会逐一展开。
