本课编写一个通道入口：速度沿高度呈抛物线分布，入口平均速度随时间周期变化。完成后，你可以在 `0/U` 中设置平均速度、脉动幅值和频率，并像使用 `fixedValue` 一样使用这个边界。

先修：[自定义入口速度边界](/lessons/programming-08/)。本课把源码、编译、算例配置、结果检查和修改参数串成一次完整操作。

## 1. 先确定入口要产生什么速度

通道长 0.1 m、高 0.01 m，二维网格厚度为 0.001 m。入口在 x=0，速度沿正 x 方向；上下壁面静止。平均入口速度取

$$\overline U(t)=U_m[1+A\sin(2\pi f t+\varphi)].$$

本例 $U_m=0.1\ \mathrm{m/s}$、$A=0.5$、$f=1\ \mathrm{Hz}$、$\varphi=0$。因此速度变化周期为 1 s，平均速度在 0.05～0.15 m/s 之间变化。

高度方向取抛物线形状：

$$g(y)=6\eta(1-\eta),\qquad \eta=\frac{y-y_0}{H}.$$

$y_0$ 是入口下缘的 y 坐标，$H$ 是入口高度。下缘和上缘的速度为零，中部速度最大。程序在每个入口面的中心计算这个形状，再按面面积归一化，使网格上的面积平均速度等于给定的 $\overline U(t)$。

| 时间 / s | 入口面积平均速度 / (m/s) | 流入体积流量 / (m³/s) |
| --- | --- | --- |
| 0 | 0.10 | 1.0×10⁻⁶ |
| 0.25 | 0.15 | 1.5×10⁻⁶ |
| 0.50 | 0.10 | 1.0×10⁻⁶ |
| 0.75 | 0.05 | 0.5×10⁻⁶ |
| 1.00 | 0.10 | 1.0×10⁻⁶ |

流量由平均速度乘入口面积得到。这里的面积是 $0.01\times0.001=10^{-5}\ \mathrm{m^2}$，二维计算保留的网格厚度也参与面积计算。

<figure><img src="/assets/science/development-boundary-results.png" alt="入口平均速度时序与三个时刻的抛物线剖面"><figcaption>入口速度时序与离散剖面。<small>配套算例的 OpenFOAM v2512 计算结果。</small></figcaption></figure>

左图比较设定函数与计算保存的入口平均速度，右图显示三个时刻各入口面的速度。后面的检查就使用这两种结果。

## 2. 解压源码，找到要修改的文件

从本页的案例入口下载 ZIP，在 Linux 工作目录解压。打开终端，进入解压后的 `foamLabPulsedInlet` 文件夹：

```bash
cd ~/OpenFOAM/foamLabPulsedInlet
ls
```

上面路径按实际解压位置调整。目录应包含：

```text
foamLabPulsedInlet/
├── Allwmake
├── boundary/
│   ├── foamLabPulsedInletFvPatchVectorField.H
│   ├── foamLabPulsedInletFvPatchVectorField.C
│   └── Make/
│       ├── files
│       └── options
├── case/
│   ├── 0/U
│   ├── 0/p
│   ├── constant/transportProperties
│   └── system/
│       ├── blockMeshDict
│       ├── controlDict
│       ├── fvSchemes
│       ├── fvSolution
│       └── decomposeParDict
└── reference-results/
```

先编辑 boundary 中的 `.H` 和 `.C`，生成共享库；再编辑 case 中的入口参数，运行 `icoFoam`。reference-results 是本文计算得到的文本结果，可与自己的输出对照。

## 3. 在头文件中声明一个新的边界类型

打开 `boundary/foamLabPulsedInletFvPatchVectorField.H`。完整内容如下：

{{HEADER}}

类继承 `fixedValueFvPatchVectorField`，因此它向速度方程提供“已经给定的边界速度”。每次更新时间时，我们负责计算这些值，基类负责固定值边界与有限体积方程之间的连接。

成员变量保存在每个边界对象中，末尾下划线用于区分成员和临时变量：

| 成员 | 字典键 | 用途与单位 |
| --- | --- | --- |
| `meanSpeed_` | meanSpeed | 时间平均的面积平均速度，m/s |
| `amplitude_` | amplitude | 相对脉动幅值，本例 0.5 |
| `frequency_` | frequency | 频率，Hz |
| `phase_` | phase | 初相位，rad |
| `yMin_` | yMin | 入口下缘 y 坐标，m |
| `height_` | height | 入口高度，m |
| `direction_` | direction | 速度方向，读入后归一化 |

