这一节给二维通道设置一个抛物线入口：靠近上下壁面的速度低，中间的速度高。入口剖面保持不变，内部流场由 `icoFoam` 随时间求解。

同一个算例还使用 `codeStream` 生成内部初始速度。对照两段代码，可以看清“单元中心”和“边界面中心”分别怎样使用。

[下载固定入口剖面算例](/downloads/programming/coded-fields-03-v2512.zip)

## 1. 先确定坐标、速度方向与剖面

通道长 $L=0.1\ \mathrm m$、高 $H=0.01\ \mathrm m$，二维厚度为 0.001 m。入口在 x=0，出口在 x=0.1 m，流动方向为正 x。

取中心最大速度 $U_{\max}=0.15\ \mathrm{m/s}$，入口速度为

$$U_x(y)=4U_{\max}\eta(1-\eta),\qquad \eta=\frac{y}{H},\qquad U_y=U_z=0.$$

当 y=0 或 y=H 时，速度为零；y=H/2 时，速度达到 0.15 m/s。这个剖面的连续面积平均速度是 $2U_{\max}/3=0.1\ \mathrm{m/s}$。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-fixed.png" alt="通道入口抛物线速度剖面、离散面中心取值与计算速度场" loading="lazy"><figcaption>入口剖面及通道中的速度分布。<small>FoamLab，OpenFOAM v2512 配套算例。</small></figcaption></figure>

黏性系数取 $\nu=10^{-3}\ \mathrm{m^2/s}$，以通道高度和平均速度计算，雷诺数约为 1。这里选择低雷诺数规则通道，便于观察入口代码与结果的对应关系。

## 2. 看完整的 `0/U`

解压后进入 `05-fixed-profile`。速度文件如下：

{{file:05-fixed-profile/0/U}}

`volVectorField` 表示每个单元保存三个速度分量，量纲 `[0 1 -1 0 0 0 0]` 对应 m/s。文件中有两处 `#codeStream`：第一处在 `internalField`，第二处在 `boundaryField/inlet/value`。

| 位置 | 生成什么 | 长度从哪里来 |
| --- | --- | --- |
| `internalField` | 全部单元的初始速度 | `mesh.nCells()` |
| `inlet/value` | 入口各面的固定速度 | `inletPatch.size()` |

本例有 1600 个单元、20 个入口面，因此两段代码生成的向量数量分别为 1600 和 20。

## 3. 先给内部单元一个抛物线初始场

`internalField` 中的核心代码是：

{{snippet:PROFILE_INIT}}

`vectorField` 与前两课的 `scalarField` 用法相似，只是每个元素是向量。`vector::zero` 将三个分量初始化为零，随后逐个写入 `(Ux, 0, 0)`。

这里从 `mesh.C()` 取 y 坐标，将同一个抛物线沿 x 方向铺满整个通道。这样初始速度已经接近入口要求的分布，计算开始时内部速度调整较小。后续速度仍由动量方程和压力校正更新。

也可以把整段初值改成：

```foam
internalField uniform (0 0 0);
```

这时流体从静止状态开始，入口仍保持相同剖面，两组计算的区别主要体现在启动过程。比较它们时保留各自的早期时间输出。

## 4. 找到入口面，而后给每个面赋值

第二处代码位于 `inlet` 的 `value` 中。它执行时，传入的 `dict` 是 inlet 子字典。文件层级为：

```text
U 场字典
└── boundaryField
    └── inlet
        └── value #codeStream
```

所以 `dict.parent()` 返回 `boundaryField`，再调用一次 `parent()` 回到 U 场字典。取得网格后，按名称查找入口：

```cpp
const IOdictionary& fieldDict = static_cast<const IOdictionary&>
(
    dict.parent().parent()
);
const fvMesh& mesh = refCast<const fvMesh>(fieldDict.db());
const label patchID = mesh.boundaryMesh().findPatchID("inlet");
```

这段父字典访问对应上面展示的放置位置。将代码移动到其他层级时，要按新的文件层级取得字段字典。

`findPatchID("inlet")` 将边界名称转成编号。源码接着检查编号是否有效，并取得该 patch。改了网格中的入口名称时，同步修改这里的字符串和 `boundaryField` 中的键名。

最后逐面赋值：

```cpp
const fvPatch& inletPatch = mesh.boundary()[patchID];
vectorField velocity(inletPatch.size(), vector::zero);
const scalar height = 0.01, maxSpeed = 0.15;
forAll(velocity, faceI)
{
    const scalar eta = inletPatch.Cf()[faceI].y()/height;
    velocity[faceI] = vector(4.0*maxSpeed*eta*(1.0-eta), 0, 0);
}
velocity.writeEntry("", os);
```

`Cf()` 给出边界面中心坐标；`faceI` 是当前 patch 内部的面编号。公式对每个面的 y 坐标求值后，通过输出流写入 `value`。

`type fixedValue` 规定了这些面上的速度。读取时生成的列表成为固定值边界；计算随后更新内部场，入口列表保持给定的数值。

