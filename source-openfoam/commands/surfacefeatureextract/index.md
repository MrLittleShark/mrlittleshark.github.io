---
title: "surfaceFeatureExtract  提取几何表面特征线"
layout: reference
description: "读取 surfaceFeatureExtractDict，生成 eMesh 等特征文件。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 surfaceFeatureExtractDict，生成 eMesh 等特征文件。</p><h2>v2512 源码中的用途</h2><p>Extracts and writes surface features to file. All but the basic feature extraction is a work-in-progress. The extraction process is driven by the \a system/surfaceFeatureExtractDict dictionary, but the \a -dict option can be used to define an alternative location. The \a system/surfaceFeatureExtractDict dictionary contains entries for each extraction process. The name of the individual dictionary is used to load the input surface (found under \a constant/triSurface) and also as the basename for the output. If the \c surfaces entry is present in a sub-dictionary, it has absolute precedence over a surface name deduced from the dictionary name. If the dictionary name itself does not have an extension, the \c surfaces entry becomes mandatory since in this case the dictionary name cannot represent an input surface file (ie, there is no file extension). The \c surfaces entry is a wordRe list, which allows loading and combining of multiple surfaces. Any exactly specified surface names must exist, but surfaces selected via regular expressions need not exist. The selection mechanism preserves order and is without duplicates. For example,</p><h2>使用入口</h2><pre><code class="language-bash">surfaceFeatureExtract</code></pre><h2>使用条件与核对</h2><p>读取 surfaceFeatureExtractDict，生成 eMesh 等特征文件。 用法：surfaceFeatureExtract [-dict 文件] 示例：surfaceFeatureExtract
源码说明：Extracts and writes surface features to file. All but the basic feature extraction is a work-in-progress. The extraction process is driven by the \a system/surfaceFeatureExtractDict dictionary, but the \a -dict option can be used to define an alternative location. The \a system/surfaceFeatureExtractDict dictionary contains entries for each extraction process. The name of the individual dictionary is used to load the input surface (found under \a constant/triSurface) and also as the basename for the output. If the \c surfaces entry is present in a sub-dictionary, it has absolute precedence over a surface name deduced from the dictionary name. If the dictionary name itself does not have an extension, the \c surfaces entry becomes mandatory since in this case the dictionary name cannot represent an input surface file (ie, there is no file extension). The \c surfaces entry is a wordRe list, which allows loading and combining of multiple surfaces. Any exactly specified surface names must exist, but surfaces selected via regular expressions need not exist. The selection mechanism preserves order and is without duplicates. For example,
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -opt-switch</p><p>关联配置：<a href="/dictionaries/system-surfacefeatureextractdict/">surfaceFeatureExtractDict</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacefeatureextract.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceFeatureExtract
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureExtract/surfaceFeatureExtract.C


Usage: surfaceFeatureExtract [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Read surfaceFeatureExtractDict from specified location
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Extract and write surface feature lines to file.
Feature line extraction only valid on closed manifold surfaces.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureExtract/surfaceFeatureExtract.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureExtract/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
