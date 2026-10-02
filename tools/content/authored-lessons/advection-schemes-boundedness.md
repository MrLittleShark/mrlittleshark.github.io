对流格式用于计算流体穿过网格面时携带多少物理量。速度、温度和组分浓度都需要这一步。格式的选择会影响涡结构、温度锋面和浓度峰值：有的结果较平滑，有的能保留更多细节，也有的会出现振荡。

## 用一个平移脉冲比较格式

一维常速输运方程为

\[
\frac{\partial T}{\partial t}+u\frac{\partial T}{\partial x}=0,
\qquad T(x,t)=T_0(x-ut).
\]

$u$ 为给定速度，$T$ 是被输运的标量。速度恒定且没有扩散时，初始分布保持形状，沿流向移动距离 $ut$。

配套案例 `exercises/one-dimensional-advection` 使用长 1 m 的区域和 200 个等长单元。$u=1\,\mathrm{m/s}$，$\Delta t=0.001\,\mathrm{s}$。初始脉冲位于 $0.15<x<0.35\,\mathrm m$，中心为 0.25 m，峰值为 1 K；在 $t=0.2\,\mathrm s$ 时，解析中心位于 0.45 m。

这里的 `T` 表示被动温差。温差随给定速度运动，速度本身保持不变。`DT=0` 关闭了物理扩散，因此特别适合比较数值格式。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-advection-profile-errors.png" alt="一维输运中的格式误差曲线" loading="lazy"><figcaption><strong>一维输运中的格式误差曲线</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 157 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

上图用阶跃分布展示输运误差。曲线边缘被抹宽称为数值扩散；阶跃附近出现额外峰谷称为振荡。本课脉冲的初值更光滑，适合观察峰值降低和整体展宽。

## 迎风格式：取上游单元的值

令公共面左侧单元为 $P$，右侧为 $N$。当流向从左向右时，迎风格式取 $T_f=T_P$；流向反转时取 $T_f=T_N$。它使用流体到达该面之前所在单元的值。

在 `system/fvSchemes` 中配置：

```foam
divSchemes
{
    default    none;
    div(phi,T) Gauss upwind;
}
```

`div(phi,T)` 对应求解器代码中的 `fvm::div(phi,T)`。`Gauss` 表示把对流散度转换为面通量求和，`upwind` 指定面值的计算方法。`default none` 要求参与计算的散度项有明确配置，漏写时程序会指出缺失的条目。

迎风格式通常很稳健，适合初次运行和陡峭分布。它在平滑区域具有一阶空间精度，容易把锋面抹宽。对一维均匀网格，单看空间迎风离散，其主要误差类似一个附加扩散项，扩散系数约为 $u\Delta x/2$。与具体时间格式结合后，总误差还会随时间步变化。

## 中心插值：同时使用两侧单元

面位于两单元中心的中点时，中心插值为

\[
T_f=\frac{T_P+T_N}{2}.
\]

将原来的对流项替换为：

```foam
div(phi,T) Gauss linear;
```

在规则网格和平滑分布上，这种插值的空间误差通常比迎风小。但上游和下游对面值的贡献相同，当标量在少数单元内急剧变化时，计算可能产生过冲或欠冲。例如理论范围为 $0\le T\le1$，数值结果却可能出现 $T<0$ 或 $T>1$。

这种问题与变量用途有关。小幅振荡可能已经使浓度变成负值；对密度、湍动能等要求非负的量，后续物性或模型计算也会受到影响。因此比较格式时要同时记录极值和误差。

## 线性迎风与限制格式

线性迎风使用上游单元值和梯度，将数值外推到面中心：

\[
T_f=T_P+(\nabla T)_P\cdot(\mathbf x_f-\mathbf x_P),
\]

其中 $P$ 是上游单元。对应设置为

```foam
gradSchemes
{
    default Gauss linear;
    grad(T) Gauss linear;
}

divSchemes
{
    default    none;
    div(phi,T) Gauss linearUpwind grad(T);
}
```

最后的 `grad(T)` 指向梯度计算设置。`linearUpwind` 保留迎风方向，同时利用梯度提高平滑区的重建精度；梯度过大时仍可能出现新极值。

限制格式根据附近场值的变化调整高阶重建。以 `limitedLinear` 为例：

