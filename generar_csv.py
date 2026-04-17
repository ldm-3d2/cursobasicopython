import csv
import random

def generar_csv(nombre_archivo, filas):
    """
    Genera un archivo CSV con dos columnas de números aleatorios enteros.
    :param nombre_archivo: Nombre del archivo CSV a crear.
    :param filas: Cantidad de filas de datos a generar.
    """
    try:
        # Validación de parámetros
        if not isinstance(filas, int) or filas <= 0:
            raise ValueError("La cantidad de filas debe ser un entero positivo.")

        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            
            # Escribir encabezados
            escritor.writerow(["Columna1", "Columna2"])
            
            # Escribir datos aleatorios
            for _ in range(filas):
                num1 = random.randint(1, 100)  # Número aleatorio entre 1 y 100
                num2 = random.randint(1, 100)
                escritor.writerow([num1, num2])

        print(f"Archivo '{nombre_archivo}' generado con {filas} filas.")

    except Exception as e:
        print(f"Error al generar el archivo CSV: {e}")

generar_csv("datos_random.csv",10)
