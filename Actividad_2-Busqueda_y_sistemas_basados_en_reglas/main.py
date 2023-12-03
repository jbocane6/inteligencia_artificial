from search_algorithm import encontrar_mejor_ruta
from rules import transporte_masivo
punto_inicio = 'A'
punto_destino = 'M'

ruta_optima = encontrar_mejor_ruta(transporte_masivo, punto_inicio, punto_destino)

if ruta_optima:
    print(f"La mejor ruta desde {punto_inicio} hasta {punto_destino}: {ruta_optima}")
else:
    print(f"No se encontró una ruta desde {punto_inicio} hasta {punto_destino}.")
