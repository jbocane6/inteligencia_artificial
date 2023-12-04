import heapq

# encontrar_mejor_ruta: Obtiene unas reglas, punto de inicio y fin y devuelve la mejor ruta según los tiempos
# grafo: Contiene la info de estaciones y tiempos del grafo
# inicio: Punto inicial
# objetivo: Destino
def encontrar_mejor_ruta(grafo, inicio, objetivo):
    # Tupla que contiene el costo actual (inicializado en 0), el nodo de inicio y una lista vacía que representa la ruta parcial.
    cola_prioridad = [(0, inicio, [])]
    # Conjunto con los nodos que ya han sido visitados.
    visitados = set()

    # Continuará hasta que la cola de prioridad esté vacía.
    while cola_prioridad:
        # Obtiene el costo generado, el nodo donde se encuentra y la ruta actual
        costo_actual, nodo_actual, ruta_parcial = heapq.heappop(cola_prioridad)
        print(costo_actual, nodo_actual, ruta_parcial)

        # Si ya existe el nodo, completa iteración y continúa el bucle
        if nodo_actual in visitados:
            continue

        # Agrega el nodo al set
        visitados.add(nodo_actual)
        # Agrega el nodo donde está
        ruta_parcial = ruta_parcial + [nodo_actual]

        # Si está en el nodo buscado devuelve la respuesta
        if nodo_actual == objetivo:
            return ruta_parcial

        # Itera entre estaciones y tiempos para agregar las opciones encontradas por nodo
        for vecino in grafo['estaciones'][nodo_actual]:
            costo_vecino = costo_actual + grafo['tiempos'][(nodo_actual, vecino)]
            heapq.heappush(cola_prioridad, (costo_vecino, vecino, ruta_parcial))

    # En caso no pueda iterar en cola_prioridad
    return None
