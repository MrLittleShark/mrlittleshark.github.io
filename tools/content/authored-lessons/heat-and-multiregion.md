共轭传热计算同时求解流体中的对流换热和固体中的热传导。例如，水流经过加热器时，热量先在固体内传递，再通过流固界面进入水中；水流速度和材料导热系数都会影响温度分布。OpenFOAM 用不同的 region 保存这些区域的网格、场和物性。

## 流体和固体分别求解什么

对于常物性的静止固体，温度方程可写为：

\[
\rho c_p\frac{\partial T}{\partial t}
=\nabla\cdot(\lambda\nabla T)+\dot q_v.
\]

$\rho$ 是密度，$c_p$ 是比热容，$\lambda$ 是导热系数，$\dot q_v$ 是单位体积的发热功率。流体还通过运动携带能量，因此需要求解速度、压力和能量之间的耦合。实际求解器可采用焓或内能作为能量变量，并由热物性关系计算温度。

理想接触的界面满足温度连续和热流连续。若两侧法向都指向各自区域外部，则有：

\[
T_f=T_s,\qquad
\lambda_f\nabla T_f\cdot\mathbf n_f
+\lambda_s\nabla T_s\cdot\mathbf n_s=0.
\]

热接触电阻会使两侧温度出现差值，但穿过界面的热流仍需要一致。

![流体与固体区域之间的传热](/assets/diagrams/core-heat.svg)

## 实例：multiRegionHeater 的文件结构

进入 `tutorials/heatTransfer/chtMultiRegionFoam/multiRegionHeater`。`constant/regionProperties` 指定了两类区域：

```foam
regions
(
    fluid (bottomWater topAir)
    solid (heater leftSolid rightSolid)
);
```

`bottomWater` 和 `topAir` 是流体区域；`heater`、`leftSolid`、`rightSolid` 是固体区域。区域名用于目录定位，大小写保持一致。预处理后，相关目录大致如下：

```text
0/
  bottomWater/     U、p、p_rgh、T、湍流场
  topAir/         U、p、p_rgh、T、湍流场
  heater/         T 等固体字段
constant/
  regionProperties
  bottomWater/    polyMesh、thermophysicalProperties
  heater/         polyMesh、thermophysicalProperties
system/
  controlDict
  bottomWater/    fvSchemes、fvSolution、changeDictionaryDict
  heater/         fvSchemes、fvSolution、changeDictionaryDict
```

每个 region 有自己的网格；全局 `controlDict` 控制整个计算的时间推进。区域中的 `fvSchemes` 和 `fvSolution` 分别控制该区域的离散与求解。

## 固体物性怎样填写

`constant/heater/thermophysicalProperties` 的主体为：

```foam
thermoType
{
    type            heSolidThermo;
    mixture         pureMixture;
    transport       constIso;
    thermo          hConst;
    equationOfState rhoConst;
    specie          specie;
    energy          sensibleEnthalpy;
}
mixture
{
    specie
    {
        molWeight 50;
    }
    transport
    {
        kappa 80;
    }
    thermodynamics
    {
        Hf 0;
        Cp 450;
    }
    equationOfState
    {
        rho 8000;
    }
}
```

`heSolidThermo` 选择固体热物性接口。`constIso` 表示恒定、各向同性导热系数，`hConst` 使用恒定比热容，`rhoConst` 使用恒定密度。`sensibleEnthalpy` 以显焓作为能量变量。

这里 `kappa=80` 的单位为 W/(m·K)，`Cp=450` 的单位为 J/(kg·K)，`rho=8000` 的单位为 kg/m³。它们决定热扩散率 $a=\lambda/(\rho c_p)$，本例约为 $2.22\times10^{-5}\ \mathrm{m^2/s}$。相同导热系数下，比热容或密度增大，升温通常更慢；在最终稳态、无温度相关物性的纯导热问题中，温度分布主要由导热系数和边界决定。

流体使用另一组接口。例如 `bottomWater` 采用 `heRhoThermo`、`rhoConst`，并给出动力黏度 `mu` 和 Prandtl 数 `Pr`。常物性条件下 $\lambda=\mu c_p/Pr$，这些输入共同决定流体导热能力。

## 流固界面怎样传递温度

