湍流模型用来描述网格未直接解析的速度脉动对平均流动的影响。通道压降、汽车阻力和叶轮载荷等工程计算常用 RANS；需要分析涡结构、混合过程或宽频波动时，可以进一步考虑 LES。模型选择会同时影响需要的场文件、入口数据、壁面网格和计算时间。

## 层流、RANS 和 LES 的区别

流动的雷诺数为：

\[
Re=\frac{UL}{\nu},
\]

其中 $U$ 是特征速度，$L$ 是特征长度，$\nu$ 是运动黏度。雷诺数描述惯性与黏性作用的相对强弱。圆管、外流平板和自由剪切层的转捩条件不同，判断流态时还需要考虑几何、入口扰动和表面粗糙度。

| 方法 | 计算得到的主要量 | 适合的学习或应用方向 |
| --- | --- | --- |
| 层流计算 | 速度、压力随位置和时间的变化 | 低雷诺数流动、黏性主导问题 |
| 稳态 RANS | 统计平均意义下的流场 | 平均压降、平均阻力、工程参数比较 |
| URANS | 随时间变化的平均流场 | 较强的有组织非定常过程，如部分周期载荷 |
| LES | 滤波后的瞬态流场与较大涡结构 | 非定常混合、尾迹、流动噪声的流场输入 |
| DNS | 直接解析相关的湍流空间与时间尺度 | 机理研究，通常有很高的计算成本 |

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-rans-les-fields.png" alt="RANS 平均场与 LES 瞬时结构" loading="lazy"><figcaption><strong>RANS 平均场与 LES 瞬时结构</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 27 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

RANS 将瞬时速度写成平均值与脉动的和：$u_i=\bar u_i+u_i'$。将它代入方程并平均后，会出现 $\overline{u_i'u_j'}$ 这样的新未知量，即 Reynolds 应力。`kEpsilon` 和 `kOmegaSST` 等模型提供这些未知量的近似表达。

LES 使用空间滤波，直接计算网格可分辨的大尺度变化，用亚格子模型处理更小尺度的作用。LES 需要三维网格、足够小的时间步和充分长的统计时间；入口中的湍流扰动也会影响下游结果。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-averaging.png" alt="时均、空间滤波与速度脉动" loading="lazy"><figcaption><strong>时均、空间滤波与速度脉动</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 17 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

图中的红线表示瞬时信号，蓝线表示平均或滤波后的部分，二者之差对应被分离的波动。RANS 对这些波动做统计平均；LES 保留可分辨的空间变化，并对滤波尺度以下的作用建立模型。

## 实例：读取 pitzDaily 的 k–ε 设置

打开 `constant/turbulenceProperties`，其中的主体为：

```foam
simulationType RAS;

RAS
{
    RASModel    kEpsilon;
    turbulence  on;
    printCoeffs on;
}
```

`simulationType RAS` 选择雷诺平均模型类别，`RASModel` 再选择具体模型。`turbulence on` 启用湍流贡献；`printCoeffs on` 在日志中输出模型系数，便于查看当前采用的值。

`kEpsilon` 求解湍动能 $k$ 和耗散率 $\epsilon$，并由它们构造湍流运动黏度：

\[
\nu_t=C_\mu\frac{k^2}{\epsilon}.
\]

这里 $k$ 的单位是 m²/s²，$\epsilon$ 的单位是 m²/s³，$\nu_t$ 的单位是 m²/s。分子运动黏度来自 `transportProperties`，湍流黏度由流动和模型计算，因此这两个量承担不同作用。

本例还需要这些初始场：

| 文件 | 物理含义 | 入口和壁面的作用 |
| --- | --- | --- |
| `0/k` | 单位质量的湍动能 | 入口给定湍流水平，壁面配合壁面函数 |
| `0/epsilon` | 湍动能耗散率 | 控制湍流尺度与耗散 |
| `0/nut` | 湍流运动黏度 | 内部由模型更新，壁面由相应处理确定 |

## 入口湍流量怎样估算

已知平均速度 $U$、湍流强度 $I$ 和湍流长度尺度 $\ell$ 时，常用的各向同性估算为：

\[
k=\frac{3}{2}(UI)^2,
\qquad
\epsilon=C_\mu^{3/4}\frac{k^{3/2}}{\ell},
\qquad
\omega=\frac{\sqrt{k}}{C_\mu^{1/4}\ell}.
\]

