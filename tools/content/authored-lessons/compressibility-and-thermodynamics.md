可压缩流动中，密度随压力和温度变化，速度、压力与能量方程需要共同求解。喷管、压力波传播和声学共振属于典型应用。`rhoPimpleFoam` 使用瞬态压力—速度耦合方法处理这类问题，热物性模型则提供密度、比热容、黏度等关系。

`rhoPimpleFoam` 在每个时间步中更新速度、压力和热物性，并通过 PIMPLE 校正它们之间的耦合。外校正次数影响时间步内的耦合收敛程度，时间步大小影响压力波的时间分辨率。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-pimple-pressure-coupling.png" alt="PIMPLE 外校正与 PISO 内校正" loading="lazy"><figcaption><strong>PIMPLE 外校正与 PISO 内校正</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module6.pdf，p. 96 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 什么情况下需要考虑密度变化

Mach 数表示速度与声速的比值：

\[
Ma=\frac{U}{a},\qquad
a=\sqrt{\gamma RT}.
\]

$a$ 为声速，$\gamma=c_p/c_v$，$R$ 为气体常数。第二个公式适用于理想气体和相应的热容假设。常温空气中声速约为 340 m/s，速度 34 m/s 对应 $Ma\approx0.1$。

在温度变化较小的许多外流问题中，低 Mach 数可支持恒密度近似；有明显加热、浮力或组分变化时，低流速下密度仍可能改变。声学问题关注压力扰动传播，即使平均速度很小，也需要保留气体的可压缩性。

## 实例：空气的热物性文件

本课使用 `tutorials/compressible/rhoPimpleFoam/laminar/helmholtzResonance`。它比较一个显式建模的储气腔和一个用边界模型表示的储气腔。两者都通过狭窄通道与外部连接，气体的压缩与惯性形成振荡。

`constant/thermophysicalProperties` 的主体为：

```foam
thermoType
{
    type            hePsiThermo;
    mixture         pureMixture;
    transport       const;
    thermo          eConst;
    equationOfState perfectGas;
    specie          specie;
    energy          sensibleInternalEnergy;
}
mixture
{
    specie
    {
        molWeight 28.9;
    }
    thermodynamics
    {
        Cv 712;
        Hf 0;
    }
    transport
    {
        mu 1.8e-05;
        Pr 0.7;
    }
}
```

这份文件通过组合模型建立热物性：

| 条目 | 作用 | 本例的含义 |
| --- | --- | --- |
| `hePsiThermo` | 提供能量与压缩性相关接口 | 与压力求解及密度更新配合 |
| `pureMixture` | 组分描述 | 单一等效气体 |
| `const` | 输运物性模型 | 恒定黏度与 Prandtl 数 |
| `eConst` | 热力学模型 | 恒定定容比热容 |
| `perfectGas` | 状态方程 | $\rho=p/(RT)$ |
| `sensibleInternalEnergy` | 求解的能量形式 | 显内能 |

`molWeight` 的单位为 kg/kmol，`Cv` 的单位为 J/(kg·K)，`mu` 是动力黏度，单位 Pa·s，`Pr` 无量纲。由分子量可得 $R=R_u/W\approx287.7\ \mathrm{J/(kg\cdot K)}$；再由 $c_p=c_v+R$ 得到 $c_p\approx1000\ \mathrm{J/(kg\cdot K)}$，$\gamma\approx1.404$。

当 $p=10^5\ \mathrm{Pa}$、$T=300\ \mathrm K$ 时，理想气体密度约为 $1.16\ \mathrm{kg/m^3}$。这个估算可用于检查初始化时的物性量级。

## 压力和温度使用什么单位

`0.orig/p` 中的量纲与初值为：

```foam
dimensions    [1 -1 -2 0 0 0 0];
internalField uniform 1e5;
```

这里压力单位为 Pa，状态方程使用绝对压力。`0.orig/T` 的初始温度为 300，单位为 K。温度显示时需要转换为摄氏度，可在后处理中计算 $T_{\mathrm{C}}=T-273.15$。

出口压力采用：

```foam
outlet
{
    type      fixedMean;
    meanValue constant 1e5;
    value     uniform 1e5;
}
```

