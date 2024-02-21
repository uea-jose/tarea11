#2.Programa 2: Ordenación de Arreglo Multidimensional
#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.
#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
#Muestra la matriz original y la matriz con la fila ordenada.


# Definir la matriz
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#funcion ordenar con sort()
def ordenar_fila(matriz2, fila):
    matriz2[fila] = sorted(matriz2[fila])
    return matriz


# Fila a ordenar (empezando desde 0)
fila_a_ordenar = 1

# Impresion matriz original
print("=====Matriz original======:")
for i in matriz2:
    print(i, end=" ")
    print()
print("============================")

# llama a funcion y ordernar matriz
matriz_ordenada = ordenar_fila(matriz2, fila_a_ordenar)

# Mostrar matriz con la fila ordenada
print("\n=====Matriz Ordenada======:")
for i in matriz_ordenada:
    print(i, end=" ")
    print()
print("============================")
