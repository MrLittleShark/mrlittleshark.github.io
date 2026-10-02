有些初始条件按区域给定，例如局部加热、液滴内部和外部、两种材料的初始浓度。写法是先判断单元中心属于哪个区域，再给这个单元赋值。本课用一个椭圆热区练习这个过程。

[下载椭圆热区算例](/downloads/programming/coded-fields-02-v2512.zip) · 先修：[用 codeStream 生成温度初始场](/read/?slug=coded-fields-01)

## 1. 确定椭圆的位置与大小

仍使用长 0.1 m、高 0.02 m 的二维区域，周围绝热。椭圆中心位于 $(0.05,0.01)\ \mathrm m$，x 方向半轴 $a=0.02\ \mathrm m$，y 方向半轴 $b=0.005\ \mathrm m$。

定义

$$q(x,y)=\frac{(x-x_c)^2}{a^2}+\frac{(y-y_c)^2}{b^2}.$$

满足 $q\le1$ 的位置在椭圆内部或边界上，赋予 350 K；其余位置赋予 300 K。

<figure class="lesson-figure"><img src="/assets/science/coded-fields-ellipse.png" alt="椭圆几何边界、按单元中心得到的温度初值及热扩散结果" loading="lazy"><figcaption>椭圆热区：几何判定、离散初值与扩散结果。<small>FoamLab，OpenFOAM v2512 配套算例。</small></figcaption></figure>

几个坐标代入后很容易检查公式：

| 点 | q | 初始温度 |
| --- | --- | --- |
| 中心 `(0.05, 0.01)` | 0 | 350 K |
| 右端点 `(0.07, 0.01)` | 1 | 350 K |
| 上端点 `(0.05, 0.015)` | 1 | 350 K |
| `(0.075, 0.01)` | 1.5625 | 300 K |

半轴决定从中心到边缘的距离，所以完整椭圆长轴为 0.04 m、短轴为 0.01 m。

## 2. 打开 `0/T`，先创建背景场

解压后进入 `04-ellipse`。`0/T` 完整内容如下：

{{file:04-ellipse/0/T}}

前半部分的 `codeInclude`、`codeOptions`、`codeLibs` 沿用上一课。进入 `code` 后，先取得网格，再创建一个全部为 300 K 的字段：

```cpp
scalarField temperature(mesh.nCells(), 300.0);
```

这样，区域外的单元已经有正确温度。后续循环只需要把椭圆内部改成 350 K。

## 3. 对每个单元计算区域判据

重点看循环部分：

```cpp
forAll(temperature, cellI)
{
    const vector& centre = mesh.C()[cellI];
    const scalar q = sqr((centre.x()-xc)/a)
                   + sqr((centre.y()-yc)/b);
    if (q <= 1.0)
    {
        temperature[cellI] = 350.0;
    }
}
```

第一行访问当前单元中心。接下来把中心坐标移到以椭圆中心为原点的坐标系：x 减去 `xc`，y 减去 `yc`。分别除以半轴后，两个方向都按自身长度归一化，再将平方相加。

`if` 根据 q 决定是否改写温度。原来的 300 K 保留在区域外，350 K 写入区域内。循环结束后，`temperature.writeEntry("", os)` 输出完整初值。

这里只有单元中心参与判断，因此边界附近会出现台阶状的单元分布。几何判据本身是椭圆，离散温度场由网格表示；细化网格后，这个台阶会变小。

## 4. 运行并查看初始时刻

```bash
cd ~/OpenFOAM/foamLabCodedFields/04-ellipse
bash Allrun
```

打开 `VTK/04-ellipse_0.vtk`，选择 Cell Data 的 `T`。初始单元温度只有 300 K 和 350 K 两个值。用 Surface With Edges 显示网格，可以看到哪些单元中心落在椭圆内。

若打开 `case.foam`，可在读取器中关闭单元到节点的插值，或查看单元数据。节点插值会让彩图边缘出现过渡颜色，而本例的原始单元初值仍是分段常数。

随后切换到 0.05、0.1 和 0.2 s。热量向外扩散，界面附近出现中间温度，椭圆中心也逐渐降温。这些中间值由扩散方程求得。

## 5. 检查热区体积和平均温度

解析椭圆面积为 $\pi ab$。厚度 $d=0.001\ \mathrm m$，初始热区的解析体积为

$$V_h=\pi abd=3.14159\times10^{-7}\ \mathrm{m^3}.$$

