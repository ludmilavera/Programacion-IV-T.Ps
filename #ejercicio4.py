#EJERCICIO 4

def contar_vocales(palabra):
    return sum(1 for letra in palabra.lower() if letra in 'aeiouáéíóú')

def contar_consonantes(palabra):
    return sum(1 for letra in palabra.lower() if letra.isalpha() and letra not in 'aeiouáéíóú')

oracion = input("Ingrese una oración: ")
palabras = oracion.split()

total_vocales = sum(contar_vocales(palabra) for palabra in palabras)
total_consonantes = sum(contar_consonantes(palabra) for palabra in palabras)

print("Total de vocales:", total_vocales)
print("Total de consonantes:", total_consonantes)
