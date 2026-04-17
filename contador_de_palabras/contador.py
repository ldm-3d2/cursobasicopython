#Progrmama para contar palabras en un archivo de texto
#1. Pedir al usuarioa la ruta de un archivo de texto
#2. Leer el archivo de texto
#3. separar las palabras
#4. contar las palabras
#5 pedir al usuario que palabras quiere buscar y contar cuantas veces aparece la palabra
#6. mostrar el resultado

archivo = input("Introduzca la ruta del archivo de texto: ")

try:
    with open (archivo, "r", encoding="utf-8" ) as f:
        texto = f.read()
except FileNotFoundError:
        print(f"El archivo {archivo} no existe")
        exit(1)

#3 separar las palabras
import re

palabras = re. findall (r"\w", texto.lower())
total_palabras = len(palabras)
print(f"El archivo {archivo} tiene {total_palabras} palabras")

#5 pedir al usuario que palabras quiere buscar y contar cuantas veces aparece la palabra
palabra_buscada = input("Introduzca la palabra que quiere buscar: ")
veces_aparece = palabras.count(palabra_buscada)
print(f"La palabra {palabra_buscada} aparece {veces_aparece} veces en el archivo {archivo}")

