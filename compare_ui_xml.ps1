# compare_ui_xml.ps1
# Compares before/after UI XML captures for each app in moto_15 and gal_16.
# Outputs one diff file per app per device, with test number annotations.

param (
    [string]$RootDir = $PSScriptRoot
)

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

            # Build line-by-line diff
            $maxLen = [Math]::Max($beforeLines.Count, $afterLines.Count)
            $diffLines = [System.Collections.Generic.List[string]]::new()

            for ($i = 0; $i -lt $maxLen; $i++) {
                $b = if ($i -lt $beforeLines.Count) { $beforeLines[$i] } else { $null }
                $a = if ($i -lt $afterLines.Count)  { $afterLines[$i]  } else { $null }

                if ($b -ne $a) {
                    if ($null -ne $b) { $diffLines.Add("- $b") }
                    if ($null -ne $a) { $diffLines.Add("+ $a") }
                }
            }

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