`TypeName("foamLabPulsedInlet")` 定义字典使用的类型名称。稍后 `0/U` 中的 `type` 必须与这段字符串一致。C++ 类名可以更长，方便表示它是一个速度边界类。

`using fixedValueFvPatchVectorField::operator=;` 让基类的赋值重载保持可见，避免编译器报告派生类隐藏基类重载。真正更新边界值的位置仍在后面的 `updateCoeffs()`。

这里声明了五种构造方法。最常用的字典构造接收 `p`、`iF`、`dict`：`p` 是当前入口 patch，`iF` 是它所依附的内部速度场，`dict` 就是入口子字典。映射构造还接收 mapper，用于把旧边界数据转到新网格；另外两种复制构造分别保留或更换内部场引用。

两个 `clone()` 返回与当前对象相同类型的新对象。OpenFOAM 在复制或重新组织字段时通过这个接口保留自定义边界的类型和参数。

## 4. 在源文件中读入参数

打开 `boundary/foamLabPulsedInletFvPatchVectorField.C`。下面四段按顺序组成整个文件，先写头文件引用和构造方法：

{{CONSTRUCTORS}}

第一种构造提供一组可用默认值。读取 `0/U` 时使用的是第二种：冒号之后先构造 `fixedValueFvPatchVectorField(p, iF, dict)`，让基类建立 patch 与内部场的联系，并读入 value；随后读取本边界新增的参数。

`dict.get<scalar>("meanSpeed")` 要求字典中存在 meanSpeed，缺少时会报告键名。`getOrDefault<scalar>("phase", 0)` 则允许省略 phase，并使用零相位。频率 1 表示每秒一个周期，phase 的单位是弧度。

参数检查把输入范围写进程序：高度为正，方向向量非零，速度和频率非负，幅值在 0～1 之间。这个幅值范围对应本课的单向脉动入口；`amplitude 1` 时最小平均速度刚好降到零。

`direction_ /= mag(direction_)` 将方向向量除以自身长度。因此 `(1 0 0)` 和 `(2 0 0)` 都表示正 x 方向，速度大小始终由 meanSpeed 决定。

最后的 `evaluate()` 使入口在读入时就按当前时间计算一次。初始 `value uniform (0 0 0)` 提供文件中的起始值，随后由本类的速度公式更新。

后三个构造的共同工作是复制所有参数，同时用合适的基类构造处理字段。漏掉 height 或 frequency 这类成员，会使复制后的边界与原边界产生不同结果，所以复制列表应与头文件的成员列表逐项对应。

## 5. 补齐映射接口

在同一个 `.C` 文件中继续加入：

{{MAPPING}}

`autoMap()` 用于现有边界随网格映射调整。这里的新增成员都是整个入口共用的常数，没有单独按面保存的参数数组，因此基类完成速度值的映射后即可。下一次更新会根据新面中心重新计算剖面。

`rmap()` 从另一个边界反向映射数据，addr 给出面编号对应关系。先调用基类映射速度值，再将 other 转回本类，复制平均速度、频率和几何参数。`refCast` 会检查对象类型，避免把其他边界的数据当成本类成员读取。

以后若增加“每个入口面的粗糙度”或“每个面的实验修正系数”，这些数组也要在映射构造、autoMap 和 rmap 中同步处理。当前实现每次从面中心计算形状，适合本课这种固定平面矩形入口。

## 6. 逐面计算速度，并保证离散流量

继续加入 `updateCoeffs()`：

{{UPDATE}}

程序按下面的顺序计算一次入口速度。

首先检查 `updated()`。同一轮方程装配可能多次访问边界，这个标记使已经完成的计算直接返回；基类在后续更新周期会重新允许更新。

`patch().Cf()` 给出当前入口的面中心，每个元素是三分量坐标。`patch().magSf()` 给出各面的面积。`shape` 的长度等于本进程拥有的入口面数，初始全部为零。

