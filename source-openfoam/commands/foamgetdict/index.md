---
title: "foamGetDict · 从模板目录复制字典到当前算例"
layout: reference
description: "从模板目录复制字典到当前算例。"
cms_slug: "command-foamgetdict"
---

<p>从模板目录复制字典到当前算例。</p><h2>复制常用配置模板</h2>
<pre><code class="language-bash">foamGetDict decomposeParDict
foamGetDict meshQualityDict
</code></pre>
<p>模板来自 OpenFOAM 的 <code>etc/caseDicts</code> 或用户、站点配置目录。多数 system 字典写到 <code>system</code>，物性类文件按脚本规则选择目录。</p>
<h2>指定输出目录</h2>
<pre><code class="language-bash">mkdir -p templates
foamGetDict -target templates snappyHexMeshDict
</code></pre>
<p>把模板保存到单独的 <code>templates</code> 目录，便于与当前算例比较。模板中的模型、几何和数值需按算例填写。</p>
<h2>替换已有模板</h2>
<pre><code class="language-bash">foamGetDict -force decomposeParDict
</code></pre>
<p><code>-force</code> 允许覆盖同名文件。需要保留原设置时，先复制备份，再比较新模板中的条目。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-ext</td><td>&lt;ext&gt;       File extension</td></tr><tr><td>-cfg</td><td>Same as &#x27;-ext cfg&#x27; for &#x27;.cfg&#x27; files</td></tr><tr><td>-f | -force</td><td>Force overwrite of existing files</td></tr><tr><td>-no-ext</td><td>Files without extension</td></tr><tr><td>-target &lt;dir&gt;</td><td>Target directory (default: system, or auto-detected)</td></tr><tr><td>-with-api=NUM</td><td>Alternative api value for searching</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamGetDict [OPTIONS] &lt;file&gt;
options:
  -case &lt;dir&gt;       Alternative case directory, default is the cwd
  -ext  &lt;ext&gt;       File extension
  -cfg              Same as &#x27;-ext cfg&#x27; for &#x27;.cfg&#x27; files
  -f | -force       Force overwrite of existing files
  -no-ext           Files without extension
  -target &lt;dir&gt;     Target directory (default: system, or auto-detected)
  -with-api=NUM     Alternative api value for searching
  -help             Display short help and exit

Find an OpenFOAM dictionary file from etc/caseDicts/ or {user,site} locations
and copy it into the case directory. For example,

    foamGetDict decomposeParDict
    foamGetDict extrudeMeshDict
    foamGetDict createPatchDict
    foamGetDict surfaces</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamGetDict">源码与说明</a> · <a href="/assets/command-help/foamgetdict.txt">帮助文本</a></p>
