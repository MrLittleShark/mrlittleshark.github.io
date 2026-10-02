壁面附近的速度从壁面值逐渐变化到主流值，法向梯度通常很大。阻力、壁面剪切和换热都与这一梯度有关。近壁网格的任务是描述这段变化，而 $y^+$ 用来表示第一层单元中心在近壁区域中的位置。

## y⁺ 的定义

\[
y^+=\frac{u_\tau y}{\nu},
\qquad
u_\tau=\sqrt{\frac{|\tau_w|}{\rho}},
\qquad
u^+=\frac{U}{u_\tau}.
\]

$y$ 是壁面到第一层单元中心的距离，$\nu$ 是运动黏度，$\tau_w$ 是壁面剪切应力，$\rho$ 是密度。$u_\tau$ 称为摩擦速度，它把壁面剪切换算成一个速度尺度。

对于近似平直、正交的第一层网格，单元中心到壁面的距离约为首层厚度的一半。因此，用公式算得 $y=0.01\ \mathrm{mm}$ 时，对应的完整第一层厚度大约为 $0.02\ \mathrm{mm}$。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-wall-law.png" alt="无量纲壁面速度分布与近壁区域" loading="lazy"><figcaption><strong>无量纲壁面速度分布与近壁区域</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 21 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

在典型平衡湍流边界层中，黏性底层近似满足 $u^+=y^+$；更外侧的对数区域近似满足 $u^+=\ln(y^+)/\kappa+B$。$\kappa$ 和 $B$ 是壁面律中的常数。逆压梯度、分离、粗糙度以及强传热等情况会改变简单壁面律的适用程度。

## 解析近壁区还是使用壁面函数

**解析近壁区**时，将第一层单元放到黏性底层，常以 $y^+\approx1$ 作为初始网格目标，并布置足够的层数描述边界层。模型需要具有相应的近壁处理能力。

**使用传统高雷诺数壁面函数**时，首层中心通常布置在适合对数律的区域，工程上常从 $y^+$ 约 30 以上估算。上限与边界层厚度、流动状态及具体函数有关。缓冲层处在黏性与湍流作用都较强的区域，简单分段壁面律在这里可能较敏感。

部分壁面函数使用连续或混合表达，覆盖更宽的 $y^+$ 范围。阅读某个具体函数时，应看它怎样计算 `nut`、`omega` 等变量，再安排网格。网格较细时，仅看到某一个壁面函数名称还不足以判断整套近壁处理是否合适。

## 实例：估算第一层厚度

假设空气运动黏度 $\nu=1.5\times10^{-5}\ \mathrm{m^2/s}$，主流速度 $U=10\ \mathrm{m/s}$，估计局部摩擦系数 $C_f=0.005$。由定义：

\[
C_f=\frac{\tau_w}{\tfrac12\rho U^2},
\qquad
u_\tau=U\sqrt{\frac{C_f}{2}}=0.5\ \mathrm{m/s}.
\]

目标 $y^+=1$ 时，$y=\nu/u_\tau=3\times10^{-5}\ \mathrm{m}$，首层厚度约为 $0.06\ \mathrm{mm}$。目标 $y^+=50$ 时，中心距离约为 $1.5\ \mathrm{mm}$，首层厚度约为 $3\ \mathrm{mm}$。

这组结果来自给定的摩擦系数估计。第一次计算完成后，用实际 $y^+$ 分布修正网格。若局部得到 $y^+=4$ 而希望降到 1，在摩擦速度变化较小时，可先把当地首层厚度缩小为原来的四分之一，再计算并检查。

## snappyHexMesh 的绝对层厚设置

以下片段放在 `system/snappyHexMeshDict` 的 `addLayersControls` 中，假定待加层的壁面 patch 名为 `body`：

```foam
relativeSizes false;
layers
{
    body
    {
        nSurfaceLayers 12;
    }
}
firstLayerThickness 0.00006;
expansionRatio      1.2;
minThickness        0.00001;
```

