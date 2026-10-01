---
title: "foamExprParserInfo  查询表达式解析器信息"
layout: reference
description: "用于查询表达式语法及解析器支持范围。"
---
{% raw %}
<div class="source-note">源码包含此目标；当前虚拟机未找到可执行文件。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>用于查询表达式语法及解析器支持范围。</p><h2>v2512 源码中的用途</h2><p>Display token names or rules for specified expression parsers. In the Lemon grammar, terminals (uppercase) are listed first. Non-terminals (lowercase) are listed second. The current OpenFOAM grammar short naming conventions: - svalue : scalar value - sfield : scalar field - lfield : logic field - vfield : vector field - tfield : tensor field - hfield : sphericalTensor field - yfield : symmTensor field . Prefixes: &#x27;s&#x27; (surface) or &#x27;p&#x27; (point). For example, psfield for a point scalar field</p><h2>使用入口</h2><pre><code class="language-bash">foamExprParserInfo -volume -rules</code></pre><h2>使用条件与核对</h2><p>用于查询表达式语法及解析器支持范围。 用法：foamExprParserInfo [选项] 示例：foamExprParserInfo -volume -rules
源码说明：Display token names or rules for specified expression parsers. In the Lemon grammar, terminals (uppercase) are listed first. Non-terminals (lowercase) are listed second. The current OpenFOAM grammar short naming conventions: - svalue : scalar value - sfield : scalar field - lfield : logic field - vfield : vector field - tfield : tensor field - hfield : sphericalTensor field - yfield : symmTensor field . Prefixes: &#x27;s&#x27; (surface) or &#x27;p&#x27; (point). For example, psfield for a point scalar field
核验范围：源码包含此目标；当前虚拟机未找到可执行文件；未据此宣称完整算例通过。
已记录的选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamexprparserinfo.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamExprParserInfo
Evidence: not-installed
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamExprParserInfo/foamExprParserInfo.C

未取得运行时帮助。

源码路径：applications/tools/foamExprParserInfo/foamExprParserInfo.C

Display token names or rules for specified expression parsers. In the Lemon grammar, terminals (uppercase) are listed first. Non-terminals (lowercase) are listed second. The current OpenFOAM grammar short naming conventions: - svalue : scalar value - sfield : scalar field - lfield : logic field - vfield : vector field - tfield : tensor field - hfield : sphericalTensor field - yfield : symmTensor field . Prefixes: &#x27;s&#x27; (surface) or &#x27;p&#x27; (point). For example, psfield for a point scalar field</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamExprParserInfo/foamExprParserInfo.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamExprParserInfo/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
