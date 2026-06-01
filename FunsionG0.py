# par-Impar – Mayor-numero
#*****************************************
#**    Desarrollado por: Hector Lavoe   **
#*****************************************
# inicia desarrollo de la funciín dada

# cuando imprime resultado
# en el print "Su nommbre y la salida del resultado de la función"
# compruebe buen funcionamiento

# Par-Impar – Mayor-Número
# Estudiante 1: Juan Miranda

def par_impar(numero):
    if numero % 2 == 0:
        return "El número es PAR"
    else:
        return "El número es IMPAR"

print("Estudiante 1:", par_impar(8))


# Estudiante 2: Melany Rodriguez

def mayor_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print("Estudiante 2:", mayor_numero(15, 20))

#Suma-Lista – Promedio-Lista
# Estudiante 1: Juan Miranda

def suma_lista(lista):
    return sum(lista)

print("Estudiante 1:", suma_lista([10, 20, 30, 40]))


# Estudiante 2: Melany Rodriguez

def promedio_lista(lista):
    return sum(lista) / len(lista)

print("Estudiante 2:", promedio_lista([10, 20, 30, 40]))

#Cadena-Número – Cadena-Vacía
# Estudiante 1: Juan Miranda

def cantidad_caracteres(texto):
    return len(texto)

print("Estudiante 1:", cantidad_caracteres("Programacion"))


# Estudiante 2: Melany Rodriguez

def cadena_vacia(texto):
    if texto == "":
        return "La cadena está vacía"
    else:
        return "La cadena no está vacía"

print("Estudiante 2:", cadena_vacia(""))

# Lista-Número – Lista-Contenido
# Estudiante 1: Juan Miranda

def cantidad_elementos(lista):
    return len(lista)

print("Estudiante 1:", cantidad_elementos([1, 2, 3, 4, 5]))


# Estudiante 2: Melany Rodriguez

def valor_minimo(lista):
    return min(lista)

print("Estudiante 2:", valor_minimo([8, 3, 12, 1, 9]))

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

# Lista-Mayúsc – Lista-Minúsc
# Estudiante 1: Juan Miranda

def convertir_mayusculas(texto):
    return texto.upper()

print("Estudiante 1:", convertir_mayusculas("hola mundo"))


# Estudiante 2: Melany Rodriguez

def convertir_minusculas(texto):
    return texto.lower()

print("Estudiante 2:", convertir_minusculas("HOLA MUNDO"))

