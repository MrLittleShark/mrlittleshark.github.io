---
title: "foamCleanPolyMesh · -dry-run 预览清理范围，移除该选项后执行删除"
layout: reference
description: "-dry-run 预览清理范围，移除该选项后执行删除。"
cms_slug: "command-foamcleanpolymesh"
---

<p>-dry-run 预览清理范围，移除该选项后执行删除。</p><h2>用法</h2><pre><code class="language-bash">foamCleanPolyMesh -dry-run</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">foamCleanPolyMesh -dry-run -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-dry-run | -n</td><td>report actions but do not remove</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanPolyMesh [OPTION]
options:
  -case &lt;dir&gt;           case directory, default is the cwd
  -allRegions           all mesh regions
  -region &lt;name&gt;        mesh region
  -dry-run | -n         report actions but do not remove
  -help                 print the usage

Remove the contents of the constant/polyMesh directory as per the
Foam::polyMesh::removeFiles() method.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPolyMesh">源码与说明</a> · <a href="/assets/command-help/foamcleanpolymesh.txt">帮助文本</a></p>
