一个 OpenFOAM 算例通常包含 `0`、`constant` 和 `system` 三个目录。求解器从这些目录读取初始场、物性、网格和计算设置，随后把结果写入以时间命名的目录。

## 方腔算例的文件结构

基础方腔的主要文件如下。`constant/polyMesh` 由 `blockMesh` 生成，其余文件随算例提供。

```text
cavity/
├── 0/
│   ├── U                     速度初值与边界条件
│   └── p                     压力初值与边界条件
├── constant/
│   ├── transportProperties   运动黏度
│   └── polyMesh/             体网格
└── system/
    ├── blockMeshDict         生成网格的几何与划分设置
    ├── controlDict           时间、输出频率等运行设置
    ├── fvSchemes             离散格式
    └── fvSolution            线性求解器与 PISO 控制
```

![算例目录结构](/assets/diagrams/core-case-tree.svg)

`0` 对应物理时间为零时的场。运行后出现的 `0.1`、`0.2` 等目录保存相应时刻的场数据。`constant` 保存物性和基础网格；动网格计算还可能在时间目录中写出更新后的网格。`system` 中的设置决定如何生成网格、离散方程、迭代求解和保存结果。

`blockMeshDict` 描述如何生成网格，求解器实际读取的是生成后的 `polyMesh`。这一区别很重要：修改 `blockMeshDict` 后，要重新执行 `blockMesh`，新网格才会生效。

## 字典的基本语法

OpenFOAM 用“关键字与值”组织输入。下面是 `controlDict` 中的几个条目：

```foam
application     icoFoam;
deltaT          0.005;
endTime         0.5;
```

左侧是关键字，右侧是值，末尾用分号结束。空格用于分隔内容，缩进主要方便阅读。`deltaT` 表示时间步长，`endTime` 表示结束时间，二者采用秒。

设置较多时，用花括号组成子字典：

```foam
PISO
{
    nCorrectors                 2;
    nNonOrthogonalCorrectors     0;
    pRefCell                    0;
    pRefValue                   0;
}
```

这段位于 `fvSolution` 中，所有条目都属于 `PISO`。子字典结束的花括号通常不需要分号；子字典内部的普通条目仍然需要分号。

常见符号有以下用途：

| 符号 | 用途 | 示例 |
| --- | --- | --- |
| `;` | 结束一个条目 | `deltaT 0.005;` |
| `{ }` | 包围子字典 | `PISO { ... }` |
| `( )` | 向量或列表 | `(1 0 0)` |
| `[ ]` | 物理量的量纲指数 | `[0 1 -1 0 0 0 0]` |
| `//` | 单行注释 | `// time step` |
| `/* ... */` | 多行注释 | 文件开头的说明块 |

## 读懂一个完整的速度场文件

下面是方腔的完整 `0/U`，省略了开头和末尾的装饰性注释：

```foam
FoamFile
{
    version     2.0;
    format      ascii;
    class       volVectorField;
    object      U;
}

dimensions      [0 1 -1 0 0 0 0];
internalField   uniform (0 0 0);

boundaryField
{
    movingWall
    {
        type    fixedValue;
        value   uniform (1 0 0);
    }
    fixedWalls
    {
        type    noSlip;
    }
    frontAndBack
    {
        type    empty;
    }
}
```

`FoamFile` 是文件头。`version 2.0` 指文件格式版本；软件版本由运行环境决定。`format ascii` 表示文本格式，便于直接编辑。`class volVectorField` 表示定义在体网格上的向量场，`object U` 是该场的名字。

`internalField uniform (0 0 0)` 将所有单元的初始速度设为零。`uniform` 表示每个单元采用相同值，括号中的三个数依次为 $x$、$y$、$z$ 方向的速度分量，单位为米每秒。

`boundaryField` 给出边界条件：顶盖速度为 $(1,0,0)$，其余实体壁面无滑移，前后面采用二维 `empty` 条件。计算开始后，顶盖驱动内部流体，单元速度会随方程求解而改变。

当每个单元的值不同时，OpenFOAM 使用 `nonuniform` 列表存储。求解器写出的结果常见这种形式，列表长度与网格单元数有关。手工建立简单初场时使用 `uniform` 更方便；复杂空间分布可以通过 `setFields` 等工具生成。

## 量纲怎样读