`relativeSizes false` 表示这里采用实际长度，单位与网格坐标一致；按米建立网格时，`0.00006` 就是 0.06 mm。`firstLayerThickness` 是第一层完整厚度，`expansionRatio` 是相邻两层厚度比，`nSurfaceLayers` 为请求的层数。`minThickness` 控制局部层厚缩减到什么程度后放弃加层。

将此方案并入完整字典时，保留匹配的网格质量和层平滑设置，层厚定义选用 `firstLayerThickness` 与 `expansionRatio` 这一对即可。若原字典同时指定了其他层厚约束，需要整理成一致的方案。

等比增长的 $n$ 层总厚度为：

\[
H=h_1\frac{r^n-1}{r-1},
\]

其中 $h_1$ 是第一层厚度，$r$ 是增长率。本例 12 层、增长率 1.2 的总厚度约为 2.37 mm。第一层足够细但总厚度过小，会让边界层外部仍落在较粗的体网格中；可以增加层数并平滑连接外部单元。

## 查看案例中的壁面字段

pitzDaily 的 `0/nut` 使用：

```foam
upperWall
{
    type  nutkWallFunction;
    value uniform 0;
}
```

`nutkWallFunction` 通过湍动能构造近壁尺度，计算壁面湍流运动黏度。`value` 是读取字段时的初始值，运行中由壁面函数更新。同一壁面的 `k` 采用 `kqRWallFunction`，`epsilon` 采用 `epsilonWallFunction`。它们共同构成此案例的 k–ε 近壁处理。

motorBike 的 SST 案例采用 `omegaWallFunction`，并配合其 `k` 和 `nut` 条件。更换湍流模型时，同时检查这几个场以及首层位置。

## 计算并显示 y⁺

完成 pitzDaily 的求解后，在算例目录执行：

```bash
simpleFoam -postProcess -func yPlus -latestTime > log.yPlus 2>&1
paraFoam
```

`-postProcess` 使用求解器构造所需的输运与湍流模型，`-func yPlus` 调用壁面距离后处理，`-latestTime` 读取最新时间。日志会给出壁面统计；在 ParaView 中加载结果，选取壁面并以 `yPlus` 着色，可以查看局部分布。

比较几个区域：入口发展段、台阶附近、再附着区以及下游平稳区域。它们的剪切应力不同，$y^+$ 也会不同。分离点附近剪切趋近零，局部 $y^+$ 可随之减小；判断近壁网格时，还应结合速度剖面、网格层形状和所用的壁面处理。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-flatplate-profile.png" alt="平板算例的壁面单位剖面对照" loading="lazy"><figcaption><strong>平板算例的壁面单位剖面对照</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 47 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 常见问题

| 问题 | 原因或检查方法 |
| --- | --- |
| `yPlus` 找不到湍流模型 | 使用对应求解器的后处理模式，检查模型与所需场是否完整 |
| 加层后壁面大块区域没有棱柱层 | 查看加层日志与局部质量限制，检查狭缝、曲率和背景网格尺度 |
| 改了首层厚度但 y⁺ 变化很小 | 检查是否重新生成了网格、是否读入旧结果、是否采用了相对尺寸 |
| 平均 y⁺ 合适但阻力仍随网格变化明显 | 查看关键区域的局部分布，同时检查壁面切向分辨率及边界层总厚度 |

## 练习：首层和总层厚分别控制什么

保留同一几何和体网格，建立两组近壁网格：第二组首层厚度减半，通过增加层数使总层厚尽量接近第一组。比较 $y^+$、壁面剪切和总阻力。在剪切变化较小时，第二组 $y^+$ 应接近第一组的一半；阻力的变化则反映当前近壁处理对分辨率的敏感性。

进一步固定首层厚度，只增加层数，查看边界层剖面是否更平滑地连接主流。对于换热问题，再检查热边界层和所用热壁面处理；动量与热量的扩散尺度会随 Prandtl 数而改变。
