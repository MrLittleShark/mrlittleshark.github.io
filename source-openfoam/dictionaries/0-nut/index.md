---
title: "0/nut"
layout: "reference"
description: "入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：k = 1.5*(I*U)^2，epsilon = Cmu^0.75*k^1.5/L，omega = sqrt(k)/(Cmu^0.25*L)。常用 Cmu = 0.09，湍流强度 5% 对应 I = 0.05。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>0/nut</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dimensions</code> · <code>internalField</code> · <code>boundaryField</code> · <code>nutkWallFunction</code> · <code>calculated</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary 0/nut -keywords
simpleFoam -help</code></pre><h2>9.4 湍流场与热扩散场</h2><div class="table-scroll"><table>
<tr><th>字段</th><th>量纲</th><th>常见边界与设置</th></tr>
<tr><td>k</td><td>[0 2 -2 0 0 0 0]</td><td>入口固定湍动能；壁面可配 kqRWallFunction</td></tr>
<tr><td>epsilon</td><td>[0 2 -3 0 0 0 0]</td><td>k epsilon 模型使用；壁面 epsilonWallFunction</td></tr>
<tr><td>omega</td><td>[0 0 -1 0 0 0 0]</td><td>k omega 模型使用；壁面 omegaWallFunction</td></tr>
<tr><td>nut</td><td>[0 2 -1 0 0 0 0]</td><td>湍动黏度，由模型给定；壁面可用 nutkWallFunction 等</td></tr>
<tr><td>alphat</td><td>由热模型定义，常见可压缩形式为 [1 -1 -1 0 0 0 0]</td><td>量纲按所用热模型确定</td></tr>
</table></div>
<p>入口湍流量可由湍流强度 I、速度大小 U 和长度尺度 L 估算：\(k=1.5(IU)^2\)，\(\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{L}\)，\(\omega=\frac{\sqrt{k}}{C_\mu^{0.25}L}\)。常用 \(C_\mu = 0.09\)，湍流强度 5% 对应 \(I = 0.05\)。</p>
<p>近壁处理方式应与网格设计一致。采用壁面函数或直接解析近壁区域时，分别据其要求确定第一层网格厚度及目标 y+。</p>
{% endraw %}