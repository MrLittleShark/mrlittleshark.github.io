---
title: "foamUpdateCaseFileHeader · 更新算例文件头并合并连续空行"
layout: reference
description: "更新算例文件头并合并连续空行。"
cms_slug: "command-foamupdatecasefileheader"
---

<p>更新算例文件头并合并连续空行。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 原地更新文件头并合并连续空行，只在需要整理的算例副本中操作。它不转换字典条目或物理模型。</p>
<h2>示例 1：更新一份控制文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader" caseA/system/controlDict
</code></pre>
<p>在现有头部格式基础上写入当前 API 版本信息。</p>
<h2>示例 2：更新三份系统字典</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader" caseA/system/controlDict caseA/system/fvSchemes caseA/system/fvSolution
</code></pre>
<p>一次处理多个文本字典。</p>
<h2>示例 3：显式指定版本头</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader" -version=2512 caseA/system/controlDict
</code></pre>
<p>将头部版本号设为 2512，正文求解设置保持原意义。</p>
<h2>示例 4：处理整个 system 目录</h2>
<pre><code class="language-bash">find caseA/system -type f -exec "$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader" {} +
</code></pre>
<p>只选择该目录中的普通文件，批量更新符合规则的文件头。</p>
<h2>示例 5：更新后查看差异</h2>
<pre><code class="language-bash">cp caseA/system/controlDict controlDict.before
"$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader" caseA/system/controlDict
diff -u controlDict.before caseA/system/controlDict
</code></pre>
<p>比较头部与空行变化，便于在版本库提交前阅读。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-version=VER</code></td><td>Specifies version for header (default: $FOAM_API)</td></tr><tr><td><code>-h | -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamUpdateCaseFileHeader [OPTION] &lt;file1&gt; ... &lt;fileN&gt;

options:
  -version=VER      Specifies version for header (default: $FOAM_API)
  -h | -help        Print the usage

Updates the header of application files and removes consecutive blank lines.
By default, writes current OpenFOAM API number version in the header.
An alternative version can be specified with the -version option.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamUpdateCaseFileHeader">源码与说明</a> · <a href="/assets/command-help/foamupdatecasefileheader.txt">帮助文本</a></p>
