---
title: "快速开始"
layout: page
section: start
description: "用方腔算例练习环境加载、网格生成、求解与结果查看。"
cms_slug: "site-start"
---

用 OpenFOAM 做一次计算，一般分四步：准备文件、生成网格、运行求解器、查看结果。这一页用顶盖驱动方腔，带你把这四步走一遍。

## 加载环境

以下命令都在 Linux 终端里运行。还没安装的话，先看[安装课程](/read/?slug=start-openfoam-v2512)；第一次用终端，可以从 [Linux 入门](/linux/)开始。

```bash
source /usr/lib/openfoam/openfoam2512/etc/bashrc
echo "$WM_PROJECT_VERSION"
icoFoam -help
```

第一行对应 Ubuntu 软件包的默认安装路径，装在别处的话，换成实际的 `etc/bashrc`。第二行应输出 `v2512`；第三行显示方腔所用求解器 `icoFoam` 的参数。

## 复制方腔算例

```bash
mkdir -p "$FOAM_RUN"
cd "$FOAM_RUN"
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
ls
```

`cp -r` 复制整个目录，`cavity-first` 是这次练习的名字（用过的话就换一个）。复制后能看到三个主要目录：

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

`blockMesh` 按 `system/blockMeshDict` 生成 $20\times20\times1$ 个单元，`checkMesh` 再检查网格的连接和几何，正常的话输出里会有 `Mesh OK`。

![方腔网格](/assets/science/cavity-mesh.png)

这是一个二维方腔：厚度方向只有一层单元，前后边界设为 `empty`；顶盖以 $1\,\mathrm{m/s}$ 向右运动，其余壁面静止。

## 运行计算

```bash
icoFoam > log.icoFoam 2>&1
tail -n 20 log.icoFoam
```

第一行运行求解器，把输出和错误信息都存进 `log.icoFoam`；算完后，第二行显示日志的最后 20 行。计算到 $0.5\,\mathrm{s}$ 结束，结果按 `controlDict` 中的写出间隔存进各个时间目录。

日志中，`Time` 是当前时刻，`Solving for` 后面是正在求解的场，`Initial residual` 和 `Final residual` 是线性方程求解前后的残差。每一项的具体含义，[方腔课程](/read/?slug=first-cavity-result)里会详细解释。

## 查看速度场

```bash
paraFoam -builtin
```

在 ParaView 中点 **Apply**，切换到最后一个时刻，着色选 **U → Magnitude**，就能看到顶盖带动的回流。

![方腔速度大小](/assets/science/cavity-velocity.png)

如果在没有图形界面的服务器上计算，可以先建一个读取入口文件，再把整个算例复制到装有 ParaView 的电脑上：

```bash
touch cavity.foam
```

打开 `cavity.foam` 时，同目录下的网格和结果文件要一起带上。

## 接着学什么

- [算例结构与字典语法](/read/?slug=case-structure-dimensions)：看懂文件中的条目、列表和量纲。
- [顶盖驱动方腔](/read/?slug=first-cavity-result)：解释边界、雷诺数和计算结果。
- [blockMesh](/read/?slug=blockmesh-first-principles)：修改网格并比较结果。
- [C++ 入门](/cpp/)：为自定义 OpenFOAM 程序准备基础。
