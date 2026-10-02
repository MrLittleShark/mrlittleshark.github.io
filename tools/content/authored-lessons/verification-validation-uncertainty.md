数值验证研究计算中的离散和求解误差；物理确认研究模型与真实流动的一致程度。两者分别回答“数值解有多准确”和“这些方程能否描述目标问题”。实际工作中，可以从解析解比较开始，再做网格与时间步研究，最后对照条件匹配的实验数据。

## 几类误差来自哪里

| 误差或不确定性 | 例子 | 常见研究方法 |
| --- | --- | --- |
| 迭代误差 | 压力和速度仍未充分耦合收敛 | 收紧容差、增加校正，比较目标量 |
| 空间离散误差 | 粗网格把剪切层扩散得过宽 | 有规律地细化网格 |
| 时间离散误差 | 时间步太大造成波形相位偏差 | 减小时间步 |
| 模型误差 | 某湍流闭合对分离流预测有偏差 | 对照实验，比较模型适用条件 |
| 输入不确定性 | 流量、粗糙度、温度测量不准确 | 灵敏度分析和误差传播 |

同一计算可能同时存在多种影响。网格研究时，先让迭代误差足够小；瞬态问题还要保持足够的时间分辨率，才能清楚观察空间网格造成的变化。

## 实例一：与一维导热解析解比较

考虑长度 $L=0.1\ \mathrm m$、常导热系数、无内部热源的平板，两端温度分别为 300 K 和 400 K，其余边界绝热。稳态解为：

\[
T(x)=300+100\frac{x}{0.1}.
\]

因此 $x=0.025\ \mathrm m$ 时为 325 K，$x=0.05\ \mathrm m$ 时为 350 K。温度斜率为 1000 K/m，导热通量为 $q_x=-\lambda\,1000$，负号表示热量沿负 x 方向流动。

在课程的 `exercises/one-dimensional-diffusion` 中，读取几何长度和两端温度，按其实际值写出解析解；上述数值是一组便于手算的例子。用同一组采样坐标比较数值温度与解析温度，并检查曲线斜率和热流方向。

若将温度与坐标导出为包含 `x,T` 两列的 `comparison.csv`，下面的 Python 程序可计算这组例子的误差：

```python
import csv
import math

with open("comparison.csv", newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

errors = []
for row in data:
    x = float(row["x"])
    numerical = float(row["T"])
    exact = 300.0 + 100.0*x/0.1
    errors.append(numerical - exact)

if not errors:
    raise ValueError("comparison.csv 没有数据行")

rms = math.sqrt(sum(e*e for e in errors)/len(errors))
print("最大绝对误差 / K:", max(abs(e) for e in errors))
print("采样点均方根误差 / K:", rms)
```

`DictReader` 按列名读取数据，`exact` 计算相同坐标处的解析温度。最大误差显示最差采样点，均方根误差反映这组点的整体偏差。若采样点分布不均匀，这里的均方根仍按点数平均；需要空间积分误差时，应使用对应的长度或体积权重。

常系数线性温度场在正交网格上可能被离散方法非常准确地表示。研究格式阶数时，可以进一步采用具有曲率的解析解、源项或制造解，使误差随网格变化更容易测量。

## 实例二：三组网格估计收敛阶

选择一个标量目标，例如压降、阻力或某点速度。令 $f_1$、$f_2$、$f_3$ 分别是细、中、粗网格结果；特征尺寸满足 $h_2/h_1=h_3/h_2=r>1$。当结果单调收敛并进入渐近区时，可估算：

\[
p=\frac{\ln\left|\dfrac{f_3-f_2}{f_2-f_1}\right|}{\ln r},
\qquad
f_{\mathrm{ext}}=f_1+\frac{f_1-f_2}{r^p-1}.
\]

$p$ 是观测收敛阶，$f_{\mathrm{ext}}$ 是 Richardson 外推值。取一组教学数据：粗、中、细网格压降分别为 108、102、100.5 Pa，$r=2$，则 $p=2$，外推值为 100 Pa。

