import base64

# Tu cadena en base64
cadena_base64 = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

# Decodificar de base64
try:
    # Convertir de base64 a bytes
    bytes_decodificados = base64.b64decode(cadena_base64)
    
    # Convertir bytes a string legible
    texto_legible = bytes_decodificados.decode('utf-8')
    
    print("Cadena original:", cadena_base64)
    print("Texto decodificado:", texto_legible)
    
except Exception as e:
    print(f"Error al decodificar: {e}")