$ErrorActionPreference = 'Stop'
$siteRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $siteRoot
$nodeExe = (Get-Command node -ErrorAction SilentlyContinue).Source
if (-not $nodeExe) {
    $nodeExe = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe'
}
if (-not (Test-Path -LiteralPath $nodeExe)) { throw 'Please install Node.js 20 or newer.' }
& $nodeExe (Join-Path $siteRoot 'node_modules\hexo\bin\hexo') generate
if ($LASTEXITCODE -ne 0) { throw 'Hexo build failed.' }
Write-Host 'Open http://localhost:4173 in your browser. Press Ctrl+C to stop.'
& $nodeExe (Join-Path $PSScriptRoot 'serve.mjs')
