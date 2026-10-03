`functionObject` 是 OpenFOAM 的功能对象，用于在计算过程中采样、统计、导出结果，也可以处理已经保存的场。常见任务包括记录压力探针、计算流量和力系数、提取截面、生成平均场、检查水量与热功率。

## 按要得到的结果选择工具

| 课程编号 | 内容 | 主要工具与结果 |
|---|---|---|
| 00–01 | 运行方式与通用参数 | `controlDict`、`postProcess`、执行频率与输出控制 |
| 02–04 | 点、线、面与流线 | `probes`、`sets`、`surfaces`、`streamLine` |
| 05–06 | 空间统计与积分 | 极值、平均、直方图、流量、压降 |
| 07–08 | 场运算与时间统计 | 梯度、涡量、Q、平均场与脉动 |
| 09–10 | 力、壁面与湍流 | 升阻力、力矩、y+、壁面剪切、湍流量 |
| 11–12 | 传热与两相流 | 热流、换热系数、水量、液位与界面 |
| 13–15 | 导出、监测与自动控制 | VTK / EnSight、残差、守恒、条件停止 |
| 16 | 工具分类与选用索引 | 按任务查找类型、课程与扩展工具 |

## 配套算例

| 算例 | 求解内容 | 用来练习 |
|---|---|---|
| [方腔](/downloads/function-objects/01-cavity.zip) | `icoFoam`，0–0.5 s | 采样、场运算、统计、流线与导出 |
| [后台阶](/downloads/function-objects/02-pitzDaily.zip) | `simpleFoam`，100 次迭代 | 流量、压降、壁面量与力系数 |
| [冷热壁面](/downloads/function-objects/03-hotRoom.zip) | `buoyantPimpleFoam`，0–0.2 s | 壁面热流、热流传感器与换热系数 |
| [溃坝](/downloads/function-objects/04-damBreak.zip) | `interFoam`，0–0.2 s | 水相体积、液面高度与自由表面 |
| [自动停止](/downloads/function-objects/05-autoStop.zip) | 方腔，控制器提前结束 | `runTimeControl` 条件与停止时刻 |

[下载全部算例](/downloads/function-objects/function-objects-v2512.zip)。解压后进入对应算例目录，在已加载 OpenFOAM v2512 的终端运行 `bash Allrun`。每个包包含输入文件、运行脚本和参考数据。

![方腔采样和中心线速度](/assets/science/functionobjects-sampling.png)

第一次接触功能对象，可以从第 00 课运行方腔开始。已经有计算结果时，按上表直接选择需要的分析任务；各课都给出配置位置、参数含义和输出文件的读法。