循环中取面中心的 y 坐标，计算 `eta=(y-yMin)/height`。入口下缘 eta=0，上缘 eta=1，中间 eta=0.5。位于给定高度内的面使用 `6*eta*(1-eta)`；高度范围之外的面保持零值。几何整体移动后，需要在 `0/U` 中同步调整 yMin。

接下来计算两个全局和：

$$S=\sum_f S_f,\qquad G=\sum_f g_f S_f.$$

S 是入口总面积，G 是形状函数的面积加权和。最终速度为

$$\mathbf U_f=\overline U(t)g_f\frac{S}{G}\mathbf d.$$

因此，对所有面做面积平均，恰好得到 $\overline U(t)\mathbf d$。连续抛物线的平均值虽然已经归一化，网格却是在面中心采样。这里额外做一次离散归一化，使不同入口划分仍使用同一指定流量。

以本例 20 个等面积入口面为例，eta 依次为 0.025、0.075、……、0.975。这些面中心的原始形状平均值为 1.00125，因此程序乘以约 0.99875156 的修正因子。在 0.25 s，平均速度为 0.15 m/s，中间面 eta=0.475 或 0.525，速度计算为

$$U_x=0.15\times6\times0.475\times0.525/1.00125\approx0.2241573\ \mathrm{m/s}.$$

这就是后面保存文件中应该出现的中部数值。若增加到 40 个等面积面，修正因子会更接近 1，但平均流量仍保持相同。

`vectorField` 是按面存放的矢量数组，`scalarField` 是按面存放的标量数组。这里用一个方向矢量乘一个标量场，得到每个面各自的三分量速度。shape 为入口各面提供不同倍率，speed 为当前时刻提供整个入口共用的速度尺度。

当前输入的高度与速度使用普通 scalar，因此字典填写的是数值，单位由本类的接口约定为 m、m/s 和 Hz。输入 `height 10` 会被当作 10 m；若实验数据以毫米给出，应先换算。希望让程序检查量纲时，可以进一步把这些成员改为 dimensionedScalar，并同步调整字典格式、读入和写出代码。

`gSum` 会合并全部并行进程上的贡献。两进程把入口一分为二时，仍应使用整个入口的 S/G；普通局部求和会让每个分区分别归一化，在不对称划分中改变剖面。

`db().time().value()` 取得求解器当前的物理时间。用它计算正弦函数后，`operator==(...)` 将生成的整组矢量赋给边界值，最后调用基类 `updateCoeffs()` 标记本次更新完成。

## 7. 写出参数，让计算能够重启

在 `.C` 文件末尾加入：

{{WRITE}}

`fvPatchVectorField::write(os)` 写出类型等公共信息，后面的 writeEntry 保存自定义参数。最后一行 `writeEntry("value", os)` 保存当前各面的速度。

运行到 1 s 后，打开 `1/U`，入口块中应同时存在 meanSpeed、frequency、height 等参数和 20 个速度向量。重启时程序从这些参数重新创建边界，再按新的时间计算速度。

`makePatchTypeField` 把本类的构造方法注册到运行时选择表。加载共享库后，OpenFOAM 才能通过 `type foamLabPulsedInlet` 找到这些方法。头文件里的 TypeName、这里的注册和 controlDict 中的库加载分别完成命名、登记和装载。

## 8. 编译共享库

打开 `boundary/Make/files`：

{{MAKE_FILES}}

第一行是要编译的源文件。`LIB` 指定共享库输出位置，`FOAM_USER_LIBBIN` 是当前用户的 OpenFOAM 库目录，编译后会生成 `libfoamLabPulsedInlet.so`。

再打开 `boundary/Make/options`：

{{MAKE_OPTIONS}}

`-I.../finiteVolume/lnInclude` 让编译器找到 fvPatchField 等头文件；`-lfiniteVolume` 在链接时引入有限体积库的实现。

在已经加载 v2512 环境的终端中，从解压目录执行：

```bash
cd boundary
wmake libso
ls "$FOAM_USER_LIBBIN/libfoamLabPulsedInlet.so"
cd ..
```

编译输出中，先出现 `-c foamLabPulsedInletFvPatchVectorField.C`，表示把源文件编译成目标文件；最后出现 `-shared`，表示将目标文件链接为可动态加载的共享库。Make 目录下产生的机器平台子目录保存中间文件，源码仍保留在 boundary 根目录。

