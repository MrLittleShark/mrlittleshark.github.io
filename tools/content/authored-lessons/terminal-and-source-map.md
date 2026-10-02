OpenFOAM 的大部分操作通过终端完成。常用命令主要用于进入算例目录、查看输入文件、运行程序和保存日志。本课以方腔算例为例，介绍这些操作以及源码的存放位置。

## 目录与路径

终端始终有一个当前目录。执行 `pwd` 可以查看其完整路径，执行 `ls` 可以列出目录中的文件：

```bash
pwd
ls
```

路径有两种常见写法：

| 写法 | 示例 | 含义 |
| --- | --- | --- |
| 绝对路径 | `/home/chen/OpenFOAM/learning-v2512` | 从文件系统根目录 `/` 开始定位 |
| 相对路径 | `system/controlDict` | 从当前目录开始定位 |

`cd` 切换目录；`..` 表示上一级目录；`~` 表示用户主目录。例如：

```bash
cd "$HOME/OpenFOAM/learning-v2512"
cd ..
cd ~
```

Linux 区分大小写，`U` 和 `u` 是不同文件。路径使用正斜杠 `/`；包含空格或环境变量的路径放在双引号中，可以避免路径被拆成多个参数。

## 复制一个工作算例

在已加载 OpenFOAM 环境的终端执行：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
ls
```

`cp` 的前一个参数是源目录，后一个参数是目标目录；`-r` 表示连同子目录一起复制。这里得到的新算例名为 `cavity-first`。官方教程保留在原处，以后可以再次复制或用于比较。

以上写法适用于目标目录尚不存在的情况。再次练习时可以使用 `cavity-second` 等新名称：如果 `cavity-first` 已存在，`cp -r` 可能把源目录复制到它的内部，形成额外的一层目录。

在正确的算例根目录中执行 `ls`，应看到：

```text
0  constant  system
```

课程下载包也包含同一个官方算例。解压后进入包内的 `tutorials/incompressible/icoFoam/cavity/cavity`，同样可以完成下面的操作。

## 查看文件和搜索条目

计算设置保存在 `system/controlDict`。查看整个文件可用 `cat`：

```bash
cat system/controlDict
```

文件较长时使用 `less`，按方向键滚动，按 `/` 输入关键词搜索，按 `q` 退出：

```bash
less system/controlDict
```

只查找包含某个关键词的行，可用 `grep`：

```bash
grep -n 'endTime' system/controlDict
grep -n 'movingWall' 0/U
```

`-n` 在结果前显示行号。单引号把关键词作为一段完整文本传给命令。对于字典条目的值，`foamDictionary` 比文本搜索更直接：

```bash
foamDictionary system/controlDict -entry application -value
foamDictionary system/controlDict -entry deltaT -value
```

输出应分别为 `icoFoam` 和 `0.005`。`-entry` 指定要读取的条目，`-value` 只输出该条目的值，适合在脚本中使用。

## 运行程序与指定算例

`blockMesh` 根据 `system/blockMeshDict` 生成体网格。进入 `cavity-first` 后运行：

```bash
blockMesh
```

程序默认读取当前目录中的算例。也可以从其他目录用 `-case` 指定路径：

```bash
blockMesh -case "$HOME/OpenFOAM/learning-v2512/cavity-first"
```

两条命令对同一目录操作时读取相同的字典。执行后，网格文件出现在 `constant/polyMesh` 中。对已有网格运行 `blockMesh` 会重新生成该网格，做参数比较时应在不同算例副本中运行。

命令选项可以通过帮助查找：

```bash
blockMesh -help
blockMesh -help-full
```

`-help` 给出常用选项，`-help-full` 显示更完整的帮助。通常一条命令由“程序名、选项、选项值”组成，例如 `blockMesh -case cavity-first` 中的 `-case` 就需要一个目录参数。

## 保存和阅读日志

运行较长的计算时，把终端输出保存下来更便于查看：

```bash
blockMesh > log.blockMesh 2>&1
echo $?
tail -n 20 log.blockMesh
```

`>` 将标准输出写入文件，并覆盖同名旧文件；`2>&1` 将错误信息写入同一文件；`$?` 是刚刚结束的命令的退出码，通常 `0` 表示正常结束。`tail -n 20` 显示日志最后 20 行。

查看退出码应紧接着运行命令，因为后续的 `cat`、`ls` 等操作也会更新 `$?`。日志中还应检查实际生成的网格规模、计算结束时间等内容。

希望同时在屏幕显示并保存日志，可以使用管道和 `tee`：

```bash
set -o pipefail
checkMesh 2>&1 | tee log.checkMesh
```

管道 `|` 将左侧程序的输出送给右侧程序。`tee` 一边打印，一边写入文件；`pipefail` 使左侧程序失败时，整条管道也能返回失败状态。这种写法适合后续的自动运行脚本。

计算运行期间，在另一个终端进入同一算例目录，执行：

```bash
tail -f log.icoFoam
```

`-f` 会持续显示新追加的内容。按 `Ctrl+C` 结束日志跟踪；原求解器在另一个终端继续运行。

## 程序和源码分别在哪里

![程序、源码与算例的关系](/assets/diagrams/core-architecture.svg)

下面几个位置在使用和开发时最常见：

| 位置 | 保存的内容 |
| --- | --- |
| `$FOAM_APPBIN` | 已编译的标准可执行程序 |
| `$FOAM_USER_APPBIN` | 用户自行编译的可执行程序 |
| `$WM_PROJECT_DIR/applications/solvers` | 求解器源码 |
| `$WM_PROJECT_DIR/applications/utilities` | 工具程序源码 |
| `$WM_PROJECT_DIR/src` | 网格、有限体积、物性和边界条件等库源码 |
| `$WM_PROJECT_DIR/etc` | 环境设置和通用配置模板 |
| `$FOAM_TUTORIALS` | 官方教程算例 |

以 `icoFoam` 为例：

```bash
command -v icoFoam
ls "$WM_PROJECT_DIR/applications/solvers/incompressible/icoFoam"
```

第一行给出实际执行的二进制文件，第二行列出源码目录。源码包中可看到 `icoFoam.C`、`createFields.H` 和 `Make` 目录：主程序在 `.C` 文件中；`createFields.H` 读取速度、压力和黏度；`Make` 保存编译设置。部分精简安装将源码拆成单独软件包，这时可从官方源码包中阅读相同文件。

## 简单脚本怎样工作

反复运行网格生成与检查时，可以在算例根目录创建 `run-mesh.sh`，内容如下：

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
blockMesh > log.blockMesh 2>&1
checkMesh > log.checkMesh 2>&1
```

运行方式是：

```bash
bash run-mesh.sh
```

首行指定 Bash；`set -e` 在命令失败时停止脚本；`-u` 发现未定义变量时报错；`pipefail` 检查管道中各程序的退出状态。`$0` 是脚本路径，`dirname` 取出它所在目录，因此从其他目录启动脚本也会进入正确的算例。

## 排错与练习

遇到 `cannot find file .../system/controlDict`，先检查报错中的路径。如果多出或缺少一层目录，用 `pwd`、`ls` 和 `-case` 修正位置。遇到 `No such file or directory`，核对文件名大小写以及复制是否成功。编辑文件后出现 `FOAM FATAL IO ERROR`，检查报错给出的文件与行号，常见原因是缺少分号或括号。

最后，从 `learning-v2512` 目录运行一次 `blockMesh -case cavity-first`，再进入 `cavity-first` 运行 `checkMesh` 并保存日志。两份日志应指向同一个算例；网格统计应包含 400 个单元。这样即可确认路径、程序调用和日志保存都已正确配合。
