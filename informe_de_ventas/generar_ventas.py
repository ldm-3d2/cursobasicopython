"""Genera informe_de_ventas/ventas.csv: entre 1 y 3 ventas por mes."""

import csv
import random
from collections import Counter
from datetime import date
from pathlib import Path

random.seed(42)
PRODUCTOS = [
    "Libreta A4",
    "Boligrafo azul",
    "Cuaderno espiral",
    "Mochila escolar",
    "Regla 30cm",
    "Goma de borrar",
    "Marcadores",
]

DIR = Path(__file__).resolve().parent
CSV_PATH = DIR / "ventas.csv"


def main() -> None:
    rows: list[dict[str, object]] = []
    for mes in range(1, 13):
        n = random.randint(1, 3)
        dias_usados: set[int] = set()
        for _ in range(n):
            while True:
                d = random.randint(1, 28)
                if d not in dias_usados:
                    dias_usados.add(d)
                    break
            fecha = date(2026, mes, d)
            rows.append(
                {
                    "fecha": fecha.strftime("%Y-%m-%d"),
                    "producto": random.choice(PRODUCTOS),
                    "cantidad": random.randint(1, 15),
                    "precio": round(random.uniform(4.5, 120.0), 2),
                }
            )

    rows.sort(key=lambda r: str(r["fecha"]))

    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["fecha", "producto", "cantidad", "precio"]
        )
        w.writeheader()
        w.writerows(rows)

    por_mes = Counter(str(r["fecha"])[:7] for r in rows)
    assert all(1 <= por_mes[k] <= 3 for k in por_mes)
    print(f"Escrito: {CSV_PATH} ({len(rows)} filas)")
    print("Ventas por mes:", dict(sorted(por_mes.items())))


if __name__ == "__main__":
    main()
