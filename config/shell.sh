# Fuente compartida para Bash y Zsh. No contiene rutas ni secretos del dispositivo.
alias gs='git status --short --branch'
alias gl='git log --graph --decorate --oneline -20'
alias gp='git pull --ff-only'

if command -v rg >/dev/null 2>&1; then
  alias findtext='rg'
fi

if command -v python3 >/dev/null 2>&1; then
  alias py='python3'
fi

# Facilita distinguir el proyecto y la rama sin instalar un prompt adicional.
workspace_branch() {
  git symbolic-ref --quiet --short HEAD 2>/dev/null || true
}
