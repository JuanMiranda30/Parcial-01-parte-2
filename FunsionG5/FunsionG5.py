# Lista-Máximo – Lista-Factorial
# Estudiante 1: Juan Miranda

def valor_maximo(lista):
    return max(lista)

print("Estudiante 1:", valor_maximo([8, 3, 12, 1, 9]))


# Estudiante 2: Melany Rodriguez

def factorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

print("Estudiante 2:", factorial(5))
