---
title: "第 11 章　字典文件的通用语法"
layout: reference
description: "字典文件的通用语法：用法与配置实例。"
cms_slug: "reference-guide-11"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>OpenFOAM 的所有设置文件（叫”字典”，dictionary）用的是同一套语法。先花十分钟学会这套语法，后面所有文件都只是”填什么”的问题，而不是”怎么写”的问题。</p>
<h2>11.1 文件头 FoamFile</h2>
<p>每个字典文件开头都有这一段，缺了会直接报错：</p>
<pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;          // ascii 或 binary
    class       dictionary;     // 这个文件装的是什么类型的数据
    object      controlDict;    // 文件名，必须与实际文件名一致
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre>
<p>class 常见取值</p>
<div class="table-scroll"><table>
<tr><th>class</th><th>用在</th></tr>
<tr><td>dictionary</td><td>所有 system/、constant/ 下的设置文件</td></tr>
<tr><td>volScalarField</td><td>0/ 下的标量场（p、T、k…）</td></tr>
<tr><td>volVectorField</td><td>0/ 下的矢量场（U）</td></tr>
<tr><td>volSymmTensorField</td><td>对称张量场（R）</td></tr>
<tr><td>pointVectorField</td><td>点场（动网格位移）</td></tr>
<tr><td>surfaceScalarField</td><td>面场（phi）</td></tr>
</table></div>
<p>object 与文件名不一致时，多数命令会警告甚至读错。手工复制文件时记得改 object——这是初学者的高频低级错误。</p>
<h2>11.2 基本语法规则</h2>
<pre><code class="language-plaintext">关键字   值;                       // 每条以分号结尾

子字典
{
    关键字   值;
}

列表 ( a b c );                    // 括号 + 空格分隔
带长度的列表 3 ( a b c );           // 也可以显式写长度

// 单行注释
/* 多行
   注释 */</code></pre>
<p>三条容易犯的错：① 忘记分号（报错信息通常指向下一行，所以要往上找）；② 子字典 {} 后面不加分号；③ 中文全角符号混进来（从 PDF 复制时常发生），报 ill defined primitiveEntry。</p>
<h2>11.3 量纲 dimensions</h2>
<pre><code class="language-openfoam">dimensions      [0 2 -2 0 0 0 0];      // 这是不可压求解器里 p 的量纲：m²/s²</code></pre>
<p>七个数字依次是：</p>
<div class="table-scroll"><table>
<tr><th>位置</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td>物理量</td><td>质量</td><td>长度</td><td>时间</td><td>温度</td><td>物质的量</td><td>电流</td><td>光强</td></tr>
<tr><td>单位</td><td>kg</td><td>m</td><td>s</td><td>K</td><td>mol</td><td>A</td><td>cd</td></tr>
</table></div>
<p>常见量纲</p>
<div class="table-scroll"><table>
<tr><th>量</th><th>写法</th><th>单位</th></tr>
<tr><td>速度 U</td><td>[0 1 -1 0 0 0 0]</td><td>m/s</td></tr>
<tr><td>压力 p（不可压，已除以 \(\rho\)）</td><td>[0 2 -2 0 0 0 0]</td><td>\(m^{2}/s^{2}\)</td></tr>
<tr><td>压力 p（可压，真实压力）</td><td>[1 -1 -2 0 0 0 0]</td><td>Pa</td></tr>
<tr><td>运动粘度 \(\nu\)</td><td>[0 2 -1 0 0 0 0]</td><td>\(m^{2}/s\)</td></tr>
<tr><td>动力粘度 \(\mu\)</td><td>[1 -1 -1 0 0 0 0]</td><td>Pa·s</td></tr>
<tr><td>密度 \(\rho\)</td><td>[1 -3 0 0 0 0 0]</td><td>\(\mathrm{kg}/m^{3}\)</td></tr>
<tr><td>温度 T</td><td>[0 0 0 1 0 0 0]</td><td>K</td></tr>
<tr><td>k（湍动能）</td><td>[0 2 -2 0 0 0 0]</td><td>\(m^{2}/s^{2}\)</td></tr>
<tr><td>\(\varepsilon\)</td><td>[0 2 -3 0 0 0 0]</td><td>\(m^{2}/s^{3}\)</td></tr>
<tr><td>\(\omega\)</td><td>[0 0 -1 0 0 0 0]</td><td>1/s</td></tr>
</table></div>
<p>许多场运算会进行量纲一致性检查；压力 Pa 与运动学压力 \(p/\rho\) 的量纲不同。遇到 incompatible dimensions，应先确认求解器对 p 的定义，再核对物性、源项与边界。量纲检查不能发现所有物理设置错误，也不应替代单位记录。</p>
<h2>11.4 场的赋值：uniform / nonuniform</h2>
<pre><code class="language-openfoam">internalField   uniform (0 0 0);              // 全场同一个值
internalField   uniform 0;