运行求解器的终端也应加载同一套 v2512 环境，使编译与运行使用相同的头文件、库和编译选项。把源码复制到另一台 Linux 机器后，在那台机器上重新执行 wmake，便能使用其本地库配置生成对应产物。

屏幕应出现编译和链接命令，最后的 ls 显示生成库的完整路径。也可以在解压目录运行 `bash Allwmake`，它执行同一编译步骤。

修改 `.H` 或 `.C` 后重新编译；只改变 `0/U` 中的速度、频率等数值时，直接重新运行算例即可。

## 9. 把新边界写入通道算例

进入 case 目录，打开 `0/U`。下载包已给出以下完整速度配置：

{{FIELD_U}}

入口类型对应我们刚才注册的字符串。`height 0.01` 与网格上下壁面的间距一致，`yMin 0` 对应下壁位置。direction 指向正 x，即计算域内部。

出口使用 zeroGradient，让速度随内部流场延伸到出口；上下壁面用 noSlip。frontAndBack 使用 empty，与单层二维网格配套。

再打开 `0/p`，检查压力边界：

{{FIELD_P}}

入口给定速度，压力采用零法向梯度；出口固定 p=0，为整个压力场提供参考。icoFoam 的 p 是运动学压力，量纲为 m²/s²。

`constant/transportProperties` 中设 `nu 1e-5` m²/s。用平均速度 0.1 m/s 和高度 0.01 m 估计，雷诺数为 100，配套计算采用层流模型。流量随时间变化时，内部速度仍由动量方程计算，入口给定剖面只直接作用于入口面。

打开 `system/controlDict`，确认以下条目：

```foam
application icoFoam;
startFrom startTime;
startTime 0;
endTime 1;
deltaT 0.001;
writeControl runTime;
writeInterval 0.25;
writePrecision 12;
libs ("libfoamLabPulsedInlet.so");
```

这段从完整文件中摘出与运行相关的设置：从 0 计算到 1 s，每步 0.001 s，共 1000 步；每 0.25 s 保存一次场。writePrecision 决定文本输出的有效位数，线性方程的停止容差在 fvSolution 中设置。

`libs` 行负责装载自定义边界。读取 `0/U` 之前，求解器已经加载该库并获得 foamLabPulsedInlet 类型。

### 查看网格与入口高度的对应关系

打开 `system/blockMeshDict`，几何和边界的完整定义为：

{{MESH}}

vertices 中有 8 个点，前四个的 z=0，后四个的 z=0.001。每一组都按通道矩形排列；例如点 0 为 `(0 0 0)`，点 3 为 `(0 0.01 0)`，它们之间的距离就是入口高度。

`hex (0 1 2 3 4 5 6 7)` 用这些点组成一个六面体块，`(80 20 1)` 表示沿 x、y、z 分别划分 80、20、1 个单元。入口的 20 个面由 y 方向的 20 层产生，面中心从 0.00025 m 开始，每隔 0.0005 m 一个。

`inlet` 的面由点 `(0 4 7 3)` 围成，四个点的 x 都为零。outlet 位于 x=0.1，walls 合并上、下两个平面。面顶点顺序确定外法向，所以入口面积向量朝负 x，后处理中的流入 phi 相应为负。

若把通道高度改为 0.02 m，修改四个上缘点的 y 坐标，并把 `0/U` 的 height 改为 0.02。保持 20 层时，单元高度变成 1 mm；希望保持原来的分辨率则用 40 层。若只改变入口 meanSpeed，网格可以保持原样。

### 查看离散格式与线性求解设置

接着打开 `system/fvSchemes`：

{{SCHEMES}}

Euler 使用一阶时间离散，当前速度由上一时刻的场推进。`gradSchemes` 的 Gauss linear 先在线性插值得到的面值上做梯度计算；`div(phi,U)` 为速度对流项选用线性插值。这里采用规则、低雷诺数的教学通道，可以把注意力集中在边界接口和速度时序上。

`laplacianSchemes`、`snGradSchemes` 中的 corrected 加入非正交修正。本例网格正交，相关修正项很小；若后续改为倾斜或弯曲网格，应结合网格质量重新检查数值设置。`fluxRequired` 指定压力方程所需的面通量，压力校正用它更新 phi。

再打开 `system/fvSolution`：

{{SOLUTION}}

