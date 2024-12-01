import requests
from urllib.parse import quote_plus

def obtener_latitud_longitud(direccion):
    # Codificar la dirección para reemplazar los espacios por '+'
    direccion_codificada = quote_plus(direccion)
    
    # URL de la API de Nominatim con la dirección codificada
    url = f'https://nominatim.openstreetmap.org/search?q={direccion_codificada}&format=jsonv2'
    
    # Crear encabezados para la solicitud
    headers = {
        'User-Agent': 'BizaCourier/1.0 (sebasandree729@gmail.com)'  # Cambia esto por tu propio email
    }
    
    # Hacer la solicitud GET
    response = requests.get(url, headers=headers)
    
    # Verificar si la respuesta fue exitosa
    if response.status_code == 200:
        try:
            data = response.json()
            
            # Verificar si se encontraron resultados
            if data:
                # Obtener latitud y longitud
                latitud = data[0].get('lat')
                longitud = data[0].get('lon')
                
                # Retornar latitud y longitud
                return latitud, longitud
            else:
                print("No se encontraron resultados para la dirección.")
                return None, None
        except ValueError as e:
            print(f"Error al procesar la respuesta JSON: {e}")
            return None, None
    else:
        print(f"Error en la solicitud: {response.status_code}")
        return None, None

# Probar la función con una dirección
direccion = 'Avenida San Juan, Lima Chorrillos'
latitud, longitud = obtener_latitud_longitud(direccion)

if latitud and longitud:
    print(f"Latitud: {latitud}, Longitud: {longitud}")
else:
    print("No se pudo obtener latitud y longitud.")
