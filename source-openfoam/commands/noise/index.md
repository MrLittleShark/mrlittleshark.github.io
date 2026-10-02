---
title: "noise · 对压力时间信号或表面压力数据做频谱与声压级分析"
layout: reference
description: "对压力时间信号或表面压力数据做频谱与声压级分析。"
cms_slug: "command-noise"
---

<p>对压力时间信号或表面压力数据做频谱与声压级分析。</p><h2>开始前</h2>
<p>system/noiseDict已选择模型、输入文件、列或表面格式，以及采样和窗口设置；输入压力单位与rhoRef约定匹配。</p>
<h2>示例 1：执行默认噪声分析</h2>
<pre><code class="language-bash">noise
</code></pre>
<p>读取noiseDict和压力数据，计算模型支持的频谱、功率谱或声压级，写到配置的输出位置。</p>
<h2>示例 2：选择另一测点方案</h2>
<pre><code class="language-bash">noise -dict system/noise-probe2Dict
</code></pre>
<p>替代字典指定第二测点数据和相同处理设置，便于比较不同位置的频谱峰值。</p>
<h2>示例 3：增加FFT采样长度</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry N -set 2048
noise
</code></pre>
<p>N设为2048，输入数据须足以覆盖窗口；在采样频率固定时，较长窗口提高频率分辨率。</p>
<h2>示例 4：只分析指定频段</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry minFreq -set 100
foamDictionary system/noiseDict -entry maxFreq -set 2000
noise
</code></pre>
<p>将关注频率设为100至2000Hz，检查该范围内的谱峰；上界应处于输入采样可解析范围。</p>
<h2>示例 5：比较A计权声压级</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry SPLweighting -set dBA
noise
</code></pre>
<p>在其他设置不变时采用A计权，得到按听觉频率响应加权的声压级，适合与未计权dB结果比较。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-noisedict/">noiseDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: noise [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative noiseDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Perform noise analysis of pressure data

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/noise/noise.C">源码与说明</a> · <a href="/assets/command-help/noise.txt">帮助文本</a></p>
