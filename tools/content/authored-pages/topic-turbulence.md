## RANS 与 LES

如果关心的是平均压降、阻力或换热量，RANS 通常是起点：它对流动方程做平均，用湍流模型封闭雷诺应力等未知量。LES 则直接算出较大的涡，只用亚格子模型描述小尺度的作用，代价是更细的网格和更小的时间步。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-rans-les-fields.png" alt="RANS 平均场与 LES 瞬时结构" loading="lazy"><figcaption><strong>RANS 平均场与 LES 瞬时结构</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 27 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 模型、入口与壁面

在 `constant/turbulenceProperties` 中选择模型后，还要准备对应的场。`kEpsilon` 使用 `k`、`epsilon`，`kOmegaSST` 使用 `k`、`omega`；壁面条件与近壁网格一起设置。

例如入口速度 $U=10\,\mathrm{m/s}$、湍流强度 $I=5\%$ 时，

\[
k=\frac32(IU)^2=0.375\,\mathrm{m^2/s^2}.
\]

耗散率还需要长度尺度。各参数的估算、量纲和边界例子见[湍流模型课程](/read/?slug=laminar-turbulence-model-choice)。

壁面附近常用 $y^+=u_\tau y/\nu$ 衡量网格分辨率。第一层高度由目标 $y^+$ 初估，计算后再用实际分布调整。详细步骤见[近壁网格](/read/?slug=wall-resolution-yplus)。

## 配套练习

先使用 pitzDaily 比较入口湍流量和压降，再用 motorBike 练习外流网格、壁面分辨率与阻力监测。LES 结果还需选定统计时间段，比较平均值、脉动量和采样时长。

[turbulenceProperties 配置](/dictionaries/constant-turbulenceproperties/) · [采样与时间平均](/read/?slug=sampling-functions-and-observables)
