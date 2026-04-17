print ("Hello, World!")

for i  in range(5):
    print(i)
# Calcular el factorial de un numero dad

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Ingrese un numero: "))))

#Crear una lista con los cuadrados de los 3 primeros numeros naturales
def cuadrados(n):
    return [i**2 for i in range(1, n+1)]
print(cuadrados(3))


