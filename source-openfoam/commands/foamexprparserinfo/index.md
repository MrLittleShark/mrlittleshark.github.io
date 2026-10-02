---
title: "foamExprParserInfo · 用于查询表达式语法及解析器支持范围"
layout: reference
description: "用于查询表达式语法及解析器支持范围。"
cms_slug: "command-foamexprparserinfo"
---

<p>用于查询表达式语法及解析器支持范围。</p><h2>开始前</h2>
<p>需要当前安装包含 foamExprParserInfo。该工具输出表达式解析器的符号与语法规则，适合检查可用表达式写法。</p>
<h2>示例 1：查看一般场表达式的符号</h2>
<pre><code class="language-bash">foamExprParserInfo -field -tokens
</code></pre>
<p>列出 field 解析器识别的符号和类型名称。查找函数对应的终结符，有助于定位表达式解析时的未知符号。</p>
<h2>示例 2：查看一般场表达式的组合规则</h2>
<pre><code class="language-bash">foamExprParserInfo -field -rules
</code></pre>
<p>输出 field 解析器语法规则。结合 svalue、sfield、vfield 等类型，查看标量值、标量场和向量场能够怎样组合。</p>
<h2>示例 3：检查边界表达式规则</h2>
<pre><code class="language-bash">foamExprParserInfo -patch -rules
</code></pre>
<p>选择 patch 解析器，查看边界表达式的语法。编写边界相关表达式时，应以这一组规则核对，而不是直接照搬其他解析器的写法。</p>
<h2>示例 4：同时查看体场解析器符号与规则</h2>
<pre><code class="language-bash">foamExprParserInfo -volume -tokens -rules
</code></pre>
<p>打印 volume 解析器的两类信息。可对照类型前缀区分体场、表面场和点场表达式，定位输入类型不匹配的问题。</p>
<h2>示例 5：比较所有解析器</h2>
<pre><code class="language-bash">foamExprParserInfo -all -tokens -rules &gt; expression-parsers.txt
</code></pre>
<p>把全部解析器的符号和规则集中保存，用于比较同一函数或运算在不同上下文中的支持情况。大写名称通常是终结符，小写名称通常是非终结符。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 command reference
Command: foamExprParserInfo
Evidence: not-installed
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamExprParserInfo/foamExprParserInfo.C

未取得运行时帮助。

源码路径：applications/tools/foamExprParserInfo/foamExprParserInfo.C

Display token names or rules for specified expression parsers. In the Lemon grammar, terminals (uppercase) are listed first. Non-terminals (lowercase) are listed second. The current OpenFOAM grammar short naming conventions: - svalue : scalar value - sfield : scalar field - lfield : logic field - vfield : vector field - tfield : tensor field - hfield : sphericalTensor field - yfield : symmTensor field . Prefixes: &#x27;s&#x27; (surface) or &#x27;p&#x27; (point). For example, psfield for a point scalar field</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamExprParserInfo/foamExprParserInfo.C">源码与说明</a> · <a href="/assets/command-help/foamexprparserinfo.txt">帮助文本</a></p>
