---
title: "第 3 章　目录结构：文件位置与职责"
layout: reference
description: "OpenCFD v2512 目录结构：文件位置与职责；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>3.1 安装目录（&#36;WM_PROJECT_DIR）</h2>
<pre><code class="language-plaintext">OpenFOAM-v2512/
├── applications/          源代码
│   ├── solvers/           所有求解器源码（&#36;FOAM_SOLVERS）
│   ├── utilities/         所有工具源码（&#36;FOAM_UTILITIES）
│   └── test/              官方小测试程序，学写代码的好材料
├── src/                   核心库源码（&#36;FOAM_SRC）
│   ├── finiteVolume/      有限体积法核心：离散格式、边界条件
│   ├── OpenFOAM/          基础容器、场、字典读写
│   ├── TurbulenceModels/  湍流模型
│   └── ...
├── bin/                   脚本类命令（foamCloneCase、foamLog…）
├── etc/                   环境配置 + 模板字典（&#36;FOAM_ETC）
│   ├── bashrc             环境激活脚本
│   ├── config.sh/         各子模块的环境配置（含 aliases）
│   ├── caseDicts/         官方字典模板（functionObject 模板都在这）
│   └── controlDict        全局默认设置（DebugSwitches 等）
├── platforms/             编译产物
│   └── linux64GccDPInt32Opt/
│       ├── bin/           所有可执行文件（&#36;FOAM_APPBIN）
│       └── lib/           所有动态库（&#36;FOAM_LIBBIN）
├── tutorials/             官方算例（&#36;FOAM_TUTORIALS）★最重要的学习资源
└── wmake/                 编译系统</code></pre>
<p>platforms/linux64GccDPInt32Opt 这串名字什么意思：linux64 操作系统与位数 + Gcc 编译器 + DP 双精度 + Int32 32 位整型标签 + Opt 优化编译（对应的还有 Debug、Prof）。这串字符串就是环境变量 &#36;WM_OPTIONS。理解它的价值在于：当你的自定义求解器”编译成功但找不到”，多半是当前 &#36;WM_OPTIONS 与编译时不一致。</p>
<h2>3.2 算例目录（三个必备子目录）</h2>
<p>任何一个 OpenFOAM 算例都是这个结构，一个文件都不能少：</p>
<pre><code class="language-plaintext">myCase/
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
<p>一个典型算例由时间目录中的场、constant 中的网格或模型数据、system 中的离散和运行控制组成。0 是常用初始时刻，但续算可以从其他时间目录读取；动态网格还可能写入后续时间目录。建议先检查 controlDict 中的运行设置，再对照场边界、物性和网格，最后确认求解器实际读取哪些文件。</p>
<p>时间目录：算例跑起来后会生成 0.1/、0.2/… 这样的目录，里面是各个时刻的场。它们和 0/ 结构完全一样。删掉它们不影响算例定义，所以”清理算例”本质上就是删掉这些时间目录。</p>
{% endraw %}
