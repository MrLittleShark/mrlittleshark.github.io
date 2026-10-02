一份便于共享的 OpenFOAM 算例需要完整输入、清楚的运行步骤和少量能说明结果的数据。以方腔为例，读者下载后应能找到 `0`、`constant`、`system`，运行网格和求解器，再生成相同定义的中心线曲线。

## 一个容易维护的目录

```text
cavity-study/
  case/
    0/
    constant/
    system/
  scripts/
    run.sh
    plot.py
  results/
    centreline.csv
    centreline.png
  README.md
  environment.txt
```

`case` 保存求解所需输入，`scripts` 保存运行和后处理方法，`results` 保存文章中使用的数据与图。原始的大体积时间目录可以单独归档，日常交流优先提供能够重新生成结果的输入。

几何文件放在 `constant/triSurface`，被 `#include` 引用的文件与字典一起打包。自定义边界和求解器需要附上源码、编译方法及 `Make` 配置。若依赖已安装的库，在说明中给出库名、版本和获取方式。

![算例输入、运行脚本与结果文件](/assets/diagrams/core-reproducibility.svg)

## 实例：一个保留日志的运行脚本

将下面内容保存为 `scripts/run.sh`，用于新的基础方腔副本：

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../case"
: "${WM_PROJECT_VERSION:?请先加载 OpenFOAM 环境}"

printf 'OpenFOAM=%s\n' "$WM_PROJECT_VERSION"
printf 'Case=%s\n' "$PWD"

blockMesh 2>&1 | tee log.blockMesh
checkMesh 2>&1 | tee log.checkMesh

if grep -Eq 'Failed [1-9][0-9]* mesh checks' log.checkMesh; then
    printf '%s\n' '网格检查有失败项，详见 log.checkMesh。' >&2
    exit 1
fi

icoFoam 2>&1 | tee log.icoFoam
```

`#!/usr/bin/env bash` 指定 Bash 解释器。`set -e` 在命令失败时结束脚本，`-u` 检查未定义变量，`pipefail` 让管道中前面的命令失败也传递给脚本。这样 `icoFoam` 失败时，后面的 `tee` 成功写入日志不会掩盖求解器的错误。

`dirname "$0"` 取得脚本所在目录，因此从工程根目录或其他位置调用它，都能进入同一个 `case`。`${WM_PROJECT_VERSION:?...}` 检查 OpenFOAM 环境是否已加载，环境缺失时打印后面的中文提示。

`tee` 同时在终端显示并写入日志。`checkMesh` 的质量检查结果需要阅读其汇总，脚本额外识别明确的 `Failed ... mesh checks` 行。拓扑错误和网格质量问题处理后，再运行求解。

在 `cavity-study` 目录执行：

```bash
chmod +x scripts/run.sh
./scripts/run.sh
```

`chmod +x` 添加执行权限。也可以使用 `bash scripts/run.sh` 显式调用 Bash。此脚本使用基础方腔的 `icoFoam`；制作其他案例时，按实际求解器和预处理步骤调整脚本。

## README 应该怎样写

说明可以直接围绕读者的操作展开：

```markdown
# 二维顶盖驱动方腔

OpenFOAM v2512。方腔边长 0.1 m，顶盖速度 1 m/s，
运动黏度 0.01 m²/s，雷诺数为 10。

## 运行

加载 OpenFOAM 环境后，在本目录执行：

    bash scripts/run.sh

## 查看结果

在 case 目录运行 paraFoam，选择速度 U。
顶盖沿 x 方向运动，腔内形成主循环。
中心线数据由 controlDict 中的 centreline 对象输出到
case/postProcessing/centreline/。

## 修改参数

入口：此案例为封闭方腔，流动由顶盖驱动。
顶盖速度：case/0/U 中 movingWall 的 value。
运动黏度：case/constant/transportProperties 中的 nu。
网格数量：case/system/blockMeshDict 中 blocks 的单元数。
```

