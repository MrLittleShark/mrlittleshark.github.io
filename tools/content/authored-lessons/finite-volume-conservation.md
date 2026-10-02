有限体积法把计算区域划分成许多小单元，在每个单元中计算质量、动量或能量的收支。管道流动、固体导热和污染物输运虽然物理过程不同，都可以用这种方法离散。OpenFOAM 将离散后的系数组装成矩阵，再求出各单元的场值。

## 从一个单元的收支开始

设一个容器中存有 10 kg 水，每秒流入 3 kg、流出 2 kg。经过 1 s，水量增加 1 kg。把容器换成网格单元，守恒关系仍然是

\[
\text{储存量的变化率}=\text{流入率}-\text{流出率}+\text{内部产生率}.
\]

区别在于，网格单元通常通过多个面与周围单元交换物质，每个面的流量都需要计算。对一个一般的输运量 $c$，常用方程为

\[
\frac{\partial(\rho c)}{\partial t}
+\nabla\cdot(\rho\mathbf{u}c)
=\nabla\cdot(\Gamma\nabla c)+S.
\]

这里 $\rho$ 是密度，$\mathbf u$ 是速度，$\Gamma$ 是扩散系数，$S$ 是单位体积的源项。四项依次表示储存、对流、扩散和源项。取 $c$ 为无量纲质量分数时，各项单位均为 $\mathrm{kg/(m^3\,s)}$，对应的 $\Gamma=\rho D$，$D$ 的单位为 $\mathrm{m^2/s}$。

“对流”来自流体整体运动，“扩散”来自空间差异。例如，河水把染料带往下游属于对流，染料从高浓度区域向周围散开属于扩散。两种作用可以同时存在。

## 把体积内的变化写成面上的通量

把方程在单元 $V_P$ 上积分。散度定理将体积分转换为表面积分，再将表面积分近似成各网格面的求和：

\[
\frac{d(\rho_P c_P V_P)}{dt}
+\sum_f \dot m_f c_f
=\sum_f\Gamma_f(\nabla c)_f\cdot\mathbf S_f+S_PV_P.
\]

$P$ 表示当前单元，$f$ 表示它的面；$\mathbf S_f$ 是指向单元外部的面积向量，模长等于面面积。$\dot m_f=\rho_f\mathbf u_f\cdot\mathbf S_f$ 是质量流率，单位为 kg/s。按这个方向约定，正值表示流出，负值表示流入。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-fvm-convective-face-flux.png" alt="从体积分到离散面通量" loading="lazy"><figcaption><strong>从体积分到离散面通量</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 11 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

假设某面的面积为 $0.01\,\mathrm{m^2}$，流体沿外法向以 $2\,\mathrm{m/s}$ 运动，则体积流率为 $0.02\,\mathrm{m^3/s}$。若密度为 $1000\,\mathrm{kg/m^3}$，质量流率就是 $20\,\mathrm{kg/s}$。若该面质量分数为 0.1，这个面每秒带出 2 kg 对应物质。

OpenFOAM 中的 `phi` 通常保存面通量。不可压缩求解器常用体积通量，量纲为 `[0 3 -1 0 0 0 0]`；可压缩求解器常用质量通量，量纲为 `[1 0 -1 0 0 0 0]`。阅读 `div(phi,T)` 时，应将 `phi` 理解为输运通量，将 `T` 理解为被输运场。

## 为什么相邻单元能够保持守恒

考虑从左到右排列的三个单元。同一个内部面，对左侧单元是出口，对右侧单元是入口。程序只需要计算一份面通量，然后以相反符号放入两个单元的方程。

将三个单元的收支相加，内部面贡献两两抵消，剩下左右外边界的通量。这个抵消关系使局部收支与全域收支一致。即使单元形状不同，只要公共面的数值通量保持一致，这一守恒结构仍然成立。

场值通常存储在单元中心，而通量需要面上的场值。例如面 $f$ 位于 $P$、$N$ 两个单元之间，线性插值写作

\[
c_f=w_fc_P+(1-w_f)c_N.
\]

均匀正交网格中，面位于两个中心的中点，$w_f=1/2$。迎风格式则按通量方向选取上游单元值。**不同对流格式的主要区别，就在于如何计算这里的 $c_f$。**

## 从离散通量到矩阵系数

用一维稳态导热说明矩阵的来源。均匀网格的间距为 $\Delta x$，截面积为 $A$，导热系数为 $k$，内部没有热源。中间单元两侧的导热收支为

\[
\frac{kA}{\Delta x}(T_E-T_P)
-\frac{kA}{\Delta x}(T_P-T_W)=0.
\]