用常见安全系数 1.25 表示细网格 GCI：

\[
GCI_{12}=1.25\,
\frac{|f_1-f_2|/|f_1|}{r^p-1}\times100\%.
\]

该例约为 0.62%。这组数字用于演示计算过程。实际应用需要确认细化方式相似、目标量收敛、迭代误差较小，并检查三组网格之间的变化是否支持渐近假设。

对于均匀细化网格，三维尺寸可由 $h\propto N^{-1/3}$ 估计，二维网格则用 $h\propto N^{-1/2}$。局部加密、壁面层或拓扑大幅变化时，单一全局 $h$ 对局部分辨率的描述较弱，应同时记录关键区域的尺寸。

## 结果不单调时怎么办

如果压降随网格加密先增大后减小，可能存在多种误差相互抵消，也可能改变了分离位置、壁面处理或几何表示。此时先比较：壁面 $y^+$ 是否跨越不同处理区域、边界形状是否改变、采样位置和方式是否相同、每组计算是否达到相近的收敛程度。

补充更细网格或更合理的细化序列后，再判断趋势。两个网格数值接近，也可能恰好处于误差抵消的位置；多组结果与物理观测一起使用，更便于解释差异。

## 时间步研究怎样安排

固定空间网格，使用 $\Delta t$、$\Delta t/2$、$\Delta t/4$ 三组时间步。对周期问题比较频率、振幅和相位；对自由液面问题比较相同时间的前沿位置；对统计问题比较相同定义的时间平均与波动强度。

如果每个时间步使用 PIMPLE 迭代，还需让各组的时间步内收敛程度相近。自动时间步可通过降低 Courant 数上限建立比较，但实际步长随时间变化，需要保留各组步长历史。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-turbulence-flatplate-profile.png" alt="平板算例的壁面单位剖面对照" loading="lazy"><figcaption><strong>平板算例的壁面单位剖面对照</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 47 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 与实验数据怎样比较

先对齐几何、物性温度、入口条件和测量位置。速度测量可能是点值、空间平均值或时间平均值；压力测量可能是表压或压差。模拟输出采用相同定义后，差异才具有明确含义。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-multiphase-ship-validation.png" alt="自由液面高度与阻力的观测量" loading="lazy"><figcaption><strong>自由液面高度与阻力的观测量</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 85 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

左图将船体不同位置的水位与实验点比较，右图记录阻力系数随时间的变化。空间曲线用于检查波峰、波谷的位置与幅度，时间曲线用于选择统计区间，再提取平均阻力和波动幅度。

例如，实验压降为 $100\pm2\ \mathrm{Pa}$，模拟为 101 Pa。应说明 ±2 Pa 是标准不确定度还是某一置信水平的区间，同时给出模拟的数值误差估计。若实验与数值误差都约为几个 Pa，仅凭 1 Pa 差异很难区分模型之间的优劣。

对相互独立的输入标准不确定度，线性传播近似为：

\[
u_y^2=\sum_i\left(\frac{\partial y}{\partial x_i}\right)^2u_{x_i}^2.
\]

偏导数表示输出对某个输入的敏感程度，可用小幅改变输入的计算来估计。相关输入还需加入协方差项。离散误差估计与实验统计不确定度具有不同来源，合并时需要明确采用的解释。

## 常见问题与练习

误差比较出现异常大值时，先查看单位、坐标位置和归一化分母；近零变量适合使用绝对误差或明确的特征尺度。观测阶出现负数或极大值时，检查收敛趋势和迭代误差。不同网格对同一条线采用了不同插值方式时，采样误差也会进入比较。

练习可采用方腔 20×20、40×40、80×80 网格，在相同物理时刻提取中心线速度。先比较三条曲线，再选一个固定位置计算差异；靠近速度过零点时使用顶盖速度作为误差归一化尺度。进阶时选取涡心位置或流函数极值，分析场变量误差如何影响派生观测量。
