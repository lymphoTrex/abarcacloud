# Entorno compartido para PowerShell. Sin datos específicos del equipo.
function gs { git status --short --branch }
function gl { git log --graph --decorate --oneline -20 }
function gp { git pull --ff-only }
function findtext {
    if (Get-Command rg -ErrorAction SilentlyContinue) { rg @args }
    else { Write-Error 'Instala ripgrep para usar findtext.' }
}
