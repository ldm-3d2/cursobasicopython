#Calculadora
#1. Pedir al usuario que ingrese un numero, verificar que sea un numero valido, sino pedir al usuario que ingrese un numero valido y si ingresa una letra, pedir al usuario que ingrese un numero valido
#2. Pedir al usuario que ingrese simbolo de la operacion que quiere realizar, si ingresa una letra que no sea +, -, * o /, pedir al usuario que ingrese un simbolo valido
#3. Si el simbolo es +, -, * o /, realizar la operacion, sino pedir al usuario que ingrese un simbolo valido
#4. Pedir al usuario que ingrese otro numero, verificar que sea un numero valido, sino pedir al usuario que ingrese un numero valido y si ingresa una letra, pedir al usuario que ingrese un numero valido
#5. si la operacion es /, verificar que el segundo numero no sea 0, sino pedir al usuario que ingrese otro numero valido y si ingresa una letra, pedir al usuario que ingrese un numero valido
#6. Mostrar el resultado
#7. Preguntar al usuario si quiere realizar otra operacion, si es si, repetir el proceso, si no, salir

def calcular():

    while True:
        try:
            numero1 = float(input("Ingrese el primer numero: "))
            break
        except ValueError:
            print("El numero ingresado no es valido")
            
    while True:
            operacion = input("Ingrese el simbolo de la operacion que quiere realizar: ")
            if operacion  in ["+", "-", "*", "/"]:
                break
            else:
                print("El simbolo ingresado no es valido")

    while True:
        try:
            numero2 = float(input("Ingrese el segundo numero: "))
            break
        except ValueError:
            print("El numero ingresado no es valido")
    
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 == 0:
           print("Error: No se puede dividir por cero")
           return
        
        resultado = numero1 / numero2
    print(f"El resultado de la operacion es: {resultado}")
    otra_operacion = input("¿Quiere realizar otra operación? (s/n): ")
    if otra_operacion == "s":
        calcular()
    else:
        print("Gracias por usar la calculadora")
        return

calcular()
   