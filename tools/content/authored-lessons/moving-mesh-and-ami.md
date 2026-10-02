旋转叶轮、往复活塞和运动阀门需要描述物体相对流体的位置变化。OpenFOAM 提供几种处理方式：MRF 在旋转参考系中计算平均流动；动网格直接改变网格点的位置；AMI 则在两侧不共形的网格界面之间传递数据。具体选择取决于是否需要保留随时间变化的相对位置。

## MRF、网格变形与滑移网格

| 方法 | 网格怎样变化 | 常见用途 |
| --- | --- | --- |
| MRF | 网格保持固定，在指定区域加入旋转参考系项 | 稳态叶轮性能、初步设计比较 |
| 变形网格 | 边界运动，内部点随之移动 | 活塞、阀门、小幅振动 |
| 刚体运动加 AMI | 一部分网格整体运动，接口重新插值 | 转子—定子瞬态相互作用、滑移网格 |

<figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-rotor-zones.png" alt="旋转区域、静止区域与连接界面" loading="lazy"><figcaption><strong>旋转区域、静止区域与连接界面</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 153 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

MRF 中转子和定子的相对方位固定，适合建立某一相对位置下的稳态近似。需要叶片经过引起的周期载荷时，采用真实旋转的瞬态网格，并分析多个旋转周期。

## 实例一：刚体旋转的 dynamicMeshDict

进入下载包中的 `tutorials/incompressible/pimpleFoam/laminar/mixerVesselAMI2D/mixerVesselAMI2D`。`constant/dynamicMeshDict` 主体是：

```foam
dynamicFvMesh dynamicMotionSolverFvMesh;

motionSolver solidBody;
cellZone rotor;

solidBodyMotionFunction rotatingMotion;
origin (0 0 0);
axis   (0 0 1);
omega  6.2832;
```

`dynamicMotionSolverFvMesh` 使用运动求解器更新网格。`solidBody` 保持所选网格区域的相对形状，`cellZone rotor` 指定运动单元区，`rotatingMotion` 给出绕轴旋转。

`origin` 是旋转轴经过的点，`axis` 是轴方向；这里绕 z 轴旋转。`omega` 的单位是 rad/s，正方向遵循右手定则。`6.2832` 约为每秒一周，旋转周期 $T=2\pi/\omega\approx1\ \mathrm{s}$。转速为 $N$ rpm 时，角速度换算为 $\omega=2\pi N/60$。

`rotor` 由该案例的 `topoSet` 创建。网格中需要存在同名 cellZone，运动字典才能选择到对应区域。旋转轴的原点发生偏移时，整个旋转轨迹也会改变，因此应先观察网格运动再分析流场。

## AMI 接口怎样连接两侧网格

AMI 根据接口两侧面的几何重叠建立插值权重。两侧可以有不同的面数量和面尺寸，旋转时会更新映射。网格 patch 采用 `cyclicAMI` 并设置邻接 patch，场文件中采用相应的 `cyclicAMI` 条件。

```foam
rotorInterface
{
    type cyclicAMI;
}
statorInterface
{
    type cyclicAMI;
}
```

上面是场文件的边界片段，patch 名用于说明成对关系；实际案例沿用自己的网格名称。几何配对、`neighbourPatch` 和旋转变换设置位于网格生成字典或 `constant/polyMesh/boundary`。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-ami-interface.png" alt="AMI 旋转接口两侧的非共形网格" loading="lazy"><figcaption><strong>AMI 旋转接口两侧的非共形网格</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 159 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

两侧接口应在空间上覆盖相同的连接区域，法向分别朝向各自网格外部。运行日志中的 AMI 权重统计可以帮助发现覆盖不足或配对错误。只有局部区域开放的几何，需要另外定义实际的连通区域和相应接口方法。

案例的 `Allrun.pre` 用 `m4` 从参数化模板生成 `blockMeshDict`，然后运行 `blockMesh` 和 `topoSet`。串行学习流程为：

```bash
./Allrun.pre > log.prepare 2>&1
pimpleFoam > log.pimpleFoam 2>&1
paraFoam
```

该流程需要 `m4`；完整 `Allrun` 还提供并行步骤。显示网格边线并播放时间序列，可以看到旋转区整体转动，外部静止区保持位置。

