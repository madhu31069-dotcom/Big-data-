Get-Content .\meesho.log -Wait |
Where-Object { $_ -match "RETURNED" } |
ForEach-Object {
    Write-Host $_
}