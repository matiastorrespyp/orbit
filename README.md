# orbit

Portal de información empresarial.

## Matinal de Peña Flor

Se agregó un motor base para generar la matinal diaria en Markdown usando un archivo de contexto JSON.

```bash
python3 scripts/generar_matinal.py \
  --input data/pena_flor.json \
  --output output/matinal_pena_flor.md
```

Documentación detallada:

- `matinal/README.md`
- `matinal/plantilla_matinal.md`
