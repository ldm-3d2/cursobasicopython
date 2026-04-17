"""
Análisis de ventas desde ventas.csv: agregados, rankings y gráficos.
"""

import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DIR = Path(__file__).resolve().parent
CSV_PATH = DIR / "ventas.csv"
OUT_MES = DIR / "ventas_por_mes.png"
OUT_TOP5 = DIR / "top5_productos_ingresos.png"


def main() -> None:
    # 1. Cargar datos del CSV (ventas.csv)
    df = pd.read_csv(CSV_PATH, parse_dates=["fecha"])
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce")
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")
    if df["cantidad"].isna().any() or df["precio"].isna().any():
        raise ValueError("Hay valores no numéricos en cantidad o precio.")
    df["cantidad"] = df["cantidad"].astype(int)
    df["precio"] = df["precio"].astype(float)

    print("Tipos de columnas:")
    print(df.dtypes)
    print()

    df["ingreso_linea"] = df["cantidad"] * df["precio"]

    # 2. Calcular ventas totales por mes
    ventas_por_mes = (
        df.groupby(df["fecha"].dt.to_period("M"), sort=True)["ingreso_linea"]
        .sum()
    )
    ventas_por_mes.index = ventas_por_mes.index.astype(str)

    print("Ventas totales por mes (suma de cantidad * precio):")
    print(ventas_por_mes.to_frame(name="importe_total"))
    print()

    # 3. Determinar producto más vendido y con mayores ingresos
    por_producto_cant = df.groupby("producto", sort=True)["cantidad"].sum()
    por_producto_ingreso = df.groupby("producto", sort=True)["ingreso_linea"].sum()

    prod_mas_unidades = por_producto_cant.idxmax()
    prod_mayor_ingreso = por_producto_ingreso.idxmax()

    print("Producto con mayor cantidad total vendida:")
    print(f"  {prod_mas_unidades!r} -> {por_producto_cant[prod_mas_unidades]:,} unidades")
    print()
    print("Producto con mayores ingresos totales:")
    print(
        f"  {prod_mayor_ingreso!r} -> ${por_producto_ingreso[prod_mayor_ingreso]:,.2f}"
    )
    print()
    if prod_mas_unidades != prod_mayor_ingreso:
        print(
            "(Puede diferir: un producto barato con muchas unidades "
            "vs. uno caro con pocas ventas en importe.)"
        )
        print()

    # 4. Graficar ventas por mes
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    etiquetas_mes = ventas_por_mes.index.astype(str)
    ax1.bar(etiquetas_mes, ventas_por_mes.values, color="#2563eb", edgecolor="#1e40af")
    ax1.set_xlabel("Mes")
    ax1.set_ylabel("Importe total ($)")
    ax1.set_title("Ventas totales por mes")
    ax1.tick_params(axis="x", rotation=45)
    fig1.tight_layout()
    fig1.savefig(OUT_MES, dpi=150)
    print(f"Gráfico guardado: {OUT_MES}")

    # 5. Graficar top 5 productos por ingresos
    top5_ingresos = por_producto_ingreso.nlargest(5)
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    x = range(len(top5_ingresos))
    ax2.bar(x, top5_ingresos.values, color="#059669", edgecolor="#047857")
    ax2.set_xticks(list(x))
    ax2.set_xticklabels(top5_ingresos.index, rotation=35, ha="right")
    ax2.set_xlabel("Producto")
    ax2.set_ylabel("Ingresos ($)")
    ax2.set_title("Top 5 productos por ingresos")
    fig2.tight_layout()
    fig2.savefig(OUT_TOP5, dpi=150)
    print(f"Gráfico guardado: {OUT_TOP5}")
    print()

    # Ventanas sin bloquear el terminal; con MPL_INTERACTIVE=1 se intenta modo clásico.
    if os.environ.get("MPL_INTERACTIVE", "").strip().lower() in (
        "1",
        "true",
        "yes",
    ):
        plt.show()
    else:
        plt.show(block=False)
        plt.pause(0.01)
    plt.close("all")


if __name__ == "__main__":
    main()
