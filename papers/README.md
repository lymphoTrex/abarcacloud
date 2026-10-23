# Flujo para papers científicos

Este flujo está pensado para trabajar con datos y análisis en R o Python, y entregar un manuscrito verificable. No presupone una revista ni un estilo de citas.

## Herramientas recomendadas

| Caso | Herramientas | Motivo |
| --- | --- | --- |
| Manuscrito con análisis reproducible | [Quarto](https://quarto.org/docs/manuscripts/) + [Zotero](https://www.zotero.org/) | Integra texto, código, tablas, figuras y citas. |
| Coautores o revista que trabajan en Word | Microsoft Word + [plugin de Zotero](https://www.zotero.org/support/word_processor_plugin_usage) | Citas y bibliografía editables desde el documento. |
| Revista con plantilla LaTeX | [Overleaf](https://www.overleaf.com/) + Zotero | Sigue la plantilla de la revista y permite colaboración. Revisa las condiciones actuales de su integración Git. |
| Claves BibTeX estables | [Better BibTeX](https://github.com/retorquere/zotero-better-bibtex) | Exportación de `.bib` desde Zotero, si tu flujo la necesita. |

Repositorios de origen: [Quarto CLI](https://github.com/quarto-dev/quarto-cli), [Better BibTeX](https://github.com/retorquere/zotero-better-bibtex). Para el enfoque de preguntas «Grill Me», mira [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) y [Jekudy/grillme-skill](https://github.com/Jekudy/grillme-skill). El archivo de este repositorio es una adaptación original orientada a papers; no instala ni copia esos proyectos.

## Secuencia sugerida

1. Define pregunta, población, variables, diseño y revista objetivo. Usa `../prompts/grill-me-paper.md` antes de empezar a escribir.
2. Organiza las fuentes en Zotero. Comprueba DOI, autores, año, título y tipo de estudio en cada referencia. No cites artículos que no hayas verificado.
3. Copia `paper.qmd` y `references.bib` a un repositorio **separado para cada estudio**. Añade las figuras y los datos permitidos por tu protocolo.
4. Redacta Métodos y Resultados a partir del análisis real; registra decisiones, exclusiones y versiones de software. Después escribe Introducción, Discusión y Resumen.
5. Contrasta cada afirmación con su fuente o resultado. Revisa las normas de la revista, los requisitos éticos y las declaraciones que correspondan antes de enviar.

Renderiza con `quarto render paper.qmd` tras instalar Quarto. La plantilla evita resultados y referencias ficticias; debes completarla con evidencia de tu propio estudio.

## Qué guardar en Git

Guarda `.qmd`, scripts, bibliografía exportada, figuras autorizadas y archivos de entorno del proyecto. Mantén fuera datos identificables de participantes, credenciales, borradores confidenciales de coautores y documentos sujetos a acuerdos de la revista. Consulta las reglas de tu institución y del estudio antes de publicar un repositorio de investigación.
