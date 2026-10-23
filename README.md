# Entorno de trabajo de Gabriel

Configuración portable para trabajar con **Python, R y Git** en Mac, Linux y Windows. Parte de las herramientas observadas en mi Mac (Cursor, RStudio, Python, aplicaciones de análisis) y deja fuera archivos personales, contraseñas y rutas fijas del equipo.

## Inicio rápido

1. Instala Git y Python 3.8 o superior en el dispositivo. En Windows, usa PowerShell o Git Bash.
2. Clona este repositorio.
3. Revisa el plan sin modificar nada:

   ```sh
   python3 bootstrap.py
   ```

   En Windows usa `py bootstrap.py` si `python3` no está disponible.

4. Aplica la configuración:

   ```sh
   python3 bootstrap.py --apply
   ```

5. Define tu identidad de Git **en cada dispositivo** (no se publica aquí):

   ```sh
   git config --global user.name "Tu nombre"
   git config --global user.email "tu-correo-para-git"
   ```

6. Abre una terminal nueva y comprueba `git status` en un proyecto de prueba.

El instalador hace una copia de seguridad con marca de tiempo antes de editar un archivo existente. Es seguro repetirlo: no duplica las líneas que ya agregó. No instala software ni mueve tus proyectos.

## Qué contiene

| Archivo | Uso |
| --- | --- |
| `bootstrap.py` | Instala los ajustes compartidos en la cuenta local. |
| `config/gitconfig.shared` | Alias y valores de Git sin nombre, correo ni credenciales. |
| `config/shell.sh` | Atajos para Bash y Zsh; detecta herramientas opcionales. |
| `config/Microsoft.PowerShell_profile.ps1` | Atajos equivalentes para PowerShell. |
| `config/cursor-settings.json` | Preferencias sugeridas para Cursor o VS Code. |
| `config/alli-research.md` | Protocolo LABORATORIO ALLI para investigación médica y de biología celular. |
| `Brewfile` | Herramientas de terminal sugeridas para macOS con Homebrew. |
| `.gitignore` | Bloquea credenciales y archivos locales comunes. |
| `papers/` | Plantilla Quarto y flujo de referencias para artículos científicos. |
| `prompts/grill-me-paper.md` | Entrevista crítica para definir y revisar un paper. |

## Papers científicos

Empieza por [la guía de escritura](papers/README.md). Para tus trabajos con datos y análisis en **R o Python**, la ruta sugerida es **Zotero + Quarto**: referencias verificables, texto versionable y resultados reproducibles. Cuando la revista o tus coautores pidan Word, usa **Word + Zotero**. Para una plantilla LaTeX de revista, considera **Overleaf + Zotero**. Elige el formato final según las instrucciones de la revista.

El repositorio incluye una plantilla Quarto y un cuestionario `grill-me` propio para examinar pregunta, diseño, análisis, resultados, límites y afirmaciones antes de redactar. No instala automáticamente herramientas de terceros.

## Aplicaciones y paquetes

El Mac de referencia es Intel y usa macOS 13. Hay instalaciones de Cursor, RStudio, R, Python y otras aplicaciones de análisis. Este repositorio se centra en el trabajo reproducible con código y datos. Mantén tus instaladores, licencias y documentos fuera del repositorio.

- **macOS:** instala [Homebrew](https://brew.sh/) si lo deseas y ejecuta `brew bundle` desde la raíz para instalar el `Brewfile`. Luego instala [Cursor](https://www.cursor.com/), [R](https://cran.r-project.org/) y [RStudio](https://posit.co/download/rstudio-desktop/) desde sus fuentes oficiales según el sistema.
- **Linux:** instala Git, Python 3, R, `ripgrep`, `jq` y `fzf` con el gestor de paquetes de tu distribución. Cursor y RStudio son opcionales.
- **Windows:** instala Git, Python, R y las aplicaciones gráficas desde fuentes oficiales o el gestor de paquetes que ya utilices. Usa PowerShell para ejecutar `py bootstrap.py --apply`.

Los alias funcionan aunque falten `ripgrep` o `fzf`; esas herramientas son opcionales.

## Cursor y VS Code

`config/cursor-settings.json` es una propuesta portable. Revisa y fusiona sus claves con tus ajustes existentes en lugar de reemplazar el archivo completo. Puedes abrirlo desde Cursor con **Preferences: Open User Settings (JSON)**. Incluye guardado automático, formato al guardar y exclusiones de carpetas generadas; los formateadores se instalan por proyecto.

## Un proyecto nuevo

```sh
mkdir mi-proyecto && cd mi-proyecto
git init
python3 -m venv .venv
```

Activa `.venv` con `source .venv/bin/activate` en Bash/Zsh o `.venv\Scripts\Activate.ps1` en PowerShell. Agrega `requirements.txt` o `pyproject.toml` según el proyecto. Para R, registra dependencias en el proyecto cuando sean necesarias; no copies librerías globales entre máquinas.

## Sincronización entre dispositivos

Clona el repositorio en cada equipo y vuelve a ejecutar el instalador después de actualizarlo. Usa Git para código y configuración. Los datos grandes, documentos de trabajo y secretos requieren un almacenamiento apropiado para ellos. Evita subir `.env`, llaves SSH, tokens, bases de datos y archivos de investigación con información sensible.

## Ajustar o deshacer

Edita los archivos en `config/`, haz commit y ejecuta el instalador en cada equipo. El instalador conserva copias de seguridad `*.backup-AAAA...`. Para deshacer, elimina las líneas marcadas `# entorno-gabriel` del perfil de shell o PowerShell y de `~/.codex/AGENTS.md`, y la línea `include.path` correspondiente de `~/.gitconfig`; luego restaura una copia de seguridad si la necesitas.
