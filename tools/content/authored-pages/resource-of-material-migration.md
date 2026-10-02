![从输入到计算的验证链](/assets/diagrams/programming-10.svg)

`OF_material` 是面向 v2512 的课程代码与算例集合。使用前应确认具体求解器、物理模型、输入字典与运行环境。各报告覆盖的目录和测试步骤不同，某个算例的检查结果不能代表整个资料库均已完成相同级别的验证。

## 2026-09-04 报告记录的验证范围

| 层级 | 报告中的证据 | 能说明什么 |
| --- | --- | --- |
| 字典解析 | 49 个主 controlDict 成功解析 | 这些字典的基本读取通过 |
| Shell 语法 | 149 个目标脚本通过 bash -n | Shell 语法成立，不代表外部命令执行成功 |
| 基础网格 | 37 个 blockMesh 算例完成生成和 checkMesh | 已检查这些网格的生成与质量诊断 |
| 表面特征 | 18 份配置通过 surfaceFeatureExtract | 对应输入表面与特征提取接口已执行 |
| SHM 配置 | 26 份配置通过 snappyHexMesh -dry-run | 配置检查通过，不等于完整层网格生成通过 |
| 求解启动 | 22 个代表算例初始化并完成至少一步或一次迭代 | 基本求解链可启动，不代表充分收敛和长时间稳定 |

报告明确指出没有开展长生产时长计算。它覆盖列出的 `101postprocessing`、`advanced_physics`、`advanced_postprocessing`、`advanced_SHM` 和 `101SHM_basic` 等迁移目标，另有 `101programming` 与 `101OF_extended` 的独立说明。

## v2512 配置与运行检查

先确认所选 v2512 求解器读取的物性与湍流模型配置，再检查 `fvOptions`、函数对象、采样关键字、特征提取、网格字典及无图形环境绘图。不同求解器可能读取不同的模型接口，应以实际源码、官方教程和运行日志核对文件名及必需条目。

程序编译成功和算例读取成功是不同证据。尤其对于自定义边界条件，应进一步检查运行时类型注册、构造、并行映射和重启写出。

## 下载原始记录

- [总迁移报告](/downloads/programming/OF_material-V2512_MIGRATION_REPORT.md)
- [101programming 的迁移说明](/downloads/programming/of-material-programming-migration.md)：报告称 143 个构建目标通过，本站按原报告表述，未将其改写为本次重新编译的结果。
- [101OF_extended 的迁移说明](/downloads/programming/of-material-extended-migration.md)
- [cavity2D 的计算与采样说明](/downloads/programming/of-material-cavity-migration.md)：独立记录了运行至 t=50 和统计比较，应与总报告的短启动检查区分。

新增算例推荐记录四类信息：源码或字典版本、实际执行命令与退出状态、网格及守恒诊断、与解析或基准数据的差异。不要用一个“已验证”标签代替这些具体证据。
