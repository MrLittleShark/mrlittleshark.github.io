OpenFOAM 的一次计算通常包括准备文件、生成网格、运行求解器和查看结果。这里用顶盖驱动方腔完成这四步。

## 加载环境

以下命令在 Linux 终端运行。还未安装时，先阅读[安装课程](/read/?slug=start-openfoam-v2512)；第一次接触终端，可以从 [Linux 入门](/linux/)开始。

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
echo "$WM_PROJECT_VERSION"
icoFoam -help
```

第一行适用于安装到该路径的 Ubuntu 软件包。其他安装位置请替换为实际的 `etc/bashrc`。第二行应输出 `v2512`；第三行显示方腔所用求解器的参数。

## 复制方腔算例

```bash
mkdir -p "$FOAM_RUN"
cd "$FOAM_RUN"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
ls
```

`cp -r` 复制整个目录，`cavity-first` 是本次练习的名称。若已经用过这个名称，换一个新名称。复制后可以看到三个主要目录：

| 目录 | 本例包含什么 |
| --- | --- |
| `0` | 速度 `U`、压力 `p` 的初值与边界条件 |
| `constant` | 流体黏度；生成网格后还会出现 `polyMesh` |
| `system` | 网格描述、离散格式、线性求解和时间控制 |

## 生成网格

```bash
blockMesh
checkMesh
```

`blockMesh` 按 `system/blockMeshDict` 生成 $20\times20\times1$ 个单元。`checkMesh` 随后检查连接与几何，正常输出包含 `Mesh OK`。

![方腔网格](/assets/science/cavity-mesh.png)

本例是二维方腔。厚度方向只有一层单元，前后边界设置为 `empty`；顶盖以 $1\,\mathrm{m/s}$ 沿水平方向运动，其余壁面静止。

## 运行计算

```bash
icoFoam > log.icoFoam 2>&1
tail -n 20 log.icoFoam
```

第一行运行求解器，把输出与错误信息保存到 `log.icoFoam`。程序结束后，第二行显示日志最后 20 行。计算至 $0.5\,\mathrm{s}$，结果按 `controlDict` 中的写出间隔保存在时间目录中。

日志中的 `Time` 是当前时刻，`Solving for` 后是所求的场，`Initial residual` 和 `Final residual` 是线性方程求解前后的残差。各项的计算含义在[方腔课程](/read/?slug=first-cavity-result)中展开。

## 查看速度场

```bash
paraFoam -builtin
```

在 ParaView 中点击 **Apply**，切换到最后一个时刻，着色字段选择 **U → Magnitude**。可以看到顶盖驱动的回流。

![方腔速度大小](/assets/science/cavity-velocity.png)

若计算在无图形界面的服务器上进行，可创建读取入口，再把算例复制到安装了 ParaView 的电脑：

```bash
touch cavity.foam
```

打开 `cavity.foam` 时，保留同目录下的网格和结果文件。

## 接着学什么

- [算例结构与字典语法](/read/?slug=case-structure-dimensions)：看懂文件中的条目、列表和量纲。
- [顶盖驱动方腔](/read/?slug=first-cavity-result)：解释边界、雷诺数和计算结果。
- [blockMesh](/read/?slug=blockmesh-first-principles)：修改网格并比较结果。
- [C++ 入门](/cpp/)：为自定义 OpenFOAM 程序准备基础。
