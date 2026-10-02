重叠网格把流场分成几套互相覆盖的网格。物体附近的网格可以随物体运动，远处的背景网格保持不动，两者通过插值交换数据。这一课计算二维通道中旋转的矩形物体。

## 1. 算例中有哪两套网格

[下载重叠网格算例](/downloads/meshes/v2512-02-overset.zip)。解压后进入 `foamLabAdvancedMesh/02-overset`，运行：

```bash
bash Allrun
```

背景区域宽、高均为 10 mm，采用 $25\times25\times1$ 个单元。围绕物体另建 $16\times24\times1$ 的网格块，再挖去中间 $2\times4$ mm 的矩形，形成物体表面。两套网格合计保留 881 个流体单元。

流体从左侧以 1 m/s 进入，右侧流出。物体绕 $(5,5)$ mm 旋转，角速度为 20 rad/s，求解器为 `overPimpleDyMFoam`。计算到 0.28 s，每 0.04 s 保存一次。

![旋转网格与背景网格](/assets/science/advanced-mesh-overset.png)

绿色网格表示背景，彩色网格随物体转动。图中同时画出两套几何网格；真正参与方程求解的单元由每一步的重叠关系决定。

## 2. 按顺序建立区域与初始场

`Allrun` 中的准备步骤依次完成：生成网格、选择区域、挖孔、重新识别区域、恢复初始场和写入区域编号。

{{file:02-overset/Allrun}}

`topoSet` 的 `c0` 从背景网格中的一个点出发，选择连通的背景区域；`c1` 选择另外一套网格。`box` 则保留物体以外的流体单元。执行 `subsetMesh box -patch hole -overwrite` 后，新暴露的物体表面归入 `hole` 壁面。

先完成挖孔，再复制 `0.orig`，就能让初始场对应最终的边界结构。下载包中已按这个顺序组织好命令。

## 3. 用 zoneID 区分网格，用 cellZone 指定运动

`zoneID` 是每个单元的网格编号。本例通过 `setFields` 写入：

{{file:02-overset/system/setFieldsDict}}

背景区域编号为 0，旋转区域编号为 1。初始占位值 123 会被这两次区域赋值覆盖。`zoneID` 用于重叠插值；`background` 和 `movingZone` 则是 `blockMeshDict` 中命名的 **cellZone**，供运动设置选取单元。

| 名称 | 存放形式 | 作用 |
| --- | --- | --- |
| `zoneID` | 体标量场 | 区分相互重叠的网格区域 |
| `movingZone` | cellZone | 选择随物体转动的单元 |
| `overset` | 边界 patch | 标识重叠网格的插值边界 |
| `hole` | 壁面 patch | 表示挖除矩形后形成的物体表面 |

## 4. 指定背景静止、局部网格旋转

{{file:02-overset/constant/dynamicMeshDict}}

`multiSolidBodyMotionSolver` 为不同 cellZone 分别指定运动。背景使用零速度的 `linearMotion`，旋转区域使用 `rotatingMotion`。`origin` 给出转轴上一点，`axis (0 0 1)` 给出转轴方向，正角速度遵循右手定则。

经过时间 $t$，转过的角度为

$$
\theta=\omega t.
$$

本例在 0.28 s 时转过 5.6 rad，约 $320.9^\circ$。整个旋转区域始终位于背景范围内，周围留有重叠带供插值使用。

物体表面的速度条件为：

{{block:02-overset/0.orig/U:boundaryField/hole}}

它随网格运动更新壁面速度。外侧 `overset` 边界则由 `#includeEtc "caseDicts/setConstraintTypes"` 引入相应的约束边界设置。

## 5. 配置插值和压力求解

在 `system/fvSchemes` 中找到：

{{block:02-overset/system/fvSchemes:oversetInterpolation}}

`inverseDistance` 按距离构造插值权重；距离接收单元较近的供体对插值结果影响较大。`searchBox` 覆盖本例的整个几何范围，`searchBoxDivisions` 将搜索空间划分为体素，帮助寻找候选供体。由于计算只有一层厚度，z 方向设为 1。

重叠插值会改变代数系统的耦合关系。本例压力使用适合非对称矩阵的求解器：

{{block:02-overset/system/fvSolution:solvers/p}}

`PBiCGStab` 配合 `DILU`，绝对容差为 $10^{-6}$。设置 `relTol 0` 后，每次压力求解都按这个绝对容差完成。

## 6. 从日志看懂单元分类

`log.overPimpleDyMFoam` 会在时间推进中输出三类主要单元数量：

| 输出 | 含义 |
| --- | --- |
| `calculated` | 直接参与离散方程求解的单元 |
| `interpolated` | 从另一套网格取得插值信息的单元 |
| `hole` | 被屏蔽的单元，例如落入物体覆盖区的背景单元 |

随着转子运动，这些数量会改变，几何网格总数仍为 881。下载包附有按时间整理的区域统计，便于与日志对照。

在 ParaView 中按 `zoneID` 着色，可以先分清两套网格，再查看 `U`。为了便于读取，脚本导出保存时刻的 VTK 结果；第一个导出时刻为 0.04 s。

扩大物体运动范围时，应同时扩大背景域或调整覆盖区域。细化物体表面网格时，也要考虑重叠带两侧的单元尺度：供体与接收单元的尺寸相近，通常更有利于平稳传递信息。

来源：[OpenFOAM v2512 rotatingSquare 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/overPimpleDyMFoam/rotatingSquare)。本例调整了旋转中心、挖孔位置及搜索范围，使旋转网格位于背景域内。