整理后得到 $2T_P-T_W-T_E=0$。因此，这个单元的温度满足 $T_P=(T_W+T_E)/2$。这里的系数 2、−1、−1 分别进入矩阵的主对角线和相邻位置。边界单元还会将给定边界温度转移到方程右侧。

一般形式为

\[
a_PT_P+\sum_N a_NT_N=b_P.
\]

每个单元提供一行方程；所有单元连接起来，就得到 $A\mathbf T=\mathbf b$。矩阵通常很稀疏，因为一个单元主要与直接相邻的单元耦合。

## 对照 OpenFOAM 的方程代码

`scalarTransportFoam` 求解给定速度下的标量输运。下列代码摘自 v2512 的主程序，字段、网格和物性在前面的初始化代码中创建：

```cpp
fvScalarMatrix TEqn
(
    fvm::ddt(T)
  + fvm::div(phi, T)
  - fvm::laplacian(DT, T)
 ==
    fvOptions(T)
);

TEqn.relax();
fvOptions.constrain(TEqn);
TEqn.solve();
fvOptions.correct(T);
```

| 代码 | 含义 | 对应设置 |
| --- | --- | --- |
| `fvm::ddt(T)` | 组装时间变化项 | `fvSchemes/ddtSchemes` |
| `fvm::div(phi,T)` | 组装对流项 | `fvSchemes/divSchemes` 的 `div(phi,T)` |
| `fvm::laplacian(DT,T)` | 组装扩散项 | `fvSchemes/laplacianSchemes` |
| `fvOptions(T)` | 加入已配置的源项 | 源项字典 |
| `TEqn.relax()` | 对方程实施松弛 | `fvSolution/relaxationFactors` |
| `TEqn.solve()` | 求解温度线性系统 | `fvSolution/solvers/T` |

扩散项前面是负号，因为代码将扩散项从等式右侧移到了左侧。`fvm` 算子返回用于求解的矩阵；`fvc` 算子则利用当前场直接计算一个新场，例如 `fvc::grad(T)` 返回温度梯度。

`fvOptions.constrain` 在求解前给方程施加约束，`fvOptions.correct` 在求解后执行已配置的场修正。二者的作用取决于具体源项或约束模型。

## 修改一个实际算例

解压本课案例包，进入 `exercises/one-dimensional-advection`。这个算例有 200 个单元，速度恒为 $1\,\mathrm{m/s}$，输运一个温差脉冲。`constant/transportProperties` 中设为

```foam
DT [0 2 -1 0 0 0 0] 0;
```

七个指数表示量纲，`[0 2 -1 ...]` 对应 $\mathrm{m^2/s}$。最后的 `0` 将物理扩散关闭。这样方程只保留时间变化与对流，便于观察面值插值的影响。将数值改为 `0.001`，就会加入实际扩散；脉冲变宽同时包含物理扩散与离散误差的作用。

在这个目录执行：

```bash
bash Allrun
```

`Allrun` 依次生成网格、检查网格、运行 `scalarTransportFoam`，最后调用 `compare.py`。运行结束后，`0.2/T` 是最终场，`comparison.csv` 给出单元中心坐标、数值解和解析参考。对原始无扩散输入，解析解是初始脉冲沿流向平移 0.2 m。

可以先计算所有单元的 $\sum_iT_iV_i$，再观察峰值。若总量近似保持而峰值下降，说明守恒与形状精度反映的是两件不同的事：单元之间交换的总量可以正确，面上场值的近似仍会使脉冲变宽。

## 练习：手算两份相邻单元的方程

取两个等体积单元，体积均为 $0.01\,\mathrm{m^3}$，速度从左向右，三个面的体积流率均为 $0.002\,\mathrm{m^3/s}$。入口标量为 1，初始单元值为 0。采用迎风空间格式和隐式 Euler 时间格式，时间步为 1 s。

第一个单元满足 $0.01(T_1^{n+1}-0)+0.002(T_1^{n+1}-1)=0$，得到 $T_1^{n+1}=1/6$。第二个单元满足 $0.01T_2^{n+1}+0.002(T_2^{n+1}-T_1^{n+1})=0$，得到 $T_2^{n+1}=1/36$。

把两式相加，公共面的 $0.002T_1^{n+1}$ 正好抵消。将时间步减半再计算一次，可以看到时间步进入了主对角系数，进而影响每一步的更新量。

源码位置：`$FOAM_SOLVERS/basic/scalarTransportFoam/scalarTransportFoam.C`。下一课具体比较迎风、中心与限制格式如何构造面值。
