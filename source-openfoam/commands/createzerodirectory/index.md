---
title: "createZeroDirectory · 按求解器模板、湍流模型和 caseProperties 生成初始场"
layout: reference
description: "按求解器模板、湍流模型和 caseProperties 生成初始场。"
cms_slug: "command-createzerodirectory"
---

<p>按求解器模板、湍流模型和 caseProperties 生成初始场。</p><h2>开始前</h2>
<p>已有网格、system/controlDict、system/caseProperties及模型设置；每个实体边界在caseProperties中有对应条件。</p>
<h2>示例 1：生成所需初始字段</h2>
<pre><code class="language-bash">createZeroDirectory
</code></pre>
<p>根据controlDict的application和模型类型选择模板，在0目录生成匹配的场及边界条目。</p>
<h2>示例 2：使用个人模板库</h2>
<pre><code class="language-bash">createZeroDirectory -templateDir ./fieldTemplates
</code></pre>
<p>fieldTemplates具有与官方模板相同的solvers、models和边界模板结构；按自定义模板生成字段。</p>
<h2>示例 3：复制模板后定制</h2>
<pre><code class="language-bash">cp -r "$WM_PROJECT_DIR/etc/caseDicts/createZeroDirectoryTemplates" myTemplates
createZeroDirectory -templateDir ./myTemplates
</code></pre>
<p>先把官方模板复制为可编辑的个人版本，再用它生成场；后续可在该目录调整常用初值或边界模板。</p>
<h2>示例 4：湍流模型切换后重新配场</h2>
<pre><code class="language-bash">createZeroDirectory -case ./case-kOmegaSST
patchSummary -case ./case-kOmegaSST -time 0 -expand
</code></pre>
<p>独立案例已配置kOmegaSST及相应caseProperties；生成所需湍流场，并逐patch检查场类型。</p>
<h2>示例 5：多区域案例生成初值</h2>
<pre><code class="language-bash">createZeroDirectory -case ./heatExchanger
</code></pre>
<p>heatExchanger的求解器模板支持多区域，regionProperties及各区域caseProperties已配置；程序按区域分别生成流体和固体初始场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-templateDir &lt;dir&gt;</code></td><td>从指定位置读取算例设置模板。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createZeroDirectory/boundaryInfo.C">源码与说明</a> · <a href="/assets/command-help/createzerodirectory.txt">帮助文本</a></p>
