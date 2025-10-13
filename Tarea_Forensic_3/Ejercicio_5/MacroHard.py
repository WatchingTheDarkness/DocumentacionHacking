import base64

def decode_base64(texto_base64):
    """
    Decodifica texto en Base64, manejando posibles espacios y caracteres especiales
    """
    try:
        # Eliminar espacios y caracteres no deseados
        texto_limpio = texto_base64.replace(" ", "").strip()
        
        # Agregar padding si es necesario (Base64 requiere longitud múltiplo de 4)
        while len(texto_limpio) % 4 != 0:
            texto_limpio += '='
        
        # Decodificar
        texto_decodificado = base64.b64decode(texto_limpio).decode('utf-8')
        return texto_decodificado
    
    except Exception as e:
        return f"Error al decodificar: {str(e)}"

# Programa principal
if __name__ == "__main__":
    texto_base64 = input("Ingresa el texto Base64 que quieres decodificar: ")
    resultado = decode_base64(texto_base64)
    print(f"\nTexto decodificado: {resultado}")