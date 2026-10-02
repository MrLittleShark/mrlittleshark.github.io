入口速度常随时间变化：启动时逐渐升高，泵工作时周期脉动，阀门开启后维持一段时间再关闭。本课先完成两个可直接运行的例子——线性启动和正弦脉动，再介绍延迟启动、平滑启动和有限时长脉冲的改法。

[下载两组时变入口算例](/downloads/programming/coded-fields-05-v2512.zip) · 先修：[codedFixedValue 基本写法](/read/?slug=coded-fields-04)

## 1. 先选一个容易检查的入口

本课入口在空间上均匀，同一时刻所有入口面的速度都相同。这样，面积平均速度就是公式给定的速度，可以直接画出时间曲线检查。

算例仍使用长 0.1 m、高 0.01 m 的二维通道，`icoFoam` 求解速度和压力。上下壁面静止，出口压力为零，运动黏度为 $10^{-3}\ \mathrm{m^2/s}$。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-time.png" alt="线性启动入口和正弦脉动入口的设定曲线与计算输出" loading="lazy"><figcaption>两种时间函数及实际保存的入口平均速度。<small>FoamLab，OpenFOAM v2512 配套计算。</small></figcaption></figure>

## 2. 示例一：0.2 秒内从静止升到 0.1 m/s

希望入口在 t=0 时静止，随后线性加速，到 0.2 s 达到 0.1 m/s 并保持。可写成

$$U_x(t)=U_{\mathrm{target}}\min\left[\max\left(\frac{t-t_s}{t_r},0\right),1\right].$$

本例目标速度 $U_{\mathrm{target}}=0.1\ \mathrm{m/s}$、开始时间 $t_s=0$、启动历时 $t_r=0.2\ \mathrm s$。

打开 `07-ramp/0/U`，入口完整写法如下：

{{boundary:07-ramp}}

从执行顺序看，code 中只有四步：

1. 取得当前模拟时间 t。
2. 定义开始时刻、启动历时和目标速度。
3. 将时间转成 0～1 的启动比例。
4. 计算速度向量并赋给整个入口。

`max(..., scalar(0))` 把开始时刻以前的比例取为零；外层 `min(..., scalar(1))` 把达到目标后的比例限制为一。`scalar(0)` 与 `scalar(1)` 让这些常数和时间表达式使用相同标量类型。

| 时间 / s | 启动比例 | 入口速度 / (m/s) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0.05 | 0.25 | 0.025 |
| 0.10 | 0.50 | 0.050 |
| 0.20 | 1 | 0.100 |
| 0.50 | 1 | 0.100 |

这张表可以直接作为运行后的检查目标。

## 3. 运行启动算例，读取时间曲线

```bash
cd ~/OpenFOAM/foamLabCodedFields/07-ramp
bash Allrun
```

程序从 0 算到 1 s，`deltaT=0.001`，因此启动阶段包含 200 个时间步。速度场每 0.05 s 保存一次；入口平均速度每一步写入文本文件：

```text
postProcessing/inletMean/0/surfaceFieldValue.dat
```

文件每行的第一列是时间，后面的括号内依次是平均速度的 x、y、z 分量。前几行大致如下：

```text
0.001  (0.0005 0 0)
0.002  (0.0010 0 0)
0.003  (0.0015 0 0)
```

程序从第一次时间推进后开始记录，因此首行是 0.001 s。0 时刻初值保存在 `0/U`。

ParaView 中选择 inlet 查看边界速度；再选 internalMesh 观察壁面附近怎样形成速度梯度。入口均匀赋值，内部速度会因壁面黏性作用形成空间分布，这两个观察对象各有作用。

## 4. 示例二：周期为 1 秒的脉动入口

接着考虑一个围绕平均值变化的入口：

$$U_x(t)=U_m[1+A\sin(2\pi ft)].$$

取 $U_m=0.1\ \mathrm{m/s}$、相对幅值 $A=0.5$、频率 $f=1\ \mathrm{Hz}$。实际速度幅值为 $AU_m=0.05\ \mathrm{m/s}$，所以速度在 0.05～0.15 m/s 之间变化。

打开 `08-sine/0/U`，入口块如下：

{{boundary:08-sine}}

`frequency` 的单位为 Hz，即每秒周期数；`2*pi*frequency*t` 是以弧度表示的相位。`constant::mathematical::pi` 提供圆周率，`Foam::sin()` 计算正弦。

代码使用当前时间的绝对值。重启时如果模拟时间为 1.25 s，就计算 1.25 s 对应的相位，时间函数自然衔接到原计算。

