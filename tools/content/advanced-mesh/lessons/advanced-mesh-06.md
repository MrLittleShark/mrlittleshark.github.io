SRF 使用一个统一的旋转参考系。整个流场都在这个参考系中描述，求解的主要速度变量为相对速度 `Urel`。这一课运行三维旋转通道，学习转速设置、绝对与相对速度转换，以及静止入口在旋转坐标系中的边界条件。

## 1. 看清流向与旋转方向

[下载 SRF 算例](/downloads/meshes/v2512-06-srf.zip)，进入 `foamLabAdvancedMesh/06-srf` 后运行：

```bash
bash Allrun
```

计算域为四分之一周向扇区，两侧使用旋转周期边界，沿 z 方向有入口和出口。流体从 z = 0.2 m 一侧以绝对速度 $(0,0,-10)$ m/s 进入，向 z = 0 一侧流出。内壁随参考系旋转，外壁在绝对坐标系中静止。

求解器为 `SRFSimpleFoam`，湍流模型为 `kOmegaSST`，网格有 33,600 个单元。转速为 1,000 rpm，进行 1,000 次稳态迭代，每 100 次保存一次。

![SRF 相对速度与绝对速度的截面比较](/assets/science/advanced-mesh-srf.png)

两图显示同一截面上的不同速度定义。相对速度表示随转子一起观察时的流体运动，绝对速度表示静止观察者看到的流动。

## 2. 指定单一旋转参考系

{{file:06-srf/constant/SRFProperties}}

`SRFModel rpm` 选择以每分钟转数表示的模型。`origin` 和 `axis` 定义转轴，`rpmCoeffs` 中的 `rpm 1000` 给出转速。

这一文件直接使用 rpm；上一课 MRF 的 `omega` 使用 rad/s。两者通过下式换算：

$$
\Omega=\frac{2\pi\times1000}{60}\approx104.72\ \mathrm{rad/s}.
$$

SRF 应用于整个求解域，所以这里采用一个统一的转轴与转速。

## 3. 从 Urel 得到绝对速度

相对速度、绝对速度和参考系速度的关系为：

$$
\mathbf U=\mathbf U_{\mathrm{rel}}+
\boldsymbol\Omega\times(\mathbf x-\mathbf x_0).
$$

例如，距转轴 0.05 m 处的参考系圆周速度约为 5.236 m/s。即使流体在绝对坐标系中仅沿轴向进入，在旋转参考系中也会带有反向圆周速度。

求解器读取 `0/Urel` 并求解相对速度，随后重建并输出绝对速度 `U`。查看云图时，可以分别选这两个字段；它们的差值随位置变化，恰好对应参考系的局部旋转速度。

## 4. 用绝对入口速度设置相对速度边界

{{block:06-srf/0/Urel:boundaryField/inlet}}

`inletValue` 给出入口值，`relative no` 表明这个值按**绝对速度**解释。`SRFVelocity` 将其转换为当前旋转参考系下的 `Urel` 边界值。

这里的绝对入口速度沿负 z 方向，大小为 10 m/s。入口面各点距离转轴不同，转换后圆周分量也不同；采用该边界条件即可按每个面的位置完成转换。

外侧静止壁面使用同一类型：

{{block:06-srf/0/Urel:boundaryField/outerWall}}

它的绝对速度为零。转换后的相对速度为 $-\boldsymbol\Omega\times\mathbf r$，表示外壁相对于旋转参考系向反方向运动。

内侧随转子运动的壁面设置为：

{{block:06-srf/0/Urel:boundaryField/innerWall}}

这里的无滑移条件作用在 `Urel` 上：壁面相对旋转参考系静止，绝对坐标系中则随转子运动。

## 5. 用周期边界表示其余扇区

四分之一扇区两侧分别为 `cyclic_half0` 与 `cyclic_half1`。网格边界中给出旋转配对关系，速度场中选择 `cyclic`：

{{block:06-srf/0/Urel:boundaryField/cyclic_half0}}

周期面将一个扇区的出入信息传给相邻扇区，使计算代表周向重复结构。这里两个周期面的网格对应匹配，因此采用 `cyclic`；上一课持续改变相对方位的接口使用 `cyclicAMI`。

## 6. 完成迭代并查看结果

{{file:06-srf/system/controlDict}}

`endTime 1000` 对应 1,000 次稳态迭代，输出目录 `1000/` 中可同时找到 `Urel` 和 `U`。网格坐标在整个计算过程中保持不变。

在 ParaView 中打开 `case.foam`，选择最后一次输出，使用 **Slice** 在 z = 0.1025 m 处切面。先按 `Urel` 着色，再换成 `U`，观察两者在靠近转轴和远离转轴处的差异。

| 建模需求 | 适合进一步学习的方法 |
| --- | --- |
| 整个求解域使用相同转速 | SRF |
| 部分区域旋转、部分区域静止的近似稳态 | MRF |
| 需要真实跟踪转子经过固定部件 | 旋转网格 + AMI |
| 物体有大幅移动，局部网格需要独立运动 | 重叠网格 |

这几种方法都能描述运动设备，但选择的参考系、网格运动方式及输出速度的含义各有不同。实际建模时，先确定想观察的流动过程，再选择相应方法。

来源：[OpenFOAM v2512 SRFSimpleFoam/mixer 教程](https://develop.openfoam.com/Development/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/SRFSimpleFoam/mixer)。
