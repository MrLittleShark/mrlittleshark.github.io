VOF 用体积分数记录每个网格单元内各相占据的比例。以水和空气为例，`alpha.water=1` 表示单元充满水，`alpha.water=0` 表示充满空气，介于 0 和 1 之间的单元位于界面附近。水面随流动改变位置，网格可以保持固定。

## 溃坝案例计算什么

初始时，水柱位于容器左下方；释放后，水在重力作用下向右铺展，遇到障碍物和侧壁后形成回卷。案例使用 `interFoam`，需要速度 `U`、压力变量 `p_rgh` 和水相体积分数 `alpha.water`。

打开下载包中的 `tutorials/multiphase/interFoam/laminar/damBreak/damBreak`。外层同名目录还包含其他算例和批处理脚本，本课在内层具有 `0.orig`、`constant`、`system` 的目录操作。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-vof-volume-fraction.png" alt="相分数如何表示网格内的界面" loading="lazy"><figcaption><strong>相分数如何表示网格内的界面</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 78 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

对于此处的不可压缩两相模型，混合密度为：

\[
\rho=\alpha_w\rho_w+(1-\alpha_w)\rho_a.
\]

$\rho_w$、$\rho_a$ 分别是水和空气密度，$\alpha_w$ 是水相体积分数。界面单元通过体积分数连接两相物性；界面宽度受到网格和离散方法的影响。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-multiphase-dambreak-workflow.png" alt="溃坝算例的完整计算流程" loading="lazy"><figcaption><strong>溃坝算例的完整计算流程</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module1.pdf，p. 154 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

网格生成后，`setFields` 写入初始水柱，`interFoam` 推进流动，函数对象和 ParaView 提取计算结果。本课的规则容器由 `blockMesh` 生成；带曲面障碍物的案例还可在背景网格上使用 `snappyHexMesh`。

## 第一步：物性和重力

`constant/transportProperties` 的主体是：

```foam
phases (water air);
water
{
    transportModel Newtonian;
    nu  1e-06;
    rho 1000;
}
air
{
    transportModel Newtonian;
    nu  1.48e-05;
    rho 1;
}
sigma 0.07;
```

`phases` 中的相名决定了 `alpha.water` 的字段名称。`nu` 是运动黏度，单位 m²/s；`rho` 是密度，单位 kg/m³；`sigma` 是表面张力系数，单位 N/m。`Newtonian` 表示此处黏度不随剪切率改变。

重力写在 `constant/g` 中。此算例的竖直方向是 y，重力方向应与几何一致。压力变量通常写为 $p_{rgh}=p-\rho gh$，其中 $gh$ 包含重力与位置的关系。把静水压力贡献分离出来，有利于处理受重力作用的两相流。

## 第二步：建立初始水柱

先生成网格，再用 `setFields` 对选定单元赋值。`system/setFieldsDict` 的主要内容为：

```foam
defaultFieldValues
(
    volScalarFieldValue alpha.water 0
);

regions
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues
        (
            volScalarFieldValue alpha.water 1
        );
    }
);
```

`defaultFieldValues` 先将全部内部单元设为空气。`boxToCell` 根据单元中心位置选取长方体内的单元，将这些单元中的 `alpha.water` 改为 1。两个坐标分别是盒子的最小角点和最大角点，单位与网格一致。

这里水柱宽 0.1461 m、高 0.292 m；z 方向范围覆盖整个二维网格厚度。由于按单元中心选择，初始界面位置存在网格尺度的离散误差。修改水柱尺寸后，应重新执行初始化，并查看初始的相分数分布。

在新的算例副本中执行：

```bash
cp -r 0.orig 0
blockMesh > log.blockMesh 2>&1
setFields > log.setFields 2>&1
paraFoam
```

`0.orig` 保存未初始化的字段模板；第一条命令在还没有 `0` 的新副本中建立初始时间目录。此时打开 ParaView，选择时间 0，以 `alpha.water` 着色，应看到左下角的水柱。已有计算结果的算例，宜另建副本进行初始化实验，以便保留原结果。

