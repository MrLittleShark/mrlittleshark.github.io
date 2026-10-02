初始条件规定计算开始时各单元中的值；边界条件规定计算过程中边界上的约束。方腔内部初始静止，顶盖从开始时刻就以恒定速度运动，因此内部速度随后会逐渐发展。

## 场文件中的两部分设置

速度文件 `0/U` 中包含：

```foam
internalField uniform (0 0 0);

boundaryField
{
    movingWall
    {
        type    fixedValue;
        value   uniform (1 0 0);
    }
    fixedWalls
    {
        type    noSlip;
    }
    frontAndBack
    {
        type    empty;
    }
}
```

`internalField` 给出所有单元的初值。顶盖边界 `movingWall` 使用 `fixedValue`，其速度在计算中保持为 $(1,0,0)\,\mathrm{m/s}$。`fixedWalls` 使用 `noSlip`，表示静止壁面上的流体速度为零。`frontAndBack` 对应二维网格的前后面。

![方腔边界条件](/assets/diagrams/core-cavity.svg)

这段内容与文件头、量纲一起组成完整的 `0/U`。修改初值时编辑 `internalField`；修改顶盖速度时编辑 `movingWall` 下的 `value`。两处设置作用的位置不同。

## 边界名称从哪里来

网格的边界区域称为 patch。生成网格后，所有 patch 的名称和类型保存在 `constant/polyMesh/boundary`。用 `blockMesh` 建网格时，这些名称来自 `system/blockMeshDict` 中的 `boundary` 列表。

例如 `blockMeshDict` 的顶盖部分是：

```foam
movingWall
{
    type wall;
    faces
    (
        (3 7 6 2)
    );
}
```

`movingWall` 是名称；`wall` 表示它属于壁面类型；`faces` 用顶点编号列出这个边界包含的面。网格生成后，`0/U` 和 `0/p` 都要有对应的 `movingWall` 条目。

网格中的 `wall` 让程序识别壁面几何，场文件中的 `fixedValue`、`noSlip`、`zeroGradient` 则描述具体物理量的约束。例如同一块壁面，速度可以采用无滑移，温度可以采用固定温度或给定热通量。

## fixedValue 与 zeroGradient

对一个标量场 $\phi$，`fixedValue` 指定边界值：

$$
\phi=\phi_b.
$$

`zeroGradient` 指定沿边界法向的梯度为零：

$$
\frac{\partial\phi}{\partial n}=0.
$$

前者直接给定数值；后者由内部场确定边界值，使边界处的法向变化率为零。例如某单元附近温度为 $300\,\mathrm{K}$，使用零梯度边界时，边界温度会与相邻内部温度相联系。边界值可以随计算变化。

速度是向量场，`fixedValue` 的值需要写三个分量。压力、温度等标量场只写一个数：

```foam
// 速度边界片段
type  fixedValue;
value uniform (1 0 0);
```

```foam
// 标量边界片段
type  fixedValue;
value uniform 0;
```

这两个片段分别放入对应场文件的某个 patch 子字典中。速度文件使用标量值，会产生类型不匹配。

## 方腔的压力如何设置

方腔 `0/p` 的边界部分如下：

```foam
boundaryField
{
    movingWall
    {
        type zeroGradient;
    }
    fixedWalls
    {
        type zeroGradient;
    }
    frontAndBack
    {
        type empty;
    }
}
```

速度边界已经规定壁面运动，压力由压力校正方程计算，用于使速度满足质量守恒。本例所有实体边界采用压力零梯度，因此压力整体加上一个常数后，压力梯度保持相同。

为了确定压力零点，在 `system/fvSolution` 中设置参考值：

```foam
PISO
{
    nCorrectors                 2;
    nNonOrthogonalCorrectors     0;
    pRefCell                    0;
    pRefValue                   0;
}
```

`pRefCell 0` 选择编号为 0 的单元作为参考，`pRefValue 0` 将该处运动学压力设为零。`nCorrectors` 是每个时间步的 PISO 压力校正次数；方腔的正交网格采用 `nNonOrthogonalCorrectors 0`。

