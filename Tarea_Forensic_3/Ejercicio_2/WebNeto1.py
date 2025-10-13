#!/usr/bin/env python3

import binascii
import base64
import sys

def hex_to_text(hex_string):
    """Convierte hexadecimal a texto"""
    try:
        # Limpiar el string de espacios y saltos de línea
        hex_string = hex_string.strip().replace(' ', '').replace('\n', '')
        
        # Convertir hex a bytes y luego a texto
        bytes_data = bytes.fromhex(hex_string)
        return bytes_data.decode('utf-8')
    except Exception as e:
        return f"Error decodificando hexadecimal: {e}"

def base64_to_text(b64_string):
    """Convierte base64 a texto"""
    try:
        # Agregar padding si es necesario
        padding = 4 - len(b64_string) % 4
        if padding != 4:
            b64_string += '=' * padding
        
        bytes_data = base64.b64decode(b64_string)
        return bytes_data.decode('utf-8')
    except Exception as e:
        return f"Error decodificando base64: {e}"

def auto_detect_and_decode(data):
    """Intenta detectar automáticamente el formato y decodificar"""
    data = data.strip()
    
    # Detectar hexadecimal (solo caracteres 0-9, a-f, A-F)
    hex_chars = set('0123456789abcdefABCDEF')
    if all(c in hex_chars or c in ' \n\t' for c in data):
        clean_hex = data.replace(' ', '').replace('\n', '').replace('\t', '')
        if len(clean_hex) % 2 == 0:  # Longitud par típica de hex
            result = hex_to_text(clean_hex)
            if "Error" not in result:
                return "Hexadecimal detectado:\n" + result
    
    # Detectar base64
    b64_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=')
    if all(c in b64_chars for c in data.replace('\n', '').replace(' ', '')):
        try:
            result = base64_to_text(data)
            if "Error" not in result:
                return "Base64 detectado:\n" + result
        except:
            pass
    
    return "No se pudo detectar el formato automáticamente"

def main():
    print("=== DECODIFICADOR UNIVERSAL ===")
    print("1. Decodificar hexadecimal")
    print("2. Decodificar base64")
    print("3. Detección automática")
    print("4. Salir")
    
    while True:
        try:
            choice = input("\nSelecciona una opción (1-4): ").strip()
            
            if choice == '1':
                hex_input = input("Ingresa el texto hexadecimal: ")
                print("\nResultado:")
                print(hex_to_text(hex_input))
                
            elif choice == '2':
                b64_input = input("Ingresa el texto base64: ")
                print("\nResultado:")
                print(base64_to_text(b64_input))
                
            elif choice == '3':
                data_input = input("Ingresa el texto a decodificar: ")
                print("\nResultado:")
                print(auto_detect_and_decode(data_input))
                
            elif choice == '4':
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Si se pasa un argumento, decodificarlo automáticamente
    if len(sys.argv) > 1:
        input_data = ' '.join(sys.argv[1:])
        print("Decodificación automática:")
        print(auto_detect_and_decode(input_data))
    else:
        main()