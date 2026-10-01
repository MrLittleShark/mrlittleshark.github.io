---
title: "system/meshQualityDict"
layout: "reference"
description: "运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc \"caseDicts/meshQualityDict\" 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/meshQualityDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>maxNonOrtho</code> · <code>maxBoundarySkewness</code> · <code>maxInternalSkewness</code> · <code>minVol</code> · <code>minDeterminant</code></p><h2>关联命令</h2><p><a href="/commands/?q=checkMesh">checkMesh</a> · <a href="/commands/?q=snappyHexMesh">snappyHexMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/meshQualityDict -keywords
checkMesh -help</code></pre><h2>7.4 system/meshQualityDict</h2><p>运行 foamGetDict meshQualityDict 获取模板，或通过 #includeEtc &quot;caseDicts/meshQualityDict&quot; 引入。下表列出常用质量指标及示例阈值，阈值应结合网格尺度和求解要求确定。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>示例值</th></tr>
<tr><td>maxNonOrtho</td><td>最大非正交角</td><td>65</td></tr>
<tr><td>maxBoundarySkewness</td><td>边界偏斜限制</td><td>20</td></tr>
<tr><td>maxInternalSkewness</td><td>内部偏斜限制</td><td>4</td></tr>
<tr><td>maxConcave</td><td>最大凹角</td><td>80</td></tr>
<tr><td>minVol</td><td>最小单元体积</td><td>示例为 1e-13，按实际网格尺度确定</td></tr>
<tr><td>minTetQuality</td><td>最小分解四面体质量</td><td>1e-15</td></tr>
<tr><td>minArea</td><td>最小面面积</td><td>负值可关闭相应面积检查</td></tr>
<tr><td>minTwist、minTriangleTwist</td><td>面扭曲限制</td><td>以模板值为初值，按不合格面分布调整</td></tr>
<tr><td>minDeterminant</td><td>单元几何行列式限制</td><td>0.001</td></tr>
<tr><td>minFaceWeight</td><td>面插值权重下限</td><td>0.05</td></tr>
<tr><td>minVolRatio</td><td>相邻单元体积比下限</td><td>0.01</td></tr>
<tr><td>nSmoothScale、errorReduction</td><td>质量失败时缩放处理参数</td><td>4、0.75</td></tr>
</table></div>
<h2>17.11 meshQualityDict</h2><pre><code>#includeEtc &quot;caseDicts/meshQualityDict&quot;     // 直接用官方默认阈值
maxNonOrtho 65;                             // 再局部覆盖</code></pre>
<p>供 checkMesh -meshQuality 与 snappyHexMesh 共用。</p>
{% endraw %}