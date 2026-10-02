---
title: "isTrue · 把 on、yes、true 等开关值转换为 shell 返回码"
layout: reference
description: "把 on、yes、true 等开关值转换为 shell 返回码。"
cms_slug: "command-istrue"
---

<p>把 on、yes、true 等开关值转换为 shell 返回码。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 true/yes/on/t/y 返回 0，false/no/off/f/n 返回 1；其他字符串返回 2。示例采用小写值。</p>
<h2>示例 1：读取开关文字</h2>
<pre><code class="language-bash">if isTrue on; then echo "enabled"; fi
</code></pre>
<p>on 被识别为开启，输出 enabled。</p>
<h2>示例 2：处理关闭开关</h2>
<pre><code class="language-bash">if isTrue false; then echo "enabled"; else echo "disabled"; fi
</code></pre>
<p>false 返回 1，进入关闭分支。</p>
<h2>示例 3：识别无效输入</h2>
<pre><code class="language-bash">isTrue maybe
status=$?
printf 'status=%s\n' "$status"
</code></pre>
<p>普通终端中执行，得到 2；该状态区分未知值与明确关闭。</p>
<h2>示例 4：从字典读取开关</h2>
<pre><code class="language-bash">cd caseA
if isTrue -dict system/controlDict -entry runTimeModifiable; then echo "runtime editing enabled"; fi
</code></pre>
<p>-dict 将其余参数交给 foamDictionary，再判断实际条目值。</p>
<h2>示例 5：用配置控制后处理</h2>
<pre><code class="language-bash">printf 'doPostProcess yes;\n' &gt; workflowDict
if isTrue -dict workflowDict -entry doPostProcess; then checkMesh -case caseA; fi
</code></pre>
<p>创建自己的工作流程开关，yes 使网格检查分支执行；no 会跳过该步骤。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
