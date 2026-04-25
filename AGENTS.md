# Guía para agentes (TattooTycoon)

Este repositorio sigue la estructura definida en `project_structure.md`.

## Dónde leer/escribir
- `scenes/`: escenas de Godot (`.tscn`, `.scn`)
- `scripts/`: lógica en GDScript (`.gd`)
- `ui/`: UI (escenas y scripts UI)
- `assets/`: gráficos/audio/fuentes (solo ficheros de assets)
- `references/`: material de referencia (no se usa en runtime)

## Reglas de trabajo
- No mezclar UI con lógica: la lógica va en `scripts/` y se referencia desde `ui/`/`scenes/`.
- Scripts modulares y reutilizables: preferir composición y clases pequeñas.
- Nombres en `snake_case` para archivos y nodos cuando aplique.

## Límites
- No escribir fuera de estas carpetas salvo ficheros de proyecto de alto nivel (`README.md`, `project_structure.md`, configuración).
- Evitar tocar `venv/` y cualquier carpeta de dependencias.
