import base64

def decodificar_base64(codificado):
    """
    Decodifica una cadena en Base64
    
    Args:
        codificado (str): Cadena codificada en Base64
    
    Returns:
        str: Cadena decodificada
    """
    try:
        if isinstance(codificado, str):
            codificado = codificado.encode('utf-8')
        
        decodificado = base64.b64decode(codificado)
        
        try:
            return decodificado.decode('utf-8')
        except UnicodeDecodeError:
            return decodificado
    
    except Exception as e:
        return f"Error al decodificar: {e}"

if __name__ == "__main__":
    texto_codificado = "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aNoSIA.tL4mgcyUlArI1DzqWqoeZtujQ1w"
    texto_decodificado = decodificar_base64(texto_codificado)
    
    print(f"Texto codificado: {texto_codificado}")
    print(f"Texto decodificado: {texto_decodificado}")