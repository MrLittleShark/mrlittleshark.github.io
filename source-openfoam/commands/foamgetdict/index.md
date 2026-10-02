---
title: "foamGetDict · 从模板目录复制字典到当前算例"
layout: reference
description: "从模板目录复制字典到当前算例。"
cms_slug: "command-foamgetdict"
---

<p>从模板目录复制字典到当前算例。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在个人工作目录中准备 caseA 算例副本。新目标目录使用未占用的名称。</p>
<h2>示例 1：取得并行分解模板</h2>
<pre><code class="language-bash">foamGetDict -case caseA decomposeParDict
</code></pre>
<p>复制模板到 caseA/system/decomposeParDict，随后填写分区数和方法。</p>
<h2>示例 2：取得网格质量模板</h2>
<pre><code class="language-bash">foamGetDict -case caseA meshQualityDict
</code></pre>
<p>创建网格质量控制文件，可供 snappyHexMeshDict 通过 include 引用。</p>
<h2>示例 3：取得切面采样配置</h2>
<pre><code class="language-bash">foamGetDict -case caseA surfaces
</code></pre>
<p>获取函数对象模板，输出位置由脚本按模板类别选择；需再设置采样面和字段。</p>
<h2>示例 4：把模板集中到目录</h2>
<pre><code class="language-bash">mkdir -p templates
foamGetDict -target templates createPatchDict
</code></pre>
<p>-target 指定输出目录，便于比较模板后再放入算例。</p>
<h2>示例 5：更新已有字典</h2>
<pre><code class="language-bash">cp caseA/system/decomposeParDict caseA/system/decomposeParDict.before
foamGetDict -force -case caseA decomposeParDict
</code></pre>
<p>先备份再使用 -force 允许覆盖，新的分区设置仍需按算例填写。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-ext</code></td><td>&lt;ext&gt;       File extension</td></tr><tr><td><code>-cfg</code></td><td>Same as &#x27;-ext cfg&#x27; for &#x27;.cfg&#x27; files</td></tr><tr><td><code>-f | -force</code></td><td>Force overwrite of existing files</td></tr><tr><td><code>-no-ext</code></td><td>Files without extension</td></tr><tr><td><code>-target &lt;dir&gt;</code></td><td>Target directory (default: system, or auto-detected)</td></tr><tr><td><code>-with-api=NUM</code></td><td>Alternative api value for searching</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamGetDict [OPTIONS] &lt;file&gt;
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