此案例在预处理时用 `changeDictionary` 设置边界。`system/bottomWater/changeDictionaryDict` 中的温度界面条目为：

```foam
"bottomWater_to_.*"
{
    type        compressible::turbulentTemperatureRadCoupledMixed;
    Tnbr        T;
    kappaMethod fluidThermo;
    value       uniform 300;
}
```

`bottomWater_to_.*` 是匹配多个界面名称的正则表达式。`Tnbr T` 指定邻区的温度字段名；`fluidThermo` 从流体热物性与相关模型获取导热信息。固体侧使用同类耦合条件，并设置 `kappaMethod solidThermo`。`value` 为初始界面温度，后续由耦合更新。

接口两侧的配对由区域网格中的映射关系确定。预处理正确后，流体能找到对应的固体 patch，固体也能找到流体 patch。原案例还采用带辐射耦合能力的边界类型；辐射贡献由相应的辐射模型配置决定。

`heater` 底部 `minY` 固定为 500 K，流体入口为 300 K。热量因此从加热端进入固体，再传给流体并由流动带走。初始温度为 300 K，运行前期会出现固体储热过程。

## 运行顺序

在新副本中先运行预处理，再串行计算：

```bash
./Allrun.pre > log.prepare 2>&1
chtMultiRegionFoam > log.chtMultiRegionFoam 2>&1
paraFoam
```

`Allrun.pre` 依次执行 `blockMesh`、`topoSet`、恢复初始场、`splitMeshRegions -cellZones -overwrite`，然后为各区域运行 `changeDictionary`。`topoSet` 建立区域单元分组，`splitMeshRegions` 据此拆分网格，`changeDictionary` 完成各区域的字段与边界设置。

案例的 `Allrun` 提供并行流程，包含 `decomposePar -allRegions` 和 `reconstructPar -allRegions`。第一次阅读多区域结构时，串行运行更便于查看区域目录；较大计算再采用并行流程。

## 怎样看热量去了哪里

在 ParaView 中分别选择流体和固体区域，用相同温度色标比较。查看加热端、流固界面和出口温度，并沿固体厚度取一条温度曲线。理想接触界面的温度应衔接；有接触热阻的界面可以出现温差。

稳定流动、常比热的流体带走的热量可近似写为：

\[
\dot Q_f=\dot m c_p(T_{b,\mathrm{out}}-T_{b,\mathrm{in}}),
\]

其中 $T_b$ 是按质量通量加权的混合温度。出口温度不均匀时，直接使用面积平均温度会带来偏差。更一般的计算可对焓通量积分。

瞬态时，输入热量分为流体带走的热量、向外界散失的热量和区域内储存的能量。固体仍在升温时，入口与出口的热量差包含储热项。界面热流可以借助 `wallHeatFlux` 及表面积分进行查看，并按各区域的外法向统一符号。

## 常见问题

| 现象 | 检查与处理 |
| --- | --- |
| 找不到某个 region 的网格 | 查看 `Allrun.pre` 中拆分步骤是否完成，核对 `regionProperties` 与 cellZone 名称 |
| 耦合边界找不到邻区温度 | 查看接口配对、`Tnbr` 和邻区 `T` 文件 |
| `Unknown thermodynamics package` | 检查 `thermoType` 的组合，按错误列出的可用组合修正 |
| 温度在界面出现大幅跳变 | 查看是否设置了热阻，再检查界面配对和耦合迭代 |
| 求解器从旧温度继续运行 | 查看 `controlDict/startFrom` 和已有时间目录 |

## 练习：导热系数与接触热阻

先将 heater 的 `kappa` 从 80 改为 40，其他输入保持一致。比较相同物理时刻的加热器内部温差、出口温度和传热功率。较小的导热系数增加内部热阻，在固定热端温度条件下通常会减少传入冷侧的热量。

原案例 `heater_to_leftSolid` 还包含 `thicknessLayers` 和 `kappaLayers`，用于表示薄层热阻，单位面积热阻为 $R''=\delta/\lambda$。进一步修改薄层厚度，观察界面温差与传热量的变化。两侧接口采用一致的薄层定义，物理关系为 $\Delta T=q''R''$，可据此检查变化趋势。
