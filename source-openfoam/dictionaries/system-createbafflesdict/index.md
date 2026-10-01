---
title: "system/createBafflesDict"
layout: "reference"
description: "createBaffles 将内部面转换为成对边界面。internalFacesOnly 控制选面范围，baffles 定义各挡板的 type、zoneName 和 patches。下例采用预先建立的 interfaceZone 面区域。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/createBafflesDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>internalFacesOnly</code> · <code>baffles</code> · <code>faceZone</code> · <code>zoneName</code> · <code>master</code> · <code>slave</code></p><h2>关联命令</h2><p><a href="/commands/?q=createBaffles">createBaffles</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/createBafflesDict -keywords
createBaffles -help</code></pre><h2>7.9 system/createBafflesDict</h2><p>createBaffles 将内部面转换为成对边界面。internalFacesOnly 控制选面范围，baffles 定义各挡板的 type、zoneName 和 patches。下例采用预先建立的 interfaceZone 面区域。</p>
<pre><code>internalFacesOnly true;
baffles
{
    interface
    {
        type faceZone;
        zoneName interfaceZone;
        patches
        {
            master { name sideA; type wall; }
            slave  { name sideB; type wall; }
        }
    }
}</code></pre>
<p>运行 createBaffles -overwrite 生成挡板边界。两侧的传热和流动耦合由场边界条件及物理模型确定。</p>
{% endraw %}