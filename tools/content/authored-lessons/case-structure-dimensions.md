一个 OpenFOAM 算例通常包含 `0`、`constant` 和 `system` 三个目录。求解器从中读取初始场、物性、网格和计算设置，算完再把结果写进以时间命名的目录。

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

`0` 目录存放 $t=0$ 时刻的场；运行后出现的 `0.1`、`0.2` 等目录，存放对应时刻的结果。`constant` 存放物性和网格（动网格计算还会把更新后的网格写进时间目录）。`system` 里的设置决定怎样生成网格、离散方程、迭代求解和保存结果。

要特别注意：`blockMeshDict` 只是生成网格的“说明书”，求解器真正读取的是生成出来的 `polyMesh`。所以改了 `blockMeshDict` 之后，必须重新运行 `blockMesh`，新网格才会生效。

## 字典的基本语法

OpenFOAM 用“关键字与值”组织输入。下面是 `controlDict` 中的几个条目：

```foam
application     icoFoam;
deltaT          0.005;
endTime         0.5;
```

左边是关键字，右边是值，以分号结尾。空格只起分隔作用，缩进是为了好读。`deltaT` 是时间步长，`endTime` 是结束时间，单位都是秒。

设置较多时，用花括号把相关条目组成子字典：

```foam
PISO
{
    nCorrectors                 2;
    nNonOrthogonalCorrectors     0;
    pRefCell                    0;
    pRefValue                   0;
}
```

这段来自 `fvSolution`，花括号里的条目都属于 `PISO`。子字典的右花括号后面不用加分号，但里面每个普通条目仍要以分号结尾。

常见符号的含义：

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

`FoamFile` 是文件头。`version 2.0` 是文件格式的版本，与软件版本无关。`format ascii` 表示文本格式，便于直接编辑。`class volVectorField` 表示定义在体网格上的向量场，`object U` 是该场的名字。

`internalField uniform (0 0 0)` 将所有单元的初始速度设为零。`uniform` 表示每个单元采用相同值，括号中的三个数依次为 $x$、$y$、$z$ 方向的速度分量，单位为米每秒。

`boundaryField` 给出边界条件：顶盖速度为 $(1,0,0)$，其余壁面无滑移，前后面用 `empty` 表示二维。计算开始后，顶盖带动内部流体，单元里的速度会随着求解不断变化。

如果各单元的值不同，就用 `nonuniform` 列表逐个存储，求解器写出的结果大多是这种形式，列表长度等于单元数。手工设置简单初场时用 `uniform` 最方便；复杂的空间分布可以用 `setFields` 等工具生成。

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

`icoFoam` 的 `p` 是运动学压力，即压力除以密度。密度为常数时，可以这样换算回物理压差：

$$
\Delta p_{\mathrm{phys}}=\rho\,\Delta p.
$$

例如 $\rho=1000\,\mathrm{kg/m^3}$，两个位置的 `p` 相差 $0.02\,\mathrm{m^2/s^2}$，对应的物理压差为 $20\,\mathrm{Pa}$。至于压力的绝对值，还取决于参考压力的设置。

方腔的 `transportProperties` 使用简写：

```foam
nu 0.01;
```

`icoFoam` 读取 `nu` 时已经规定了它的量纲，所以简写的单位就是 $\mathrm{m^2/s}$。也可以把量纲显式写出来：

```foam
nu [0 2 -1 0 0 0 0] 0.01;
```

写出量纲便于检查：如果误写成动力黏度的量纲，程序会报“量纲不匹配”。但量纲对、数值错的情况程序发现不了，只能靠核对物性数据和雷诺数。

## 文件包含与设置复用

较大的算例常把公共设置放在单独的文件里，再用 `#include` 引入，例如：

```foam
#include "meshQualityDict"
```

被引入的文件会原样并入当前字典。复制或分享算例时，别漏了这些被包含的文件。

方腔的 `fvSolution` 还包含这种写法：

```foam
pFinal
{
    $p;
    relTol 0;
}
```

`$p;` 把同级 `p` 子字典的条目整体复制过来，再用 `relTol 0` 覆盖其中的相对容差。这样，最后一次压力校正和前面几次用同一个线性求解器，只是停止条件更严格。

## 读取、修改与排错

用 `foamDictionary` 查看条目：

```bash
foamDictionary 0/U -entry dimensions -value
foamDictionary 0/U -entry boundaryField/movingWall/value -value
foamDictionary system/controlDict -entry deltaT -value
```

条目路径用斜杠分隔层级：第二条命令依次进入 `boundaryField`、`movingWall`，读出其中的 `value`。

在算例副本中，将时间步改为 `0.0025`：

```bash
foamDictionary system/controlDict -entry deltaT -set 0.0025
foamDictionary system/controlDict -entry deltaT -value
```

`-set` 会直接改写文件，第二条命令马上就能看到新值。注意：在 `writeControl timeStep` 下，时间步变小后，同样的 `writeInterval` 对应的物理时间间隔也会变短，后面的课会具体讨论。

| 报错或现象 | 检查位置 |
| --- | --- |
| `unexpected token` 或读到文件末尾 | 上一个条目是否缺少分号、括号是否配对 |
| `keyword ... is undefined` | 关键字是否拼错、是否放进了错误的子字典 |
| `inconsistent dimensions` | 输入量纲与方程要求是否一致 |
| 找不到 `#include` 文件 | 引入文件的相对位置和文件名 |

## 动手练习

读取 `0/U`、`0/p` 和 `constant/transportProperties`，找出速度、运动学压力和运动黏度的量纲。然后把 `nu` 改成带量纲的完整写法，数值仍为 `0.01`——物理设置并没有变。

再把 `0/U` 中顶盖的速度改为 `(0.5 0 0)`，并用 `foamDictionary` 读出结果。这一改动只影响顶盖的运动速度，内部流体的初始速度仍由 `internalField` 决定。下一课就用这些文件运行方腔，看流体怎样从静止发展起来。
