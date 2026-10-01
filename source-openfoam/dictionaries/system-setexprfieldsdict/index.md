---
title: "system/setExprFieldsDict"
layout: "reference"
description: "下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDic"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/setExprFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>expressions</code> · <code>field</code> · <code>expression</code> · <code>fieldMask</code> · <code>dimensions</code> · <code>create</code></p><h2>关联命令</h2><p><a href="/commands/?q=setExprFields">setExprFields</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/setExprFieldsDict -keywords
setExprFields -help</code></pre><h2>7.6 system/setExprFieldsDict</h2><pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setExprFieldsDict;
}
expressions
(
    setTemperature
    {
        field T;
        expression &quot;300 + 10*pos().x()&quot;;
    }
);</code></pre>
<p>下例在已有温度场 T 上设置随坐标变化的温度，运行 setExprFields 后生效。fieldMask 限定赋值区域，create 和 dimensions 用于新建场。表达式语法可通过 foamExprParserInfo 查询。边界表达式使用 setExprBoundaryFieldsDict，其结构按边界场接口配置。</p>
{% endraw %}