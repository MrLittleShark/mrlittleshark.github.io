OpenFOAM 的大部分操作都在终端里完成：进入算例目录、查看输入文件、运行程序、保存日志。本课用方腔算例把这些操作练一遍，最后再看看源码放在哪里。

## 目录与路径

终端总有一个“当前目录”。`pwd` 显示它的完整路径，`ls` 列出其中的文件：

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

Linux 区分大小写，`U` 和 `u` 是两个不同的文件。路径用正斜杠 `/` 分隔；含空格或环境变量的路径要加双引号，否则可能被拆成好几个参数。

## 复制一个工作算例

在已加载 OpenFOAM 环境的终端执行：

```bash
mkdir -p "$HOME/OpenFOAM/learning-v2512"
cd "$HOME/OpenFOAM/learning-v2512"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
ls
```

`cp` 的第一个参数是源目录，第二个是目标目录；`-r` 表示连同子目录一起复制。这样就得到了新算例 `cavity-first`，官方教程原封不动，以后可以再复制或拿来对照。

这条命令要求目标目录事先不存在。再次练习时换个名字，比如 `cavity-second`：如果 `cavity-first` 已经存在，`cp -r` 会把源目录复制到它里面，多出一层目录。

在算例根目录执行 `ls`，应该看到：

```text
0  constant  system
```

课程下载包里也有这个官方算例，解压后进入 `tutorials/incompressible/icoFoam/cavity/cavity`，同样可以完成下面的操作。

## 查看文件和搜索条目

计算设置在 `system/controlDict` 里。用 `cat` 查看整个文件：

```bash
cat system/controlDict
```

文件较长时使用 `less`，按方向键滚动，按 `/` 输入关键词搜索，按 `q` 退出：

```bash
less system/controlDict
```

只想找包含某个关键词的行，用 `grep`：

```bash
grep -n 'endTime' system/controlDict
grep -n 'movingWall' 0/U
```

`-n` 让结果带上行号；单引号保证关键词作为一个整体传给命令。如果要读字典条目的值，`foamDictionary` 比文本搜索更直接：

```bash
foamDictionary system/controlDict -entry application -value
foamDictionary system/controlDict -entry deltaT -value
```

输出应分别为 `icoFoam` 和 `0.005`。`-entry` 指定要读的条目，`-value` 只输出它的值，很适合在脚本里用。

## 运行程序与指定算例

`blockMesh` 根据 `system/blockMeshDict` 生成体网格。进入 `cavity-first` 后运行：

```bash
blockMesh
```

程序默认读取当前目录下的算例；在别的目录，也可以用 `-case` 指定算例路径：

```bash
blockMesh -case "$HOME/OpenFOAM/learning-v2512/cavity-first"
```

两种写法读取的是同一份字典，运行后网格都会出现在 `constant/polyMesh` 里。注意，再次运行 `blockMesh` 会覆盖已有网格；要比较不同参数，请在不同的算例副本里分别运行。

忘了某个命令有哪些选项，可以查帮助：

```bash
blockMesh -help
blockMesh -help-full
```

`-help` 列出常用选项，`-help-full` 列出全部。一条命令一般由“程序名 + 选项 + 选项值”组成，比如 `blockMesh -case cavity-first` 中，`-case` 后面跟的就是目录。

## 保存和阅读日志

计算时间较长时，最好把终端输出保存到文件里，方便回头查看：

```bash
blockMesh > log.blockMesh 2>&1
echo $?
tail -n 20 log.blockMesh
```

`>` 把标准输出写进文件（会覆盖同名旧文件）；`2>&1` 把错误信息也写进同一个文件；`$?` 是上一条命令的退出码，`0` 一般表示正常结束。`tail -n 20` 显示日志的最后 20 行。

退出码要紧接着查看，因为之后运行的 `cat`、`ls` 也会改写 `$?`。除了退出码，还要在日志里核对网格规模、结束时间等内容。

想一边在屏幕上看、一边保存日志，可以用管道加 `tee`：

```bash
set -o pipefail
checkMesh 2>&1 | tee log.checkMesh
```

管道 `|` 把左边程序的输出交给右边的程序；`tee` 一边打印一边写文件；`pipefail` 保证左边程序失败时，整条管道也返回失败。后面写自动运行脚本时会用到这种写法。

计算运行期间，在另一个终端进入同一算例目录，执行：

```bash
tail -f log.icoFoam
```

`-f` 会持续显示新写入的内容。按 `Ctrl+C` 只是停止跟踪日志，另一个终端里的求解器照常运行。

## 程序和源码分别在哪里

![程序、源码与算例的关系](/assets/diagrams/core-architecture.svg)

使用和开发时，最常打交道的是这几个位置：

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

第一行显示实际执行的程序文件，第二行列出源码目录。源码目录里有 `icoFoam.C`、`createFields.H` 和 `Make`：主程序在 `.C` 文件里，`createFields.H` 负责读入速度、压力和黏度，`Make` 里是编译设置。有些精简安装没有附带源码，这时可以到官方源码包里找同样的文件。

## 简单脚本怎样工作

如果要反复生成和检查网格，可以在算例根目录新建 `run-mesh.sh`：

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

第一行指定用 Bash 运行；`set -e` 让脚本在任一命令失败时停下；`-u` 在用到未定义变量时报错；`pipefail` 检查管道里每个程序的退出状态。`$0` 是脚本自身的路径，`dirname` 取出它所在的目录，所以即使从别的目录启动，脚本也会先进入正确的算例。

## 排错与练习

遇到 `cannot find file .../system/controlDict`，先看报错里的路径：多了或少了一层目录，就用 `pwd`、`ls` 和 `-case` 调整。遇到 `No such file or directory`，核对文件名大小写，并确认复制是否成功。改完文件后出现 `FOAM FATAL IO ERROR`，按报错给出的文件和行号去找，最常见的原因是漏了分号或括号。

最后做个小练习：在 `learning-v2512` 目录运行 `blockMesh -case cavity-first`，再进入 `cavity-first` 运行 `checkMesh` 并保存日志。两份日志应该对应同一个算例，网格统计里应有 400 个单元。做到这一步，说明路径、程序调用和日志保存都没问题了。
