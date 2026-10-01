---
title: "system/setFieldsDict"
layout: "reference"
description: "setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/setFieldsDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>defaultFieldValues</code> · <code>regions</code> · <code>boxToCell</code> · <code>sphereToCell</code> · <code>cylinderToCell</code> · <code>fieldValues</code></p><h2>关联命令</h2><p><a href="/commands/?q=setFields">setFields</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/setFieldsDict -keywords
setFields -help</code></pre><h2>7.5 system/setFieldsDict</h2><p>setFields 首先按 defaultFieldValues 设置全域初值，再依次执行 regions 中的区域赋值。区域重叠时，后续赋值覆盖先前结果。目标场文件须预先建立，并设置相应的 class 和 dimensions。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object setFieldsDict;
}
defaultFieldValues
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);
regions
(
    boxToCell
    {
        box (0 0 -1) (0.2 0.3 1);
        fieldValues (volScalarFieldValue alpha.water 1);
    }
);</code></pre>
<p>boxToCell 按单元位置选取长方体区域；sphereToCell 通过 centre 和 radius 定义球形区域；cylinderToCell 通过 p1、p2 和 radius 定义圆柱区域。边界面可采用 boxToFace 等选择器。</p>
<p>赋值后检查 alpha.water 的极值与空间分布，边界条件在场文件中另行设置。需采用数学表达式赋值时，使用 setExprFields。</p>
<h2>17.2 setFieldsDict（区域初始化）</h2><pre><code>defaultFieldValues              // 先把全场设成默认值
(
    volScalarFieldValue alpha.water 0
    volVectorFieldValue U (0 0 0)
);

regions                          // 再覆盖指定区域
(
    boxToCell
    {
        box (0 0 -1) (0.1461 0.292 1);
        fieldValues ( volScalarFieldValue alpha.water 1 );
    }

    cylinderToCell
    {
        p1 (0 0 0);  p2 (0 0 0.1);  radius 0.05;
        fieldValues ( volScalarFieldValue T 500 );
    }

    sphereToCell
    {
        origin (0 0 0);  radius 0.1;
        fieldValues ( volScalarFieldValue p 1e6 );
    }
);</code></pre>
<p>常用区域类型：boxToCell、sphereToCell、cylinderToCell、rotatedBoxToCell、surfaceToCell（用 STL 划区）、cellToCell（用已有 cellSet）、zoneToCell。</p>
<p>注意：setFields 直接修改 0/ 里的文件。跑之前先 cp -r 0.orig 0，否则第二次运行是在被改过的场上再改一次。</p>
{% endraw %}