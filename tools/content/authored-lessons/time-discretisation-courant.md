瞬态计算将连续时间划分为一系列时间步。时间格式规定怎样使用已有时刻的场来求下一步，时间步长则规定两次求解相隔多久。二者共同影响峰值、相位、衰减速度和计算成本。

## 先看一阶隐式 Euler

对于随时间变化的量 $T$，隐式 Euler 将时间导数近似为

\[
\left.\frac{dT}{dt}\right|^{n+1}
\approx\frac{T^{n+1}-T^n}{\Delta t}.
\]

$n$ 是旧时刻，$n+1$ 是新时刻。空间项也使用新时刻的未知量，因此需要建立并求解方程组。在 `system/fvSchemes` 中配置：

```foam
ddtSchemes
{
    default Euler;
}
```

OpenFOAM 的 `Euler` 是一阶隐式时间格式，常用于初次计算和变化较剧烈的启动阶段。其时间误差通常与 $\Delta t$ 成正比：进入正常收敛区间后，时间步减半，主要时间误差约减半。

用衰减方程 $dT/dt=-\lambda T$ 可以直接看到效果。令 $\lambda=1\,\mathrm{s^{-1}}$，$T(0)=1$，隐式 Euler 给出

\[
T^{n+1}=\frac{T^n}{1+\lambda\Delta t}.
\]

取 $\Delta t=1\,\mathrm s$，一步得到 $T(1)=0.5$，解析值为 $e^{-1}\approx0.3679$。取 $\Delta t=0.1\,\mathrm s$，十步得到约 0.3855。两种步长都能平稳计算，较小步长更准确地描述衰减过程。

## backward 与 CrankNicolson

`backward` 使用多个时间层。等时间步下，其二阶后向差分为

\[
\left.\frac{dT}{dt}\right|^{n+1}
\approx\frac{3T^{n+1}-4T^n+T^{n-1}}{2\Delta t}.
\]

相应设置为：

```foam
ddtSchemes
{
    default backward;
}
```

它使用 $n$ 和 $n-1$ 两层历史数据来计算新值；启动阶段还需要建立历史层。变时间步计算时，程序会根据新旧步长调整系数。比较二阶格式时应观察已经完成启动的时间区间。

另一种常见选择为：

```foam
ddtSchemes
{
    default CrankNicolson 0.9;
}
```

Crank–Nicolson 用新旧时刻的信息构造时间积分。OpenFOAM 后面的系数控制偏心程度：0 对应 Euler，1 对应纯 Crank–Nicolson；`0.9` 混入一定的 Euler 特性，以减弱启动或剧烈变化时的振荡。实际误差阶还取决于偏心参数、启动处理和时间步变化，应通过步长细化观察。

| 设置 | 使用特点 | 常见比较指标 |
| --- | --- | --- |
| `Euler` | 一阶，启动简单，耗散较明显 | 峰值衰减、总计算量 |
| `backward` | 多时间层，平滑解上二阶 | 相位、幅值、步长收敛 |
| `CrankNicolson 0.9` | 调整偏心以兼顾时间精度和阻尼 | 启动振荡、周期响应 |
| `steadyState` | 时间导数为零 | 稳态迭代收敛 |

## Courant 数表示一步内的输运距离

在一维均匀网格中，Courant 数为

\[
Co=\frac{|u|\Delta t}{\Delta x}.
\]

分子是流体在一个时间步内运动的距离，分母是单元长度。$Co=0.2$ 表示一步约移动五分之一个单元，$Co=2$ 表示一步约跨过两个单元。

![Courant 数与时间步](/assets/diagrams/core-courant.svg)

一般不可压缩有限体积网格常按各面的体积通量计算

\[
Co_P=\frac{\Delta t}{2V_P}\sum_f|\phi_f|.
\]

$V_P$ 是单元体积，$\phi_f$ 的单位为 $\mathrm{m^3/s}$。在一维定常流中，两侧面的通量绝对值相同，公式恰好化为 $|u|\Delta t/\Delta x$。小单元和高速区往往决定最大 Courant 数，所以日志中的最大值比全域平均值更适合检查局部时间分辨率。

