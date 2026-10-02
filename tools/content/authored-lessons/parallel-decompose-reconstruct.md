并行计算将一个算例的网格分成多个子域，由多个进程同时求解。相邻子域通过 MPI 交换边界数据。OpenFOAM 的基本流程是分区、并行求解和结果重构，分别对应 `decomposePar`、带 `-parallel` 的求解器以及 `reconstructPar`。

## 实例：把方腔分成四个子域

进入下载包中的 `tutorials/incompressible/icoFoam/cavity/cavity`，在新副本中建立 `system/decomposeParDict`：

```foam
FoamFile
{
    format ascii;
    class dictionary;
    object decomposeParDict;
}

numberOfSubdomains 4;
method scotch;
```

`numberOfSubdomains` 是子域数量，通常与 MPI 进程数一致。`scotch` 按网格连通关系分区，在分配单元数的同时尽量减少子域之间的连接。它适合多种非结构化网格，无需手动指定 x、y、z 方向的切分数。

![四个子域之间的数据交换](/assets/diagrams/core-parallel.svg)

先建立网格，再分区和求解：

```bash
blockMesh > log.blockMesh 2>&1
decomposePar > log.decomposePar 2>&1
mpirun -np 4 icoFoam -parallel > log.icoFoam.parallel 2>&1
reconstructPar -latestTime > log.reconstructPar 2>&1
```

第一步生成完整网格。第二步把网格和初始场写入 `processor0` 到 `processor3`；`-np 4` 启动四个 MPI 进程，`-parallel` 使 `icoFoam` 读取分区并进行进程间通信。最后一条命令将最新时间的结果合并到算例根目录。

`> log... 2>&1` 把正常输出和错误输出保存到日志。执行下一步前检查上一条命令是否正常结束，求解失败时从日志中的第一处具体异常开始排查。

## 分区目录包含哪些内容

```text
case/
  0/                     完整初始场
  constant/polyMesh/     完整网格
  system/                控制字典
  processor0/
    0/                   第 0 个子域的初始场
    constant/polyMesh/   第 0 个子域的网格
    0.5/                 该子域在 0.5 s 的结果
  processor1/
  processor2/
  processor3/
  0.5/                   reconstructPar 生成的完整结果
```

分区边界是求解器交换数据的位置，它们由工具自动生成。原来的入口、出口和壁面条件仍代表同一个物理问题。网格划分位置改变后，求和顺序和线性迭代路径可能略有变化，因此串行与并行结果通常在数值容差内比较。

## 规则网格也可以按方向切分

二维方腔可以在 `decomposeParDict` 中使用：

```foam
numberOfSubdomains 4;
method simple;

simpleCoeffs
{
    n     (2 2 1);
    delta 0.001;
}
```

`n` 指定三个方向的分区数，乘积需要等于 `numberOfSubdomains`。`(2 2 1)` 把 x、y 方向各分成两份，厚度方向保持一份。`delta` 是几何切分时使用的小扰动系数，用来处理切分位置的退化情况，通常保留教程中的设置即可。

对于细长流道，沿主方向分区通常容易保持每个子域形状规整。复杂几何、局部加密或多区域计算中，单元数和实际计算工作量可能分布不均，需要结合分区统计和运行计时调整方法。

## 重构、查看和续算

`reconstructPar -latestTime` 只重构最新时间。需要指定时间段时可使用：

```bash
reconstructPar -time '0.1:0.5'
```

冒号表示从 0.1 到 0.5 的时间范围，实际处理已有的写出时间。重构读取各分区的字段并恢复完整数据；动网格和拓扑变化案例还涉及网格恢复，应根据案例流程区分 `reconstructPar` 与 `reconstructParMesh`。

并行续算时，将 `controlDict` 设置为：

```foam
startFrom latestTime;
```

保留各分区的最新时间目录，再使用相同的 MPI 进程数启动求解器。此时结果主要位于 `processor*` 中，根目录有没有重构结果不决定并行续算的起点。改变进程数需要重新分布网格和场，可以研究 `redistributePar`，并在原结果的副本上操作。

多区域算例使用 `decomposePar -allRegions`，使每个 region 都完成分区；对应的重构也使用 `-allRegions`。各区域子目录的位置与单区域案例不同，第一次运行可以先查看工具日志列出的区域名。

## 怎样比较串行与并行结果

从同一份未运行的输入创建两个副本：一个直接运行 `icoFoam`，另一个使用四个进程。保持相同网格、结束时间、时间步和离散设置。在相同物理时刻比较方腔两条中心线上的速度，也可以比较体积平均动能。

相对差异可写为：

\[
\delta_q=\frac{|q_{\mathrm{parallel}}-q_{\mathrm{serial}}|}
{q_{\mathrm{scale}}}.
\]

当参考量接近零时，分母采用明确的特征尺度，例如顶盖速度，能避免无意义的大相对误差。显著差异需要检查两个副本是否从相同初值开始、是否到达同一时间，以及每个分区的字段是否完整。

## 并行效率为什么不会随核数等比例增加

单进程耗时 $T_1$、$p$ 个进程耗时 $T_p$ 时，加速比和效率为：

\[
S_p=\frac{T_1}{T_p},\qquad E_p=\frac{S_p}{p}.
\]

例如单进程 400 s、四进程 140 s，则加速比约 2.86，效率约 71%。这是计算公式的示例数据。通信、同步、串行部分和写盘都会限制加速。

400 单元的教学方腔主要用于学习命令，每个进程分到的计算量很少，启动和通信开销可能使并行更慢。性能测试应选取有足够单元的算例，固定问题规模比较 1、2、4、8 个进程，并记录硬件和计时范围。

OpenFOAM 日志中的 `ClockTime` 可帮助观察实际运行耗时。比较时保持写出频率一致：频繁输出大量场文件可能让磁盘成为主要瓶颈。集群还需通过调度器申请资源，并使用平台指定的 MPI 启动方式。

## 大量文件怎样管理

默认分区文件模式下，进程数与时间目录数增加会产生大量文件。支持的安装可使用 `collated` 文件处理模式减少文件数量，例如在相匹配的步骤中传入 `-fileHandler collated`。它会改变结果组织方式，具体性能取决于文件系统和 MPI 支持。先在小副本中确认分区、求解与读取流程，再用于大规模计算。

## 常见报错

| 报错或现象 | 常见原因 | 处理方法 |
| --- | --- | --- |
| 找不到某个 `processorN` | MPI 进程数与分区数不一致 | 检查 `numberOfSubdomains` 和 `-np` |
| 初始字段大小与网格不符 | 修改完整网格后沿用旧分区 | 在新副本中重新分区 |
| 某个 rank 首先出现 `FOAM FATAL ERROR` | 字段、边界或局部数值错误 | 查找该进程最早的具体报错，后续 MPI 终止信息是连带结果 |
| 进程增多但耗时增加 | 子域过小、负载不均或 I/O 占比过高 | 查看单元分配和计时，减少进程数或输出频率 |
| 重构缺少一个时间的场 | 部分分区没有写完该时间 | 查看求解退出位置及所有分区的时间目录 |

## 练习

对同一个较细方腔网格比较 `scotch` 与 `simple (2 2 1)`。记录分区单元数、计算耗时和中心线速度差异。然后将写出频率降低，观察耗时是否明显变化。这两个实验分别展示分区通信和磁盘输出对性能的影响。
