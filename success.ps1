Get-Content .\meesho.log -Wait |
Where-Object { $_ -match "SUCCESS" } |
ForEach-Object {
    Write-Host $_
}