## 5. 其余边界怎样配合入口

速度文件中，出口用 `zeroGradient`，使速度可以按内部流动向出口延伸；上下壁面用 `noSlip`，速度为零；前后用 `empty`。

压力文件完整内容如下：

{{file:05-fixed-profile/0/p}}

`icoFoam` 的 p 是运动学压力，量纲为 $\mathrm{m^2/s^2}$。出口设为零，提供压力参考；入口与壁面的压力使用零法向梯度。速度和压力共同定义这个流动问题。

## 6. 运行与输出设置

```bash
cd ~/OpenFOAM/foamLabCodedFields/05-fixed-profile
bash Allrun
```

`Allrun` 先导出初始速度，再运行 `icoFoam`。计算从 0 到 1 s，步长为 0.001 s，每 0.05 s 保存一次，生成 0.05、0.1……1 等时间目录。

`system/fvSolution` 中，U 使用 `smoothSolver`，绝对容差为 `1e-9`；p 使用 PCG/DIC，绝对容差为 `1e-10`。PISO 每步进行两次压力—速度校正。时间离散采用 Euler，速度对流项采用 `Gauss linear`。

本例 x 向网格间距为 0.00125 m，按最大入口速度估算，$U_{\max}\Delta t/\Delta x=0.12$。日志同时给出实际 Courant 数，可在提高速度或加密网格后检查时间步是否仍合适。

## 7. 逐项核对入口结果

高度方向有 20 层网格，第一个入口面中心在 y=0.00025 m，最后一个在 y=0.00975 m。代入公式得到：

| 面中心位置 | 速度 x 分量 |
| --- | --- |
| y=0.00025 m | 0.014625 m/s |
| y=0.00475 m | 0.149625 m/s |
| y=0.00525 m | 0.149625 m/s |
| y=0.00975 m | 0.014625 m/s |

最靠近壁面的入口面中心位于通道内部，速度大于零。上下壁面本身由 `noSlip` 设置为零，两者对应不同的面。

使用 ParaView 的 Extract Block 选中 inlet，查看 U 的 x 分量；或者打开 `VTK/inlet/inlet_0.vtk`。计算后再看 1 s 的入口数据，数值应与初始固定列表一致。

入口面积平均速度记录在：

```text
postProcessing/inletMean/0/surfaceFieldValue.dat
```

20 个等面积面采用面中心采样，离散平均为 0.100125 m/s。它与解析积分得到的 0.1 m/s 有 0.125% 差异。这是离散采样引起的；第六节会通过面积归一化精确指定离散平均速度。

入口面积为 $10^{-5}\ \mathrm{m^2}$，因此体积流量大小为 $1.00125\times10^{-6}\ \mathrm{m^3/s}$。`inletFlux` 文件中的值为负，因为入口流动方向与网格外法向相反。

## 8. 改成其他固定剖面

### 改变速度大小

把入口代码中的 `maxSpeed` 改为 0.3，整条曲线放大两倍。若还希望初始内部场与入口一致，同步修改 `internalField` 中的 `maxSpeed`。

### 改变入口高度

把通道高度改为 0.02 m 时，先修改 `blockMeshDict` 顶部顶点，再将两段代码的 `height` 改为 0.02。保持 20 层时，单元高度加倍；改成 40 层可保持原来的分辨率。

### 使用偏移坐标

若入口下缘位于 y=0.03 m，可写成：

```cpp
const scalar yMin = 0.03;
const scalar eta = (inletPatch.Cf()[faceI].y()-yMin)/height;
```

`eta` 表示从入口下缘量起的相对高度。在倾斜入口上，可进一步把全局 y 坐标换成沿局部高度方向的投影。

### 生成固定的温度边界

在温度文件的对应 patch 下，仍用 `type fixedValue` 和 `value #codeStream`，把 `vectorField` 改为 `scalarField`。例如按高度设置壁面温度：

```cpp
scalarField temperature(inletPatch.size(), 300.0);
forAll(temperature, faceI)
{
    const scalar eta = inletPatch.Cf()[faceI].y()/height;
    temperature[faceI] = 300.0 + 20.0*eta;
}
temperature.writeEntry("", os);
```

同一套面中心访问方式可以用于速度、温度或浓度，字段类型与量纲随物理量相应调整。

## 9. 固定剖面与时变剖面如何衔接

本课的 `codeStream` 在文件读取时生成数据。即使表达式读取了当时的时间，生成的 `fixedValue` 列表也代表那次读取得到的值。

下一课使用 `codedFixedValue`：把计算公式放进边界更新过程。先复现本课的固定剖面，再在第五课读取当前时间，实现逐渐启动与周期变化。

## 参考

教学思路参考 Wolf Dynamics 的 `codeStream_BC` 入口剖面实例。接口：[OpenFOAM v2512 codeStream](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/OpenFOAM/db/dictionary/functionEntries/codeStream/codeStream.H)。
