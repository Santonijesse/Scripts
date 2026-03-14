# compare_ui_xml.ps1
# Compares before/after UI XML captures for each app in moto_15 and gal_16.
# Outputs one diff file per app per device, with test number annotations.
# Uses LCS-based diff so shifted/unchanged lines are not reported as changes.

param (
    [string]$RootDir = $PSScriptRoot
)

function Get-LcsDiff {
    param([string[]]$Before, [string[]]$After)

    $n = $Before.Count
    $m = $After.Count

    # Build LCS DP table
    $dp = New-Object 'int[,]' ($n + 1), ($m + 1)
    for ($i = 1; $i -le $n; $i++) {
        for ($j = 1; $j -le $m; $j++) {
            if ($Before[$i - 1] -eq $After[$j - 1]) {
                $dp[$i, $j] = $dp[($i - 1), ($j - 1)] + 1
            } else {
                $up   = $dp[($i - 1), $j]
                $left = $dp[$i, ($j - 1)]
                $dp[$i, $j] = [Math]::Max($up, $left)
            }
        }
    }

    # Backtrack to produce diff lines
    $stack = [System.Collections.Generic.Stack[string]]::new()
    $i = $n; $j = $m
    while ($i -gt 0 -or $j -gt 0) {
        if ($i -gt 0 -and $j -gt 0 -and $Before[$i - 1] -eq $After[$j - 1]) {
            $i--; $j--   # unchanged line — skip
        } elseif ($j -gt 0 -and ($i -eq 0 -or $dp[$i, ($j - 1)] -ge $dp[($i - 1), $j])) {
            $stack.Push("+ $($After[$j - 1])")
            $j--
        } else {
            $stack.Push("- $($Before[$i - 1])")
            $i--
        }
    }

    $result = [System.Collections.Generic.List[string]]::new()
    while ($stack.Count -gt 0) { $result.Add($stack.Pop()) }
    return $result
}

$devices = @("moto_15", "gal_16")
$outputBase = Join-Path $RootDir "ui_xml_diffs"

foreach ($device in $devices) {
    $uiXmlBase = Join-Path $RootDir "$device\ui_xml"
    if (-not (Test-Path $uiXmlBase)) {
        Write-Host "[$device] ui_xml directory not found, skipping." -ForegroundColor Yellow
        continue
    }

    $outputDir = Join-Path $outputBase $device
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

    $appDirs = Get-ChildItem -Path $uiXmlBase -Directory | Sort-Object Name

    foreach ($appDir in $appDirs) {
        $app = $appDir.Name
        $appPath = $appDir.FullName

        # Find all "before" files and pair them with matching "after" files
        $beforeFiles = Get-ChildItem -Path $appPath -Filter "*_before_*.xml" | Sort-Object {
            if ($_.BaseName -match '_before_(\d+)$') { [int]$Matches[1] } else { 0 }
        }

        if ($beforeFiles.Count -eq 0) { continue }

        $outputFile = Join-Path $outputDir "$app`_diffs.txt"
        $outputLines = [System.Collections.Generic.List[string]]::new()
        $anyDiffs = $false

        foreach ($beforeFile in $beforeFiles) {
            if ($beforeFile.BaseName -notmatch '_before_(\d+)$') { continue }
            $testNum = $Matches[1]

            $afterName = $beforeFile.Name -replace '_before_', '_after_'
            $afterFile = Join-Path $appPath $afterName

            if (-not (Test-Path $afterFile)) {
                $outputLines.Add("=== Test $testNum : after file missing ($afterName) ===")
                $outputLines.Add("")
                continue
            }

            $beforeLines = Get-Content $beforeFile
            $afterLines  = Get-Content $afterFile

            $diffLines = Get-LcsDiff -Before $beforeLines -After $afterLines

            if ($diffLines.Count -gt 0) {
                $anyDiffs = $true
                $outputLines.Add("=== Test $testNum ===")
                $outputLines.Add("  Before: $($beforeFile.Name)")
                $outputLines.Add("  After : $afterName")
                $outputLines.Add("")
                foreach ($line in $diffLines) {
                    $outputLines.Add($line)
                }
                $outputLines.Add("")
            }
        }

        if ($anyDiffs) {
            $outputLines | Set-Content -Path $outputFile -Encoding UTF8
            Write-Host "[$device] $app -> $($outputFile | Split-Path -Leaf)" -ForegroundColor Green
        } else {
            Write-Host "[$device] $app -> no differences found" -ForegroundColor DarkGray
        }
    }
}

Write-Host "`nDone. Diffs saved to: $outputBase" -ForegroundColor Cyan
