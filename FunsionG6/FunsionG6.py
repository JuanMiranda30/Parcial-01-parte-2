# Lista-Negativo – Lista-Positivo
# Estudiante 1: Juan Miranda


def numeros_negativos(lista):
    negativos = []

    for numero in lista:
        if numero < 0:
            negativos.append(numero)

    return negativos

print("Estudiante 1:", numeros_negativos([-5, 2, -8, 7, -1]))
