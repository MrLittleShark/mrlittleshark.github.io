OpenFOAM 是用于流体流动、传热和多相流等问题的开源计算软件。使用它时，通常先在文本文件中设置几何、物性和边界条件，再运行网格工具与求解器，最后用 ParaView 查看结果。本课程使用 **OpenFOAM v2512**。

## OpenFOAM 由哪些部分组成

以计算管道中的水流为例，需要给出管道尺寸、入口流速、出口压力和水的黏度。OpenFOAM 根据这些输入，计算网格中各处的速度和压力。

| 组成 | 作用 | 本课程中的例子 |
| --- | --- | --- |
| 求解器 | 求解特定物理模型的控制方程 | `icoFoam`：不可压缩牛顿流体的瞬态层流 |
| 工具程序 | 生成网格、设置初值、检查和导出数据 | `blockMesh`、`checkMesh`、`foamToVTK` |
| C++ 库 | 提供网格、矩阵、离散算子和物理模型 | `finiteVolume`、各类边界条件 |
| 算例 | 保存一次计算的输入与结果 | 官方 `cavity` 方腔算例 |

![OpenFOAM 的程序、算例与结果](/assets/diagrams/core-architecture.svg)

求解器的名字出现在运行命令中；网格、物性和边界条件保存在算例目录里。同一个求解器可以运行许多不同算例。例如，`icoFoam` 既可以计算顶盖驱动方腔，也可以计算适合其物理假设的其他层流问题。湍流、多相流和可压缩流动则需要相应的求解器与模型。

初学阶段主要修改算例文件。学习二次开发时，才会进一步编译自己的求解器或边界条件。后续编程课程会介绍这部分内容。

## 选择运行环境

课程中的命令在 **Linux 的 Bash 终端**执行。Windows 用户可以在 VMware 中安装 Ubuntu，或使用 WSL2；已有 Ubuntu 虚拟机的读者可以直接继续使用。

| 环境 | 使用方式 | 文件建议放置位置 |
| --- | --- | --- |
| Ubuntu 电脑 | 在桌面打开终端 | 用户主目录下 |
| VMware Ubuntu | 在虚拟机内打开终端 | 虚拟机的 Linux 文件系统中 |
| WSL2 Ubuntu | 打开 Ubuntu 终端 | `/home/用户名/` 下 |

计算会频繁读写文件，Linux 本地目录通常比 Windows 共享目录更适合作为工作目录。共享目录适合传递讲义、压缩包和结果图片。

如果已经安装 OpenFOAM，可以直接阅读下面的“加载运行环境”。尚未安装时，可选择 Ubuntu 软件包安装。源码安装适合需要管理编译器、第三方库或修改核心库的读者，初次学习可先使用软件包。

## 在 Ubuntu 中安装 v2512

以下命令将添加 OpenFOAM 官方软件源并安装固定版本。先安装下载工具：

```bash
sudo apt update
sudo apt install curl ca-certificates
```

`sudo` 使这一条命令获得系统管理权限；`apt update` 更新软件包索引；`apt install` 安装指定软件。输入密码时，终端通常不显示字符，输入完成后按回车即可。

下载并运行官方软件源配置脚本：

```bash
curl -fsSL https://dl.openfoam.com/add-debian-repo.sh \
    -o /tmp/add-openfoam-repo.sh
sudo bash /tmp/add-openfoam-repo.sh
apt-cache policy openfoam2512-default
```

第一条命令把脚本保存到 `/tmp`，第二条运行脚本，添加软件源及其签名密钥。最后一条查询 `openfoam2512-default` 是否有可安装版本；输出中的 `Candidate` 应是一个版本号。

存在可安装版本后执行：

```bash
sudo apt install openfoam2512-default
```

软件源是否提供对应包取决于 Ubuntu 版本和处理器架构。如果 `Candidate` 显示 `(none)`，检查前面脚本中的软件源错误，并查看 [OpenFOAM 安装说明](https://www.openfoam.com/download/openfoam-installation-on-linux) 对当前系统的支持情况。

## 加载运行环境

软件包安装完成后，在终端执行：

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
foamVersion
command -v icoFoam
icoFoam -help
```

这四行分别完成以下操作：

1. `source` 读取环境脚本，使当前终端能够找到 OpenFOAM 的程序和动态库。
2. `foamVersion` 显示版本信息，其中应包含 `v2512`。
3. `command -v icoFoam` 显示将要执行的程序路径。
4. `icoFoam -help` 显示求解器用途和可用参数。

`-help` 只显示帮助，不会开始流体计算。安装路径与上面不同的读者，应将第一行替换为自己安装目录中的 `etc/bashrc` 路径。环境脚本路径由安装方式决定，后面的命令相同。

关闭终端后，这次 `source` 的设置随之结束。长期使用同一版本时，可以用文本编辑器打开 `~/.bashrc`，在末尾加入：

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
```

其中 `~` 表示当前用户的主目录，例如 `/home/chen`。保存后新打开的 Bash 终端会自动加载 OpenFOAM。同时保留多个版本时，可以为每个版本定义一个别名，在新终端中选择需要的版本：

```bash
alias of2512='source /usr/lib/openfoam/openfoam2512/etc/bashrc'
```

这样输入 `of2512` 即可加载该版本。一个终端内使用一套环境，有助于保持程序与动态库一致。

## 找到教程与工作目录

OpenFOAM 用环境变量保存常用目录。变量名前的 `$` 表示读取变量的值：

```bash
echo "$WM_PROJECT_DIR"
echo "$FOAM_TUTORIALS"
echo "$FOAM_RUN"
```

`WM_PROJECT_DIR` 是软件安装根目录；`FOAM_TUTORIALS` 指向随软件提供的教程；`FOAM_RUN` 是约定的个人算例目录。`echo` 只把值打印出来。

为了使后续章节的路径一致，本课程将算例统一放在个人目录下：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
```

`HOME` 也是环境变量，表示用户主目录。`mkdir -p` 会创建缺少的上级目录，已存在的目录会保留。

官方方腔位于：

```text
$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity
```

这里连续两个 `cavity` 是官方目录的组织方式：外层放置一组方腔练习，内层是基础算例。下一课会把这个算例复制到个人目录，再介绍文件查看、日志保存和命令选项。

## 常见问题

| 现象 | 常见原因 | 处理方法 |
| --- | --- | --- |
| `icoFoam: command not found` | 当前终端尚未加载环境 | 执行安装目录中的 `source .../etc/bashrc` |
| `source` 提示文件不存在 | 环境脚本路径与安装位置不一致 | 查看 `/usr/lib/openfoam` 中的实际目录名，或自己的源码安装目录 |
| `error while loading shared libraries` | 程序与动态库路径不一致，或依赖缺失 | 新开终端，只加载 v2512；软件包缺失依赖时修复对应包 |
| 普通复制操作出现 `Permission denied` | 正在软件安装目录中创建文件 | 将算例复制到 `$HOME/OpenFOAM/learning-v2512` 后修改 |
| Windows 终端无法识别 `source` | 命令在 PowerShell 中执行 | 打开虚拟机或 WSL2 的 Ubuntu 终端 |

## 动手练习

关闭当前终端，重新打开一个终端，运行 `foamVersion` 和 `icoFoam -help`。若添加了自动加载语句，这两个命令应直接可用；若使用别名，先运行 `of2512`。

再执行下面的命令：

```bash
ls "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity"
```

输出中应包含 `0`、`constant` 和 `system`。这三个目录分别保存初始场、物性及网格、计算控制设置。后面几课将围绕它们完成第一次计算。
