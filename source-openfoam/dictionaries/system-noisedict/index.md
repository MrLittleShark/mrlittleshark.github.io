---
title: "system/noiseDict"
layout: "reference"
description: "noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/noiseDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>noiseModel</code> · <code>pointNoise</code> · <code>surfaceNoise</code></p><h2>关联命令</h2><p><a href="/commands/?q=noise">noise</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/noiseDict -keywords
noise -help</code></pre><h2>10.7 system/noiseDict 与粒子后处理</h2><p>noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。</p>
<p>particleTracksDict 指定粒子云、采样频率和轨迹长度，轨迹重建使用求解阶段保存的粒子标识。steadyParticleTracksDict 用于稳态轨迹处理。字段设置采用对应粒子模型的教程结构。</p>
{% endraw %}