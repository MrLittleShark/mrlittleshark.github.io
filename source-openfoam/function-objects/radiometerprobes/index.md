---
title: "radiometerProbes"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-radiometerprobes"
description: "辐射计与热电偶模型采样"
---
{% raw %}
<p>辐射计与热电偶模型采样</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    radiometerProbesExample
    {
        type radiometerProbes;
        libs (utilityFunctionObjects);
    probeLocations ((0.5 0.5 0.5));
        probeNormals ((0 0 1));
        writeControl timeStep;
        writeInterval 10;
    }
}</code></pre><p>模拟具有方向的辐射计探针。每个 probeLocation 对应一个 probeNormal，法向决定探针接收辐射的方向；算例需要提供该工具使用的辐射模型。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>radiometerProbes</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>probeLocations</code></td><td>探针坐标列表，每个坐标写成 (x y z)。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>probeNormals</code></td><td>每个辐射探针对应的法向向量，与坐标列表一一对应。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>模拟具有方向的辐射计探针。每个 probeLocation 对应一个 probeNormal，法向决定探针接收辐射的方向；算例需要提供该工具使用的辐射模型。</p><pre><code class="language-foam">radiometerProbesExample
{
    type radiometerProbes;
    libs (utilityFunctionObjects);
probeLocations ((0.5 0.5 0.5));
    probeNormals ((0 0 1));
    writeControl timeStep;
    writeInterval 10;
}</code></pre><h3 id="example-2">示例 2 · 反向放置探针</h3><p>测点位置不变，接收方向反向，可比较来自两侧的辐射。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">probeNormals ((0 0 -1));</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">radiometerProbesExample
{
    type radiometerProbes;
    libs (utilityFunctionObjects);
probeLocations ((0.5 0.5 0.5));
    probeNormals ((0 0 -1));
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-3">示例 3 · 同时放置两个定向探针</h3><p>两个探针沿相同方向测量，对照不同空间位置的辐射强度。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">probeLocations ((0.5 0.5 0.5) (0.5 0.5 0.8));
probeNormals ((0 0 1) (0 0 1));</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">radiometerProbesExample
{
    type radiometerProbes;
    libs (utilityFunctionObjects);
probeLocations ((0.5 0.5 0.5) (0.5 0.5 0.8));
    probeNormals ((0 0 1) (0 0 1));
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">radiometerProbesExample
{
    type radiometerProbes;
    libs (utilityFunctionObjects);
probeLocations ((0.5 0.5 0.5));
    probeNormals ((0 0 1));
    writeControl timeStep;
    writeInterval 10;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">radiometerProbesExample
{
    type radiometerProbes;
    libs (utilityFunctionObjects);
probeLocations ((0.5 0.5 0.5));
    probeNormals ((0 0 1));
    writeControl timeStep;
    writeInterval 5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/radiometerProbes/radiometerProbes.H">OpenFOAM v2512 · radiometerProbes 接口</a>。</p>
{% endraw %}