参考压力影响压力的整体零点。对这个封闭不可压缩问题，比较压差比比较任意零点下的绝对数值更有物理意义。

## 二维计算为什么使用 empty

OpenFOAM 使用三维网格数据结构。二维平面问题通常在厚度方向保留一个单元，并将两侧设为 `empty`，使离散求解排除该方向。

方腔的配合关系如下：

| 位置 | 设置 |
| --- | --- |
| `blockMeshDict` 的 `blocks` | 厚度方向单元数为 1 |
| `blockMeshDict` 的 `frontAndBack` | `type empty` |
| `0/U` 的 `frontAndBack` | `type empty` |
| `0/p` 的 `frontAndBack` | `type empty` |

`empty` 要与平面几何、单层网格和所有参与求解的场一致。三维管道壁面或真实厚度方向的流动，应使用相应的三维网格和物理边界条件。

## 开放流动中的入口与出口

方腔是封闭域。对于简单的不可压缩通道，常见设置是入口给定速度、出口给定压力：

| 边界 | 速度 `U` | 压力 `p` |
| --- | --- | --- |
| 入口 | `fixedValue`，给定入口速度 | `zeroGradient` |
| 出口 | `zeroGradient`，适合主要向外流出的情况 | `fixedValue`，给定参考压力 |
| 静止壁面 | `noSlip` | 与求解器匹配的压力梯度条件 |

这种配合中，入口流量由速度和入口面积确定，出口压力提供压力基准。出口处存在明显回流时，需要能够处理流向切换的边界条件，并考虑延长出口段，使强回流尽量位于计算域内部。

例如某个标量在流出时用零梯度、流入时给定入口值，可采用下面的片段：

```foam
outlet
{
    type        inletOutlet;
    inletValue  uniform 0;
    value       uniform 0;
}
```

`inletValue` 是发生回流时采用的值，`value` 提供初始边界值。具体数值应根据该标量在外部流体中的状态确定。速度与压力的出口组合还要符合求解器和通量定义，后续通道与湍流算例会给出完整配置。

## 改变初始状态会怎样

将方腔的内部速度设为：

```foam
internalField uniform (0.1 0 0);
```

表示流体起初整体具有向右速度，而壁面仍按 `boundaryField` 约束。初始场与壁面约束之间的差异会在早期调整，压力校正还会修正通量，使其满足连续性。

对稳定存在且唯一的低雷诺数稳态解，不同合理初值通常主要影响达到稳态所需的过程；对于非定常、多稳态或带自由液面的流动，初始状态本身就是物理问题的一部分。此时应根据实验启动过程设置初值。

## 常见错误

| 报错或现象 | 原因 | 处理方法 |
| --- | --- | --- |
| `Cannot find patchField entry` | 场文件缺少网格中的某个 patch | 对照 `constant/polyMesh/boundary` 补齐名称 |
| `inconsistent patch and patchField types` | `empty` 等约束类型在网格和场中不一致 | 同步网格与所有场文件的设置 |
| 速度初始值读入失败 | 向量缺少括号或分量数不对 | 使用 `uniform (Ux Uy Uz)` |
| 封闭域压力方程缺少参考 | 全梯度压力条件下未指定基准 | 检查求解算法字典中的参考压力设置 |
| 顶盖速度改了，几何仍然不动 | 基础方腔采用固定网格上的切向壁面速度 | 几何运动需要另外选择动网格求解设置 |

## 动手练习

在两个新的方腔副本中，分别使用零初速和 `uniform (0.1 0 0)`，保持边界和其他参数相同。比较 $t=0.01\,\mathrm{s}$ 的速度场，再把计算延长，比较后期中心线速度。

第二个练习只改变 `pRefValue`。在重新从相同初值求解后，检查速度、两点压差和压力整体数值：速度与压差应基本一致，压力零点随参考值平移。这个练习可以直接观察参考压力与物理压差的区别。
