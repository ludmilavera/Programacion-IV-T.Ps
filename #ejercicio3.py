#ejercicio3

def cargar_vector(nombre, cantidad):
    print(f"\nCargando vector {nombre}:")
    return [int(input(f"{nombre}[{i+1}] = ")) for i in range(cantidad)]

def suma_vector(vector):
    return sum(vector)

def sumar_vectores(A, B):
    return [A[i] + B[i] for i in range(len(A))]

N = int(input("Cantidad de elementos en el vector A: "))
M = int(input("Cantidad de elementos en el vector B: "))

vector_A = cargar_vector("A", N)
vector_B = cargar_vector("B", M)

print("Suma de A:", suma_vector(vector_A))
print("Suma de B:", suma_vector(vector_B))

if N == M:
    vector_resultado = sumar_vectores(vector_A, vector_B)
    print("Suma de vectores (A + B):", vector_resultado)
else:
    print("Los vectores no tienen la misma longitud.")
