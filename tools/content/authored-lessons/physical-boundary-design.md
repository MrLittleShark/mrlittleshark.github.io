边界条件规定了流体怎样进入、离开计算域，以及怎样与壁面接触。例如，已知入口速度和出口压力时，计算结果会给出域内的压力分布、出口速度和壁面剪切力。入口、出口和壁面的名称写在网格中，各物理量的条件则写在 `0/U`、`0/p` 等场文件中。

## 先区分网格边界和场边界

`constant/polyMesh/boundary` 记录边界面属于哪一个 patch。常见的网格类型有 `patch`、`wall`、`empty`、`symmetryPlane` 和 `cyclic`。`0/U` 中的 `fixedValue`、`noSlip`、`zeroGradient` 等类型，负责计算该 patch 上的速度。

这两个层次需要配合。例如，实体壁面在网格中设为 `wall`，速度场可设为 `noSlip`；二维算例厚度方向的两个面在网格和所有场文件中均使用 `empty`。这样，程序既知道边界的几何属性，也知道需要怎样处理各个变量。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-multiphase-ship-boundaries.png" alt="自由液面计算域与边界定义" loading="lazy"><figcaption><strong>自由液面计算域与边界定义</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 88 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 实例：pitzDaily 的入口、出口和壁面

本例是带台阶的二维通道，使用 `simpleFoam` 计算稳态流动。进入下载包中的 `tutorials/incompressible/simpleFoam/pitzDaily`，打开 `0/U`。其中的 `boundaryField` 为：

```foam
boundaryField
{
    inlet
    {
        type  fixedValue;
        value uniform (10 0 0);
    }
    outlet
    {
        type zeroGradient;
    }
    upperWall
    {
        type noSlip;
    }
    lowerWall
    {
        type noSlip;
    }
    frontAndBack
    {
        type empty;
    }
}
```

`inlet` 等名称与网格中的 patch 一一对应。`uniform (10 0 0)` 表示入口各面均取相同的速度，三个分量分别沿 x、y、z 方向，单位是 m/s。`noSlip` 将静止壁面上的速度设为零。出口的 `zeroGradient` 表示速度沿边界法向的梯度为零，边界值由相邻内部单元外推得到。

压力场的入口和出口设置与速度不同。`0/p` 中相应片段是：

```foam
inlet
{
    type zeroGradient;
}
outlet
{
    type  fixedValue;
    value uniform 0;
}
upperWall
{
    type zeroGradient;
}
lowerWall
{
    type zeroGradient;
}
```

入口速度已经指定，入口压力由内部流动决定；出口压力固定为参考值，出口速度则由连续性和动量方程求出。这个组合适合学习给定流量下的通道流动。

本例 `p` 的量纲是 `[0 2 -2 0 0 0 0]`，表示运动学压力，即物理压力除以恒定密度。因此，出口的零值是参考压力。两个位置的物理压差由下式换算：

\[
\Delta p_{\mathrm{Pa}}=\rho\,\Delta p_{\mathrm{OpenFOAM}}.
\]

例如密度为 $1.2\ \mathrm{kg/m^3}$、场中的压差为 $20\ \mathrm{m^2/s^2}$ 时，物理压差为 $24\ \mathrm{Pa}$。对于使用 Pa 压力的可压缩求解器，直接采用场中的压差即可。

## 已知体积流量时怎样设置入口

如果实验给定的是体积流量，可以将 `0/U` 的入口改成：

```foam
inlet
{
    type               flowRateInletVelocity;
    volumetricFlowRate constant 0.002;
    value              uniform (0 0 0);
}
```

`volumetricFlowRate` 的单位是 m³/s，正数表示流入。该条件按入口面积计算法向速度，使整个入口满足给定流量；`value` 为字段初始化提供值，运行时入口速度由流量条件更新。若入口面积为 $0.01\ \mathrm{m^2}$，本例对应的平均法向速度是 $0.2\ \mathrm{m/s}$。

二维模型仍有实际网格厚度，体积流量包含这一厚度。将二维截面厚度缩小十倍而保持体积流量不变，入口平均速度会增大十倍。处理二维实验数据时，需要先把“单位厚度流量”换算成当前网格厚度下的流量。

## 出口发生回流时

出口局部速度指向域内时，需要给进入计算域的温度、组分或湍流量指定值。例如，输运标量 `C` 的外界值为零，可以使用：

```foam
outlet
{
    type       inletOutlet;
    inletValue uniform 0;
    value      uniform 0;
}
```

`inletOutlet` 根据面通量切换：流出时采用零梯度，流入时采用 `inletValue`。这里的数值应对应域外环境；温度场需要填写温度，湍动能场需要填写湍动能。向量场则使用 `(x y z)` 形式。

速度与压力还可以配合 `pressureInletOutletVelocity` 等条件，用于压力驱动的开口。选用时一起检查速度、压力以及回流携带的各个标量。若出口正好切过主要分离涡，将出口移到更下游通常更便于建立稳定的出流边界。

## 对称面、周期面和滑移壁面

| 边界 | 表示的物理关系 | 设置要点 |
| --- | --- | --- |
| `symmetryPlane` | 两侧流场关于平面对称 | 网格和场均使用相应对称类型，边界应为平面 |
| `slip` | 法向速度为零，切向速度可滑移 | 可用于理想化无摩擦壁面，区别于黏性固壁 |
| `cyclic` | 一侧离开的流动从配对面进入 | 网格中建立 `neighbourPatch` 配对及几何变换，场中使用 `cyclic` |
| `empty` | 忽略一个空间方向的变化 | 用于符合二维网格要求的前后面 |

周期管道需要额外的驱动力，例如压力梯度或适当的动量源。两端使用周期条件后，单靠周期映射不会产生持续流量。

## 运行并检查边界是否按预期工作

在新的 pitzDaily 副本中运行：

```bash
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
simpleFoam > log.simpleFoam 2>&1
paraFoam
```

先查看入口速度是否为 `(10 0 0)`，再查看壁面速度和出口压力。流场应出现台阶下游的分离与再附着区域。对入口、出口的 `phi` 求和，可比较体积流量收支；OpenFOAM 的边界面法向朝向域外，因此入口通量通常为负，出口为正。

| 现象或报错 | 检查位置 | 处理方法 |
| --- | --- | --- |
| `Cannot find patchField entry` | `boundary` 与各场的 `boundaryField` | 为提示的 patch 补齐对应场条件，检查大小写 |
| 壁面函数报告 patch 类型错误 | 网格边界类型 | 将对应实体面设为 `wall` 并重新生成网格 |
| 入口流量比预期大很多 | 几何单位、二维厚度、入口面积 | 根据实际面积重新计算速度或流量 |
| 出口附近持续出现大涡和剧烈波动 | 出口位置和回流条件 | 延长出口段，设置符合外界状态的回流值 |

## 练习：改变一个边界量

将入口速度从 10 m/s 改为 5 m/s，保持几何和黏度不变。入口体积流量应减半，雷诺数也随之减半；重新比较压降和回流区长度。湍流入口采用固定湍流强度时，还需要按新速度重新计算 `k`、`epsilon` 或 `omega`，计算方法见下一课。

进阶时可以建立圆管层流案例，与充分发展解 $\Delta p/L=32\mu\bar U/D^2$ 比较。这里 $D$ 是管径、$\bar U$ 是截面平均速度、$\mu$ 是动力黏度。取压截面应避开入口发展段。pitzDaily 是台阶通道，适合研究分离流动，其压降由相应几何和湍流状态决定。