`fixedMean` 约束 patch 的平均值，保留该边界内部的空间变化。它与逐个边界面固定同一个压力的 `fixedValue` 有不同的作用。声学计算对边界反射敏感，后续可以在相同几何中比较适合该方程组的波传播出口处理。

## 边界模型怎样代替储气腔

`modelled` 方案使用 `plenumPressure`。原文件中的主要参数为：

```foam
plenum
{
    type                   plenumPressure;
    gamma                  1.4;
    R                      287.04;
    supplyMassFlowRate     0.0001;
    supplyTotalTemperature 300;
    plenumVolume           0.000125;
    plenumDensity          1.1613;
    plenumTemperature      300;
    inletAreaRatio         1.0;
    inletDischargeCoefficient 0.8;
    timeScale              1e-4;
    value                  uniform 1e5;
}
```

`plenumVolume` 给出储气腔体积，单位 m³；`supplyMassFlowRate` 是供气质量流量，单位 kg/s。`plenumDensity` 和 `plenumTemperature` 用于初始化腔内状态，`inletDischargeCoefficient` 表示入口流量系数，考虑实际入口流动与理想关系的偏离。`gamma`、`R` 属于此边界模型的气体参数，修改工作气体时应与主体热物性保持一致。

显式建模方案直接计算腔内网格上的流动；边界方案用集中参数表示腔内状态，可以减少单元数。比较二者时，压力振荡频率与幅值是主要观测量。

## 运行两个方案并读取压力历史

此案例的 `Allrun` 会选择对应网格片段，创建 `resolved` 和 `modelled` 两个子案例，随后生成网格、分区并进行并行计算。在新副本中执行：

```bash
./Allrun -test > log.Allrun 2>&1
```

`-test` 保留案例求解流程，并跳过脚本末尾的交互绘图。需要已安装的 MPI。两个方案的压力探针文件分别位于 `resolved/postProcessing/probes/0/p` 和 `modelled/postProcessing/probes/0/p`。探针坐标和编号写在文件头中，可以在颈部选取同一个物理位置比较。

画压力扰动时取 $p'=p-10^5\ \mathrm{Pa}$，横轴为时间，纵轴为 Pa。比较完整时间曲线后，再计算主频。理想 Helmholtz 共振频率可估为：

\[
f_H=\frac{a}{2\pi}\sqrt{\frac{A}{V L_{\mathrm{eff}}}},
\]

$A$ 是颈部面积，$V$ 是储气腔体积，$L_{\mathrm{eff}}$ 是包含端部修正的有效颈长。这个简化式解释了腔体越大、频率通常越低的趋势；实际流动损失与几何会影响频率和衰减。

## 时间步怎样影响声学结果

流体对流时间尺度约为 $\Delta x/U$，声波跨单元的时间尺度约为 $\Delta x/a$。低流速时两者可能相差很多。压力基隐式算法能够在较大的声学 Courant 数下运行，但声波相位和幅值仍需要足够的时间分辨率。

若目标频率为 1000 Hz，一个周期是 0.001 s。每周期取 50 个采样点时，采样间隔需为 $2\times10^{-5}$ s；再减半时间步比较频率与幅值，可检查当前时间分辨率。频谱的间隔约为 $1/T_{\mathrm{sample}}$，需要区分临近峰时，应延长采样时长。

## 常见问题与练习

| 问题 | 检查位置 |
| --- | --- |
| 密度或温度出现非物理值 | 绝对压力、温度初值、热物性单位，以及发散最早出现的区域 |
| `Unknown thermodynamics package` | `thermoType` 组合及该求解器支持的能量形式 |
| 找不到网格包含文件 | 使用案例 `Allrun` 生成两个方案的符号链接与目录 |
| 压力历史过于稀疏 | 探针写出频率与实际时间步 |

将 `modelled` 方案的储气腔体积增加为原来的两倍，其余参数保持一致。集中参数近似下，频率约降为原来的 $1/\sqrt2$。从压力时间序列估计主频，再解释与该近似的差异。进一步可减小时间步或细化颈部网格，比较频率、振幅和衰减速度对数值分辨率的敏感性。
