function validacion 
{
param([Parameter(Mandatory=$true, valueFromPipeline=$true)][string[]][allowEmptyString()]$user,$Pass)
begin{Write-Host "Login"}
process
{
if($user -eq "Roberto" -and $Pass -eq "Contraseña") {Write-Host "User correcto"}
else{Write-Host "User invalido"}
}
end{Write-Host "Fin de login"}
}
validacion Roberto Contraseña