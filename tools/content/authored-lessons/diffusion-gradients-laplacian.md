导热使高温区域的能量向低温区域传递；分子扩散使浓度逐渐均匀；黏性使相邻流层交换动量。这些过程都与空间梯度有关。在 OpenFOAM 中，相应项通常通过 `laplacianSchemes` 离散，梯度和面插值共同决定扩散通量。

## 一根两端温度固定的杆

考虑长 $L=0.1\,\mathrm m$ 的均匀杆，左端 400 K，右端 300 K，侧面绝热，内部没有热源。稳态导热方程和边界条件为

\[
\frac{d^2T}{dx^2}=0,
\qquad T(0)=400\,\mathrm K,
\qquad T(L)=300\,\mathrm K.
\]

积分两次，得到直线分布

\[
T(x)=400-100\frac{x}{L}.
\]

杆中心 $x=0.05\,\mathrm m$ 的温度为 350 K。若导热系数为 $k=10\,\mathrm{W/(m\,K)}$，Fourier 定律给出

\[
q_x''=-k\frac{dT}{dx}
=10000\,\mathrm{W/m^2}.
\]

温度沿正 $x$ 方向降低，热流沿正 $x$ 方向流动，因此热流密度为正。热流密度乘以截面积，才是单位时间通过截面的热量，单位为 W。

## 离散时需要面法向梯度

单元温度存储在中心，热量通过网格面传递。对于正交网格，相邻中心连线与面法向平行，因此可用两中心温差计算法向梯度：

\[
\left(\frac{\partial T}{\partial n}\right)_f
\approx\frac{T_N-T_P}{d_{PN}}.
\]

$d_{PN}$ 是两个单元中心的距离。面上导热流率约为 $-k_fA_f(T_N-T_P)/d_{PN}$。其中温差、距离、导热系数和面积各自有明确作用：温差越大，导热越强；传热距离越长，导热越弱。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-diffusion-orthogonal-comparison.png" alt="正交与非正交网格中的扩散通量" loading="lazy"><figcaption><strong>正交与非正交网格中的扩散通量</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 29 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

边界面也使用同样的距离概念。均匀网格的第一个单元中心到边界只有 $\Delta x/2$，所以给定边界温度的通量系数是 $2kA/\Delta x$。这也是第一个单元中心温度通常不等于边界温度的原因。

## 配置并运行一维导热

本课下载包中的 `exercises/one-dimensional-diffusion` 已给出完整输入。它使用 `laplacianFoam`，沿长度方向有 40 个单元。打开 `constant/transportProperties`：

```foam
DT [0 2 -1 0 0 0 0] 1e-5;
```

`DT` 是热扩散率，单位为 $\mathrm{m^2/s}$。均匀材料满足 $DT=k/(\rho c_p)$。因此，`1e-5` 决定温度变化的快慢；计算热流密度时则使用导热系数 $k$。二者通过密度和比热联系起来。

`system/fvSchemes` 的主要内容如下：

```foam
ddtSchemes
{
    default steadyState;
}
gradSchemes
{
    default Gauss linear;
}
divSchemes
{
    default none;
}
laplacianSchemes
{
    default Gauss linear orthogonal;
}
interpolationSchemes
{
    default linear;
}
snGradSchemes
{
    default orthogonal;
}
```

`steadyState` 将时间导数取为零，直接求稳态分布。`Gauss linear orthogonal` 可以分成三部分：`Gauss` 对各面扩散通量求和，`linear` 指定扩散系数等量的面插值，`orthogonal` 用单元中心连线计算面法向梯度。这里的均匀长方体网格适合正交处理。

`gradSchemes` 控制完整空间梯度，`snGradSchemes` 控制面法向梯度。上面的 Laplacian 条目已经明确指定 `orthogonal`；修改它时应同步考虑独立法向梯度算子的设置。

在练习目录中执行：

```bash
bash Allrun
```

脚本先运行 `blockMesh` 和 `checkMesh`，再求解温度，最后生成 `comparison.csv`。这个稳态例子的输出目录为 `1`，其名称表示迭代位置；温度由稳态方程直接求得。