这里先说明物理问题和数值量级，再给运行与结果位置，最后列出常改参数。对较复杂案例，补充所需的 MPI 进程数、几何预处理工具和大致磁盘空间。结果图片应包含变量名、单位、色标和物理时间，读者可以直接与自己的结果比较。

案例的局限也可以具体说明。例如二维方腔适合学习层流数值方法，而具有真实三维侧壁的装置需要相应三维模型。用一句话交代适用条件即可。

## 怎样记录计算环境

在已加载 OpenFOAM 的终端运行：

```bash
{
    foamVersion
    uname -a
    command -v icoFoam
    command -v mpirun
    mpirun --version
} > environment.txt 2>&1
```

大括号把多条命令的输出写入同一个文件。`foamVersion` 记录软件版本，`uname -a` 记录系统信息，`command -v` 记录实际调用的程序路径，MPI 版本便于排查并行运行差异。串行案例可省略 MPI 两行；自定义程序再记录编译器版本和依赖库。

发布前检查环境记录中的用户名、私人路径和机器信息，保留对复现有帮助的部分。GitHub 令牌、服务器密码与个人密钥始终存放在自己的认证配置中。

## 参数研究怎样组织

为不同参数保存独立目录，例如 `Re10`、`Re100`、`Re1000`。每组目录拥有自己的输入和日志，结果汇总表记录真正使用的参数：

| 案例 | 顶盖速度 / m·s⁻¹ | 运动黏度 / m²·s⁻¹ | 网格 | 结束时间 / s |
| --- | ---: | ---: | --- | ---: |
| Re10 | 1 | 0.01 | 40×40 | 按计算设置填写 |
| Re100 | 1 | 0.001 | 40×40 | 按计算设置填写 |
| Re1000 | 1 | 0.0001 | 80×80 | 按计算设置填写 |

雷诺数由 $Re=UL/\nu$ 计算。改变黏度后，稳定性、所需网格和达到稳定状态的时间可能一起变化，因此目录名以外还应保留完整字典。后处理脚本从这些目录读取结果，统一坐标、变量、单位和图例。

## 使用 Git 保存输入修改

可以将工程加入 Git，通过提交记录查看边界、网格和数值设置的变化。大型自动生成结果一般单独保存。下面是一份针对上述目录结构的 `.gitignore` 示例：

```gitignore
case/processor*/
case/postProcessing/
case/log.*
case/[1-9]*/
case/0.*/
```

这些规则忽略常见并行目录、自动采样、日志和正时间结果，同时保留 `case/0/`。`results` 中用于文章的精选 CSV 和图片仍会被记录。正式归档时再把必要运行日志放入专门的资料包，便于查看这次计算的实际过程。

提交前查看 `git status`，确认新的几何、包含文件和自定义源码已经加入。网格由 `blockMesh` 生成时通常保留生成字典即可；外部导入且无法直接重建的网格，则需要把原始网格或可靠的下载位置一同提供。

## 分享问题时怎样提供有效信息

问题描述写明目标、运行命令和具体异常。例如：“pitzDaily 改为 SST 后，启动时提示找不到 omega；附件中包含当前 0、constant 和 system。”同时附报错前后的相关日志以及必要输入，讨论者就能定位到字段或模型设置。

复现包可以保留小网格和最短触发时间，以减少下载与计算成本。简化时仍保留触发问题所需的边界、包含文件、几何和库。如果错误只在并行时发生，还应给出分区方法、进程数和最先报错的进程信息。

## 练习：从压缩包重新开始

将当前工程压缩后解压到一个新位置，仅按 README 中的步骤运行。检查脚本是否依赖原来的绝对路径、是否缺少 `#include` 文件、结果图能否由后处理脚本重新生成。修正发现的依赖后，再分享下载链接。

进阶项目可以让持续集成自动检查字典、编译自定义库，并运行规模很小的基础案例。耗时较长的工程计算单独保存结果与日志，两类任务采用各自合适的执行环境。
