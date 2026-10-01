---
title: "splitMeshRegions  按连通性或 cellZone 拆分网格区域"
layout: reference
description: "各目标区域分别配置字典和场文件。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>各目标区域分别配置字典和场文件。</p><h2>v2512 源码中的用途</h2><p>Splits mesh into multiple regions. Each region is defined as a domain whose cells can all be reached by cell-face-cell walking without crossing - boundary faces - additional faces from faceset (-blockedFaces faceSet). - any face between differing cellZones (-cellZones) Output is: - volScalarField with regions as different scalars (-detectOnly) or - mesh with multiple regions and mapped patches. These patches either cover the whole interface between two region (default) or only part according to faceZones (-useFaceZones) or - mesh with cells put into cellZones (-makeCellZones) Note: - multiple cellZones can be combined into a single region (cluster) for further analysis using the &#x27;addZones&#x27; or &#x27;combineZones&#x27; option: -addZones &#x27;((allSolids zoneA &quot;zoneB.*&quot;)(allFluids none otherZone))&#x27; or -combineZones &#x27;((zoneA &quot;zoneB.*&quot;)(none otherZone)) This can be combined with e.g. &#x27;cellZones&#x27; or &#x27;cellZonesOnly&#x27;. The addZones option supplies the destination region name as first element in the list. The combineZones option synthesises the region name e.g. zoneA_zoneB0_zoneB1 - cellZonesOnly does not do a walk and uses the cellZones only. Use this if you don&#x27;t mind having disconnected domains in a single region. This option requires all cells to be in one (and one only) cellZone. - cellZonesFileOnly behaves like -cellZonesOnly but reads the cellZones from the specified file. This allows one to explicitly specify the region distribution and still have multiple cellZones per region. - prefixRegion prefixes all normal patches with region name (interface (patches already have region name prefix) - Should work in parallel. cellZones can differ on either side of processor boundaries in which case the faces get moved from processor patch to mapped patch. Not very well tested. - If a cell zone gets split into more than one region it can detect the largest matching region (-sloppyCellZones). This will accept any region that covers more than 50% of the zone. It has to be a subset so cannot have any cells in any other zone. - If explicitly a single region has been selected (-largestOnly or -insidePoint) its region name will be either - name of a cellZone it matches to or - &quot;largestOnly&quot; respectively &quot;insidePoint&quot; or - polyMesh::defaultRegion if additionally -overwrite (so it will overwrite the input mesh!) - writes maps like decomposePar back to original mesh: - pointRegionAddressing : for every point in this region the point in the original mesh - cellRegionAddressing : ,, cell ,, cell ,, - faceRegionAddressing : ,, face ,, face in the original mesh + &#x27;turning index&#x27;. For a face in the same orientation this is the original facelabel+1, for a turned face this is -facelabel-1 - boundaryRegionAddressing : for every patch in this region the patch in the original mesh (or -1 if added patch)</p><h2>使用入口</h2><pre><code class="language-bash">splitMeshRegions -cellZones -overwrite</code></pre><h2>使用条件与核对</h2><p>各目标区域分别配置字典和场文件。 用法：splitMeshRegions [选项] 示例：splitMeshRegions -cellZones -overwrite
源码说明：Splits mesh into multiple regions. Each region is defined as a domain whose cells can all be reached by cell-face-cell walking without crossing - boundary faces - additional faces from faceset (-blockedFaces faceSet). - any face between differing cellZones (-cellZones) Output is: - volScalarField with regions as different scalars (-detectOnly) or - mesh with multiple regions and mapped patches. These patches either cover the whole interface between two region (default) or only part according to faceZones (-useFaceZones) or - mesh with cells put into cellZones (-makeCellZones) Note: - multiple cellZones can be combined into a single region (cluster) for further analysis using the &#x27;addZones&#x27; or &#x27;combineZones&#x27; option: -addZones &#x27;((allSolids zoneA &quot;zoneB.*&quot;)(allFluids none otherZone))&#x27; or -combineZones &#x27;((zoneA &quot;zoneB.*&quot;)(none otherZone)) This can be combined with e.g. &#x27;cellZones&#x27; or &#x27;cellZonesOnly&#x27;. The addZones option supplies the destination region name as first element in the list. The combineZones option synthesises the region name e.g. zoneA_zoneB0_zoneB1 - cellZonesOnly does not do a walk and uses the cellZones only. Use this if you don&#x27;t mind having disconnected domains in a single region. This option requires all cells to be in one (and one only) cellZone. - cellZonesFileOnly behaves like -cellZonesOnly but reads the cellZones from the specified file. This allows one to explicitly specify the region distribution and still have multiple cellZones per region. - prefixRegion prefixes all normal patches with region name (interface (patches already have region name prefix) - Should work in parallel. cellZones can differ on either side of processor boundaries in which case the faces get moved from processor patch to mapped patch. Not very well tested. - If a cell zone gets split into more than one region it can detect the largest matching region (-sloppyCellZones). This will accept any region that covers more than 50% of the zone. It has to be a subset so cannot have any cells in any other zone. - If explicitly a single region has been selected (-largestOnly or -insidePoint) its region name will be either - name of a cellZone it matches to or - &quot;largestOnly&quot; respectively &quot;insidePoint&quot; or - polyMesh::defaultRegion if additionally -overwrite (so it will overwrite the input mesh!) - writes maps like decomposePar back to original mesh: - pointRegionAddressing : for every point in this region the point in the original mesh - cellRegionAddressing : ,, cell ,, cell ,, - faceRegionAddressing : ,, face ,, face in the original mesh + &#x27;turning index&#x27;. For a face in the same orientation this is the original facelabel+1, for a turned face this is -facelabel-1 - boundaryRegionAddressing : for every patch in this region the patch in the original mesh (or -1 if added patch)
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-addZones -blockedFaces -case -cellZones -cellZonesFileOnly -cellZonesOnly -combineZones -debug-switch -decomposeParDict -detectOnly -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -insidePoint -largestOnly -lib -makeCellZones -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -prefixRegion -region -roots -sloppyCellZones -useFaceZones -world</p><p>关联配置：<a href="/dictionaries/constant-regionproperties/">regionProperties</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/splitmeshregions.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: splitMeshRegions
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMeshRegions/splitMeshRegions.C


Usage: splitMeshRegions [OPTIONS]
Options:
  -addZones &lt;lists of zones&gt;
                    Combine zones in follow-on analysis
  -blockedFaces &lt;faceSet&gt;
                    Specify additional region boundaries that walking does not
                    cross
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cellZones        Additionally split cellZones off into separate regions
  -cellZonesFileOnly &lt;file&gt;
                    Like -cellZonesOnly, but use specified file
  -cellZonesOnly    Use cellZones only to split mesh into regions; do not use
                    walking
  -combineZones &lt;lists of zones&gt;
                    Combine zones in follow-on analysis
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -detectOnly       Do not write mesh
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -insidePoint &lt;point&gt;
                    Only write region containing point
  -largestOnly      Only write largest region
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -makeCellZones    Place cells into cellZones instead of splitting mesh
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -prefixRegion     Prefix region name to all patches, not just coupling patches
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -sloppyCellZones  Try to match heuristically regions to existing cell zones
  -useFaceZones     Use faceZones to patch inter-region faces instead of single
                    patch
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split mesh into multiple regions (detected by walking across faces)

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMeshRegions/splitMeshRegions.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMeshRegions/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