```foam
div(phi,T) Gauss limitedLinear 1;
```

参数范围为 0 到 1：接近 0 时限制较弱、趋近线性插值；1 对应较强的限制。在平滑区尽量保持较高精度，在陡变附近加强限制。最终是否保持变量范围，还与时间离散、源项、网格和边界处理有关。

| 格式 | 面值构造 | 比较时重点观察 |
| --- | --- | --- |
| `upwind` | 上游单元值 | 峰值降低、锋面展宽 |
| `linear` | 两侧线性插值 | 过冲、欠冲、波形振荡 |
| `linearUpwind grad(T)` | 上游值加梯度修正 | 梯度质量、极值、波形保持 |
| `limitedLinear 1` | 受限制的线性重建 | 陡变处限制强度及扩散 |

## 分别运行并画在同一张图上

从刚解压、尚未运行的练习目录复制三份。假设当前目录包含 `one-dimensional-advection`：

```bash
cp -a one-dimensional-advection advection-upwind
cp -a one-dimensional-advection advection-linear
cp -a one-dimensional-advection advection-limited

foamDictionary advection-linear/system/fvSchemes \
    -entry 'divSchemes/div(phi,T)' -set 'Gauss linear'
foamDictionary advection-limited/system/fvSchemes \
    -entry 'divSchemes/div(phi,T)' -set 'Gauss limitedLinear 1'

(cd advection-upwind && bash Allrun)
(cd advection-linear && bash Allrun)
(cd advection-limited && bash Allrun)
```

`cp -a` 保留完整输入和目录结构。`foamDictionary` 只修改指定条目，单引号保护含括号的键名和带空格的值。每对圆括号启动一个子 shell，进入副本运行后自动返回当前目录。三个计算使用相同网格、时间步和结束时刻，差别只有对流格式。

每份目录都会生成 `comparison.csv`。在它们的上一级目录运行以下 Python 代码；绘图需要安装 Matplotlib：

```python
import csv
import matplotlib.pyplot as plt

names = ['advection-upwind', 'advection-linear', 'advection-limited']
for name in names:
    with open(f'{name}/comparison.csv', newline='') as file:
        rows = list(csv.DictReader(file))
    x = [float(row['x_m']) for row in rows]
    t = [float(row['T_computed']) for row in rows]
    plt.plot(x, t, label=name.removeprefix('advection-'))

reference = [float(row['T_reference']) for row in rows]
plt.plot(x, reference, 'k--', label='Analytical')
plt.xlabel('x [m]')
plt.ylabel('T [K]')
plt.legend()
plt.tight_layout()
plt.savefig('advection-comparison.png', dpi=200)
```

`DictReader` 按列名读取数据；`x_m` 是单元中心坐标，`T_computed` 是数值解。三个副本的网格一致，最后读取的一组坐标也可用于解析参考。黑色虚线表示保持形状的理想平移，三条实线显示各格式的结果。

## 怎样解释差异

配套原始基线采用 `Euler + upwind`。已有计算在 $t=0.2\,\mathrm s$ 得到峰值约 0.776896 K，线积分约 $0.100000\,\mathrm{K\,m}$，平均绝对误差约 0.0287741 K。脉冲总量基本保持，峰值却明显下降，反映出这一组合的数值扩散。

均匀网格上的线积分为 $I=\sum_iT_i\Delta x$；一般网格的平均绝对误差可写成

\[
E_1=\frac{\sum_iV_i|T_i-T_i^{\mathrm{ref}}|}{\sum_iV_i}.
\]

线积分检查输运总量，$E_1$ 检查整体形状，最大值和最小值检查局部过冲。把这几个数与剖面一起看，格式的特点会比只看彩色云图清楚。

进阶比较可以改用方波初值，观察陡变附近的行为；也可以保持余弦脉冲，将单元数依次增加到 400 和 800。改网格、速度或结束时刻后，同步修改 `compare.py` 中的坐标和解析参数。

稳态教程中常见 `bounded Gauss ...`。其中 `bounded` 会加入与离散通量散度相关的修正，帮助处理迭代过程中的连续性偏差。`bounded` 修正散度形式，`limitedLinear` 限制面值重构。场值范围还取决于所选空间格式、时间步和边界条件。
