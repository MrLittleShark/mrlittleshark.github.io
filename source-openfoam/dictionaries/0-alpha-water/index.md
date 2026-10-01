---
title: "0/alpha.water"
layout: "reference"
description: "温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>0/alpha.water</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>inletOutlet</code> · <code>constantAlphaContactAngle</code> · <code>dynamicAlphaContactAngle</code> · <code>theta0</code> · <code>limit</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=interIsoFoam">interIsoFoam</a> · <a href="/commands/?q=setFields">setFields</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary 0/alpha.water -keywords
interFoam -help</code></pre><h2>9.3 温度场与多相流场</h2><p>温度场 T 采用温度量纲，初值示例为 internalField uniform 300;。等温壁面使用 fixedValue，绝热壁面通常使用 zeroGradient。externalWallHeatFluxTemperature 可指定热通量或功率，并通过 mode、kappaMethod 等参数定义施加方式和导热率来源。</p>
<p>p_rgh 表示扣除静水压项后的压力，常见定义为 \(p_{\mathrm{rgh}}=p-\rho gh\)。参考高度和量纲由求解器确定，不可压缩 Boussinesq 模型可采用归一化形式。恢复实际压力时，应按该求解器的定义还原静水压项。</p>
<p>alpha.water 表示水相体积分数，为无量纲量，取值范围为 [0,1]；多相体系中各相体积分数之和为 1。入口可指定相分数，开放边界可采用 inletOutlet，壁面可采用 zeroGradient 或接触角条件。字段后缀 water 与 phases 中的相名对应。</p>
{% endraw %}