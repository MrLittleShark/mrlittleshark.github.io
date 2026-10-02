![编程模块的数据关系](/assets/diagrams/programming-07.svg)

本页按照资料目录中实际出现的 `system/controlDict` 清点算例入口。已排除显式备份目录、处理器子域与结果时间目录。同一物理问题的不同参数版本仍可能是不同入口，因此条目数不能解释为独立物理模型数量或全部已验证算例数。

| 资料目录 | 找到的 controlDict 入口 |
| --- | ---: |
| `101BLOCKMESH` | 6 |
| `101OF` | 33 |
| `101OF_extended` | 15 |
| `101SHM_basic` | 8 |
| `101postprocessing` | 2 |
| `101programming` | 32 |
| `advanced_SHM` | 8 |
| `advanced_physics` | 28 |
| `advanced_postprocessing` | 3 |

## 按目标选择材料

- **初次运行与后处理**：先看 `101OF/cavity2D`，理解网格、初值、时间控制、中心线采样与基准比较。
- **改变网格拓扑**：进入 `101BLOCKMESH`、`101SHM_basic`，分别学习结构化块网格和表面驱动网格；先运行网格检查，再运行求解器。
- **初始化与边界编程**：看 `101programming/codeStream_INIT`、`codeStream_BC`；它们把小段 C++ 嵌入字典，适合理解字段构造。
- **修改方程**：看 `101programming/my_solvers`，从 Laplace、对流扩散到 icoFoam 的修改逐步增加复杂度。
- **统计与批处理**：看 `101postprocessing`、`advanced_postprocessing`，留意采样文件名、列号和函数对象的版本变化。
- **复杂物理与网格**：`advanced_physics`、`advanced_SHM` 包含更高成本的算例。按对应报告核对短启动、完整网格及长时间求解分别是否执行过。

[下载完整目录清单 JSON](/downloads/programming/of-material-case-catalog.json)。清单记录入口路径和 controlDict 中的 application，仅作导航，不替代逐例运行说明。

## 源码阅读次序

先读脚本确定命令链，再读 `controlDict` 确定实际应用程序，然后看 `0/`、`constant/`、`fvSchemes` 和 `fvSolution`。自定义求解器进一步检查 `Make/files` 的目标名称及 `createFields.H`。若脚本导入外部网格，应保留相对目录结构和输入网格文件。

本网站提供下列精选源包；其他大体积结果与生产网格不重复放入 GitHub Pages 静态站点。

[下载精选源码与算例](/downloads/programming/OF_material-v2512-selected-examples.zip) · [包内目录、校验值与范围](/downloads/programming/OF_material-selected-manifest.json)
