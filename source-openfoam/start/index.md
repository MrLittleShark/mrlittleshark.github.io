---
title: 快速开始
layout: page
description: 检查 v2512 环境，复制并运行第一个方腔流动算例。
---

先完成一次“复制算例 → 生成网格 → 检查网格 → 求解 → 查看结果”，再逐步理解每个配置文件。

## 1 确认软件分支与环境

本站使用 **openfoam.com 分支的 OpenFOAM v2512**。不同分支的版本号、求解器和字典名称可能不同，请先核对实际环境。Windows 用户可在 WSL2 的 Ubuntu 中进行操作；下面的命令在 Linux Bash 终端执行。

还没有安装时，从 [v2512 官方发布页面](https://www.openfoam.com/news/main-news/openfoam-v2512) 选择适合系统的安装包，或查阅 [v2512 官方下载目录](https://dl.openfoam.com/source/v2512/)。安装位置取决于所用安装方式。

```bash
# 适用于安装在此目录的 Ubuntu 软件包；其他安装方式请改成实际路径
source /usr/lib/openfoam/openfoam2512/etc/bashrc
foamVersion
echo "$WM_PROJECT_DIR"
echo "$FOAM_TUTORIALS"
icoFoam -help
```

**检查结果：**版本信息应包含 `2512`，教程路径存在，`icoFoam -help` 能正常显示帮助。遇到 `command not found` 时，先检查环境脚本的位置与当前终端，不要直接修改算例文件。

## 2 复制方腔算例

在加载环境的同一个终端中执行。下面使用一个新目录保存本次练习，避免覆盖已有计算。

```bash
mkdir -p "$FOAM_RUN"
cd "$FOAM_RUN"
# 如果 cavity-first 已存在，请换一个新的目标名称
cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" cavity-first
cd cavity-first
pwd
ls 0 constant system
```

**检查结果：**当前目录应为自己的 `cavity-first`，并包含 `0`、`constant` 和 `system`。如果官方教程路径不存在，先用 `find "$FOAM_TUTORIALS" -path '*/icoFoam/*/system/controlDict'` 查找本机教程位置。

<div class="directory-map"><a href="/reference/guide-19/"><code>0/</code><h3>初始场与边界</h3><p>速度 U、压力 p</p></a><a href="/reference/guide-18/"><code>constant/</code><h3>物性与网格</h3><p>黏度、polyMesh</p></a><a href="/reference/guide-12/"><code>system/</code><h3>计算控制</h3><p>网格字典、格式与求解设置</p></a></div>

## 3 生成网格并检查

逐条运行，确认前一步成功后再执行下一条。

```bash
blockMesh > log.blockMesh 2>&1
tail -n 15 log.blockMesh
checkMesh > log.checkMesh 2>&1
tail -n 25 log.checkMesh
```

**检查结果：**网格生成正常结束，`checkMesh` 报告 `Mesh OK`。出现 `FOAM FATAL ERROR` 或网格失败项时，先阅读错误前后的日志，修正后再开始求解。

## 4 求解与查看结果

```bash
icoFoam > log.icoFoam 2>&1
tail -n 20 log.icoFoam
paraFoam -builtin
```

日志正常结束时通常包含 `End`。在 ParaView 中点击 **Apply**，选择速度 `U` 或压力 `p`，切换到最后保存的时刻。先观察网格和边界，再用流线或矢量观察方腔中的回流。

若当前环境不能打开图形窗口，可执行 `touch case.foam`，在能访问同一算例目录的 ParaView 中打开此文件；也可用 `foamToVTK -latestTime` 导出。`.foam` 文件只是读取入口，查看结果时还需要同目录下的网格与场数据。

## 5 第一次练习

1. 记录版本号、算例路径和实际执行的命令。
2. 找出 `system/controlDict` 中的终止时间和时间步长。
3. 保存一张网格图、一张速度图，并解释顶盖与其他壁面的区别。
4. 在副本中改变一个参数，重新计算并记录结果变化。

这些步骤说明学习操作流程，本站建设过程中未在当前 Windows 环境重新运行该算例。结果判断应以自己的计算日志为准。

<a class="button" href="/lessons/01/">进入第 01 讲 →</a> <a class="button secondary" href="/community/">遇到问题，去答疑区</a>
