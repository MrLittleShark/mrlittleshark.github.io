---
title: functionObject 配置方法
layout: reference
section: function-objects
description: 在 controlDict 中添加功能对象，设置输入字段、运行频率和输出位置。
---

functionObject 在求解过程中完成场运算、采样、统计和结果输出。例如 `probes` 记录测点压力，`forces` 积分壁面载荷，`mag` 把速度向量转换为速度大小。一个算例可以同时配置多个对象。

## 1. 在 controlDict 中添加对象

在已有算例的 `system/controlDict` 中找到 `functions`，加入下面的对象：

```foam
functions
{
    speed
    {
        type            mag;
        libs            (fieldFunctionObjects);
        field           U;
        result          speed;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval   1;
    }
}
```

`speed` 是对象名；`type mag` 选择求模运算。输入为速度场 `U`，输出为标量场 `speed`。每一步更新结果，在求解器保存完整场时同时保存它。运行原算例的求解器后，时间目录中会出现 `speed`，可在 ParaView 中选择该场查看速度云图。

## 2. 把对象放在单独文件

对象较多时，可以把 `functions` 内的对象放到 `system/functions` 中，主文件保留：

```foam
functions
{
    #include "functions"
}
```

这里的 `system/functions` 直接从 `speed { ... }` 这样的对象开始写。若原算例已经使用这一方式，就在已有的 `system/functions` 中添加新对象。

## 3. 对已有结果执行后处理

对于只依赖已保存字段的运算，可以使用 `postProcess`。例如处理已保存的速度场：

```bash
# 最新时刻的速度大小
postProcess -func 'mag(U)' -latestTime

# 指定时间区间的速度梯度
postProcess -func 'grad(U)' -time '0.1:0.5'

# 指定算例的涡量
postProcess -case ../cavity -func vorticity -latestTime
```

这些命令调用已安装的预配置模板。需要修改输出名或更多参数时，使用完整字典。以另存的 `system/myPostProcess` 为例，文件内放置一个 `functions { ... }` 字典，然后运行：

```bash
postProcess -dict system/myPostProcess -fields '(U p)' -latestTime
```

`forces`、`yPlus` 等需要动量或湍流模型的工具，通常随求解器运行最方便。求解器提供 `-postProcess` 接口时，也可由该求解器建立所需模型后执行，例如：

```bash
simpleFoam -postProcess -dict system/myPostProcess -latestTime
```

## 4. 常用参数

| 参数 | 设置方法 | 作用 |
|---|---|---|
| `type` | `probes`、`forces` 等类型名 | 选择功能对象 |
| `libs` | 例如 `(sampling)`、`(forces)` | 加载对应共享库 |
| `enabled` | `true` 或 `false` | 启用或暂时停用对象 |
| `region` | 默认 `region0`，或填写区域名 | 基于网格的对象选择工作区域 |
| `executeControl` | `timeStep`、`writeTime`、`runTime` 等 | 何时计算或更新 |
| `executeInterval` | 与执行方式配套的数值 | 执行间隔 |
| `writeControl` | `timeStep`、`writeTime`、`runTime` 等 | 何时保存结果 |
| `writeInterval` | 与写出方式配套的数值 | 保存间隔 |
| `timeStart` / `timeEnd` | 模拟时间 | 工作时间范围 |

`timeStep` 的间隔是步数；`runTime` 的间隔是模拟时间；`writeTime` 跟随主计算的保存时刻。`onEnd` 在计算结束时调用，`none` 关闭对应调度。还有按实际耗时触发的 `clockTime`、`cpuTime`，以及参与输出时间对齐的 `adjustableRunTime`。

例如平均场应每步累积，而文件可以每十步保存一次：

```foam
executeControl  timeStep;
executeInterval 1;
writeControl    timeStep;
writeInterval   10;
```

## 5. 查看输出

| 输出内容 | 常见位置 | 查看方式 |
|---|---|---|
| 速度模、梯度等场 | 算例的时间目录 | ParaView 中选择相应字段 |
| 探针时序与统计值 | `postProcessing/对象名/起始时间/` | 文本、Python 或其他绘图工具 |
| VTK、EnSight 等导出文件 | 工具的输出目录 | 用对应格式读取器打开 |
| 运行信息与诊断 | 求解日志 | 按对象名搜索 |

多个对象有输入依赖时，按生成顺序排列。例如先用 `mag` 生成 `speed`，再让 `histogram` 统计 `speed` 的分布。时间平均等对象需要连续采样，统计区间和执行频率应在计算前设好。

[返回 functionObject 速查](/function-objects/)
