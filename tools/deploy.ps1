$ErrorActionPreference = 'Stop'
$siteRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $siteRoot
$nodeExe = (Get-Command node -ErrorAction SilentlyContinue).Source
if (-not $nodeExe) { $nodeExe = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' }
if (-not (Test-Path -LiteralPath $nodeExe)) { throw 'Please install Node.js 20.19 or newer.' }
& $nodeExe (Join-Path $siteRoot 'node_modules\hexo\bin\hexo') generate
if ($LASTEXITCODE -ne 0) { throw 'Hexo build failed.' }
& $nodeExe (Join-Path $siteRoot 'node_modules\hexo\bin\hexo') deploy
if ($LASTEXITCODE -ne 0) { throw 'Hexo deployment failed.' }
