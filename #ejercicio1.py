#ejercicio1

def maximo_de_tres(a, b, c):
    return max(a, b, c)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

mayor = maximo_de_tres(a, b, c)
print("El número mayor es:", mayor)
