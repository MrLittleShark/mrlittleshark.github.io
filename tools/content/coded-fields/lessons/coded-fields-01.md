想让一块材料左边温度低、右边温度高，可以直接按坐标计算每个网格单元的温度。`#codeStream` 就是把这段计算写在场文件里的方法。本课从 300 K 的均匀温度开始，再生成线性温度分布和高斯热斑。

配套程序使用 `laplacianFoam` 求解热扩散，三个算例只改变初始温度，网格、扩散系数和计算时间保持相同。

[下载本课三个算例](/downloads/programming/coded-fields-01-v2512.zip) · [下载本模块全部九例](/downloads/programming/coded-fields-all-v2512.zip)

## 1. 准备算例与开发环境

将下载包解压到 Linux 的个人工作目录。下面以 `~/OpenFOAM/foamLabCodedFields` 为例，实际放在其他位置时，修改 `cd` 后的路径。

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
cd ~/OpenFOAM/foamLabCodedFields
ls
```

环境脚本的路径对应 Ubuntu 软件包安装方式。已经加载 v2512 环境时可以直接进入目录。首次使用动态代码会调用 C++ 编译器，检查下面三个命令能否找到：

```bash
command -v laplacianFoam
command -v wmake
command -v g++
```

这三个算例分别是：

| 目录 | 初始温度 | 学习内容 |
| --- | --- | --- |
| `01-uniform` | 全部 300 K | 创建字段、输出字段 |
| `02-linear` | 沿 x 方向从 300 K 增加到 320 K | 读取单元中心、逐个赋值 |
| `03-gaussian` | 300 K 背景上的局部热斑 | 用空间函数生成光滑初值 |

每个目录都包含 `0/T`、`constant/transportProperties` 和 `system`。本课主要编辑 `0/T`；下载包中的其他文件已经配好。

## 2. 这个温度场将怎样变化

计算区域长 0.1 m、高 0.02 m，厚度为 0.001 m。网格为 80×20×1，共 1600 个单元。前后面设为 `empty`，用于二维计算；四周设为绝热边界。

温度满足

$$\frac{\partial T}{\partial t}=\nabla\cdot(D_T\nabla T).$$

这里 $D_T=10^{-4}\ \mathrm{m^2/s}$ 为常数。温差产生扩散，温度逐渐变得均匀；绝热边界使热量留在计算区域内。使用常数物性时，可通过体积平均温度检查这一点。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-temperature.png" alt="均匀、线性和高斯温度初值及其扩散结果" loading="lazy"><figcaption>三个初始温度场与 0.2 s 的扩散结果。<small>FoamLab，OpenFOAM v2512 配套算例。</small></figcaption></figure>

## 3. 示例一：生成 300 K 的均匀初值

打开 `01-uniform/0/T`。完整文件如下，后两例也使用相同的文件结构：

{{file:01-uniform/0/T}}

先看代码外面的三个部分：

- `class volScalarField` 表示单元中心标量场。一个单元保存一个温度数值。
- `dimensions [0 0 0 1 0 0 0]` 表示温度量纲，本文数值使用 K。
- `internalField` 设置内部单元的初值；`boundaryField` 设置边界约束。

`inlet` 和 `outlet` 在这里沿用了网格的左右边界名称。它们的温度条件都是 `zeroGradient`，即法向温度梯度为零，在本例中对应绝热。名称本身不会使热扩散问题变成流入、流出问题。

### 编译设置负责什么

`codeInclude` 引入 `fvCFD.H`，使下面的代码能够使用网格、字段和输入输出类型。`codeOptions` 告诉编译器在哪里找头文件；`codeLibs` 指定链接的库。首次读取 `0/T` 时，OpenFOAM 会在算例的 `dynamicCode` 目录中生成源码、编译共享库并加载。

`#{` 和 `#}` 包住一段原样保存的代码，末尾分号结束对应字典条目。下载包把同一组编译选项写在一行，复制时保留这一格式即可。

