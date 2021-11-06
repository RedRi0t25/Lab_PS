#Practica9
#DNS
$dns =  ipconfig /displaydns 
$Path = "C:\Users\vgrob\Downloads\laboratorio xd\Practica010\RDNS.txt"
$codificado = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($dns))
Set-Content -Value "$codificado" -Path $Path
