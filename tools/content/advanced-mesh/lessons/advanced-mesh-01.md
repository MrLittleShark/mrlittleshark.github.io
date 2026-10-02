锥体沿轴向移动时，附近的流体网格要随边界变形。这一课用 `pimpleFoam` 计算移动锥体周围的层流，并观察同一批网格节点在移动前后的位置。

## 1. 下载算例，先看计算对象

[下载 movingCone 教学算例](/downloads/meshes/v2512-01-deforming.zip)，解压后进入 `foamLabAdvancedMesh/01-deforming`。加载 OpenFOAM v2512 环境后运行：

```bash
bash Allrun
```

算例采用轴对称楔形网格，共 1,900 个单元。`x` 是锥体运动方向；几何文件中的长度乘以 `scale 0.001` 后以米计。`movingWall` 是移动的锥面，`fixedWall` 是固定壁面，`left` 是允许流体进出的边界，前后两个 `wedge` 面表示轴对称条件。

本次计算从 0 开始，到 0.003 s 结束，时间步长为 0.000005 s，每 100 步保存一次，即每 0.0005 s 保存一次。锥体以 1 m/s 沿正 x 方向移动，最终位移为 3 mm。

![移动锥体前后的网格和速度场](/assets/science/advanced-mesh-deforming.png)

图中网格线来自计算输出。锥体移动后，左侧网格拉伸、右侧网格压缩，单元数量保持不变。

## 2. 选择网格运动方法

打开 `constant/dynamicMeshDict`：

{{file:01-deforming/constant/dynamicMeshDict}}

| 设置 | 在这个算例中的作用 |
| --- | --- |
| `dynamicMotionSolverFvMesh` | 每个时间步更新网格节点的位置 |
| `motionSolverLibs (fvMotionSolvers)` | 加载网格运动求解器所在的库 |
| `velocityComponentLaplacian` | 求解一个方向上的网格速度，再用速度更新位置 |
| `component x` | 只计算 x 方向的网格运动 |
| `directional (1 200 0)` | 对网格速度的平滑采用方向相关系数，使运动从锥面向周围网格传递 |

网格运动求解器与流动求解器负责不同的量：前者计算节点怎么移动，后者计算流体的速度和压力。这里用拉普拉斯型方程把边界给定的网格速度延伸到内部；流体仍由 `pimpleFoam` 求解不可压缩动量方程。

`directional` 的数值是运动扩散模型的系数，用来调整网格变形分布。它们与流体黏度分别写在不同文件中：流体物性在 `constant/transportProperties`。

## 3. 给锥面指定网格速度

打开 `0/pointMotionUx`，找到移动壁面：

{{block:01-deforming/0/pointMotionUx:boundaryField/movingWall}}

这个场保存网格节点的 x 方向速度，量纲为速度。`uniformValue constant 1` 表示移动壁面的所有节点都以 1 m/s 运动。经过时间 $t$，该壁面的位移为

$$
\Delta x(t)=1\,\mathrm{m/s}\times t.
$$

固定壁面的设置是：

{{block:01-deforming/0/pointMotionUx:boundaryField/fixedWall}}

两处分别给出 1 和 0，内部节点的运动则由网格运动方程求出。与锥面相连的外侧边界采用 `slip`，允许节点沿边界切向移动；前后面保留 `wedge`，维持轴对称约束。

## 4. 让流体壁面速度跟上网格

接着打开 `0/U`：

{{block:01-deforming/0/U:boundaryField/movingWall}}

`pointMotionUx` 控制几何位置，`U` 控制流体边界值。这里的 `movingWallVelocity` 根据壁面实际运动计算流体壁面速度，让无滑移条件随锥体一起移动。`value` 提供初始值，后续更新由边界条件完成。

在运动控制体上，穿过面的相对体积通量为

$$
\phi_{\mathrm{rel},f}=(\mathbf U_f-\mathbf U_{m,f})\cdot\mathbf S_f,
$$

其中 $\mathbf U_m$ 是网格速度。网格本身移动时，流体相对控制面的输运量也会改变。这正是运动网格计算需要同时更新几何和通量的原因。

本例的压力出口使用 `totalPressure`，移动壁面的压力采用 `zeroGradient`。打开 `0/p`，可以沿相同的边界名称逐一对照。

## 5. 读懂时间控制与迭代设置

{{file:01-deforming/system/controlDict}}

`writePrecision 10` 控制文本输出的有效数字；方程的收敛容差写在 `fvSolution` 中。两者分别影响文件保存和方程求解。

{{block:01-deforming/system/fvSolution:PIMPLE}}

每个时间步进行两次外迭代，使新网格上的速度与压力相互协调。`correctPhi yes` 在网格更新后修正通量。网格速度方程则有自己的线性求解设置：

{{block:01-deforming/system/fvSolution:solvers/cellMotionUx}}

这里采用 PCG 和 DIC，容差为 $10^{-8}$，`relTol 0` 表示按绝对容差结束该次求解。

## 6. 查看结果与网格变化

用 ParaView 打开下载包运行后生成的 `case.foam`，点击 **Apply**，将显示方式改为 **Surface With Edges**。选取 0、0.0015 和 0.003 s，可以看到节点连续移动；按 `U` 的大小着色，可以同时查看流体响应。

日志分为三组：`log.blockMesh` 记录网格生成，`log.pimpleFoam` 记录时间推进，`log.checkMesh.final` 记录最终网格质量。本次运行结束于 0.003 s，最大节点位移约 3 mm，最终最小单元体积为正，网格检查通过。

继续研究这种方法时，可以比较不同运动速度、时间步长和运动扩散系数对网格压缩的影响。变形幅度越来越大时，适合转向后面的重叠网格；转子持续旋转且接口位置规则时，可以学习旋转网格与 AMI。

来源：[OpenFOAM v2512 movingCone 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/movingCone)。
