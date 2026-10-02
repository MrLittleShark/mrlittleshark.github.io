这一节完成一个更实用的入口：速度沿高度呈抛物线分布，面积平均速度随时间周期变化。高度、平均速度、幅值、频率和相位都放进字典参数，便于修改工况。

最后用同一个算例练习从已有结果继续计算，以及沿入口高度分成两个进程运行。

[下载脉动剖面算例与参考数据](/downloads/programming/coded-fields-06-v2512.zip) · [下载全部九例](/downloads/programming/coded-fields-all-v2512.zip)

## 1. 把空间形状与时间函数分开

设入口面积平均速度为

$$\overline U(t)=U_m[1+A\sin(2\pi ft+\varphi)].$$

本例 $U_m=0.1\ \mathrm{m/s}$、$A=0.5$、$f=1\ \mathrm{Hz}$、$\varphi=0$。空间形状采用

$$g(y)=4\eta(1-\eta),\qquad \eta=\frac{y}{H},\quad H=0.01\ \mathrm m.$$

g 在中心等于 1，在上下缘等于 0。将它乘以随时间变化的系数，就得到同一形状、强弱周期变化的入口剖面。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-pulsed.png" alt="归一化脉动入口的平均速度时间曲线和三个时刻的速度剖面" loading="lazy"><figcaption>平均速度按正弦变化，入口保持抛物线形状。<small>FoamLab，OpenFOAM v2512 配套计算。</small></figcaption></figure>

## 2. 为什么需要面积归一化

第三课给定中心最大速度 0.15 m/s 时，连续剖面平均为 0.1 m/s，但 20 个面中心采样后的离散平均为 0.100125 m/s。如果实验提供的是入口流量，希望设置的平均值直接等于网格上的平均值，就可以做一次面积归一化。

设第 i 个入口面面积为 $S_i$，形状值为 $g_i$，令

$$U_{x,i}(t)=\overline U(t)\,g_i\,\frac{\sum_j S_j}{\sum_j g_jS_j}.$$

把它代回面积平均的定义，得到

$$\frac{\sum_i U_{x,i}S_i}{\sum_i S_i}=\overline U(t).$$

归一化改变整条曲线的幅值，保留各面之间的相对形状。对于非等面积网格，也可以使用同样的公式。

本例入口平面垂直 x 轴，所有速度都沿正 x，因此平均速度乘总面积就是体积流量。倾斜入口的通量则应按速度与面面积向量的点积计算。

## 3. 把工况参数放进 `codeContext`

打开 `09-pulsed-profile/0/U`。入口块中先定义参数：

```foam
codeContext
{
    height 0.01;
    meanSpeed 0.1;
    amplitude 0.5;
    frequency 1.0;
    phase 0.0;
}
```

| 参数 | 单位 | 本例含义 |
| --- | --- | --- |
| height | m | 从 y=0 到上缘的入口高度 |
| meanSpeed | m/s | 一个周期的时间平均速度 |
| amplitude | 无量纲 | 相对脉动幅值；0.5 对应平均值上下变化 50% |
| frequency | Hz | 每秒周期数；1 表示周期 1 s |
| phase | rad | 初相位；0 从平均值开始并增大 |

这些普通标量条目的单位由本课约定，代码按 SI 单位计算。`height` 应与网格一致；时间来自求解器的物理时间。

`codedFixedValue` 将 `codeContext` 传给动态生成的边界对象。code 中用

```cpp
const dictionary& parameters = this->dict();
const scalar meanSpeed = parameters.get<scalar>("meanSpeed");
```

读取参数。`get<scalar>` 说明需要读取一个标量；缺少条目时，错误信息会指出对应键名。

## 4. 完整入口代码

下面是下载包中的 inlet 块，复制时连同 `codeContext` 和编译设置一起保留：

{{boundary:09-pulsed-profile}}

按作用可以把它读成四段。

### 第一段：读参数并检查取值

`height` 取正值，`frequency` 和 `meanSpeed` 非负，`amplitude` 取 0～1。这组范围对应本课的单向脉动入口，最低速度为 $U_m(1-A)$。

若要研究往复流，可进一步允许 A>1，并配套适合反向流动的出口和其他场边界。那时速度会在部分周期内为负，物理工况也随之改变。

### 第二段：逐面计算形状

`patch().Cf()` 提供面中心，`patch().magSf()` 提供面面积。代码按高度计算 `shape[faceI]`；`max(..., 0)` 将剖面区间外的形状设为零。

面积和使用：

```cpp
const scalar totalArea = gSum(areas);
const scalar weightedShape = gSum(shape*areas);
```

`shape*areas` 是逐元素相乘。`gSum` 对所有进程上的局部数据求全局和，所以入口被多个进程分割时仍使用同一个归一化系数。

### 第三段：由当前时间计算平均速度

代码读取 t，计算正弦，并加上 phase。改变 phase 可以从同一周期的不同位置开始：phase=π/2 时，入口在初始时刻处于最大值；phase=π 时，从平均值开始减小。

### 第四段：把每个面的速度写回边界

```cpp
velocity[faceI] = vector(speed*shape[faceI]*totalArea/weightedShape, 0, 0);
```

`speed` 是当时要求的平均速度，后面的面积比完成归一化。循环最后使用 `operator==(velocity)` 更新整个入口。

## 5. 运行并核对四个时刻

```bash
cd ~/OpenFOAM/foamLabCodedFields/09-pulsed-profile
bash Allrun
```

程序从 0 计算到 1 s，步长 0.001 s，场文件每 0.05 s 保存一次。入口均值和流量每步记录，方便画出连续时间曲线。