## 第三步：开口边界怎样配合

顶部 `atmosphere` 允许空气进出。`0/alpha.water` 中使用：

```foam
atmosphere
{
    type       inletOutlet;
    inletValue uniform 0;
    value      uniform 0;
}
```

流入时设置为纯空气，流出时外推内部相分数。与它配套，`U` 使用 `pressureInletOutletVelocity`，`p_rgh` 使用案例提供的 `totalPressure`。壁面速度采用 `noSlip`，压力采用 `fixedFluxPressure`，使压力梯度与指定的壁面通量相协调。

若要研究接触角，需要选择适合模型的相分数壁面条件，并给出接触角或相关参数。基础溃坝案例的零梯度相分数壁面用于其现有教学设置。

## 第四步：时间步与界面输运

案例 `controlDict` 中启用了自动时间步：

```foam
deltaT         0.001;
adjustTimeStep yes;
maxCo          1;
maxAlphaCo     1;
maxDeltaT      1;
```

`deltaT` 是初始时间步；`maxCo` 限制整体流动 Courant 数，`maxAlphaCo` 限制界面附近的 Courant 数，`maxDeltaT` 给出时间步上限。运行时程序根据当前速度和网格调整步长。减小这些限制通常增加时间步数，可以用于检查界面运动对时间分辨率的敏感性。

`fvSolution` 中，原案例相分数条目的核心设置为：

```foam
"alpha.water.*"
{
    nAlphaCorr      2;
    nAlphaSubCycles 1;
    cAlpha          1;
    MULESCorr       yes;
    nLimiterIter   5;
    solver         smoothSolver;
    smoother       symGaussSeidel;
    tolerance      1e-8;
    relTol         0;
}
```

`nAlphaCorr` 控制相分数校正次数，`nAlphaSubCycles` 将相分数更新划分为子步，`cAlpha` 控制人工界面压缩强度。`MULESCorr` 启用相应的 MULES 校正，限制器帮助控制相分数的有界性。过强的压缩会影响界面形状和局部噪声，参数应结合网格、时间步与观测量进行比较。

现在运行：

```bash
interFoam > log.interFoam 2>&1
```

日志包含当前时间、Courant 数以及相分数范围。用 ParaView 的 Contour 提取 `alpha.water=0.5` 可以显示界面；二维算例也可直接查看相分数截面和速度矢量。

## 检查水量和时间变化

域内水体积可以由 $V_w=\sum_i\alpha_{w,i}V_i$ 计算。将以下对象加入 `controlDict` 已有的 `functions`：

```foam
waterVolume
{
    type          volFieldValue;
    libs          (fieldFunctionObjects);
    regionType    all;
    operation     volIntegrate;
    fields        (alpha.water);
    writeFields   false;
    writeControl  timeStep;
    writeInterval 1;
}
```

`volIntegrate` 将体积分数乘各单元体积后求和，输出的单位是 m³。初始结果应接近水柱宽、高与网格厚度的乘积，差异主要来自单元选择。水尚未流出顶部时，观察该值是否保持稳定；若水流出开口，需要把出口水相通量计入总体收支。

## 常见问题与练习

`setFields` 找不到 `alpha.water` 时，检查 `0` 是否已经建立、相名是否一致。整个域仍为蓝色时，查看初始化日志是否选中了单元，并核对坐标和几何缩放。界面附近出现剧烈压力波动时，定位局部网格质量、时间步、密度比和表面张力作用，再调整对应设置。

练习时保留相同的初始水柱，分别用原网格和加密网格计算，并将 `maxAlphaCo` 从 1 减到 0.5 作时间步比较。比较同一物理时刻的水前沿位置、壁面水位和水体积曲线。这样可以分别观察空间分辨率与时间分辨率对结果的影响。

进一步研究液滴或毛细流时，还需关注曲率计算、接触角以及表面张力对应的时间尺度。这类问题中，表面张力可比惯性更重要，溃坝的默认设置需要随物理尺度调整。