`dimensions` 中的七个数依次是质量、长度、时间、温度、物质的量、电流和发光强度的指数。例如速度为 $LT^{-1}$，因此写成：

```foam
dimensions [0 1 -1 0 0 0 0];
```

![基本量纲的排列](/assets/diagrams/core-dimensions.svg)

| 物理量 | 量纲 | OpenFOAM 写法 |
| --- | --- | --- |
| 速度 $U$ | $LT^{-1}$ | `[0 1 -1 0 0 0 0]` |
| 运动黏度 $\nu$ | $L^2T^{-1}$ | `[0 2 -1 0 0 0 0]` |
| 动力黏度 $\mu$ | $ML^{-1}T^{-1}$ | `[1 -1 -1 0 0 0 0]` |
| 压力 $p_{\mathrm{phys}}$ | $ML^{-1}T^{-2}$ | `[1 -1 -2 0 0 0 0]` |
| 运动学压力 $p_{\mathrm{phys}}/\rho$ | $L^2T^{-2}$ | `[0 2 -2 0 0 0 0]` |

`icoFoam` 的 `p` 是运动学压力。密度为常数时，物理压力差可由下式换算：

$$
\Delta p_{\mathrm{phys}}=\rho\,\Delta p.
$$

例如 $\rho=1000\,\mathrm{kg/m^3}$，两个位置的 `p` 相差 $0.02\,\mathrm{m^2/s^2}$，对应的物理压差为 $20\,\mathrm{Pa}$。压力的绝对零点还取决于参考压力设置。

方腔的 `transportProperties` 使用简写：

```foam
nu 0.01;
```

`icoFoam` 在读取 `nu` 时指定了运动黏度量纲，所以简写中的单位是 $\mathrm{m^2/s}$。也可显式写成：

```foam
nu [0 2 -1 0 0 0 0] 0.01;
```

显式量纲便于检查。若误填成动力黏度的量纲，程序会报告量纲不匹配；若量纲正确而数值填错，仍需通过物性数据和雷诺数判断。

## 文件包含与设置复用

较大的算例会把公共设置放进独立文件，再通过 `#include` 引入。例如：

```foam
#include "meshQualityDict"
```

引入的文件在这里作为字典的一部分读取。复制和分享算例时，应保留被包含的文件。

方腔的 `fvSolution` 还包含这种写法：

```foam
pFinal
{
    $p;
    relTol 0;
}
```

`$p;` 复用同级 `p` 子字典中的条目，然后用 `relTol 0` 覆盖相对容差。这样普通压力校正与最后一次校正可以共用同一个线性求解器，而最后一次采用更严格的停止条件。

## 读取、修改与排错

用 `foamDictionary` 查看条目：

```bash
foamDictionary 0/U -entry dimensions -value
foamDictionary 0/U -entry boundaryField/movingWall/value -value
foamDictionary system/controlDict -entry deltaT -value
```

斜杠分隔子字典层级。第二条命令依次进入 `boundaryField`、`movingWall`，读取其中的 `value`。

在算例副本中，将时间步改为 `0.0025`：

```bash
foamDictionary system/controlDict -entry deltaT -set 0.0025
foamDictionary system/controlDict -entry deltaT -value
```

`-set` 会直接改写文件，第二条命令可立即查看新值。后续采用 `writeControl timeStep` 时，减小时间步也会改变同一写出间隔对应的物理时间，下一课之后会具体讨论。

| 报错或现象 | 检查位置 |
| --- | --- |
| `unexpected token` 或读到文件末尾 | 上一个条目是否缺少分号、括号是否配对 |
| `keyword ... is undefined` | 关键字是否拼错、是否放进了错误的子字典 |
| `inconsistent dimensions` | 输入量纲与方程要求是否一致 |
| 找不到 `#include` 文件 | 引入文件的相对位置和文件名 |

## 动手练习

读取 `0/U`、`0/p` 和 `constant/transportProperties`，找出速度、运动学压力和运动黏度的量纲。随后把 `nu` 改成带量纲的完整写法，数值仍为 `0.01`。这种修改保持物理设置不变。

再把 `0/U` 中顶盖的速度改为 `(0.5 0 0)`，并用 `foamDictionary` 读出结果。此时改变的是顶盖运动速度，内部流体的初始速度仍由 `internalField` 决定。下一课将用这些文件运行方腔，观察流体如何从静止状态发展起来。