| 时间 / s | 入口平均速度 / (m/s) | 流入体积流量大小 / (m³/s) |
| --- | --- | --- |
| 0.25 | 0.15 | `1.5e-6` |
| 0.50 | 0.10 | `1.0e-6` |
| 0.75 | 0.05 | `0.5e-6` |
| 1.00 | 0.10 | `1.0e-6` |

入口面积是 $0.01\times0.001=10^{-5}\ \mathrm{m^2}$。查看 `inletFlux` 文件时，对应数值带负号，表示流入；出口的 `outletFlux` 为正。

在 ParaView 中选中 inlet，比较 0.25 s 和 0.75 s。两条剖面的形状相同，前者速度是后者的三倍。0.25 s 时两个中心面的速度约为 0.2241573 m/s，低于简单连续公式的峰值 0.225 m/s，原因是离散面位置和归一化共同决定了各面数值。

## 6. 用 Python 读几个关键值

在算例目录运行以下代码，打印入口平均速度文件中四个目标时刻的记录：

```bash
python3 - <<'PY'
from pathlib import Path
targets = (0.25, 0.5, 0.75, 1.0)
path = Path("postProcessing/inletMean/0/surfaceFieldValue.dat")
for line in path.read_text().splitlines():
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    values = line.replace("(", " ").replace(")", " ").split()
    t, ux, uy, uz = map(float, values)
    if any(abs(t-target) < 1e-8 for target in targets):
        print(f"t={t:.2f} s, mean Ux={ux:.8f} m/s")
PY
```

`replace` 去掉向量外面的括号，`split` 按空白分列，`map(float, ...)` 把字符串转成数值。最终应依次得到 0.15、0.10、0.05、0.10 m/s。

对照通量时，可读取 `inletFlux` 与 `outletFlux` 相同时刻的值并相加，检查流入、流出是否平衡。

## 7. 从 1 秒继续算到 1.25 秒

完成前面的计算后，在同一个算例目录执行：

```bash
foamDictionary system/controlDict -entry startFrom -set latestTime
foamDictionary system/controlDict -entry endTime -set 1.25
icoFoam > log.restart 2>&1
```

`latestTime` 选择当前已有的最大时间目录。求解器从其中读取 U 和 p，再往后推进。正弦函数使用绝对模拟时间，所以 1.25 s 的入口平均速度回到 0.15 m/s。

重启后的边界参数从所选时间目录的 U 读取。查看 `1/U`，可以看到 codeContext 和 code 已随结果保存。要建立新的工况，建议另解压一份干净算例并修改 `0/U`；要有意改变重启工况，则修改实际读取的重启文件。

这一过程也说明了“按时间设置初值”的含义：初始场对应选定开始时刻的一份状态。重启使用保存的流场作为新的起点；时间循环中的连续变化由求解方程和时变边界共同产生。

## 8. 沿高度拆成两个进程

另解压一份干净的 `09-pulsed-profile` 作为并行工况。配套 `system/decomposeParDict` 内容为：

{{file:09-pulsed-profile/system/decomposeParDict}}

`n (1 2 1)` 表示 x、y、z 方向分别分成 1、2、1 份。入口被沿高度分给两个进程，每个进程持有一部分入口面。

```bash
blockMesh > log.blockMesh 2>&1
decomposePar > log.decomposePar 2>&1
mpirun -np 2 icoFoam -parallel > log.parallel 2>&1
reconstructPar -latestTime > log.reconstructPar 2>&1
```

`decomposePar` 划分网格与初始场；`mpirun` 启动两个求解进程；`reconstructPar` 将最后时刻重新组装成一个完整场，便于后处理。

各进程执行相同的全局求和调用。即使某个进程分不到入口面，也应参与 `gSum`，使归一化使用完整入口面积。在代码中把求和放在逐面循环外，并由所有进程执行，正是为这种情况准备的。

与串行比较时，先检查 1 s 的入口平均速度，再比较重构后的内部 U。配套参考数据包含串行、两进程和重启的检查结果。

## 9. 改参数的三个对照

### 对照一：关掉脉动

新工况中把 `codeContext/amplitude` 改为 0。运行后入口平均速度始终是 0.1 m/s，空间剖面保持抛物线。与脉动工况相比，可以区分时间变化造成的影响。

### 对照二：频率加倍

恢复 amplitude=0.5，将 frequency 改为 2。周期缩短为 0.5 s，0.125 s 达到 0.15 m/s，0.375 s 达到 0.05 m/s。可将写出间隔改为 0.025 s，保留每周期 20 份场输出。

### 对照三：从最大速度开始

frequency 恢复为 1，phase 设为 `1.57079632679`。初始相位为 π/2，入口从峰值开始，0.5 s 达到最小值。将这条曲线与零相位曲线叠加，会看到四分之一个周期的平移。

## 10. 怎样扩展为自己的边界

圆管入口可以把 shape 改为 $\max[1-(r/R)^2,0]$，其中 r 是面中心到管轴的距离；面积归一化部分可以保留。由实验流量 $Q(t)$ 控制入口时，可使用 $\overline U(t)=Q(t)/S$，再分配到各个面。

对于温度和浓度，使用 `scalarField` 计算各面值，赋值接口仍相同。要控制法向梯度、混合传热条件或更复杂的状态，可继续学习 `codedMixed` 或完整边界类开发。

当边界有多组可重用参数、独立成员状态或需要在多个项目中共享时，可阅读已有教程：[编写随时间变化的入口速度边界](/read/?slug=development-boundary)。它把同类脉动剖面做成 `.H/.C` 共享库，展示从字典代码到完整边界类的衔接。

## 参考

[v2512 codedFixedValue](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/finiteVolume/fields/fvPatchFields/derived/codedFixedValue/codedFixedValueFvPatchField.H) · [字段全局求和接口](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/OpenFOAM/fields/Fields/Field/FieldFunctions.H)。
