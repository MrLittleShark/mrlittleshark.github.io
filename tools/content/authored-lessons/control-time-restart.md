`system/controlDict` 控制计算从何时开始、何时结束、时间步多大，以及多久保存一次结果。合理设置这些参数，可以保留需要的瞬态数据，也方便从中间时刻继续计算。

## 一个完整的 controlDict

下面是基础方腔的配置，可直接与算例中的文件对照：

```foam
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      controlDict;
}

application     icoFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         0.5;
deltaT          0.005;

writeControl    timeStep;
writeInterval   20;
purgeWrite      0;
writeFormat     ascii;
writePrecision  6;
writeCompression off;
timeFormat      general;
timePrecision   6;
runTimeModifiable true;
```

`application` 记录所用求解器，官方运行脚本可据此选择程序。在终端直接执行 `icoFoam` 时，实际运行的程序由这条命令决定。

`startFrom startTime` 表示从指定的 `startTime` 读取场；`stopAt endTime` 表示推进到 `endTime` 结束。上述设置从 0 算到 $0.5\,\mathrm{s}$，时间步长为 $0.005\,\mathrm{s}$。

## 时间步与写出间隔

![时间步与结果写出](/assets/diagrams/core-time.svg)

求解器每一步更新流场，结果按照写出规则保存。上面的 `writeControl timeStep` 表示按步数计数，`writeInterval 20` 表示每 20 步写一次，因此写出间隔为：

$$
\Delta t_{\mathrm{write}}=20\times0.005=0.1\,\mathrm{s}.
$$

计算会生成 `0.1`、`0.2` 等时间目录，而每两次写出之间仍然进行了 20 个时间步。

如果希望每 $0.01\,\mathrm{s}$ 保存一次，在时间步保持不变时可改成：

```foam
writeControl    timeStep;
writeInterval   2;
```

这会增加文件数量，但不会改变求解步长。调整 `deltaT` 会改变时间离散；调整 `writeInterval` 主要改变输出频率和存储成本。

## 常见写出方式

| `writeControl` | `writeInterval` 的含义 | 适用情况 |
| --- | --- | --- |
| `timeStep` | 时间步数 | 固定时间步，按固定步数保存 |
| `runTime` | 模拟的物理时间间隔 | 按物理时间安排输出 |
| `adjustableRunTime` | 物理时间间隔，并配合时间步调整命中写出时刻 | 支持相应调步逻辑的求解器 |
| `clockTime` | 实际经过的秒数 | 长时间任务按墙钟时间保存 |
| `cpuTime` | 消耗的 CPU 秒数 | 按计算成本安排保存 |

例如使用 `runTime` 时，`writeInterval 0.1` 表示约每 $0.1\,\mathrm{s}$ 模拟时间写出一次。固定时间步恰好整除间隔时，写出时刻能够自然对齐；不能整除时，通常在越过相应时间区间的时间步写出。

对于本课的固定步长 `icoFoam`，使用 `timeStep` 最直观。以后使用可变时间步求解器时，再根据时间步控制方式选择 `adjustableRunTime`。

## 时间步大小怎样判断

对流问题常用 Courant 数衡量一个时间步内流体通过的局部网格尺度，简单估计为：

$$
Co\approx\frac{|U|\Delta t}{\Delta x}.
$$

方腔网格的 $\Delta x=0.1/20=0.005\,\mathrm{m}$。用顶盖速度 $1\,\mathrm{m/s}$ 和时间步 $0.005\,\mathrm{s}$ 估计，可得 $Co\approx1$。求解器日志中的 Courant 数根据实际单元体积和面通量计算，应以日志中的最大值监测局部情况。

网格加密到 $40\times40\times1$ 后，网格尺度减半。若希望保持相近的 Courant 数，可先把时间步也减半为 `0.0025`。更细的时间步通常能提高瞬态分辨率，同时增加计算成本。

Courant 数限制与所用离散格式、求解算法和物理模型有关。判断时间精度时，还应比较减小时间步前后的速度、压力、力等目标量。

