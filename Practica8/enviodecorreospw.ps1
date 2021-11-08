$Python='python.exe'
$Script = Read-Host -Prompt "Ruta del programa"
#$Path = Read-Host -Prompt "Ruta del archivo txt"

$url = Read-Host -Prompt "URL"

$usr = Read-Host -Prompt "Correo: "

$receptor = Read-Host -Prompt "Correo destino: "

$mensaje = Read-Host -Prompt "Escriba el mensaje: "

$asunto = Read-Host -Prompt "Escriba el asunto: "

$contraseña = Read-Host -Prompt "PassWord: "


try {
     & $Python $Script -url $url -usr $usr -rec $recr -msj $msj -asunto $asunto -pw $pw
} catch {
    Write-Host "Ocurrio un error :(. Verifique la direccion del archivo o su nombr"
}