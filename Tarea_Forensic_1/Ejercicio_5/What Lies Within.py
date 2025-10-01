from PIL import Image
import numpy as np
import os

def decode_picoctf_specific(image_path):
    """
    Decodificación específica para retos picoCTF
    """
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        
        print(f"Formato de imagen: {img_array.shape}")
        
        # Método 1: LSB tradicional en todos los canales
        height, width = img_array.shape[:2]
        channels = img_array.shape[2] if len(img_array.shape) == 3 else 1
        
        # Extraer bits LSB
        binary_data = []
        if len(img_array.shape) == 3:
            for y in range(height):
                for x in range(width):
                    for c in range(min(3, channels)):  # Solo RGB, no alpha
                        binary_data.append(str(img_array[y, x, c] & 1))
        else:
            for y in range(height):
                for x in range(width):
                    binary_data.append(str(img_array[y, x] & 1))
        
        # Convertir a texto
        binary_string = ''.join(binary_data)
        
        # Buscar 'picoCTF{' en diferentes combinaciones de bits
        target = "picoCTF{"
        target_binary = ''.join(format(ord(c), '08b') for c in target)
        
        # Probar diferentes offsets
        for offset in range(8):
            test_bits = binary_string[offset:]
            message = ""
            found = False
            
            for i in range(0, len(test_bits)-7, 8):
                if i + 8 > len(test_bits):
                    break
                byte = test_bits[i:i+8]
                char_code = int(byte, 2)
                
                # Solo caracteres ASCII imprimibles
                if 32 <= char_code <= 126:
                    message += chr(char_code)
                    # Verificar si encontramos el patrón
                    if target in message:
                        found = True
                        break
                else:
                    # Si encontramos carácter no imprimible, reiniciamos
                    if len(message) > 0:
                        if target in message:
                            found = True
                        break
            
            if found:
                # Extraer el mensaje completo hasta }
                start_idx = message.find(target)
                end_idx = message.find('}', start_idx)
                if end_idx != -1:
                    return message[start_idx:end_idx+1]
                else:
                    return message[start_idx:]
        
        return "No se encontró picoCTF{...} con LSB simple"
        
    except Exception as e:
        return f"Error: {str(e)}"