### 四行 C++ 怎样生成 1600 个温度

{{snippet:TEMP_CODES:01-uniform}}

第一行把当前的字段字典作为 `IOdictionary` 使用。这个对象保存了文件信息，并关联到对象注册表。第二行从注册表取得当前网格 `mesh`。

第三行创建名为 `temperature` 的 `scalarField`：长度取 `mesh.nCells()`，每个元素赋为 `300.0`。本例因此得到 1600 个 300 K。

最后一行将字段写入输出流 `os`。OpenFOAM 再从这个输出中读取 `internalField`。空字符串 `""` 表示这里仅输出条目值，外面的 `internalField` 键已经写好了。全部数值相同时，输出可以使用紧凑的 `uniform` 形式；空间变化的值则写成 `nonuniform List<scalar>`。

日常设置均匀初值，一行 `internalField uniform 300;` 就够了。这个例子使用代码，是为了先熟悉“取得网格—创建字段—输出字段”的完整过程。

## 4. 先运行第一例

```bash
cd ~/OpenFOAM/foamLabCodedFields/01-uniform
bash Allrun
```

`Allrun` 依次执行以下步骤。也可以逐条运行，边运行边查看日志：

```bash
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
foamToVTK -ascii -legacy -time 0 -fields '(T)' > log.initialVTK 2>&1
laplacianFoam > log.laplacianFoam 2>&1
foamToVTK -ascii -legacy -latestTime -fields '(T)' > log.finalVTK 2>&1
```

第三条命令导出初始温度，同时触发 `codeStream` 的读取与编译。网格先由 `blockMesh` 生成，所以代码读取单元中心时已经有可用的网格。第四条命令才开始推进热扩散方程。

第一次编译会显示生成动态库的信息。同一段代码再次运行时通常直接加载已有库，启动会快一些。日志保存在算例目录，不会淹没终端。

## 5. 示例二：按 x 坐标设置线性温度

接着打开 `02-linear/0/T`。编译设置和边界条件与第一例相同，`code` 中改为：

{{snippet:TEMP_CODES:02-linear}}

目标分布为

$$T(x,0)=300+20\frac{x}{L},\qquad L=0.1\ \mathrm m.$$

`forAll(temperature, cellI)` 遍历当前字段。`cellI` 是单元编号，`mesh.C()[cellI]` 是该单元中心的坐标向量，`.x()` 取 x 分量。代码用这个坐标计算温度，再写入相同编号的位置。

| 位置 | 公式得到的温度 | 含义 |
| --- | --- | --- |
| x=0 | 300 K | 左端的解析值 |
| x=0.05 m | 310 K | 区域中部的解析值 |
| x=0.1 m | 320 K | 右端的解析值 |

单元中心位于边界内部。80 个等宽单元的第一个中心在 x=0.000625 m，温度为 300.125 K；最后一个中心温度为 319.875 K。初始场中看到这两个极值，正是按单元中心采样的结果。

```bash
cd ../02-linear
bash Allrun
```

两端绝热，而初始线性分布在两端有非零梯度。开始计算后，靠近两端的温度会先调整，随后整个分布逐渐趋向平均温度 310 K。若希望两端始终保持 300 K 和 320 K，可把左右温度边界分别改为 `fixedValue`；那就变成了持续由边界维持温差的问题。

## 6. 示例三：生成一个光滑热斑

第三例在背景温度上叠加高斯函数：

$$T(x,y,0)=300+50\exp\left[-\frac12\left(\frac{(x-x_c)^2}{\sigma_x^2}+\frac{(y-y_c)^2}{\sigma_y^2}\right)\right].$$

中心取 $(x_c,y_c)=(0.05,0.01)\ \mathrm m$，两个方向的宽度取 $\sigma_x=0.01\ \mathrm m$、$\sigma_y=0.003\ \mathrm m$。x 方向宽度较大，因此热斑沿通道长度方向拉伸。

