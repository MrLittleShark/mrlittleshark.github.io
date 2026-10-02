搅拌器中的叶片不断转动，外壁保持静止。旋转网格方法让叶片附近的网格实际转动，再用 AMI 在旋转区与静止区之间传递流动信息。本课运行一个二维搅拌槽，观察叶片、网格和接口的变化。

## 1. 运行半圈旋转

[下载旋转网格与 AMI 算例](/downloads/meshes/v2512-04-ami.zip)，进入 `foamLabAdvancedMesh/04-ami` 后运行：

```bash
bash Allrun
```

网格共有 3,072 个单元，厚度方向一层，前后采用 `empty`。转轴沿 z 方向，转速约为每秒 1 圈。`pimpleFoam` 从静止流体开始计算，到 0.5 s 结束，每 0.1 s 保存结果。

![AMI 网格转动前后的速度分布](/assets/science/advanced-mesh-ami.png)

两图使用相同色标。0.1 s 时转子转过约 $36^\circ$，内部网格随之改变方位，外部网格仍在原位。两区之间的圆形接口是 AMI。

## 2. 建立分开的旋转区和静止区

算例使用 `system/blockMeshDict.m4` 描述重复的圆周分块。脚本先用 m4 展开宏，再交给 `blockMesh`：

{{file:04-ami/Allrun}}

`blockMeshDict.m4` 中，旋转部分的块带有 `rotor` 标记，生成同名 cellZone。接口两侧分别命名为 `AMI1` 和 `AMI2`；它们在几何上重合，在拓扑上保持分开。

`topoSet` 在这里选取接口面，生成名为 `AMI` 的 faceSet，便于查看。旋转区域的 cellZone 已由 `blockMesh` 建立。

{{file:04-ami/system/topoSetDict}}

## 3. 设置转轴和角速度

{{file:04-ami/constant/dynamicMeshDict}}

`motionSolver solidBody` 将指定区域当作刚体移动，旋转区内部各节点之间的距离保持不变。`cellZone rotor` 限定转动范围；外侧单元保持静止。

`omega 6.2832` 的单位为 rad/s。角速度与每分钟转数的关系为

$$
\omega=\frac{2\pi n}{60}.
$$

本例对应约 60 rpm。在 0.5 s 内，旋转角度约为 $\pi$，即半圈。转轴位置与圆形接口的圆心一致，转动时两侧接口继续覆盖同一圆周。

## 4. 两侧接口怎样连接

生成的网格中，AMI 边界使用 `cyclicAMI`，并通过 `neighbourPatch` 相互指向。字段也要选择相应边界类型，例如 `0.orig/U` 中的速度：

{{block:04-ami/0.orig/U:boundaryField/AMI1}}

{{block:04-ami/0.orig/U:boundaryField/AMI2}}

AMI 根据两侧面之间的几何重叠计算权重。一个接收面可以从多个对侧面取得信息，因此两侧网格可以采用不同的面划分；旋转后则更新面之间的重叠关系。

转子表面使用：

{{block:04-ami/0.orig/U:boundaryField/rotor}}

`movingWallVelocity` 从网格运动取得壁面速度。静止外壁也使用同一类型，因为其网格速度为零，得到的壁面速度相应为零。

## 5. 控制转动过程的时间分辨率

{{file:04-ami/system/controlDict}}

初始时间步为 0.001 s，随后按 `maxCo 0.5` 调整。每步转角为

$$
\Delta\theta=\omega\Delta t.
$$

以初始时间步计算，每步约转 $0.36^\circ$。输出间隔 0.1 s 决定保存多少幅结果，时间步则决定求解时运动推进得多细。研究叶片经过固定位置时的压力波动，需要根据叶片通过频率同时安排这两个尺度。

在 `fvSolution` 中，PIMPLE 控制压力与速度的校正次数：

{{block:04-ami/system/fvSolution:PIMPLE}}

## 6. 查看接口权重与实际网格运动

打开 `log.pimpleFoam`，查找 `AMI` 和 `sum(weights)`。本次计算中，记录到的接口权重和最小值为 1，最大值约为 1.00027，接近完整覆盖对应的 1。这个量帮助判断两侧接口的几何覆盖与插值情况。

在 ParaView 中按以下顺序查看：

1. 打开 `case.foam`，选择 **Surface With Edges**，观察初始圆形接口。
2. 切换到 0.1 s，确认叶片附近网格转动、外侧网格不动。
3. 按 `U` 大小着色，观察叶片对周围流体的驱动。
4. 播放到 0.5 s，检查接口两侧始终保持接触，流场能跨接口延伸。

本例使用层流模型，作用是展示真实转动与接口交换。继续扩展到三维叶轮时，需要同时安排叶片附近网格、旋转区外径和端部间隙；旋转区应完整包住随转子运动的表面。

来源：[OpenFOAM v2512 mixerVesselAMI2D 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D)。