`I` 以小数表示，5% 写成 0.05。$\ell$ 表示含能涡的特征尺度，可以来自测量或适合当前入口的经验估计。它与网格尺寸是不同的量。

例如 $U=10\ \mathrm{m/s}$、$I=0.05$、$\ell=0.01\ \mathrm{m}$、$C_\mu=0.09$，得到 $k=0.375\ \mathrm{m^2/s^2}$、$\epsilon\approx3.77\ \mathrm{m^2/s^3}$、$\omega\approx112\ \mathrm{s^{-1}}$。这是用于解释估算方法的一组输入；pitzDaily 原文件中的耗散率为 14.855，采用了不同的湍流尺度。

对应 `0/k` 的入口可以写为：

```foam
inlet
{
    type  fixedValue;
    value uniform 0.375;
}
```

同样，在 `0/epsilon` 中填入估算得到的耗散率。改变入口速度而保持 $I$ 和 $\ell$ 不变时，$k$ 随 $U^2$ 变化，$\epsilon$ 随 $U^3$ 变化；这说明速度和入口湍流量需要一起调整。

## 将模型改为 k–ω SST

SST 使用 $k$ 和比耗散率 $\omega$，在近壁区和远离壁面的区域采用不同的混合处理，并限制湍流剪切应力。它是壁面边界层和逆压梯度问题中常见的工程模型。

在独立副本中，将模型设置改为：

```foam
simulationType RAS;
RAS
{
    RASModel    kOmegaSST;
    turbulence  on;
    printCoeffs on;
}
```

随后补齐 `0/omega`，其量纲是 `[0 0 -1 0 0 0 0]`；检查 `fvSolution` 中有适用于 `omega` 的线性求解器条目，`fvSchemes` 中有对应输运离散。墙面的 `k`、`omega`、`nut` 条件也要与近壁网格配合。

下载包中的 motorBike 提供了 SST 的完整示例，可以查看其 `0.orig/omega`、`0.orig/nut` 和 `constant/turbulenceProperties`。复制到另一几何时，保留新算例自己的 patch 名称和物理边界。`epsilon` 与 `omega` 的定义和量纲不同，创建 `omega` 时应按入口尺度重新计算数值，并设置对应边界。

## 层流与 LES 的设置入口

适用 `turbulenceProperties` 的求解器可通过以下条目选择层流：

```foam
simulationType laminar;
```

LES 常见设置形式如下，具体算例还需相应的三维网格、瞬态离散和边界条件：

```foam
simulationType LES;
LES
{
    LESModel    WALE;
    turbulence  on;
    printCoeffs on;
    delta       cubeRootVol;
}
```

`WALE` 是一种亚格子黏度模型；`delta cubeRootVol` 使用单元体积立方根构造滤波尺度。高度拉伸的单元在不同方向有不同分辨率，分析 LES 网格时应分别考察流向、法向和展向尺寸。

## 从日志和结果判断模型是否正确启用

运行 `simpleFoam` 后，日志开头会打印所选模型。检查它是否与配置一致，再查看 `k`、`epsilon` 或 `omega` 的求解记录，以及 `nut` 的空间分布。模型产生的湍流黏度会改变动量扩散，因此会影响速度剖面、分离区和压降。

| 问题 | 常见原因 | 处理位置 |
| --- | --- | --- |
| 提示找不到 `omega` | 仅修改了模型名称 | 增加完整场文件并配置求解器条目 |
| `Unknown RASModel` | 名称大小写错误或当前库没有该模型 | 根据错误输出的可用模型列表选择 |
| `k`、`epsilon` 反复被限制到很小值 | 初值、边界、网格或离散导致局部异常 | 先定位异常区域，再检查对应输入和数值设置 |
| LES 的统计量持续变化 | 启动过程尚未结束或采样窗口不足 | 监测分段平均值，增加代表性的统计时间 |

## 练习：入口湍流强度的影响

在同一份 pitzDaily 网格上，比较 $I=2\%$、$5\%$、$10\%$ 三组入口，保持速度和长度尺度一致。分别计算 `k` 与 `epsilon`，比较再附着位置和下游速度剖面。更大的入口湍流量通常会改变剪切层发展，但变化幅度取决于入口到分离位置的距离及模型。

进阶比较可固定几何、边界和观测位置，再比较 k–ε 与 SST。近壁设置分别满足各模型的要求，并对两者都进行网格检查；由此得到的差异才便于分析模型对分离、混合和压降的影响。
