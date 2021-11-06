#nmap
#ip local 
$local = Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias Wi-Fi
$ip = $local.IPAddress

#ip publica
$publica = Invoke-RestMethod ifconfig.me

#nmap a un segmento de la red 
$segmento_ip = nmap -sP $ip/24

$hola = nmap $ip

#nmap a una ip publica Comprueba si hay un servidor identd (auth) que está falsificando sus respuestas.
$ip_publica = nmap --script=auth-spoof www.facebook.com


$1 = "Información obtenida: Ip local: ", [string]$ip, "`n`nIp pública: ", [string]$publica
$2 = "`n`nSegmento de red privada:`n", [string]$segmento_ip
$3 = "`n`nNmap a una ip publica:`n", [string]$ip_publica 
$4 = "`n`nNmap a una ip del segmento:`n", [string]$hola

$texto = [string]$1, [string]$2, [string]$3, [string]$4
$texto_final = [string]$texto

$codificacion = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($texto_final))
try{
    Set-Content -Value "$codificacion" -Path C:\Users\vgrob\Downloads\laboratorio xd\nmap_resul.txt
}   catch{
           $Path_Personal = Read-Host "Inserta el path"
           Set-Content -Value "$codificacion" -Path $Path_Personal
}
Write-Host "Información enviada"