## 实例二：movingCone 的变形网格

`movingCone` 使用网格速度的扩散方程，把运动壁面的速度向内部网格传播。`dynamicMeshDict` 为：

```foam
dynamicFvMesh dynamicMotionSolverFvMesh;
motionSolverLibs (fvMotionSolvers);
motionSolver velocityComponentLaplacian;

component   x;
diffusivity directional (1 200 0);
```

`velocityComponentLaplacian` 求解一个坐标分量的网格运动速度；`component x` 表示这里只求 x 方向。`diffusivity` 控制内部网格运动的平滑分布，`directional` 给不同方向设置不同的扩散权重。这个系数描述网格运动传播方式，与流体的运动黏度属于不同设置。

对应的 `0/pointMotionUx` 是定义在网格点上的标量场，量纲为速度。运动壁面的片段为：

```foam
movingWall
{
    type         uniformFixedValue;
    uniformValue constant 1;
}
fixedWall
{
    type         uniformFixedValue;
    uniformValue constant 0;
}
```

运动壁面的网格点以 x 方向 1 m/s 移动，固定壁面的网格速度为零。内部点的运动由扩散方程求得。流体速度 `U` 的运动壁面条件则需要与壁面运动配合，常用 `movingWallVelocity` 根据网格运动更新无滑移速度。

更换为位移型运动求解器时，所需场可能是 `pointDisplacement`，量纲变为长度。速度型与位移型方法应分别使用匹配的初始场和边界条目。

## MRF 字典的基本写法

具备 `rotor` 单元区的 MRF 案例可在 `constant/MRFProperties` 中设置：

```foam
MRF1
{
    active              yes;
    cellZone            rotor;
    nonRotatingPatches  ();
    origin              (0 0 0);
    axis                (0 0 1);
    omega               6.2832;
}
```

`MRF1` 是该旋转区的名称。`nonRotatingPatches` 列出旋转区域中仍应按静止壁面处理的 patch，例如某些穿过旋转 cellZone 的静止外壳。空列表适合没有此类特殊壁面的配置。MRF 与真实运动网格对壁面速度和参考系的处理不同，比较时应确认输出速度的定义及模型接口。

## 时间步与运动质量

旋转网格每步的角位移为 $\Delta\theta=\omega\Delta t$。本例 $\omega\approx2\pi\ \mathrm{rad/s}$，时间步 0.001 s 对应约 $0.36^\circ$。接口单元尺度、叶片经过频率以及目标载荷变化共同决定需要的角分辨率。

变形网格还需考虑边界位移相对于局部单元尺寸的比例。运动持续压缩某些单元时，应查看最小体积、非正交度和扭曲程度。对于输出了运动网格的时刻，可使用 `checkMesh -latestTime` 检查最新网格；需要覆盖整个运动周期时，对相应输出时间逐一检查。

网格运动下，穿过网格面的质量传输由流体与网格的相对速度决定：

\[
\dot m_f=\rho_f(\mathbf U_f-\mathbf U_{m,f})\cdot\mathbf S_f.
\]

$\mathbf U_m$ 是网格速度，$\mathbf S_f$ 是有向面面积。后处理 `phi` 时，需要确认当前求解器写出的通量采用相对还是绝对定义，才能正确解释质量收支。

## 常见问题与练习

| 现象 | 检查位置 |
| --- | --- |
| 提示找不到 cellZone | `topoSet` 是否完成、`cellZone` 名称是否一致 |
| AMI 面匹配或权重异常 | 两侧几何覆盖、法向、配对名称和旋转变换 |
| 运动开始后单元体积变负 | 局部变形、时间步、网格运动扩散设置及可用运动范围 |
| 网格在动而壁面流体速度错误 | `U` 的运动壁面条件及参考系设置 |

将 AMI 案例角速度增加一倍，同时先将时间步减半，保持每步角位移接近原值。观察旋转周期是否减半，再比较扭矩和速度历史。随后固定转速，只减半时间步，检查载荷曲线的幅值与相位是否接近。进阶时可以比较 MRF 平均结果与滑移网格的周期平均结果，分析叶片—定子相互作用带来的差异。
