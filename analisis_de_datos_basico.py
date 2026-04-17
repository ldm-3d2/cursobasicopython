#Analisis de datos basico
#Consigue un pequeño conjunto de datos, por ejemplo un CSV con dos columnas de números (puedes crearlo manualmente).
#Escribe un script analisis.py que lea el CSV (utiliza pandas si quieres, Cursor te ayudará a importarlo y usarlo).
#Calcula estadísticas simples: media, mediana, desviación estándar de cada columna.
#Genera una gráfica de dispersión de una columna vs. la otra (aquí tendrás que usar matplotlib; prueba a pedirle a Cursor "Traza un scatter plot de col1 vs. col2").
#Observa cómo la IA incluso puede escribir el código de Matplotlib para ti.
#Ejecuta el script; si estás en Cursor, la gráfica debería abrirse en una ventana externa (o en el panel de plot de VS Code si está habilitado).
#Este ejercicio mezcla programación con un toque de data science, exhibiendo la versatilidad de Cursor.

import pandas as pd
import matplotlib.pyplot as plt

#Leer el CSV
df = pd.read_csv("datos_random.csv")

#Calcular estadísticas simples
print("media:")
print(df.mean())
print("mediana:")
print(df.median())
print("desviacion_estandar:")
print(df.std())