40 个单元的中心坐标为 $x_i=(i+1/2)L/40$，其中 $i=0,\ldots,39$。第一个中心位于 0.00125 m，解析温度为 398.75 K；最后一个中心的温度为 301.25 K。边界上的 400 K 和 300 K 存在于边界场中。

## 用数值结果计算热流

已有基线结果在输出的 12 位有效数字内与解析直线重合。它同时说明一个特点：均匀正交网格对这种线性稳态解可以非常准确，进一步细化网格时温度曲线变化很小。

可以用结果表计算相邻单元之间的热流密度：

```python
import csv

with open('comparison.csv', newline='') as file:
    rows = list(csv.DictReader(file))

k = 10.0                         # W/(m K)
x = [float(r['x_m']) for r in rows]
t = [float(r['T_computed']) for r in rows]
q = [-k * (t[i+1] - t[i]) / (x[i+1] - x[i])
     for i in range(len(x) - 1)]
print('内部面热流密度范围 [W/m2]:', min(q), max(q))
```

循环逐对读取相邻中心温度，用实际距离计算梯度，再乘以 $-k$。线性稳态分布对应各内部面相同的热流密度，结果应接近 $10000\,\mathrm{W/m^2}$。若两端热流明显不同，则需要检查求解是否收敛、是否存在热源以及边界通量的符号。

## 非正交网格怎样处理

在一般网格中，中心连线可能偏离面法向。沿中心连线求得的导数只包含所需法向梯度的一部分，需要使用重建梯度补充其余分量。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-diffusion-nonorthogonal-correction.png" alt="扩散通量的非正交分解" loading="lazy"><figcaption><strong>扩散通量的非正交分解</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 30 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

图中的面积向量分解将扩散通量分为主要部分与修正部分。主要部分进入隐式矩阵，非正交修正常以显式项加入。一般非正交网格可使用：

```foam
laplacianSchemes
{
    default Gauss linear corrected;
}
snGradSchemes
{
    default corrected;
}
```

`corrected` 加入非正交修正。修正需要梯度，因此 `gradSchemes` 也参与影响结果。网格倾斜严重时，显式修正可能相对较大，可先改善局部网格，再研究限制修正和校正循环。

`laplacianFoam` 的校正循环读取 `fvSolution/SIMPLE`：

```foam
SIMPLE
{
    nNonOrthogonalCorrectors 1;
}
```

这里的 `1` 表示在基础求解之外，再做一次非正交校正。重新求解时，修正项使用更新后的温度梯度。对正交基线取 `0` 即可；在倾斜网格中，可比较 0、1、2 对温度和热流的影响。

非正交角描述方向偏差，面心偏斜则描述面中心偏离中心连线交点的程度。两者会影响不同的插值环节，`checkMesh` 中应分别查看。

## 扩展：两种材料串联

若左半段导热系数为 $k_1=10\,\mathrm{W/(m\,K)}$，右半段为 $k_2=1\,\mathrm{W/(m\,K)}$，长度均为 0.05 m，两端温度仍为 400 K 和 300 K，则稳态热流密度为

\[
q''=\frac{400-300}{0.05/10+0.05/1}
\approx1818.18\,\mathrm{W/m^2}.
\]

左段温降约 9.09 K，界面温度约 390.91 K；右段承担其余温降。导热较差的材料对应更大的温度梯度。

当网格面落在材料界面上，面两侧中心到界面的距离分别为 $d_P$、$d_N$，等效面导热系数由串联热阻给出：

\[
k_f=\frac{d_P+d_N}{d_P/k_P+d_N/k_N}.
\]

两侧距离相等时退化为调和平均。它使两段热阻相加，并保持界面两侧热流一致。配套单材料例子中的 `DT` 是均匀常量；实现这一扩展可使用支持多材料的固体传热设置，或在自定义求解器中将系数改为场，并明确面系数处理。

练习时还可以将左端改为 500 K。解析中心温度变为 400 K，热流密度加倍。随后改为瞬态 `Euler`，观察温度逐渐接近稳态直线，便能区分稳态分布与导热过程的时间尺度。
