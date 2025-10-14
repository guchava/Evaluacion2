import requests
import sys

API_KEY = '97ea0149-e034-4b19-b44f-b121b881e246'

def obtener_ruta(origen, destino, vehiculo):
    url = 'https://graphhopper.com/api/1/route'
    params = {
        'point': [origen, destino],
        'vehicle': vehiculo,
        'locale': 'es',
        'instructions': 'true',
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

def validar_vehiculo():
    vehiculos_validos = ['car', 'foot', 'motorcycle', 'bike']
    while True:
        vehiculo = input("Seleccione el tipo de vehículo (car, foot, motorcycle, bike) o 's' para salir: ").strip().lower()
        if vehiculo in ['s', 'salir']:
            print("Saliendo del programa. CHAO PROFEES!")
            sys.exit()
        if vehiculo in vehiculos_validos:
            return vehiculo
        else:
            print("Vehículo inválido. Intente de nuevo.")

def pedir_coordenadas(mensaje):
    entrada = input(mensaje).strip().lower()
    if entrada in ['s', 'salir']:
        print("Saliendo del programa. CHAO PROFEE!")
        sys.exit()
    return entrada

print("Ingrese las coordenadas de origen (latitud,longitud) o 's' para salir: ")
origen = pedir_coordenadas("")

print("Ingrese las coordenadas de destino (latitud,longitud) o 's' para salir: ")
destino = pedir_coordenadas("")

vehiculo = validar_vehiculo()

ruta = obtener_ruta(origen, destino, vehiculo)

if 'paths' in ruta and len(ruta['paths']) > 0:
    path = ruta['paths'][0]
    distancia_km = path['distance'] / 1000 
    tiempo_seg = path['time'] / 1000  
    tiempo_min = tiempo_seg / 60  

    print(f"\nDistancia: {distancia_km:.2f} km")
    print(f"Duración estimada: {tiempo_min:.2f} minutos\n")

    print("Instrucciones de la ruta:\n")
    for instruccion in path['instructions']:
        print(instruccion['text'])
else:
    print("No se encontró ruta para los datos proporcionados.")