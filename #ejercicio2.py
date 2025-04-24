#ejercicio2

def maximo_de_tres(a, b, c):
    return max(a, b, c)

def maximo_de_diez(lista):
    mayor = lista[0]
    for num in lista[1:]:
        mayor = maximo_de_tres(mayor, num, mayor)
    return mayor

numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = maximo_de_diez(numeros)
print("El mayor de los 10 números es:", mayor)
