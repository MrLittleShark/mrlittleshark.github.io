---
title: "第 3 章　目录结构：文件都放在哪儿"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>3.1 安装目录（$WM_PROJECT_DIR）</h4>
<pre><code>OpenFOAM-v2512/
├── applications/          源代码
│   ├── solvers/           所有求解器源码（$FOAM_SOLVERS）
│   ├── utilities/         所有工具源码（$FOAM_UTILITIES）
│   └── test/              官方小测试程序，学写代码的好材料
├── src/                   核心库源码（$FOAM_SRC）
│   ├── finiteVolume/      有限体积法核心：离散格式、边界条件
│   ├── OpenFOAM/          基础容器、场、字典读写
│   ├── TurbulenceModels/  湍流模型
│   └── ...
├── bin/                   脚本类命令（foamCloneCase、foamLog…）
├── etc/                   环境配置 + 模板字典（$FOAM_ETC）
│   ├── bashrc             环境激活脚本
│   ├── config.sh/         各子模块的环境配置（含 aliases）
│   ├── caseDicts/         官方字典模板（functionObject 模板都在这）
│   └── controlDict        全局默认设置（DebugSwitches 等）
├── platforms/             编译产物
│   └── linux64GccDPInt32Opt/
│       ├── bin/           所有可执行文件（$FOAM_APPBIN）
│       └── lib/           所有动态库（$FOAM_LIBBIN）
├── tutorials/             官方算例（$FOAM_TUTORIALS）★最重要的学习资源
└── wmake/                 编译系统</code></pre>
<p>platforms/linux64GccDPInt32Opt 这串名字什么意思：linux64 操作系统与位数 + Gcc 编译器 + DP 双精度 + Int32 32 位整型标签 + Opt 优化编译（对应的还有 Debug、Prof）。这串字符串就是环境变量 $WM_OPTIONS。理解它的价值在于：当你的自定义求解器”编译成功但找不到”，多半是当前 $WM_OPTIONS 与编译时不一致。</p>
<h4>3.2 算例目录（三个必备子目录）</h4>
<p>任何一个 OpenFOAM 算例都是这个结构，一个文件都不能少：</p>
<pre><code>myCase/
├── 0/                     初始条件与边界条件（每个场一个文件）
│   ├── U                  速度
│   ├── p                  压力
│   ├── k, epsilon, nut    湍流量（用湍流模型时才需要）
│   └── alpha.water        相分数（多相流时才需要）
├── constant/              不随时间变的东西
│   ├── polyMesh/          网格数据（points/faces/owner/neighbour/boundary）
│   ├── transportProperties       物性（粘度、密度…）
│   ├── turbulenceProperties      湍流模型选择
│   ├── g                         重力（浮力/多相流时需要）
│   └── triSurface/               STL 几何（用 snappyHexMesh 时）
└── system/                怎么算
    ├── controlDict        时间控制、输出控制、functionObject
    ├── fvSchemes          离散格式
    ├── fvSolution         线性求解器与算法控制
    ├── blockMeshDict      网格生成（放 system/ 下）
    ├── decomposeParDict   并行分区
    └── setFieldsDict      场初始化</code></pre>
<p>为什么是这三个目录：OpenFOAM 把一个算例拆成”初始状态（0/）+ 不变的物理与几何（constant/）+ 数值方法与流程（system/）“。这个划分是强制的——求解器启动时按固定路径去找这些文件，找不到就报错退出。理解了这个划分，你看任何一个陌生算例都知道从哪里下手：先看 system/controlDict 知道它用什么求解器算多久，再看 0/ 知道边界条件，最后看 constant/ 知道物性。</p>
<p>时间目录：算例跑起来后会生成 0.1/、0.2/… 这样的目录，里面是各个时刻的场。它们和 0/ 结构完全一样。删掉它们不影响算例定义，所以”清理算例”本质上就是删掉这些时间目录。</p>
{% endraw %}