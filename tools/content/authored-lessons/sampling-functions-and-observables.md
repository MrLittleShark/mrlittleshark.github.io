OpenFOAM 的 function objects 可以在求解时计算并输出探针、截面、积分量和统计量。常用设置放在 `system/controlDict` 的 `functions` 中。这样，压力历史、出口流量和阻力等数据会随计算一起生成，后处理时可以直接读取文本或场文件。

## 先选择需要的数据形式

| 需要的数据 | 常用对象 | 输出示例 |
| --- | --- | --- |
| 某点的压力随时间变化 | `probes` | 压力时间序列 |
| 中心线上的速度 | `sets` | 坐标与速度分量 |
| 一个截面上的场 | `surfaces` | VTK 截面 |
| 出口总流量 | `surfaceFieldValue` | 通量求和 |
| 域内某场的平均或积分 | `volFieldValue` | 平均温度、水相体积 |
| 平均速度与脉动统计 | `fieldAverage` | `UMean`、`UPrime2Mean` |

![点、线和截面采样位置](/assets/diagrams/core-sampling.svg)

## 实例一：方腔中的两个探针

在基础方腔的 `controlDict` 中加入以下内容；若已有 `functions`，把 `cavityProbes` 加入现有的大括号中：

```foam
functions
{
    cavityProbes
    {
        type            probes;
        libs            (sampling);
        fields          (p U);
        writeControl    timeStep;
        writeInterval   1;
        probeLocations
        (
            (0.05 0.05 0.005)
            (0.025 0.05 0.005)
        );
    }
}
```

`cavityProbes` 是这个对象的名称，也用于输出目录；`type probes` 选择点采样，`libs (sampling)` 加载对应库。`fields` 列出压力和速度，`probeLocations` 中的坐标以米为单位。基础方腔边长 0.1 m、厚度 0.01 m，这两个点位于厚度中面。

`writeControl timeStep` 与 `writeInterval 1` 表示每个时间步输出一次。它独立于整场的写出间隔，因而可以频繁记录少量探针，而较少保存体积较大的全场结果。

运行 `icoFoam` 后查看 `postProcessing/cavityProbes/0/p` 和 `U`。文件头给出探针编号和位置；每一行先写时间，再按探针顺序写数值。`p` 是标量，`U` 每个点包含 `(Ux Uy Uz)` 三个分量。方腔中的压力单位为 m²/s²，转换为 Pa 时乘以流体密度。

## 实例二：提取一条中心线

在同一个 `functions` 中添加：

```foam
centreline
{
    type                sets;
    libs                (sampling);
    writeControl        writeTime;
    setFormat           raw;
    interpolationScheme cellPoint;
    fields              (U p);
    sets
    (
        vertical
        {
            type    uniform;
            axis    y;
            start   (0.05 0.001 0.005);
            end     (0.05 0.099 0.005);
            nPoints 99;
        }
    );
}
```

`uniform` 在起点和终点之间均匀布置 99 个采样点；`axis y` 以 y 坐标作为输出的独立坐标。起点和终点略离开壁面，便于明确采样内部流场。`cellPoint` 结合单元与点上的信息进行插值，能得到较平滑的曲线；`cell` 使用所在单元值，粗网格上会呈分段变化。

`writeControl writeTime` 使线采样随整场写出进行，输出在 `postProcessing/centreline/<time>/` 中。画中心线时，取速度的 x 分量并按顶盖速度归一化，即 $u/U_{\mathrm{lid}}$；纵坐标可用 $y/L$。对比不同网格时保留相同采样位置与插值规则。

## 实例三：出口流量

对 pitzDaily 等具有入口和出口的算例，在 `functions` 中加入：

```foam
outletFlow
{
    type          surfaceFieldValue;
    libs          (fieldFunctionObjects);
    regionType    patch;
    name          outlet;
    operation     sum;
    fields        (phi);
    writeFields   false;
    writeControl  timeStep;
    writeInterval 1;
}
```

`regionType patch` 指定网格边界，`name outlet` 是 patch 名称。`phi` 是已经对每个面面积积分的通量，因此使用 `sum` 求和。对于常密度不可压缩求解器，通常得到 m³/s；可压缩求解器的 `phi` 通常是 kg/s，读取字段量纲即可区分。

边界法向朝向域外，流出为正、流入为负。可以复制此对象并改名为 `inletFlow`，将 patch 改为 `inlet`。稳态无质量源时，两者的代数和应接近零。对于温度这种“单位面积上定义的场值”，计算面积平均才采用 `areaAverage`；通量和普通场值对应不同的积分操作。

## 实例四：从指定时刻开始求平均

瞬态流动中，先观察压力、速度或阻力历史，选择启动变化结束后的统计起点。例如，从 2 s 开始累计速度均值与脉动二阶矩：

```foam
flowAverage
{
    type            fieldAverage;
    libs            (fieldFunctionObjects);
    timeStart       2;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    restartOnRestart false;
    fields
    (
        U
        {
            mean       on;
            prime2Mean on;
            base       time;
        }
    );
}
```

`executeInterval 1` 每步更新统计，`writeControl writeTime` 在整场写出时保存统计结果。`mean` 生成 `UMean`，`prime2Mean` 生成速度脉动的对称二阶矩场 `UPrime2Mean`，其中包括 $\overline{u_i'u_j'}$ 各分量。

`base time` 按时间进行平均，适用于变时间步：步长较大的状态应有相应的时间权重。`base iteration` 按采样次数平均。`restartOnRestart false` 配合已保存的统计状态可以在续算时延续累计；需要重新统计时，可明确开启重置或使用新的对象名称与起始时间。

平均的数学定义为：

\[
\overline{U}=\frac{1}{T}\int_{t_0}^{t_0+T}U(t)\,dt.
\]

$t_0$ 是统计起点，$T$ 是累计时长。对周期流动，比较多个周期的平均；对湍流统计，可以比较前后两个时间段的均值是否接近，并观察增大统计窗口后的变化。

## 已有结果还能怎样处理

只需读取已保存字段的采样对象，通常可以用通用后处理程序执行：

```bash
postProcess -latestTime
```

它读取 `controlDict` 中的对象并处理选定时间。依赖湍流模型或热物性对象的操作，需要相应求解器的后处理模式，例如 `simpleFoam -postProcess -func yPlus -latestTime`。运行时才存在、没有写出的高频数据则需要重新计算或从现有的较稀疏时间点近似分析。

## 常见问题

| 现象 | 检查方法 |
| --- | --- |
| 探针返回异常值或提示找不到单元 | 将采样点显示在几何中，检查坐标与单位是否在流体域内 |
| 字段找不到 | 确认当前时间有该字段；依赖模型计算的字段使用对应求解环境 |
| 结果文件只有很少几行 | 检查对象自己的 `writeControl` 和 `writeInterval` |
| 出口流量符号与预想相反 | 检查面法向约定和是否发生回流 |
| 平均场受早期启动过程影响 | 调整统计起点，检查已有累计状态是否延续 |

## 练习

为方腔同时添加两个探针和一条中心线。计算结束后，在同一时刻从中心线读取中心点速度，与中心探针比较。两者可能因插值方法而有小差异，可以将插值方案统一后再次检查。

进阶时选择一个周期流动，分别用每步、每 5 步、每 20 步的探针数据计算频谱。观察采样变稀后高频分量是否混叠。采样频率需高于目标最高频率的两倍；实际分析波形与幅值时，通常还需要更多的每周期采样点。
