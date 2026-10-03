---
title: "setTimeStep"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-settimestep"
description: "按指定规则设置时间步。"
---
{% raw %}
<p>按指定规则设置时间步。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    setTimeStepExample
    {
        type setTimeStep;
        libs (utilityFunctionObjects);
    deltaT 0.005;
    }
}</code></pre><p>用 deltaT 指定求解器下一步采用的时间步长。该值可写成常量，也可使用随时间变化的 Function1；放入算例后由运行中的求解器调用。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>setTimeStep</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>deltaT</code></td><td>时间步长，可使用常量或 Function1 时间函数。</td><td>必填</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>用 deltaT 指定求解器下一步采用的时间步长。该值可写成常量，也可使用随时间变化的 Function1；放入算例后由运行中的求解器调用。</p><pre><code class="language-foam">setTimeStepExample
{
    type setTimeStep;
    libs (utilityFunctionObjects);
deltaT 0.005;
}</code></pre><h3 id="example-2">示例 2 · 把时间步减半</h3><p>对相同流场和网格，时间步减半也会相应降低对流 Courant 数，同时增加推进相同时长所需的步数。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">deltaT 0.0025;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">setTimeStepExample
{
    type setTimeStep;
    libs (utilityFunctionObjects);
deltaT 0.0025;
}</code></pre></details><h3 id="example-3">示例 3 · 分阶段改变时间步</h3><p>启动阶段从较小时间步开始，随后按表格插值过渡到 0.005；时间点采用模拟时间。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">deltaT table ((0 0.001) (0.1 0.005) (1 0.005));</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">setTimeStepExample
{
    type setTimeStep;
    libs (utilityFunctionObjects);
deltaT table ((0 0.001) (0.1 0.005) (1 0.005));
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">setTimeStepExample
{
    type setTimeStep;
    libs (utilityFunctionObjects);
deltaT 0.005;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">setTimeStepExample
{
    type setTimeStep;
    libs (utilityFunctionObjects);
deltaT 0.005;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E6%96%87%E4%BB%B6%E4%B8%8E%E6%8E%A7%E5%88%B6">文件与控制速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/setTimeStep/setTimeStepFunctionObject.H">OpenFOAM v2512 · setTimeStep 接口</a>。</p>
{% endraw %}