`03-gaussian/0/T` 的核心代码如下：

{{snippet:TEMP_CODES:03-gaussian}}

`sqr()` 计算平方。`r2` 是按两个宽度缩放后的距离平方，没有量纲。中心处 `r2=0`，温度达到解析峰值 350 K；沿 x 方向离开中心一个 `sigmaX`、且 y 保持在中心时，温升降为 $50e^{-1/2}\approx30.33\ \mathrm K$。

`const vector& centre` 引用当前单元中心坐标，方便同时读取 x、y。`Foam::exp()` 计算指数函数。这里的 `50.0` 是温升幅值，`300.0` 是背景温度，两者可以分别调整。

```bash
cd ../03-gaussian
bash Allrun
```

温度场按单元中心采样，本网格没有恰好落在热斑中心的单元，因此初始最大值略低于 350 K。扩散以后，热斑峰值降低、范围扩大。

## 7. 时间、输出与求解精度在哪里设置

三个算例的关键设置相同：

| 文件与条目 | 值 | 本例中的作用 |
| --- | --- | --- |
| `controlDict/startTime` | 0 | 从 `0/T` 的初值开始 |
| `controlDict/endTime` | 0.2 | 计算到 0.2 s |
| `controlDict/deltaT` | 0.002 | 每步推进 0.002 s，共 100 步 |
| `controlDict/writeInterval` | 0.05 | 每 0.05 s 保存一次温度场 |
| `fvSchemes/ddtSchemes` | Euler | 一阶隐式时间离散 |
| `fvSolution/solvers/T/tolerance` | `1e-10` | 温度线性方程的绝对残差阈值 |
| `fvSolution/solvers/T/relTol` | 0 | 每次求解按绝对阈值停止 |
| `controlDict/writePrecision` | 12 | 文本输出保留的有效数字数 |

隐式 Euler 适合本课的扩散计算。若要比较时间离散误差，可将 `deltaT` 减半，比较相同时间的温度。`tolerance` 控制线性方程解到什么程度；网格尺寸、时间步和离散格式共同影响温度分布的数值误差。

## 8. 在 ParaView 中比较结果

运行 `paraFoam`，或在 ParaView 中打开 `Allrun` 创建的 `case.foam`，点击 Apply。选择 `internalMesh`，着色字段选 `T`，视角沿 z 方向看平面。

依次切换 0、0.05、0.1 和 0.2 s。比较高斯热斑时，把色标固定为 300～350 K，这样颜色变化就对应同一个温度范围。查看单元中心离散值时，可直接打开 `VTK` 文件并选择 Cell Data 中的 `T`。

平均温度保存在：

```text
postProcessing/meanTemperature/0/volFieldValue.dat
```

均匀算例保持 300 K，线性算例保持约 310 K；高斯热斑的平均值由初始热量决定。先看这个文件，再看彩图，可以同时了解整体热量与局部分布。

## 9. 修改参数，自己做三个对照

1. 将线性例中的 `20.0` 改为 `40.0`。右端解析温度变为 340 K，平均温度变为 320 K。
2. 将高斯例中的 `sigmaX` 改为 `0.005`。热斑变窄，峰值参数保持相同，区域内总温升积分随之减小。
3. 保留原热斑，将网格从 `(80 20 1)` 改为 `(160 40 1)`，重新运行。比较初始最大温度，以及 0.2 s 的中心附近温度。

每组对照使用单独的算例副本。复制原始包中的目录后修改，就能在 ParaView 中同时打开两组结果。

下一节继续使用温度场，改成“椭圆内 350 K、椭圆外 300 K”，学习区域判定和分段初值。

## 参考

接口：[OpenFOAM v2512 codeStream 源码](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/OpenFOAM/db/dictionary/functionEntries/codeStream/codeStream.H)。