本课标量案例有 $\Delta x=1/200=0.005\,\mathrm m$、$u=1\,\mathrm{m/s}$、$\Delta t=0.001\,\mathrm s$，因此 $Co=0.2$。如果把单元数加倍而保持时间步，$Co$ 就增大到 0.4；要保持 0.2，应把时间步减半。

## 时间步与输出间隔分别控制什么

`system/controlDict` 可以写成：

```foam
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         0.2;
deltaT          0.001;
writeControl    timeStep;
writeInterval   50;
```

程序从 0 s 计算到 0.2 s，每步推进 0.001 s，共推进 200 步。`writeInterval 50` 表示每 50 步保存一次场，对应 0.05 s。求解实际经历了所有时间步，磁盘上只保留其中一部分。

如果把 `deltaT` 减半并希望保持相同输出时刻，可把 `writeInterval` 改为 100。若维持 50，则输出间隔随之变成 0.025 s。绘图中的时间采样还取决于保存频率，特别是分析峰值和频率时，需要保留足够密的记录。

## 自动时间步怎样使用

`pimpleFoam` 包含根据 Courant 数调整时间步的代码。在完整的 `pimpleFoam` 算例 `controlDict` 中可设置：

```foam
adjustTimeStep  yes;
maxCo           0.5;
maxDeltaT       0.001;
writeControl    adjustableRunTime;
writeInterval   0.02;
```

`maxCo` 给出对流 Courant 数的控制目标；`maxDeltaT` 给出时间步上限。前者随速度和网格限制步长，后者在低速阶段仍维持足够的时间分辨率。`adjustableRunTime` 允许程序调整步长以命中每 0.02 s 的输出时刻。

例如，流场变慢后 Courant 数允许使用 0.01 s，但关注的振动周期只有 0.02 s，仍需要更小的时间步。此时 `maxDeltaT` 就能约束物理时间分辨率。

`icoFoam` 和本课的 `scalarTransportFoam` 使用给定步长，没有 `pimpleFoam` 的这套自动步长调用。用它们做对比时，直接修改 `deltaT`，再检查对应时间尺度。多相流还需要考虑界面运动和表面张力，可压缩流还需要考虑声学传播，控制参数由具体求解器决定。

## 做一次时间步细化

使用标量输运练习的三份独立副本，固定 200 个单元、`upwind` 空间格式以及 0.2 s 的结束时刻，分别取 $\Delta t=0.001$、0.0005、0.00025 s。原有 `compare.py` 的最终时刻仍为 0.2 s，可直接用于比较。

| 时间步 / s | 时间步数 | 一维 Courant 数 | 每 0.05 s 输出对应的步数 |
| --- | --- | --- | --- |
| 0.001 | 200 | 0.2 | 50 |
| 0.0005 | 400 | 0.1 | 100 |
| 0.00025 | 800 | 0.05 | 200 |

记录峰值、平均绝对误差和耗时。这里空间迎风误差仍然存在，减小时间步后总误差可能趋于一个由空间离散决定的水平。随后换用较细网格或更高精度空间格式，可以继续分辨时间误差的影响。

也可以固定步长，只比较 `Euler`、`backward` 和 `CrankNicolson 0.9`。这一组回答时间格式的影响，上一组回答步长的影响，两组分别进行后更容易解释差别。

## 周期流动的时间分辨率

若圆柱绕流的涡脱落周期约为 0.1 s，使用 0.02 s 时间步，每周期只有 5 个计算点；使用 0.001 s 则有 100 个。后者能够更细致地描述峰值位置，但最终还应比较周期、平均力和振幅随步长的变化。

分析频率时，采样间隔必须小于所关注周期的一半才能满足最基本的采样条件；准确重现波形通常需要更多采样点。可以通过探针或力系数函数对象记录每个时间步，同时较低频率地保存整个三维场，从而控制磁盘占用。

源码中 `pimpleFoam.C` 的 `setDeltaT.H` 调用连接了这些控制参数与实际步长；`fvSchemes` 则决定每一步如何离散时间导数。下一课介绍时间步内部的速度和压力如何相互校正。
