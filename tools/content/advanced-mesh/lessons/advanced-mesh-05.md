MRF 是多重参考系方法。它在指定区域中加入旋转参考系相关项，用固定的网格计算旋转设备的流动。这一课用 `simpleFoam` 求解二维搅拌槽，重点学习旋转区域、转速和壁面之间的关系。

## 1. 从一个固定网格开始

[下载 MRF 算例](/downloads/meshes/v2512-05-mrf.zip)，进入 `foamLabAdvancedMesh/05-mrf` 后运行：

```bash
bash Allrun
```

算例有 3,072 个单元，转子周围区域命名为 `rotor`。流体使用不可压缩 RANS 模型，湍流模型为 `kEpsilon`。转速为约 1,000 rpm，计算进行 500 次 SIMPLE 迭代，每 50 次保存一次。

![MRF 搅拌槽速度与迭代残差](/assets/science/advanced-mesh-mrf.png)

速度场随迭代形成，网格节点坐标始终保持不变。`50/`、`100/` 等输出目录表示稳态迭代进度；本例的 `deltaT 1` 用于推进迭代编号。

## 2. 用 cellZone 圈定旋转参考系

网格中的 cellZone 是一组单元的集合。`blockMeshDict.m4` 中给旋转块附上 `rotor` 名称，生成网格时就建立了该区域。

`constant/MRFProperties` 中的设置为：

{{file:05-mrf/constant/MRFProperties}}

| 参数 | 本例含义 |
| --- | --- |
| `MRF1` | 这一组 MRF 设置的名称，可用于区分多组区域 |
| `cellZone rotor` | 在 rotor 单元区域应用旋转参考系处理 |
| `active yes` | 启用这一组设置 |
| `origin (0 0 0)` | 转轴经过原点 |
| `axis (0 0 1)` | 绕 z 轴旋转 |
| `omega 104.72` | 角速度 104.72 rad/s，约 1,000 rpm |
| `nonRotatingPatches ()` | 本例没有需要额外排除的区域内静止壁面 |

在转动区域中，局部参考系速度与位置有关：

$$
\mathbf U_\Omega=\boldsymbol\Omega\times(\mathbf x-\mathbf x_0).
$$

因此距离转轴越远，参考系的圆周速度越大。MRF 据此处理区域内的旋转效应、通量及相关边界速度。

## 3. 壁面怎么与参考系配合

`0.orig/U` 中转子壁面写为：

{{block:05-mrf/0.orig/U:boundaryField/rotor}}

本例的 `simpleFoam` 在 MRF 流程中调用边界速度修正，把旋转区域内随转子运动的壁面按 $\boldsymbol\Omega\times\mathbf r$ 更新。读初始场时，再结合 `MRFProperties` 和求解器的 MRF 调用，就能理解最终的转子壁面速度。

`nonRotatingPatches` 用于列出旋转区域内仍需视作静止的壁面，例如穿入该区域的固定支撑件。这里使用空列表，因为静止外壁位于旋转 cellZone 之外。

几何中的叶片方位在计算中固定下来。MRF 适合估计特定相对位置下的近似稳态流动；需要解析叶片经过定子时的周期变化时，可以使用上一课的 AMI 瞬态旋转网格。

## 4. 设置稳态迭代和松弛

{{file:05-mrf/system/controlDict}}

这里 `writeControl timeStep` 配合 `writeInterval 50`，每 50 次迭代保存场。最终到达 `endTime 500` 后结束。

`fvSolution` 中的 SIMPLE 设置与松弛系数为：

{{block:05-mrf/system/fvSolution:SIMPLE}}

{{block:05-mrf/system/fvSolution:relaxationFactors}}

压力采用 0.3 的场松弛；速度和湍流方程采用 0.5 的方程松弛。这样可以减缓相邻迭代之间的变化，使旋转驱动下的耦合系统逐步建立稳定解。

`pRefCell 0` 和 `pRefValue 0` 为压力提供参考值。本例主要由封闭壁面构成，压力场需要一个参考来确定整体常数偏移。

## 5. 线性容差与外迭代各看什么

压力方程的线性求解设置是：

{{block:05-mrf/system/fvSolution:solvers/p}}

`tolerance 1e-08` 控制一次线性求解的绝对残差，`relTol 0.05` 允许残差相对本次初值降低到 5% 后结束。这些线性求解嵌套在 SIMPLE 外迭代中。

右图画的是**每次外迭代开始时**压力和速度方程的残差。500 次迭代结束时，压力约为 $3.56\times10^{-4}$，两个平面速度分量约为 $1.54\times10^{-5}$。继续研究稳态结果时，可同时监测搅拌扭矩和代表位置的速度，判断目标量是否随迭代稳定。

## 6. MRF 与 AMI 怎样选择

| 问题 | MRF | 旋转网格 + AMI |
| --- | --- | --- |
| 网格节点 | 保持固定 | 旋转区节点随时间移动 |
| 叶片相对外壁的位置 | 固定在选定方位 | 随时间连续变化 |
| 常见用途 | 旋转机械近似稳态估计、初始流场 | 叶片通过、周期压力、转动引起的瞬态 |
| 主要配置 | `MRFProperties` | `dynamicMeshDict` 与 AMI 边界 |

两课的网格规模相近，但转速、湍流模型和求解方式不同，图中的速度大小分别对应各自的设置。比较两种方法对同一物理问题的影响时，应先统一转速、物性、几何和流动模型。

来源：[OpenFOAM v2512 mixerVessel2D 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/mixerVessel2D)。
