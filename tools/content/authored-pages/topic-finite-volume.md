## 一个单元中的收支

有限体积法把计算区域分成许多单元，在每个单元上写守恒关系：**单元内的变化量，来自穿过各个面的输运和单元内部的源项。** 质量、动量和能量方程都可以按这个思路处理。

以标量 $\phi$ 为例，固定控制体 $V_P$ 上的通用输运方程为

\[
\frac{\mathrm d}{\mathrm dt}\int_{V_P}\rho\phi\,\mathrm dV
+\int_{\partial V_P}\rho\phi\mathbf U\cdot\mathbf n\,\mathrm dS
=\int_{\partial V_P}\Gamma\nabla\phi\cdot\mathbf n\,\mathrm dS
+\int_{V_P}S_\phi\,\mathrm dV.
\]

左侧依次是积累和对流，右侧是扩散和源项。把面积分写成各个面上的求和后，问题就变为：怎样求出面上的速度、标量值和梯度？

<figure class="wolf-figure"><img src="/assets/wolf/wolf-fvm-convective-face-flux.png" alt="从体积分到离散面通量" loading="lazy"><figcaption><strong>从体积分到离散面通量</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 11</small></figcaption></figure>

相邻单元共用的面只需计算一份通量，在两个单元中分别取正、负号。这样相加时内部面的贡献抵消，整个区域的变化由外边界通量和源项决定。

## 从面值到离散格式

OpenFOAM 通常在单元中心保存场值，计算对流和扩散时还需要面值。

- **迎风格式**使用流动上游单元的值，处理陡峭变化时较稳定，但会使分布变平滑。
- **线性插值**按几何权重组合两侧单元值，在光滑场上有较高精度。
- **受限格式**根据局部变化调整高阶重构，在精度与过冲控制之间作取舍。
- **非正交修正**处理面法向与相邻单元中心连线不一致时的扩散通量。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-advection-profile-errors.png" alt="一维输运中的格式误差曲线" loading="lazy"><figcaption><strong>一维输运中的格式误差曲线</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 157</small></figcaption></figure>

图中的差异可通过[对流离散课程](/read/?slug=advection-schemes-boundedness)配套算例比较。先使用相同网格和时间步，只改变格式，再查看剖面、极值和总积分。

## 一个可手算的例子

考虑质量为 $M=1\,\mathrm{kg}$ 的混合单元。流入、流出质量流率均为 $F=2\,\mathrm{kg/s}$，入口浓度为 $\phi_\mathrm{in}=1$，单元初始浓度为 0。忽略扩散和源项，采用隐式 Euler：

\[
\frac{M}{\Delta t}(\phi^{n+1}-\phi^n)
+F\phi^{n+1}=F\phi_\mathrm{in}.
\]

当 $\Delta t=0.1\,\mathrm{s}$ 时，

\[
(10+2)\phi^{n+1}=2,\qquad \phi^{n+1}=\frac16.
\]

这里的 $10=M/\Delta t$ 来自积累项，$2=F$ 来自流出，右侧的 2 来自入口。多个单元相互连接后，右侧和左侧还会出现邻居单元的未知值，最终形成稀疏线性方程组。

[守恒方程与单元积分](/read/?slug=algorithm-theory-01)进一步推导边界与源项；[稀疏矩阵与迭代](/read/?slug=algorithm-theory-03)给出三个单元的完整矩阵和求解代码。

## 对应到 OpenFOAM 代码

下面是被动标量对流扩散方程的常见写法。`T`、`phi` 和 `DT` 需要由程序预先创建：

```cpp
fvScalarMatrix TEqn
(
    fvm::ddt(T)
  + fvm::div(phi, T)
  - fvm::laplacian(DT, T)
);
TEqn.solve();
```

`fvm::ddt` 装配时间项，`fvm::div` 装配对流项，`fvm::laplacian` 装配扩散项。扩散项移到左侧，因此使用负号。这里 `phi` 是面体积通量，`DT` 是扩散系数。

代码确定要求解的方程；`fvSchemes` 选择各项的离散格式，`fvSolution` 选择线性求解方法与容差。边界条件也会进入矩阵系数和源项。完整程序见[对流扩散求解器编程](/read/?slug=programming-10)。

## 学习顺序

| 内容 | 课程 |
| --- | --- |
| 单元积分、面通量、边界与源项 | [有限体积基础](/read/?slug=finite-volume-conservation)、[守恒方程推导](/read/?slug=algorithm-theory-01) |
| 对流、扩散和时间离散 | [对流格式](/read/?slug=advection-schemes-boundedness)、[扩散与非正交修正](/read/?slug=diffusion-gradients-laplacian)、[时间离散](/read/?slug=time-discretisation-courant) |
| 截断误差、稳定性与收敛性 | [误差与稳定性理论](/read/?slug=algorithm-theory-02)、[网格与时间步比较](/read/?slug=grid-time-verification) |
| 矩阵求解与压力耦合 | [线性迭代](/read/?slug=algorithm-theory-03)、[压力方程与面通量](/read/?slug=algorithm-theory-04) |
| 程序实现 | [对流扩散方程](/read/?slug=programming-10)、[SIMPLE](/read/?slug=programming-14)、[自定义插值](/read/?slug=programming-15) |

配图来源为 Wolf Dynamics 培训讲义；图下保留作者、页码与许可。