| 时间 / s | 正弦相位 | 入口速度 / (m/s) |
| --- | --- | --- |
| 0 | 0 | 0.10 |
| 0.25 | π/2 | 0.15 |
| 0.50 | π | 0.10 |
| 0.75 | 3π/2 | 0.05 |
| 1.00 | 2π | 0.10 |

```bash
cd ../08-sine
bash Allrun
```

同样查看 `inletMean` 文件，并对照表中的四个计算输出时刻。下载包的 `reference-results` 也包含曲线 CSV，可导入表格软件绘图。

本例内部初值为零，而正弦入口在 t=0 附近约为 0.1 m/s，因此计算包含一次启动调整。希望从已有周期流动继续计算时，可使用已保存的流场重启；希望平滑起步时，可采用后面介绍的启动函数乘以正弦函数。

## 5. 输出频率与时间步怎样配合

本例每个周期包含 1000 个计算步、20 份场输出。入口均值每步记录，能够清楚显示正弦曲线。完整速度场输出较少，可以减少文件数量。

若将频率改为 5 Hz，周期变成 0.2 s。保持原步长时每周期有 200 步，但每周期只保存 4 份场，动画会比较粗略。可将 `writeInterval` 改成 0.01，以每周期 20 份输出查看流场变化。

时间步影响计算分辨率，保存间隔影响留下多少数据。改变频率后，分别考虑这两个设置，并用减小时间步的对照计算检查流场响应。

## 6. 示例三：延迟 0.3 秒再启动

在斜坡例中将参数改成：

```cpp
const scalar start = 0.3, rampTime = 0.2, targetSpeed = 0.1;
```

其余三行代码保持原样。t≤0.3 s 时入口静止，0.3～0.5 s 加速，0.5 s 后保持 0.1 m/s。先算出 0.3、0.4 和 0.5 s 的目标值，再与 `inletMean` 对照。

## 7. 示例四：两端加速度为零的平滑启动

线性斜坡在开始和结束处发生加速度突变。使用半余弦函数可以把这两个端点变得更平滑。用下面内容替换 `07-ramp` 的 code 主体：

```cpp
const scalar t = this->db().time().value();
const scalar rampTime = 0.2, targetSpeed = 0.1;
const scalar s = min(max(t/rampTime, scalar(0)), scalar(1));
const scalar pi = constant::mathematical::pi;
const scalar factor = 0.5*(1.0-Foam::cos(pi*s));
operator==(vector(targetSpeed*factor, 0, 0));
```

当 s=0 或 s=1 时，函数斜率为零；s=0.5 时速度为目标值的一半。两种启动方法的总历时相同，但加速过程不同。可对照入口曲线和通道中部的速度时序。

把 `targetSpeed` 换成正弦例算出的 `speed`，就得到“先平滑启动，再持续脉动”的入口。

## 8. 示例五：仅在指定时间段开启

下面的矩形脉冲在 0.2≤t<0.6 s 时入口速度为 0.1 m/s，其余时刻为零：

```cpp
const scalar t = this->db().time().value();
const scalar speed = (t >= 0.2 && t < 0.6) ? 0.1 : 0.0;
operator==(vector(speed, 0, 0));
```

`&&` 表示两个时间条件同时满足；`? :` 根据条件选择开启值或关闭值。这个例子有两次瞬时速度跳变，会带来较强瞬态响应。若实际装置有有限开闭时间，可在两个端点接入线性或半余弦过渡。

这三种扩展复用配套通道，只修改 code。给每组实验保留独立目录，并把生成类型的 `name` 改成易辨识的名称，例如 `foamLabSmoothRamp`，方便阅读日志。

## 9. 相同思路如何设置时变温度

在温度边界中，把向量赋值改成标量：

```cpp
const scalar t = this->db().time().value();
const scalar pi = constant::mathematical::pi;
const scalar temperature = 300.0 + 10.0*Foam::sin(2.0*pi*t);
operator==(temperature);
```

这个温度边界以 300 K 为平均值、10 K 为幅值，周期为 1 s。将它放入前面热扩散算例的一个真实 patch 下，使用 `codedFixedValue`、标量 `value uniform 300` 和相应 codeInclude，即可研究周期加热。

## 10. 下一步：时间函数乘上空间剖面

本课把同一个速度向量赋给所有入口面。下一课将这个时间函数与抛物线形状相乘，并用实际面面积归一化，让入口平均速度严格跟随给定曲线。同时把参数移到 `codeContext`，练习重启和并行运行。

## 参考

[v2512 codedFixedValue 源码与示例](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/finiteVolume/fields/fvPatchFields/derived/codedFixedValue/codedFixedValueFvPatchField.H)。
