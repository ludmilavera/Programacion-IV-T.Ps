# EJERCICIO 6

def cargar_matriz(nombre, filas, columnas):
    print(f"\nCargando matriz {nombre}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"{nombre}[{i}][{j}] = "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    C = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def multiplicar_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    C = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] * B[i][j])
        C.append(fila)
    return C

def mostrar_matriz(nombre, matriz):
    print(f"\nMatriz {nombre}:")
    for fila in matriz:
        print(fila)

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz_A = cargar_matriz("A", filas, columnas)
matriz_B = cargar_matriz("B", filas, columnas)

print("\n¿Desea realizar la suma o el producto de las matrices?")
opcion = input("Escriba 'suma' o 'producto': ").strip().lower()

if opcion == "suma":
    matriz_C = sumar_matrices(matriz_A, matriz_B)
elif opcion == "producto":
    matriz_C = multiplicar_matrices(matriz_A, matriz_B)
else:
    print("Opción inválida. No se realizará ninguna operación.")
    matriz_C = []

mostrar_matriz("A", matriz_A)
mostrar_matriz("B", matriz_B)
if matriz_C:
    mostrar_matriz("C", matriz_C)
