---
title: "ensightCloud"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-ensightcloud"
description: "颗粒数据格式导出"
---
{% raw %}
<p>颗粒数据格式导出</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    ensightCloudExample
    {
        type ensightCloud;
        libs (lagrangianFunctionObjects);
    clouds (kinematicCloud);
        fields (U d);
        format binary;
        writeControl writeTime;
    }
}</code></pre><p>将拉格朗日颗粒云转换为 EnSight 输出。clouds 选择云，fields 选择颗粒属性；示例保留速度 U 和粒径 d。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>ensightCloud</code></td></tr><tr><td><code>clouds</code></td><td>要处理的多个颗粒云名称或匹配表达式。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>cloud</code></td><td>要处理的颗粒云名称。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>selection</code></td><td>单元或颗粒的选择规则子字典。</td><td>可选</td><td><code>空字典</code></td></tr><tr><td><code>format</code></td><td>文件编码格式：ascii 或 binary。</td><td>可选</td><td><code>binary</code></td></tr><tr><td><code>width</code></td><td>输出编号的补零位数。</td><td>可选</td><td><code>8</code></td></tr><tr><td><code>directory</code></td><td>输出目录名称。</td><td>可选</td><td><code>postProcessing/对象名</code></td></tr><tr><td><code>overwrite</code></td><td>是否清理并重新生成已有导出目录。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>consecutive</code></td><td>输出数据是否使用连续编号。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>prune</code></td><td>是否省略没有颗粒的空颗粒云。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>timeFormat</code></td><td>EnSight 索引中时间值的格式。</td><td>可选</td><td><code>scientific</code></td></tr><tr><td><code>timePrecision</code></td><td>EnSight 索引中时间值的数字精度。</td><td>可选</td><td><code>5</code></td></tr><tr><td><code>writeControl</code></td><td>写出方式，例如 timeStep 按步数、writeTime 随主计算输出。</td><td>可选</td><td><code>timeStep</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>将拉格朗日颗粒云转换为 EnSight 输出。clouds 选择云，fields 选择颗粒属性；示例保留速度 U 和粒径 d。</p><pre><code class="language-foam">ensightCloudExample
{
    type ensightCloud;
    libs (lagrangianFunctionObjects);
clouds (kinematicCloud);
    fields (U d);
    format binary;
    writeControl writeTime;
}</code></pre><h3 id="example-2">示例 2 · 只导出颗粒直径</h3><p>减少属性文件数量，适合只查看粒径的空间分布。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">fields (d);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">ensightCloudExample
{
    type ensightCloud;
    libs (lagrangianFunctionObjects);
clouds (kinematicCloud);
    fields (d);
    format binary;
    writeControl writeTime;
}</code></pre></details><h3 id="example-3">示例 3 · 以文本格式查看所有云</h3><p>匹配算例中的颗粒云，并以文本格式保存便于检查的属性值。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">clouds (&quot;.*&quot;);
format ascii;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">ensightCloudExample
{
    type ensightCloud;
    libs (lagrangianFunctionObjects);
clouds (&quot;.*&quot;);
    fields (U d);
    format ascii;
    writeControl writeTime;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">ensightCloudExample
{
    type ensightCloud;
    libs (lagrangianFunctionObjects);
clouds (kinematicCloud);
    fields (U d);
    format binary;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">ensightCloudExample
{
    type ensightCloud;
    libs (lagrangianFunctionObjects);
clouds (kinematicCloud);
    fields (U d);
    format binary;
    writeControl writeTime;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%A2%97%E7%B2%92%E4%B8%8E%E4%B8%A4%E7%9B%B8">颗粒与两相速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/lagrangian/ensightCloud/ensightCloudWriteObject.H">OpenFOAM v2512 · ensightCloud 接口</a>。</p>
{% endraw %}
