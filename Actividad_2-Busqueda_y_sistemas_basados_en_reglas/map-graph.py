import networkx as nx
import matplotlib.pyplot as plt
from rules import transporte_masivo

def graficar_red(grafo):
    G = nx.Graph()
    
    # Agregar nodos
    G.add_nodes_from(grafo['estaciones'].keys())
    
    # Agregar conexiones
    for estacion, conexiones in grafo['estaciones'].items():
        for conexion in conexiones:
            G.add_edge(estacion, conexion, weight=grafo['tiempos'].get((estacion, conexion), 1))

    # Dibujar la red
    pos = nx.spring_layout(G)  # Algoritmo de disposición
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')
    
    plt.title("Red de Estaciones y Conexiones")
    plt.show()

# Llamar a la función para graficar
graficar_red(transporte_masivo)