p 使用 PCG 和 DIC 预条件器，U 使用 smoothSolver 与 symGaussSeidel 平滑器。`tolerance 1e-10` 与 `1e-9` 分别规定两类线性方程求解的残差停止阈值；`relTol 0` 使本例每次按绝对容差求解。

`pFinal { $p; relTol 0; }` 先复制 p 的设置，再明确最后一次压力校正的相对容差。PISO 内部的 `nCorrectors 2` 表示每个时间步进行两次压力—速度校正。它与每次线性方程求解的迭代次数属于两个层次：前者控制耦合循环，后者在日志中显示为 No Iterations。

`deltaT 0.001` 使每个脉动周期包含 1000 步。按本例最大入口速度和 x 向网格间距估计，对流 Courant 数约为 0.18。提高 meanSpeed 或细化网格后，可先用相同比例减小时间步，并检查日志中的最大 Courant 数。要评价时间精度，可再用 0.0005 s 重算，对照同一位置的速度时序。

## 10. 生成网格，开始计算

在 case 目录依次运行：

```bash
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
icoFoam > log.icoFoam 2>&1
```

先打开 `log.checkMesh`。网格是 80×20×1，共 1600 个单元，入口有 20 个面。检查结果应显示 `Mesh OK.`。再打开 `log.icoFoam`，查看时间是否推进到 1，并在末尾出现 End。

每一步求解速度，再通过 PISO 压力校正调整通量。`fvSolution` 的 `nCorrectors 2` 指定两次压力校正，`pFinal` 为最后一次压力求解提供设置；本例将其容差设为与 p 相同的 `1e-10`，相对容差为 0。

计算后 case 下应出现 `0.25`、`0.5`、`0.75`、`1` 四个新时间目录。可以运行 `paraFoam`，只显示 inlet 边界并用 U 的 x 分量着色，切换时间查看剖面强弱的周期变化。

## 11. 检查平均速度、流量和保存的边界值

controlDict 已配置三个 surfaceFieldValue 对象。它们每步分别计算入口 U 的面积平均、入口 phi 的求和和出口 phi 的求和。打开：

```text
postProcessing/inletMean/0/surfaceFieldValue.dat
postProcessing/inletFlux/0/surfaceFieldValue.dat
postProcessing/outletFlux/0/surfaceFieldValue.dat
```

第一列是时间。inletMean 在 0.25 s 的值应为 `(0.15 0 0)`，inletFlux 应为 `-1.5e-6`，outletFlux 应接近 `1.5e-6`。

phi 使用网格的外法向约定，入口流入为负，出口流出为正。因此比较入口和出口时，应检查两者相加是否接近零。直接比较两者符号会把正常流入、流出误认为方向错误。

再打开 `0.25/U` 的 inlet 块。它包含 20 个面速度，中间两个面速度约为 0.2241573 m/s，靠近壁面的两个面约为 0.0219101 m/s。面中心位于 y=0.25 mm、0.75 mm 等位置，最靠壁的入口面中心也有非零速度；壁面本身由相邻的 noSlip patch 处理。

配套计算的入口平均速度与设定函数之差小于 $5\times10^{-14}$ m/s，入口与出口体积流量和的最大绝对值约为 $1.1\times10^{-16}$ m³/s。这两项检查分别确认边界函数和该算例的流量守恒。分析内部非定常速度时，还可通过减小时间步、细化网格比较离散影响。

### 直接用文本结果做一次数值检查

如果希望快速读取关键时刻，可以在 case 目录运行下面的 Python 代码。它读取刚才的入口平均速度文件，只打印四个保存时刻对应的结果：

```bash
python3 - <<'PY'
from pathlib import Path

path = Path("postProcessing/inletMean/0/surfaceFieldValue.dat")
targets = (0.25, 0.50, 0.75, 1.00)
for line in path.read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    values = line.replace("(", "").replace(")", "").split()
    time, ux, uy, uz = map(float, values)
    if any(abs(time - target) < 1e-8 for target in targets):
        print(f"t={time:.2f} s, mean Ux={ux:.8f} m/s")
PY
```

输出应依次为 0.15000000、0.10000000、0.05000000、0.10000000 m/s。括号只是向量的文本格式，代码先去除括号，再把时间和三个速度分量转换为浮点数。

