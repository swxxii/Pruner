#! /usr/bin/pwsh
Clear-Host
##########################################################################
# Pruner.ps1 - https://github.com/swxxii/Pruner
# A PowerShell script to remove completed torrents from qBittorrent 
# ########################################################################

#   CONFIGURATION

# Remove torrents once completed for this many minutes
$PruneAfter = 10

# Change to the IP and Port of your qBittorrent server
$Server = "10.0.0.4:8081"

#   MAIN SCRIPT EXECUTION

$OlderThan = Get-Date (Get-Date).AddMinutes($PruneAfter * -1)

$Result = Invoke-RestMethod -Uri http://$Server/query/torrents?filter=completed

foreach ($torrent in $result) {
    $fin = [timezone]::CurrentTimeZone.ToLocalTime((Get-Date 01.01.1970) + ([System.TimeSpan]::fromseconds($torrent.completion_on)))
    $prune = ($fin -lt $OlderThan)
    Write-Output $torrent.name
    Write-Output ('Hash = ' + $torrent.hash)
    Write-Output ('Finished on ' + $fin + ' [' + $torrent.completion_on + ']')
    Write-Output "Prune = $prune"
    Write-Output ""

    If ($Fin) {
        $Body = ('hashes=' + $torrent.hash)
        Invoke-RestMethod -Method Post -Uri http://$Server/command/delete -Body $Body
    }
}

