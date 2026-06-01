# Lista-Negativo – Lista-Positivo
# Estudiante 1: Juan Miranda

def numeros_negativos(lista):
    negativos = []

    for numero in lista:
        if numero < 0:
            negativos.append(numero)

    return negativos

print("Estudiante 1:", numeros_negativos([-5, 2, -8, 7, -1]))


# Estudiante 2: Melany Rodriguez

def numeros_positivos(lista):
    positivos = []

    for numero in lista:
        if numero > 0:
            positivos.append(numero)

    return positivos

print("Estudiante 2:", numeros_positivos([-5, 2, -8, 7, -1]))
