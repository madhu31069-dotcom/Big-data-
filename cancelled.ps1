Get-Content .\meesho.log -Wait |
Where-Object { $_ -match "CANCELLED" } |
ForEach-Object {
    Write-Host $_
}