有些求解器会读取 `adjustTimeStep`、`maxCo` 和 `maxDeltaT`，自动调整时间步。`icoFoam` 的本课程实现采用固定 `deltaT` 时间循环，按 Courant 数自动调步需要求解器中的相应逻辑。方腔练习直接修改 `deltaT` 即可。

## 从最新结果继续计算

假设方腔已计算到 $0.5\,\mathrm{s}$，现在希望继续到 $1\,\mathrm{s}$。保留算例中的 `0.5` 目录，将以下两个条目改为：

```foam
startFrom       latestTime;
endTime         1;
```

然后运行：

```bash
icoFoam > log.icoFoam-restart 2>&1
```

`latestTime` 自动选择最大的可用时间目录。求解器从该目录读入速度、压力和相关状态，继续推进。`startTime` 在这种选择下不负责指定起始目录。

希望明确从某一时刻继续时，使用：

```foam
startFrom       startTime;
startTime       0.3;
endTime         1;
```

这要求 `0.3` 目录及所需场文件存在。求解器不能从仅保存在图片中的状态恢复计算。需要续算时，应保留时间目录、物性和数值设置；多步时间格式、动网格或带模型状态的计算还应保留所需历史数据。

## 输出格式与精度

`writeFormat ascii` 生成可直接阅读的文本文件；`binary` 适合较大数据量，可减少文件体积和读写成本。`writeCompression on` 进一步压缩写出文件，会增加一定的压缩计算开销。

`writePrecision` 控制 ASCII 数值的写出精度。方腔默认值为 6。进行较严格的续算对比时，可以提高到：

```foam
writePrecision  12;
```

这可以减少读取已写出数据时产生的舍入差异。它与求解器内部采用的浮点精度是不同设置。

`timePrecision` 控制时间目录名的精度。时间步很小时，应留出足够有效数字，避免相邻写出时刻得到相同的目录名。

`purgeWrite 0` 保留全部写出时刻；正整数会只保留规定数量的近期输出并清理更早的写出结果。需要完整瞬态历史或准备做曲线分析时，使用 0 更方便。

## 运行中修改结束时间

`runTimeModifiable true` 允许程序在运行过程中重新读取支持动态修改的配置。比如计算即将到达 `0.5`，可以把 `endTime` 改成 `1`，使计算继续。

需要保存当前状态后停止时，可以把 `stopAt` 改为：

```foam
stopAt writeNow;
```

求解器在读取到该设置后，于相应时间步写出并结束。希望在下一次计划写出时停止，可使用 `nextWrite`。重启前将 `stopAt` 恢复成 `endTime`。

动态修改能否生效取决于程序何时重新读取该字典及具体参数。网格拓扑、场类型等结构性变化通常需要结束运行后重新准备算例。

## 比较一次计算与分段续算

准备两个相同副本，均将 `writePrecision` 设为 12。

1. `cavity-continuous` 从 0 直接算到 1。
2. `cavity-restart` 从 0 算到 0.5，再使用 `latestTime` 续算到 1。
3. 在 ParaView 中提取两者 $t=1\,\mathrm{s}$ 的同一条中心线，比较 `U_X` 和 `U_Y`。

对于相同网格、固定时间步和 Euler 时间格式，这两种运行方式的结果应非常接近。小差异可能来自写出精度及计算过程中的舍入；明显差异应检查读取的起始时间、参数是否一致、历史场是否完整。

## 常见问题

| 现象 | 检查方法 |
| --- | --- |
| 启动后立即出现 `End` | 检查 `endTime` 是否大于实际读取的起始时间，以及 `stopAt` 的值 |
| 指定 `0.3` 后找不到场 | 检查该目录是否确实写出，是否包含所需的 `U`、`p` 等文件 |
| 输出比预计少 | 检查 `writeControl` 的单位、`writeInterval` 和 `purgeWrite` |
| 细化网格后计算更不稳定 | 查看最大 Courant 数，减小时间步并检查网格质量 |
| 续算覆盖了原来的后续结果 | 从较早时刻重算会写入相同时间目录；做对比时保留独立副本 |
