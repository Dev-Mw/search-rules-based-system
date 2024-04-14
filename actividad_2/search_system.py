# Este es un programa que se encarga de realizar una busqueda
# de la mejor ruta desde un punto A un punto B.
#
# Correo: rsoteloc@ibero.edu.co
# Autor: Dario Sotelo / ID: 100103047
# Fecha: 21/03/2024


# Base de conocimiento de conexiones entre estaciones
conexiones = {
    'Estacion1': ['Estacion2', 'Estacion3'],
    'Estacion2': ['Estacion1', 'Estacion4'],
    'Estacion3': ['Estacion1', 'Estacion5'],
    'Estacion4': ['Estacion2', 'Estacion5'],
    'Estacion5': ['Estacion3', 'Estacion4']
}


# Función para encontrar la mejor ruta usando el algoritmo de búsqueda Dijkstra
def encontrar_mejor_ruta(conexiones, inicio, fin):
    # Inicializar los nodos y distancias
    nodos_no_visitados = set(conexiones.keys())
    distancias = {nodo: float('inf') for nodo in nodos_no_visitados}
    distancias[inicio] = 0
    ruta_anterior = {}

    # Algoritmo de búsqueda Dijkstra
    while nodos_no_visitados:
        nodo_actual = min(nodos_no_visitados, key=lambda nodo: distancias[nodo])
        nodos_no_visitados.remove(nodo_actual)
        for vecino in conexiones[nodo_actual]:
            nueva_distancia = distancias[nodo_actual] + 1  # Distancia unitaria entre estaciones
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                ruta_anterior[vecino] = nodo_actual

    # Reconstruir la ruta desde el inicio hasta el fin
    ruta = [fin]
    while ruta[-1] != inicio:
        ruta.append(ruta_anterior[ruta[-1]])
    ruta.reverse()

    return ruta


# Ejemplo de uso
inicio = 'Estacion1'
fin = 'Estacion4'
ruta = encontrar_mejor_ruta(conexiones, inicio, fin)
print("La mejor ruta desde", inicio, "hasta", fin, "es:", ruta)

###
# Salida del programa
###

# (venv)$ La mejor ruta desde Estacion1 hasta Estacion4 es: ['Estacion1', 'Estacion2', 'Estacion4']
