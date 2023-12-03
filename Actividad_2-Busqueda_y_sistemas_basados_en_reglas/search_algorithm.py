import heapq

def encontrar_mejor_ruta(grafo, inicio, objetivo):
    cola_prioridad = [(0, inicio, [])]
    visitados = set()

    while cola_prioridad:
        costo_actual, nodo_actual, ruta_parcial = heapq.heappop(cola_prioridad)

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)
        ruta_parcial = ruta_parcial + [nodo_actual]

        if nodo_actual == objetivo:
            return ruta_parcial

        for vecino in grafo['estaciones'][nodo_actual]:
            costo_vecino = costo_actual + grafo['tiempos'][(nodo_actual, vecino)]
            heapq.heappush(cola_prioridad, (costo_vecino, vecino, ruta_parcial))

    return None
