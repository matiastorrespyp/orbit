#!/usr/bin/env python3
"""Motor base para generar una matinal empresarial en Markdown."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def cargar_contexto(ruta: Path) -> dict:
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def lista_a_markdown(items: list[str]) -> str:
    if not items:
        return "- Sin información disponible"
    return "\n".join(f"- {item}" for item in items)


def construir_matinal(contexto: dict, fecha: str | None = None) -> str:
    nombre = contexto.get("nombre", "Empresa")
    comuna = contexto.get("comuna", "No definida")
    fecha_actual = fecha or str(date.today())

    encabezado = f"# Matinal de {nombre}\n\n"
    meta = f"**Fecha:** {fecha_actual}  \n**Comuna:** {comuna}\n\n"

    secciones = {
        "## 1) Resumen ejecutivo": contexto.get("resumen", []),
        "## 2) Agenda del día": contexto.get("agenda", []),
        "## 3) Indicadores clave": contexto.get("indicadores", []),
        "## 4) Alertas y riesgos": contexto.get("alertas", []),
        "## 5) Oportunidades": contexto.get("oportunidades", []),
        "## 6) Próximas acciones": contexto.get("acciones", []),
    }

    cuerpo = []
    for titulo, items in secciones.items():
        cuerpo.append(f"{titulo}\n{lista_a_markdown(items)}\n")

    return encabezado + meta + "\n".join(cuerpo).strip() + "\n"


def guardar_salida(contenido: str, salida: Path) -> None:
    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def parsear_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una matinal de empresa en formato Markdown"
    )
    parser.add_argument("--input", required=True, help="Ruta al JSON de contexto")
    parser.add_argument("--output", required=True, help="Ruta de salida Markdown")
    parser.add_argument(
        "--fecha",
        required=False,
        help="Fecha opcional en formato YYYY-MM-DD. Si no se indica usa la fecha de hoy.",
    )
    return parser.parse_args()


def main() -> None:
    args = parsear_args()
    contexto = cargar_contexto(Path(args.input))
    contenido = construir_matinal(contexto, fecha=args.fecha)
    guardar_salida(contenido, Path(args.output))
    print(f"Matinal generada en: {args.output}")


if __name__ == "__main__":
    main()
