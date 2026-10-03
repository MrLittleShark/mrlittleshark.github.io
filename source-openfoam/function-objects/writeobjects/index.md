---
title: "writeObjects"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-writeobjects"
description: "将对象数据库中的指定对象写入文件。"
---
{% raw %}
<p>将对象数据库中的指定对象写入文件。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    writeObjects1
    {
        type            writeObjects;
        libs            (utilityFunctionObjects);
        writeOption     log;
        objects         ( &quot;.*&quot; );
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         1000;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    onEnd;
        writeInterval 1;
    }
}</code></pre><p>将内存中选定对象写到时间目录。objects 控制名称筛选，writeOption 控制选择的写出属性；log 模式用于查看匹配到的对象信息。</p><p>配套教程配置：<code>incompressible/pisoFoam/RAS/cavity/system/FOs/FOwriteObjects</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>writeObjects</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>writeOption</code></td><td>anyWrite、autoWrite、noWrite 控制写出筛选；log 用于列出匹配对象。</td><td>可选</td><td><code>anyWrite</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>fields</code></td><td>需要处理的场名称列表。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>objects</code></td><td>需要读取、写出或移除的数据库对象名称列表。</td><td>可选</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>将内存中选定对象写到时间目录。objects 控制名称筛选，writeOption 控制选择的写出属性；log 模式用于查看匹配到的对象信息。</p><pre><code class="language-foam">writeObjects1
{
    type            writeObjects;
    libs            (utilityFunctionObjects);
    writeOption     log;
    objects         ( &quot;.*&quot; );
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    onEnd;
    writeInterval 1;
}</code></pre><h3 id="example-2">示例 2 · 保存指定对象</h3><p>选择 U 和 p，按本对象的写出时刻保存。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeOption anyWrite;
objects (U p);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">writeObjects1
{
    type            writeObjects;
    libs            (utilityFunctionObjects);
    writeOption anyWrite;
    objects (U p);
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    onEnd;
    writeInterval 1;
}</code></pre></details><h3 id="example-3">示例 3 · 仅保存自动写出对象</h3><p>按对象自身 AUTO_WRITE 属性筛选。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeOption autoWrite;
objects (&quot;.*&quot;);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">writeObjects1
{
    type            writeObjects;
    libs            (utilityFunctionObjects);
    writeOption autoWrite;
    objects (&quot;.*&quot;);
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    onEnd;
    writeInterval 1;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">writeObjects1
{
    type            writeObjects;
    libs            (utilityFunctionObjects);
    writeOption     log;
    objects         ( &quot;.*&quot; );
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 1;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">writeObjects1
{
    type            writeObjects;
    libs            (utilityFunctionObjects);
    writeOption     log;
    objects         ( &quot;.*&quot; );
    region          region0;
    enabled         true;
    log             true;
    timeStart 0.1;
    timeEnd 0.5;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    onEnd;
    writeInterval 1;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E6%96%87%E4%BB%B6%E4%B8%8E%E6%8E%A7%E5%88%B6">文件与控制速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-13">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/writeObjects/writeObjects.H">OpenFOAM v2512 · writeObjects 接口</a>。</p>
{% endraw %}
