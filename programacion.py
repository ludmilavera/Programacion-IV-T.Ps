#ejercicio1
def contar_digitos(numero):
    return len(str(abs(numero)))  # Convierte el número en positivo y cuenta los dígitos

# Entrada del usuario
num = int(input("Ingrese un número entero: "))
print(f"El número tiene {contar_digitos(num)} dígitos.")