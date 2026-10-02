水面运动到哪里，就在哪里增加网格；水面离开后，再把细网格合并。这一课用 `interFoam` 和 `dynamicRefineFvMesh` 计算三维水体释放，学习按水相体积分数控制动态加密。

## 1. 算例与初始水体

[下载动态加密算例](/downloads/meshes/v2512-03-refinement.zip)，进入 `foamLabAdvancedMesh/03-refinement` 后运行：

```bash
bash Allrun
```

计算域为 $1\times1\times1$ m 的立方体，基础网格为 $16^3$ 个单元。删去内部障碍物占据的 64 个单元后，初始流体网格有 4,032 个单元。重力沿负 z 方向，y = 1 m 的侧面为大气边界，其余外边界和障碍物表面为壁面。

初始速度为零。`setFieldsDict` 把指定盒子内的水相体积分数设为 1，其余设为 0：

{{file:03-refinement/system/setFieldsDict}}

`alpha.water = 1` 表示水，0 表示空气，0 与 1 之间表示包含界面的混合单元。这里按**单元中心是否位于盒内**赋值，所以实际离散水体的边界随基础网格排列取整。

计算从 0 到 0.3 s，每 0.05 s 保存一次。重力驱动水体运动，求解器在推进两相流的同时更新局部网格。

![动态加密前后的水相分布与网格](/assets/science/advanced-mesh-refinement.png)

图为 x = 0.5 m 截面，竖直方向为 z。水气过渡区附近出现细网格，远处保留粗网格；右图的 8,834 是整个三维计算域的单元总数。

## 2. 读懂动态加密字典

{{file:03-refinement/constant/dynamicMeshDict}}

| 参数 | 本例取值 | 为什么这样设置 |
| --- | --- | --- |
| `refineInterval` | 1 | 每个时间步检查一次界面位置 |
| `field` | `alpha.water` | 根据水相体积分数识别水气界面 |
| `lowerRefineLevel` / `upperRefineLevel` | 0.001 / 0.999 | 选择包含两相的过渡单元 |
| `maxRefinement` | 1 | 最多分裂一级，便于直接观察粗细网格的区别 |
| `maxCells` | 50000 | 控制计算规模的上限 |
| `nBufferLayers` | 1 | 在加密区周围保留缓冲，减少粗细网格反复切换 |
| `unrefineLevel` | 10 | 允许离开加密保护区的单元参与合并；实际合并还受拓扑与缓冲层约束 |
| `dumpLevel` | `true` | 输出 `cellLevel`，在 ParaView 中查看加密级别 |

这个文件的控制参数直接位于字典顶层，与下载包保持一致。

## 3. 一级加密意味着什么

本例使用六面体八叉加密：一个父单元分成八个子单元，三个方向的尺度都减半。基础网格间距为

$$
\Delta x_0=\frac{1}{16}=0.0625\ \mathrm m.
$$

一级加密后，局部间距为 0.03125 m，体积为原来的 $1/8$。如果有 $N_r$ 个单元被分裂且暂时没有合并，总单元数增加 $7N_r$。

初始场由纯水和纯空气单元组成。开始推进后，输运使界面经过的单元出现中间体积分数，随后触发加密。因此，网格数量的变化应沿时间查看。

## 4. 网格变了，通量怎样处理

`correctFluxes` 列出了拓扑变化时涉及的面场：

{{entry:03-refinement/constant/dynamicMeshDict:correctFluxes}}

这里的 `none` 表示该列表不从某个指定的体向量场重建对应通量。下载包沿用这个两相流教程的设置，相关通量由求解器自己的两相输运和压力校正流程处理。

面通量与体积分数共同决定两相质量输运。网格分裂和合并后，新的单元体积、场值映射及面通量都需要保持协调；水量统计可以直接反映这种协调是否良好。

## 5. 细网格也会影响时间步长

{{file:03-refinement/system/controlDict}}

本例开启 `adjustTimeStep`，并将 `maxCo` 与 `maxAlphaCo` 都设为 0.5。对于相同速度，单元尺度减半后，保持相近 Courant 数需要减小时间步长。

体积分数方程还设置了子循环：

{{block:03-refinement/system/fvSolution:solvers/"alpha.water.*"}}

`nAlphaSubCycles 3` 将一个流动时间步中的体积分数输运分成三个子步。它与 `maxAlphaCo` 一起控制界面推进的时间分辨率。

## 6. 看单元数，也看水量

总水量由每个单元中的水相体积相加得到：

$$
V_w(t)=\sum_P\alpha_{w,P}(t)V_P(t).
$$

本例初始水量为 0.087890625 m³。它对应粗网格上实际初始化的水体，而几何盒子的解析体积是 0.084375 m³；差异来自前述按单元中心选取的离散边界。

![单元数与水量变化](/assets/science/advanced-mesh-refinement-history.png)

下载包的 `reference-results/refinement-history.csv` 给出了保存时刻、单元数、水量及体积分数范围。先按 `cellLevel` 着色观察 0 级与 1 级网格，再按 `alpha.water` 着色，就能把加密位置与水面联系起来。

最终普通网格检查通过。完整几何检查还会把粗细交界处的共面分裂面列入 `concaveCells`：本例这些单元仍为凸体，独立逐面检查确认所有顶点位于各外法向平面的内侧或平面上。日志和检查结果随算例说明保留，方便定位到具体的粗细连接处。

## 7. 下一步怎样扩大算例

增加到二级加密时，最细单元的边长将成为基础单元的 $1/4$，体积为 $1/64$；先估计计算规模，再选择 `maxCells`。也可以改用涡量或温度梯度构造加密指示场，让网格跟随其他流动结构。

这个例子采用三维六面体网格。学习二维问题时，可先沿用单层结果展示方式；实际加密设置则应依据所选加密器支持的网格拓扑安排。

来源：[OpenFOAM v2512 damBreakWithObstacle 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreakWithObstacle)。
