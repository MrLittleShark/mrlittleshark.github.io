![应用程序的构建链](/assets/diagrams/programming-00.svg)

这组材料适合已经能运行基本算例、准备阅读或修改 OpenFOAM 源码的学习者。前 8 课建立程序、字典、场、并行和类库的基础；08—12 进入边界条件、函数对象、输运方程、网格与源项；13—16 讨论时间推进、SIMPLE、离散格式和轨迹积分。

## 使用方法

每课提供代码讲解、配置实例和源码包。下载后先运行原例，再修改代码比较结果；编译命令和修改位置在课程中说明。

| 编号 | 课程 | 下载 |
| --- | --- | --- |
| 00 | [helloWorld](/read/?slug=programming-00) | [精简源码](/downloads/programming/OFtutorial00_helloWorld-v2512.zip) |
| 01 | [inputOutput](/read/?slug=programming-01) | [精简源码](/downloads/programming/OFtutorial01_inputOutput-v2512.zip) |
| 02 | [commandLineArgumentsAndOptions](/read/?slug=programming-02) | [精简源码](/downloads/programming/OFtutorial02_commandLineArgumentsAndOptions-v2512.zip) |
| 03 | [understandingTheMesh](/read/?slug=programming-03) | [精简源码](/downloads/programming/OFtutorial03_understandingTheMesh-v2512.zip) |
| 04 | [basicFieldOperations](/read/?slug=programming-04) | [精简源码](/downloads/programming/OFtutorial04_basicFieldOperations-v2512.zip) |
| 05 | [basicParallelComputing](/read/?slug=programming-05) | [精简源码](/downloads/programming/OFtutorial05_basicParallelComputing-v2512.zip) |
| 06 | [customClasses](/read/?slug=programming-06) | [精简源码](/downloads/programming/OFtutorial06_customClasses-v2512.zip) |
| 07 | [customLibraries](/read/?slug=programming-07) | [精简源码](/downloads/programming/OFtutorial07_customLibraries-v2512.zip) |
| 08 | [customBC](/read/?slug=programming-08) | [精简源码](/downloads/programming/OFtutorial08_customBC-v2512.zip) |
| 09 | [runtimePostprocessingUtility](/read/?slug=programming-09) | [精简源码](/downloads/programming/OFtutorial09_runtimePostprocessingUtility-v2512.zip) |
| 10 | [transportEquation](/read/?slug=programming-10) | [精简源码](/downloads/programming/OFtutorial10_transportEquation-v2512.zip) |
| 11 | [modifyingTheMesh](/read/?slug=programming-11) | [精简源码](/downloads/programming/OFtutorial11_modifyingTheMesh-v2512.zip) |
| 12 | [momentumSource](/read/?slug=programming-12) | [精简源码](/downloads/programming/OFtutorial12_momentumSource-v2512.zip) |
| 13 | [waveEquationSolver](/read/?slug=programming-13) | [精简源码](/downloads/programming/OFtutorial13_waveEquationSolver-v2512.zip) |
| 14 | [SIMPLE_algorithm](/read/?slug=programming-14) | [精简源码](/downloads/programming/OFtutorial14_SIMPLE_algorithm-v2512.zip) |
| 15 | [discretisation](/read/?slug=programming-15) | [精简源码](/downloads/programming/OFtutorial15_discretisation-v2512.zip) |
| 16 | [particleTracking](/read/?slug=programming-16) | [精简源码](/downloads/programming/OFtutorial16_particleTracking-v2512.zip) |

## v2512 接口调整

原资料总说明标注 v2512，但逐例编译发现部分文件仍包含另一 OpenFOAM 分支的接口。本站在独立副本中修复了处理器 patch 头文件、边界字段写出、日志文件接口、网格点移动接口、动量源基类和采样类型，并保存编译与运行证据。原资料目录保持不变。

| 实验 | 原始内容或实际问题 | 网站下载副本的修订 |
| --- | --- | --- |
| 05 并行 | processorPolyPatch 未显式声明 | 加入对应头文件，四进程运行通过 |
| 08 边界 | writeEntry(os, "value", *this) 与 v2512 不匹配 | 使用 writeEntry("value", os)，编译、短运行与后处理通过 |
| 09 函数对象 | 旧 logFiles::file(index) 接口 | 改为 files(index)，显式写文件头 |
| 11 网格 | clone(points) 不匹配；三维外表面被设为 empty | 使用 pointField(points) 与 patch；仍有 1 项 underdeterminedCells 检查失败，明确作为拓扑演示 |
| 12 动量源 | 仍继承 Foundation fvModel 并读 fvModels | 迁移至 OpenCFD fv::option/fvOptions，修改构造、字段注册及 addSup 签名 |
| 15 插值格式 | lineCell 采样类型已不可用 | 使用 v2512 cellCentre，执行至原设定结束时刻 |

17 个示例的编译步骤和运行入口见各节课程。第 11 课用于演示网格构造，其 5 单元网格仍有 `underdeterminedCells` 质量问题，课内给出定位方法。

源码包保留 GPL-3.0-or-later 许可证和原作者信息，请在自己的 v2512 环境中从源码编译。
