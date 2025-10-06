def binario_a_texto(binario):
    # Eliminar espacios en blanco
    binario = binario.replace(" ", "").replace("\n", "")
    
    # Verificar que solo contenga 0s y 1s
    if not all(c in '01' for c in binario):
        return "Error: El código binario solo debe contener 0s y 1s"
    
    # Verificar que la longitud sea múltiplo de 8
    if len(binario) % 8 != 0:
        return "Error: La longitud del código binario debe ser múltiplo de 8"
    
    # Dividir en grupos de 8 bits y convertir
    bytes_list = [binario[i:i+8] for i in range(0, len(binario), 8)]
    texto = ''.join([chr(int(byte, 2)) for byte in bytes_list])
    
    return texto

def main():
    print("🔤 CONVERSOR DE BINARIO A TEXTO 🔤")
    print("=" * 40)
    
    while True:
        print("\nIngresa tu código binario (solo 0s y 1s):")
        print("Puedes pegar múltiples líneas, o escribe 'salir' para terminar")
        
        binario_input = input("> ")
        
        if binario_input.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta luego! 👋")
            break
        
        if binario_input.strip() == "":
            continue
        
        resultado = binario_a_texto(binario_input)
        
        print("\n" + "=" * 40)
        print("📝 RESULTADO:")
        print(resultado)
        print("=" * 40)

if __name__ == "__main__":
    main()