---
title: "wallShearStress"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-wallshearstress"
description: "输出壁面剪切应力。"
---
{% raw %}
<p>输出壁面剪切应力。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    wallShearStress
    {
        type wallShearStress;
        libs (fieldFunctionObjects);

        writeControl writeTime;
        writeInterval 1;
    }
}</code></pre><p>从动量输运模型取得壁面剪切应力。本例选择壁面，结果可用于识别低剪切或剪切方向改变的区域；不可压缩模型中的输出可能采用运动应力量纲。</p><p>示例算例：后台阶湍流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>wallShearStress</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>可选</td><td><code>所有 wall 类型边界</code></td></tr><tr><td><code>writeFields</code></td><td>是否将计算得到的场或所选原始场写出。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>从动量输运模型取得壁面剪切应力。本例选择壁面，结果可用于识别低剪切或剪切方向改变的区域；不可压缩模型中的输出可能采用运动应力量纲。</p><pre><code class="language-foam">wallShearStress
{
    type wallShearStress;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
}</code></pre><h3 id="example-2">示例 2 · 只检查下壁面</h3><p>保留研究对象对应的壁面数据，便于提取回流区附近的剪切应力。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">patches (lowerWall);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallShearStress
{
    type wallShearStress;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    patches (lowerWall);
}</code></pre></details><h3 id="example-3">示例 3 · 只保存统计信息</h3><p>保留监测输出，减少每个时刻的场文件。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeFields false;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallShearStress
{
    type wallShearStress;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    writeFields false;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallShearStress
{
    type wallShearStress;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallShearStress
{
    type wallShearStress;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E6%B9%8D%E6%B5%81%E4%B8%8E%E5%A3%B0%E5%AD%A6">湍流与声学速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-10">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/wallShearStress/wallShearStress.H">OpenFOAM v2512 · wallShearStress 接口</a>。</p>
{% endraw %}
