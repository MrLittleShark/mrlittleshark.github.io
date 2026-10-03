---
title: "coded"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-coded"
description: "在功能对象接口中嵌入 C++ 操作"
---
{% raw %}
<p>在功能对象接口中嵌入 C++ 操作</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    codedExample
    {
        type coded;
        libs (utilityFunctionObjects);
    name reportTime;
        codeExecute
        #{
            Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
        #};
    }
}</code></pre><p>在功能对象接口中编译并执行一段 C++。name 给动态类命名，codeExecute 在执行阶段运行；本例只向日志写出当前模拟时间。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>coded</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>name</code></td><td>对象、区域或动态代码的名称，具体含义见示例。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>codeInclude</code></td><td>C++ 头文件包含语句。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeOptions</code></td><td>编译器选项，加入 EXE_INC。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeLibs</code></td><td>链接库选项，加入 LIB_LIBS。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeData</code></td><td>动态对象的成员变量定义。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>localCode</code></td><td>局部辅助函数等 C++ 定义。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeRead</code></td><td>读取字典时执行的 C++ 代码。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeExecute</code></td><td>执行阶段运行的 C++ 代码。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeWrite</code></td><td>写出阶段运行的 C++ 代码。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeEnd</code></td><td>计算结束时运行的 C++ 代码。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>codeContext</code></td><td>传递给动态代码的附加配置子字典。</td><td>可选</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在功能对象接口中编译并执行一段 C++。name 给动态类命名，codeExecute 在执行阶段运行；本例只向日志写出当前模拟时间。</p><pre><code class="language-foam">codedExample
{
    type coded;
    libs (utilityFunctionObjects);
name reportTime;
    codeExecute
    #{
        Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
    #};
}</code></pre><h3 id="example-2">示例 2 · 每十步执行一次代码</h3><p>将打印频率降为每十步一次，便于在日志中观察而不会每步重复输出。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">executeControl timeStep;
executeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">codedExample
{
    type coded;
    libs (utilityFunctionObjects);
name reportTime;
    codeExecute
    #{
        Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
    #};
    executeControl timeStep;
    executeInterval 10;
}</code></pre></details><h3 id="example-3">示例 3 · 在指定时间段执行代码</h3><p>只在模拟时间 0.1 到 0.3 之间运行该对象，适合针对一个阶段添加诊断。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.3;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">codedExample
{
    type coded;
    libs (utilityFunctionObjects);
name reportTime;
    codeExecute
    #{
        Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
    #};
    timeStart 0.1;
    timeEnd 0.3;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">codedExample
{
    type coded;
    libs (utilityFunctionObjects);
name reportTime;
    codeExecute
    #{
        Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
    #};
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">codedExample
{
    type coded;
    libs (utilityFunctionObjects);
name reportTime;
    codeExecute
    #{
        Info&lt;&lt; &quot;Time = &quot; &lt;&lt; mesh().time().value() &lt;&lt; nl;
    #};
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E6%96%87%E4%BB%B6%E4%B8%8E%E6%8E%A7%E5%88%B6">文件与控制速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/codedFunctionObject/codedFunctionObject.H">OpenFOAM v2512 · coded 接口</a>。</p>
{% endraw %}
