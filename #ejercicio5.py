# EJERCICIO 5

def calcular_potencia(x, k):
    return x ** k

def contar_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    x_str = str(x)
    return x_str == x_str[::-1]

while True:
    print("\nMENÚ")
    print("1. Calcular la potencia K de un número X")
    print("2. Obtener la cantidad de dígitos de un número X")
    print("3. Determinar si un número es capicúa")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        x = int(input("Número X: "))
        k = int(input("Potencia K: "))
        print(f"{x}^{k} = {calcular_potencia(x, k)}")
    elif opcion == '2':
        x = int(input("Número X: "))
        print("Cantidad de dígitos:", contar_digitos(x))
    elif opcion == '3':
        x = int(input("Número X: "))
        if es_capicua(x):
            print("Es capicúa.")
        else:
            print("No es capicúa.")
    elif opcion == '4':
        print("Fin del programa.")
        break
    else:
        print("Opción inválida.")
