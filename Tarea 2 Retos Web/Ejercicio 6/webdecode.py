import base64

def decodificar_base64(texto_codificado):
    """
    Decodifica texto en Base64
    """
    try:
        # Asegurarse de que el texto esté en formato bytes
        if isinstance(texto_codificado, str):
            texto_codificado = texto_codificado.encode('utf-8')
        
        # Decodificar
        texto_decodificado = base64.b64decode(texto_codificado)
        
        # Intentar convertir a string si es texto
        try:
            return texto_decodificado.decode('utf-8')
        except UnicodeDecodeError:
            return texto_decodificado
            
    except Exception as e:
        return f"Error al decodificar: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Ingresa el texto en Base64 a decodificar: ")
    resultado = decodificar_base64(texto)
    print(f"Texto decodificado: {resultado}")