def decode_rgb_separated(image_path):
    """
    Decodifica separando los canales RGB
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        height, width, channels = img_array.shape
        
        # Probar diferentes métodos de extracción
        
        # Método 1: Canal R solamente
        binary_r = []
        for y in range(height):
            for x in range(width):
                binary_r.append(str(img_array[y, x, 0] & 1))
        
        message_r = bits_to_text(''.join(binary_r))
        if 'picoCTF{' in message_r:
            return extract_flag(message_r)
        
        # Método 2: Canal G solamente
        binary_g = []
        for y in range(height):
            for x in range(width):
                binary_g.append(str(img_array[y, x, 1] & 1))
        
        message_g = bits_to_text(''.join(binary_g))
        if 'picoCTF{' in message_g:
            return extract_flag(message_g)
        
        # Método 3: Canal B solamente
        binary_b = []
        for y in range(height):
            for x in range(width):
                binary_b.append(str(img_array[y, x, 2] & 1))
        
        message_b = bits_to_text(''.join(binary_b))
        if 'picoCTF{' in message_b:
            return extract_flag(message_b)
        
        # Método 4: Intercalado RGB
        binary_interleaved = []
        for y in range(height):
            for x in range(width):
                binary_interleaved.append(str(img_array[y, x, 0] & 1))  # R
                binary_interleaved.append(str(img_array[y, x, 1] & 1))  # G
                binary_interleaved.append(str(img_array[y, x, 2] & 1))  # B
        
        message_interleaved = bits_to_text(''.join(binary_interleaved))
        if 'picoCTF{' in message_interleaved:
            return extract_flag(message_interleaved)
        
        return "No se encontró en canales separados"
        
    except Exception as e:
        return f"Error: {str(e)}"

def bits_to_text(binary_string):
    """Convierte bits a texto ASCII"""
    message = ""
    for i in range(0, len(binary_string)-7, 8):
        byte = binary_string[i:i+8]
        char_code = int(byte, 2)
        if 32 <= char_code <= 126:  # Caracteres imprimibles
            message += chr(char_code)
        else:
            # Si encontramos carácter no imprimible, seguimos pero marcamos
            message += f"[{char_code:02X}]"
    
    return message

def extract_flag(text):
    """Extrae la flag del texto"""
    start = text.find('picoCTF{')
    if start == -1:
        return "No se encontró picoCTF{"
    
    end = text.find('}', start)
    if end == -1:
        # Buscar en los siguientes 100 caracteres
        potential_end = text.find('}', start + 8)
        if potential_end != -1:
            return text[start:potential_end+1]
        return text[start:start+100] + "..."
    
    return text[start:end+1]

def decode_alpha_channel(image_path):
    """
    Decodifica usando el canal alpha si existe
    """
    try:
        img = Image.open(image_path)
        if img.mode != 'RGBA':
            return "La imagen no tiene canal alpha"
        
        img_array = np.array(img)
        height, width = img_array.shape[:2]
        
        # Extraer LSB del canal alpha
        binary_alpha = []
        for y in range(height):
            for x in range(width):
                binary_alpha.append(str(img_array[y, x, 3] & 1))  # Canal alpha
        
        message = bits_to_text(''.join(binary_alpha))
        if 'picoCTF{' in message:
            return extract_flag(message)
        
        return "No se encontró en canal alpha"
        
    except Exception as e:
        return f"Error alpha: {str(e)}"

def decode_every_n_bits(image_path, n=1):
    """
    Decodifica tomando bits cada n posiciones
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        height, width = img_array.shape[:2]
        
        # Extraer todos los bits
        all_bits = []
        for y in range(height):
            for x in range(width):
                for c in range(3):
                    all_bits.append(str(img_array[y, x, c] & 1))
        
        # Probar diferentes espaciados
        for spacing in [1, 2, 3, 4, 8]:
            spaced_bits = all_bits[::spacing]
            message = bits_to_text(''.join(spaced_bits))
            if 'picoCTF{' in message:
                return f"Espaciado {spacing}: {extract_flag(message)}"
        
        return "No se encontró con espaciado"
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    image_path = r"C:\Users\watch\Downloads\NotasHacking\DocumentacionHacking\Tarea_Forensic_1\Ejercicio_5\buildings.png"
    
    if not os.path.exists(image_path):
        print("❌ El archivo no existe")
        return
    
    print("🔍 Buscando flag picoCTF...")
    print("=" * 60)
    
    # Probar diferentes métodos
    methods = [
        ("LSB tradicional", decode_picoctf_specific),
        ("Canales RGB separados", decode_rgb_separated),
        ("Canal Alpha", decode_alpha_channel),
        ("Bits espaciados", decode_every_n_bits),
    ]
    
    for method_name, method_func in methods:
        print(f"\n🔄 Probando: {method_name}")
        result = method_func(image_path)
        print(f"   Resultado: {result}")
        
        if 'picoCTF{' in result and 'Error' not in result:
            print(f"\n🎯 ¡FLAG ENCONTRADA con {method_name}!")
            print(f"🚩 {result}")
            break
    
    # Si no se encontró, mostrar más opciones
    print("\n" + "=" * 60)
    print("🔄 Probando método avanzado: LSB de solo los primeros píxeles...")
    
    # Método específico: solo primeros píxeles
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        
        # Solo procesar los primeros 1000 píxeles
        binary_data = []
        count = 0
        for y in range(img_array.shape[0]):
            for x in range(img_array.shape[1]):
                if count > 1000:
                    break
                for c in range(3):
                    binary_data.append(str(img_array[y, x, c] & 1))
                count += 1
        
        message = bits_to_text(''.join(binary_data))
        if 'picoCTF{' in message:
            print(f"🎯 ¡FLAG ENCONTRADA en primeros píxeles!")
            print(f"🚩 {extract_flag(message)}")
        else:
            print("❌ No se encontró en primeros píxeles")
            
    except Exception as e:
        print(f"Error en método avanzado: {e}")

if __name__ == "__main__":
    main()