internalField   nonuniform List&lt;vector&gt;       // 逐单元给值（一般由程序生成）
400
(
(0 0 0)
(0.1 0 0)
...
);</code></pre>
<p>nonuniform 按网格位置逐项保存场值，适合非均匀初始场和计算结果。批量修改宜使用 setFields、setExprFields 或其他明确的场处理流程，避免改变元素数量或破坏网格编号对应关系。</p>
<h2>11.5 边界条件块 boundaryField 与正则匹配</h2>
<pre><code class="language-openfoam">boundaryField
{
    inlet           { type fixedValue; value uniform (1 0 0); }
    outlet          { type zeroGradient; }

    "(top|bottom)"  { type symmetryPlane; }        // 正则：同时匹配 top 和 bottom
    "wall.*"        { type noSlip; }               // 所有以 wall 开头的 patch
    ".*"            { type zeroGradient; }         // 兜底：其余全部
}</code></pre>
<p>正则的两条规则：① 必须用双引号包起来，不然被当作普通名字；② 精确名字优先于正则，多个正则匹配时后面的优先。兜底 ".*" 放最后是个好习惯，可以避免”漏了一个 patch 导致启动失败”。</p>
<h2>11.6 变量、宏与文件包含（把重复的东西提出来）</h2>
<p>① 定义与引用变量</p>
<pre><code class="language-openfoam">flowVelocity     (10 0 0);
pressure         0;

internalField    uniform $flowVelocity;      // 用 $ 引用</code></pre>
<p>② 引用嵌套条目</p>
<pre><code class="language-plaintext">$..solvers/p/tolerance      // .. 表示上一层
$:solvers.p.tolerance       // 从文件根部开始的绝对路径</code></pre>
<p>③ 包含另一个文件（最有用的技巧）</p>
<pre><code class="language-openfoam">#include        "initialConditions"          // 相对本文件的路径
#includeIfPresent "myOverrides"              // 存在才包含，不存在不报错
#includeEtc     "caseDicts/setConstraintTypes"   // 从 $FOAM_ETC 里包含
#includeFunc solverInfo               // 引入官方 functionObject 模板</code></pre>
<p>典型用法：在算例根目录建一个 initialConditions 文件</p>
<pre><code class="language-plaintext">// &lt;算例&gt;/initialConditions
flowVelocity        (10 0 0);
pressure            0;
turbulentKE         0.375;
turbulentEpsilon    14.855;</code></pre>
<p>然后 0/U、0/p、0/k、0/epsilon 全都 #include "../initialConditions" 并用 $flowVelocity 这样引用。好处：改工况只改一个文件，不会出现”U 改了 k 忘了改”的错误。做参数扫描时这更是必须的。</p>
<p>④ 表达式计算</p>
<pre><code class="language-openfoam">#include "initialConditions"

// 用 #calc 写一段 C++ 表达式（会动态编译）
nu              #calc "1.0/$Re";
endTime         #calc "10.0*$period";

// v2012 起也可以用更轻量的 #eval（不需要编译，速度快）
deltaT          #eval "1e-3/2";</code></pre>
<p>⑤ 删除继承来的条目</p>
<pre><code class="language-plaintext">#remove         someKeyword;
#remove         ( key1 key2 );</code></pre>
<p>⑥ 检查展开结果</p>
<p>用了一堆 #include 和 #calc 后，怎么知道程序最终读到了什么？</p>
<pre><code class="language-bash">foamDictionary system/controlDict -expand
foamDictionary 0/U -expand -entry boundaryField/inlet</code></pre>
<p>这条命令能省掉大量猜测。</p>
<h2>11.7 常用”填空词”</h2>
<div class="table-scroll"><table>
<tr><th>写法</th><th>含义</th></tr>
<tr><td>uniform &lt;值&gt;</td><td>均匀场</td></tr>
<tr><td>constant &lt;值&gt;</td><td>常数（部分模型用）</td></tr>
<tr><td>table ((t1 v1) (t2 v2))</td><td>分段线性表（随时间变化）</td></tr>
<tr><td>tableFile { file "..."; }</td><td>从文件读表</td></tr>
<tr><td>polynomial ((c0 0)(c1 1))</td><td>多项式</td></tr>
<tr><td>expression "..."</td><td>表达式（v2012+ 的 exprValue 类边界条件）</td></tr>
<tr><td>$internalField</td><td>用内部场的值（边界 value 里常见）</td></tr>
<tr><td>#include "..."</td><td>包含文件</td></tr>
<tr><td>yes/no、true/false、on/off</td><td>开关都通用</td></tr>
</table></div><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>
