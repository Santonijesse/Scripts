param(
    [Parameter(Mandatory=$true)]
    [string]$ScriptName
)

# Find the script in gen/ or temp/ directories
$scriptPath = $null
foreach ($dir in @("gen", "temp")) {
    $candidate = Join-Path $PSScriptRoot "$dir\$ScriptName.py"
    if (Test-Path $candidate) {
        $scriptPath = $candidate
        break
    }
}

if (-not $scriptPath) {
    Write-Error "Script '$ScriptName.py' not found in gen/ or temp/ directories."
    exit 1
}

Write-Host "Running $scriptPath 10 times with 3s delay..."

for ($i = 1; $i -le 10; $i++) {
    Write-Host "`n--- Run $i / 10 ---"
    python $scriptPath
    if ($i -lt 10) {
        Start-Sleep -Seconds 3
    }
}

Write-Host "`nDone."
