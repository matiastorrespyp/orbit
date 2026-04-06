# Matinal de Peña Flor

Este módulo reutiliza el **motor base de matinal** para producir un informe diario en Markdown.

## Estructura

- `scripts/generar_matinal.py`: motor de generación.
- `data/pena_flor.json`: contexto inicial para Peña Flor.
- `output/matinal_pena_flor.md`: ejemplo de salida.

## Uso

```bash
python3 scripts/generar_matinal.py \
  --input data/pena_flor.json \
  --output output/matinal_pena_flor.md
```

También puedes indicar una fecha manual:

```bash
python3 scripts/generar_matinal.py \
  --input data/pena_flor.json \
  --output output/matinal_pena_flor.md \
  --fecha 2026-04-06
```
