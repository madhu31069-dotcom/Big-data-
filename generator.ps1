$status = @("SUCCESS","CANCELLED","RETURNED")
$users = @("Arun","Priya","Rahul","Divya","Kumar","Anu","Ravi","Karthik")

$id = 1000

while ($true)
{
    $id++

    $s = $status | Get-Random
    $u = $users | Get-Random

    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ORDER_ID=$id USER=$u STATUS=$s"

    $line | Add-Content .\meesho.log

    switch ($s)
    {
        "SUCCESS" {
            $line | Add-Content .\success.log
        }

        "CANCELLED" {
            $line | Add-Content .\cancelled.log
        }

        "RETURNED" {
            $line | Add-Content .\returned.log
        }
    }

    Start-Sleep -Seconds 2
}