更换 frequency 后，可同步修改 targets 中的时刻；更换对象名称后，需要修改路径中的 inletMean。这样可以把源码中的参数、运行字典和数值结果直接对应起来。

## 12. 从保存结果继续计算，再检查并行运行

先测试重启。在同一 case 目录执行：

```bash
foamDictionary system/controlDict -entry startFrom -set latestTime
foamDictionary system/controlDict -entry endTime -set 1.25
icoFoam > log.restart 2>&1
```

当前最大时间目录为 1，所以这次从 1 s 接着计算，生成 1.25。打开 `1.25/U`，入口平均速度应回到 0.15 m/s。频率、相位等参数由保存文件读取，正弦函数使用累计物理时间，因此重启前后时间连续。

接着使用一份重新解压的干净 case 测试两进程。在该目录运行：

```bash
blockMesh
decomposePar
mpirun -np 2 icoFoam -parallel > log.parallel 2>&1
reconstructPar
```

decomposeParDict 使用 `n (1 2 1)`，沿高度方向把入口分给两个进程。它同时检验映射构造和跨进程的 gSum。重构后对比 1/U，配套计算的串行、两进程内部速度最大差约为 $2.3\times10^{-11}$ m/s。

## 13. 修改一个参数，观察变化

复制一份干净 case 作为对照目录，在它的 `0/U` 中把 `amplitude 0.5` 改成 `amplitude 0`。保持 meanSpeed=0.1，重新生成网格并运行。

这时入口平均速度始终为 0.1 m/s，形状仍为抛物线，流入体积流量始终为 $10^{-6}$ m³/s。reference-results 提供脉动工况的数据，可把两条入口平均速度曲线画在一起比较。配套的零幅值计算已得到上述恒定平均值。

再把 amplitude 恢复为 0.5，将 frequency 改成 2。预期周期缩短到 0.5 s，0.125 s 达到 0.15 m/s，0.375 s 达到 0.05 m/s。想保存这些时刻，可把 writeInterval 改为 0.125。设置文件变更只影响新计算，源码公式保持不变。

如果把 height 改成 0.02，而网格仍只有 0.01 m 高，程序会按照更高入口的前半段计算形状。这正好说明几何参数的作用：先确定真实入口的上下缘，再填写 yMin 和 height。改变几何高度时，应同步更新 blockMeshDict。

## 14. 常见问题对应到具体文件

| 现象 | 检查位置与处理 |
| --- | --- |
| `Unknown patchField type foamLabPulsedInlet` | 检查 controlDict 的 libs、库文件是否存在，以及 0/U 的 type 拼写 |
| 提示共享库无法打开 | 重新加载 v2512 环境，确认库位于当前 FOAM_USER_LIBBIN，重新执行 wmake libso |
| 提示缺少 meanSpeed 或 height | 在当前读取的 U 文件入口块补齐对应键；重启时检查所选时间目录中的 U |
| 提示 height 或 amplitude 范围错误 | 高度设为正值，幅值设在 0～1；本例 amplitude=1.5 会在读入时给出具体输入错误 |
| 报告入口面积或形状加权和为零 | 检查 inlet 是否为空，以及 yMin、height 是否覆盖实际面中心 |
| 更改 0/U 后重启结果不变 | latestTime 使用已有最大时间目录中的 U；新工况从独立干净算例开始，或有意修改重启文件 |
| `pFinal` 条目缺失 | 在 fvSolution/solvers 中保留下载包的 pFinal 设置，供 PISO 最后一次压力求解使用 |

## 15. 进一步改成实验波形或三维入口

实际泵或风机的入口曲线常由实验给出。可以保留空间剖面、离散归一化和映射接口，把计算 speed 的正弦表达式替换为 `Function1<scalar>` 时间函数，再由字典选择 table、constant 等形式。新增可复制的函数对象后，要同时更新构造、复制和 write。

三维圆管入口则先由面中心计算到圆心轴线的径向距离，再使用 $1-(r/R)^2$ 这样的形状。面积归一化部分仍可保留。需要倾斜平面时，应将高度坐标改为沿指定局部方向的投影，并用面积法向检查所要求的是速度均值还是法向体积流量。

这些扩展都可以沿本课的检查顺序进行：先核对保存的入口值，再核对面积平均和通量，最后查看内部流动响应。
