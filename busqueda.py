# creacion de matrz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Valor a buscar
elemento_a_buscar = 2
# Función para buscar un valor en la matriz
def buscar_valor(matriz, valorBusqueda):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valorBusqueda:
                return print(f"El valor {valorBusqueda} se encontró en la posición ({fila}, {columna})")
    return print(f"El valor {valorBusqueda} no se encontró en la matriz.")


# Resultado qye estaba buscando
print(buscar_valor(matriz, elemento_a_buscar))
