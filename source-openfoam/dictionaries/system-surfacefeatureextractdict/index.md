---
title: "system/surfaceFeatureExtractDict"
layout: "reference"
description: "输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMes"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/surfaceFeatureExtractDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>extractionMethod</code> · <code>extractFromSurfaceCoeffs</code> · <code>includedAngle</code> · <code>writeObj</code></p><h2>关联命令</h2><p><a href="/commands/?q=surfaceFeatureExtract">surfaceFeatureExtract</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/surfaceFeatureExtractDict -keywords
surfaceFeatureExtract -help</code></pre><h2>7.3 system/surfaceFeatureExtractDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object surfaceFeatureExtractDict;
}
body.stl
{
    extractionMethod extractFromSurface;
    extractFromSurfaceCoeffs { includedAngle 150; }
    writeObj yes;
}</code></pre>
<p>输入表面 body.stl 存放于 constant/triSurface。includedAngle 按特征提取器的包含角定义取值，其定义与 resolveFeatureAngle 不同。writeObj 控制可视化文件输出。运行 surfaceFeatureExtract 后，将生成的 eMesh 文件名用于后续特征线配置。</p>
<h2>17.7 surfaceFeatureExtractDict</h2><pre><code>body.stl
{
    extractionMethod    extractFromSurface;
    includedAngle       150;          // 夹角超过它的棱视为特征边
    subsetFeatures      { nonManifoldEdges no; openEdges yes; }
    writeObj            yes;          // 输出 obj 方便在 ParaView 里检查
}</code></pre>
<p>includedAngle 越大，提取的边越多。150 是常用起点：太小会漏掉圆角过渡处的特征，太大会把曲面上的三角片棱也当成特征。</p>
{% endraw %}