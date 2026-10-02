![求解器的构成](/assets/diagrams/programming-10.svg)

此包来自用户提供的 v2512 适配目录，保留 8 个教学入口及弯管例所需的小型 Fluent 输入网格，移除生成网格、历史解、并行分区、编译对象和可视化结果。它用于逐步理解代码与字典，不是完整 OF_material 镜像。

## 包含哪些示例

| 入口 | 适合研究的问题 |
| --- | --- |
| cavity2D | 标准求解、统计、中心线采样和 Ghia 对照 |
| codeStream_INIT/cylinder | 几何区域与初值列表 |
| codeStream_INIT/elliptical_IC | 椭圆判据和体积离散误差 |
| codeStream_INIT/rayleigh_taylor | 扰动界面初值的构造 |
| codeStream_BC/2Delbow_UparabolicInlet | 入口剖面和动态代码 |
| my_laplace_v1、v2、v3 | 自定义方程、字段创建和控制循环的递进 |

## 运行前检查

解压后保留 `OF_material/101programming` 与 `OF_material/meshes_and_geometries` 的相对关系，弯管脚本通过相对路径导入网格。先阅读 `run_solver.sh`：有些例采用四个 MPI 进程，有些脚本会清理已有结果。首次实验复制到独立目录，保留源包作为基线。

Laplace 应用在对应源码目录执行 `wmake`，再进入 `test_case` 运行脚本。应用目标名由 `Make/files` 决定，不能假设源码目录名就是 PATH 中的可执行名。

## 怎么把它用于课程

先完成[标量输运求解器](/read/?slug=programming-10)，再比较 Laplace 例去掉对流项后剩余的矩阵与字典。接着完成[初值 codeStream](/read/?slug=resource-coded-initialization)和[自定义入口边界](/read/?slug=programming-08)，比较“读取时生成一个场”和“边界更新时计算面值”的区别。

包内迁移说明是原资料的历史记录。本站没有将全包每个案例重新跑到生产时长，用户应按任务选择网格、时间步和守恒诊断。课程资料图的来源与版本应写入图注。

[下载精选源包](/downloads/programming/OF_material-v2512-selected-examples.zip) · [下载说明](/downloads/programming/OF_material-selected-README.md) · [SHA-256 与包范围](/downloads/programming/OF_material-selected-manifest.json)

来源：Wolf Dynamics 基础培训与用户提供的 v2512 适配代码。原文件版权与许可声明保留；基础课件标注 CC BY-SA 4.0，包含 GPL 声明的 C++ 文件沿用其原许可。此包不包含高级培训的整本课件，也不将第三方材料重新声明为本站原创。