整个区域体积为 $0.1\times0.02\times0.001=2\times10^{-6}\ \mathrm{m^3}$，解析热区体积分数约为 0.15708。因此连续几何对应的平均温度为

$$\overline T=300+50\frac{V_h}{V}\approx307.854\ \mathrm K.$$

离散热区由整单元组成，其体积等于所有热单元体积之和。配套 80×20×1 网格选中 252 个热单元，热区面积为 $3.15\times10^{-4}\ \mathrm{m^2}$，比解析面积约大 0.268%；离散初值的平均温度为 307.875 K。差异来自边界单元的取舍。

`postProcessing/meanTemperature/0/volFieldValue.dat` 记录计算期间的体积平均温度。它应保持在这份离散初值的平均值附近。比较热量守恒时，应以实际离散初值为基准。

## 6. 扩展一：改成圆形热区

令两个半轴相等即可得到圆。对于当前高度 0.02 m 的区域，可以取半径 0.005 m：

```cpp
const scalar a = 0.005, b = 0.005;
```

中心与温度保持原值。圆面积变为 $\pi(0.005)^2$，是原椭圆面积的四分之一；对应的初始总温升积分也变为四分之一。

## 7. 扩展二：叠加两个热区

保留字段的 300 K 背景，把循环内的判据改为两个圆。下面两个热区半径均为 0.004 m，中心沿 x 分开：

```cpp
const scalar x = centre.x();
const scalar y = centre.y();
const scalar r = 0.004;
const bool leftHot = sqr(x-0.03) + sqr(y-0.01) <= sqr(r);
const bool rightHot = sqr(x-0.07) + sqr(y-0.01) <= sqr(r);
if (leftHot || rightHot)
{
    temperature[cellI] = 350.0;
}
```

`bool` 保存判定结果，`||` 表示两者满足任意一个即可。将 `||` 改成 `&&` 时，选中的就是两个区域的交集；上述两圆相互分开，因此交集为空，温度会全部保持 300 K。

## 8. 扩展三：给椭圆边缘加一个平滑过渡

若希望温度在边缘连续变化，可以把 `if` 块替换成：

```cpp
const scalar epsilon = 0.08;
const scalar weight = 0.5*(1.0 - Foam::tanh((Foam::sqrt(q)-1.0)/epsilon));
temperature[cellI] = 300.0 + 50.0*weight;
```

`sqrt(q)=1` 对应椭圆边界，那里 `weight=0.5`，温度为 325 K；向内逐渐接近 350 K，向外逐渐接近 300 K。`epsilon` 控制归一化径向坐标上的过渡宽度，数值越小，过渡越陡。

这个 `epsilon` 是无量纲参数。由于椭圆两个半轴长度不同，相同归一化宽度在 x、y 方向对应的实际长度也不同。若需要各方向相同的物理过渡厚度，应改用到边界的距离函数。

## 9. 怎样迁移到体积分数初值

在已有完整两相流算例中，可以把相同的几何判据写入 `0/alpha.water`：字段类型仍为 `volScalarField`，量纲改为 `[0 0 0 0 0 0 0]`，区域内设 1、区域外设 0。这里的 1 表示水相占满该单元，0 表示该单元没有水相。

```cpp
scalarField alpha(mesh.nCells(), 0.0);
forAll(alpha, cellI)
{
    const vector& c = mesh.C()[cellI];
    const scalar q = sqr((c.x()-xc)/a) + sqr((c.y()-yc)/b);
    alpha[cellI] = (q <= 1.0 ? 1.0 : 0.0);
}
alpha.writeEntry("", os);
```

这段代码替换的是初值生成部分。两相流的速度、压力、重力、物性与求解设置继续由两相流算例提供。本课下载包仍是热扩散算例，便于专门观察几何初值。

## 10. 练习：平移、加密、比较

先将 `xc` 从 0.05 改为 0.04，检查热区是否向左移动 0.01 m。随后用 `(160 40 1)` 网格重新生成相同椭圆，比较热区面积与解析面积的差异。最后尝试平滑过渡，比较初始边缘和 0.05 s 的温度剖面。

计算前查看 0 时刻，计算后再查看同一位置的结果。这样可以分别看清代码生成了什么初值，以及扩散方程怎样改变它。

## 参考

几何初始化教学思路参考 Joel Guerrero / Wolf Dynamics 的编程讲义及随附 `codeStream_INIT/elliptical_IC` 算例；本课使用重新编写的 v2512 热扩散案例。

接口：[OpenFOAM v2512 codeStream](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/OpenFOAM/db/dictionary/functionEntries/codeStream/codeStream.H)。
