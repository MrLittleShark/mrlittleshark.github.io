OpenFOAM 是一款开源的计算流体力学软件，可以计算流动、传热、多相流等问题。用它做计算的一般流程是：先在文本文件里写好几何、物性和边界条件，再运行网格工具和求解器，最后用 ParaView 查看结果。本课程使用 **OpenFOAM v2512**。

## OpenFOAM 由哪些部分组成

以管道中的水流为例：给出管道尺寸、入口流速、出口压力和水的黏度，OpenFOAM 就能算出网格中每一处的速度和压力。

| 组成 | 作用 | 本课程中的例子 |
| --- | --- | --- |
| 求解器 | 求解特定物理模型的控制方程 | `icoFoam`：不可压缩牛顿流体的瞬态层流 |
| 工具程序 | 生成网格、设置初值、检查和导出数据 | `blockMesh`、`checkMesh`、`foamToVTK` |
| C++ 库 | 提供网格、矩阵、离散算子和物理模型 | `finiteVolume`、各类边界条件 |
| 算例 | 保存一次计算的输入与结果 | 官方 `cavity` 方腔算例 |

![OpenFOAM 的程序、算例与结果](/assets/diagrams/core-architecture.svg)

运行时输入的是求解器的名字；网格、物性和边界条件则保存在算例目录里。同一个求解器可以运行许多不同算例。例如，`icoFoam` 既可以计算顶盖驱动方腔，也可以计算适合其物理假设的其他层流问题。湍流、多相流和可压缩流动则需要相应的求解器与模型。

初学阶段主要是修改算例文件；到二次开发时，才需要编译自己的求解器或边界条件，这部分放在后面的编程课程里。

## 选择运行环境

课程中的命令在 **Linux 的 Bash 终端**执行。Windows 用户可以在 VMware 中安装 Ubuntu，或者使用 WSL2；已经有 Ubuntu 虚拟机的话，直接用它即可。

| 环境 | 使用方式 | 文件建议放置位置 |
| --- | --- | --- |
| Ubuntu 电脑 | 在桌面打开终端 | 用户主目录下 |
| VMware Ubuntu | 在虚拟机内打开终端 | 虚拟机的 Linux 文件系统中 |
| WSL2 Ubuntu | 打开 Ubuntu 终端 | `/home/用户名/` 下 |

计算过程会频繁读写文件，所以工作目录最好放在 Linux 本地，而不是 Windows 共享目录里。共享目录用来传讲义、压缩包和结果图片就好。

已经装好 OpenFOAM 的读者，可以直接跳到“加载运行环境”。还没安装的，建议先用 Ubuntu 软件包安装；源码安装适合需要自己管理编译器、第三方库或修改核心库的读者，初学时不必走这条路。

## 在 Ubuntu 中安装 v2512

下面的命令会添加 OpenFOAM 官方软件源，并安装指定版本。先安装下载工具：

```bash
sudo apt update
sudo apt install curl ca-certificates
```

`sudo` 让这条命令以管理员权限运行；`apt update` 更新软件包索引；`apt install` 安装指定的软件。输入密码时终端不会显示字符，输完按回车即可。

下载并运行官方软件源配置脚本：

```bash
curl -fsSL https://dl.openfoam.com/add-debian-repo.sh \
    -o /tmp/add-openfoam-repo.sh
sudo bash /tmp/add-openfoam-repo.sh
apt-cache policy openfoam2512-default
```

第一条命令把脚本下载到 `/tmp`，第二条运行它，添加软件源和签名密钥；最后一条查询 `openfoam2512-default` 是否可以安装，输出里的 `Candidate` 应该是一个版本号。

确认有可安装的版本后，执行：

```bash
sudo apt install openfoam2512-default
```

软件源是否提供这个包，取决于 Ubuntu 版本和处理器架构。如果 `Candidate` 显示 `(none)`，先检查上一步脚本有没有报错，再查看 [OpenFOAM 安装说明](https://www.openfoam.com/download/openfoam-installation-on-linux) 对当前系统的支持情况。

## 加载运行环境

软件包安装完成后，在终端执行：

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
foamVersion
command -v icoFoam
icoFoam -help
```

这四行命令的作用：

1. `source` 读取环境脚本，让当前终端能找到 OpenFOAM 的程序和动态库。
2. `foamVersion` 显示版本信息，其中应包含 `v2512`。
3. `command -v icoFoam` 显示将要执行的程序路径。
4. `icoFoam -help` 显示求解器用途和可用参数。

`-help` 只显示帮助，不会开始计算。如果你的安装路径不同，把第一行换成自己安装目录下的 `etc/bashrc`；安装方式只影响这一行，后面的命令都一样。

`source` 只对当前终端有效，关掉终端设置就没了。如果一直用这个版本，可以用文本编辑器打开 `~/.bashrc`，在末尾加入：

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
```

`~` 表示当前用户的主目录，例如 `/home/chen`。保存后，新打开的 Bash 终端会自动加载 OpenFOAM。如果电脑上装了多个版本，可以给每个版本定义一个别名，打开新终端后再选择要用的版本：

```bash
alias of2512='source /usr/lib/openfoam/openfoam2512/etc/bashrc'
```

之后输入 `of2512` 就能加载这个版本。一个终端只加载一个版本，可以避免程序和动态库来自不同版本。

## 找到教程与工作目录

OpenFOAM 用环境变量保存常用目录。变量名前的 `$` 表示读取变量的值：

```bash
echo "$WM_PROJECT_DIR"
echo "$FOAM_TUTORIALS"
echo "$FOAM_RUN"
```

`WM_PROJECT_DIR` 是软件的安装根目录；`FOAM_TUTORIALS` 指向软件自带的教程；`FOAM_RUN` 是约定的个人算例目录。`echo` 只是把它们的值打印出来。

为了让后面各课的路径保持一致，本课程把算例统一放在个人目录下：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
```

`HOME` 也是环境变量，表示用户主目录。`mkdir -p` 会顺带创建缺少的上级目录；目录已经存在也不会报错。

官方方腔位于：

```text
$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity
```

路径里有两个 `cavity`，这是官方教程的组织方式：外层是一组方腔练习，内层是最基础的那个算例。下一课会把它复制到个人目录，并介绍查看文件、保存日志和命令选项。

## 常见问题

| 现象 | 常见原因 | 处理方法 |
| --- | --- | --- |
| `icoFoam: command not found` | 当前终端尚未加载环境 | 执行安装目录中的 `source .../etc/bashrc` |
| `source` 提示文件不存在 | 环境脚本路径与安装位置不一致 | 查看 `/usr/lib/openfoam` 中的实际目录名，或自己的源码安装目录 |
| `error while loading shared libraries` | 程序与动态库路径不一致，或依赖缺失 | 新开终端，只加载 v2512；软件包缺失依赖时修复对应包 |
| 普通复制操作出现 `Permission denied` | 正在软件安装目录中创建文件 | 将算例复制到 `$HOME/OpenFOAM/learning-v2512` 后修改 |
| Windows 终端无法识别 `source` | 命令在 PowerShell 中执行 | 打开虚拟机或 WSL2 的 Ubuntu 终端 |

## 动手练习

关掉当前终端，重新打开一个，运行 `foamVersion` 和 `icoFoam -help`。如果加了自动加载，这两个命令应该能直接用；如果用的是别名，先运行 `of2512`。

再执行下面的命令：

```bash
ls "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity"
```

输出中应该有 `0`、`constant` 和 `system` 三个目录，分别存放初始场、物性与网格、计算控制设置。接下来几课会围绕它们完成第一次计算。
