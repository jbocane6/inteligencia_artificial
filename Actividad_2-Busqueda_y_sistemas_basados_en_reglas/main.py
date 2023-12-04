from search_algorithm import encontrar_mejor_ruta
from rules import transporte_masivo

letras_permitidas = set('abcdefghijklmnABCDEFGHIJKLMN') # Letras permitidas para las estaciones

# Mientras ingresen valores no permitidos
while True:
    punto_inicio = input('Ingrese estación inicio A - N: ')
    punto_destino = input('Ingrese estación de llegada A - N: ')
    
    if punto_inicio in letras_permitidas and punto_destino in letras_permitidas:
        break
    else:
        print("Por favor, ingrese solo letras válidas de A a N.")

# Se llama al método enviando el grafo, el punto inicial y de destino
ruta_optima = encontrar_mejor_ruta(transporte_masivo, punto_inicio.upper(), punto_destino.upper())

# Si el resultado es diferente a none
if ruta_optima:
    print(f"La mejor ruta desde {punto_inicio} hasta {punto_destino}: {ruta_optima}")
else:
    print(f"No se encontró una ruta desde {punto_inicio} hasta {punto_destino}.")
