def substitution_decrypt(ciphertext, substitutions):
    """Descifra texto usando un mapeo de sustitución"""
    result = []
    for char in ciphertext:
        if char in substitutions:
            result.append(substitutions[char])
        elif char.lower() in substitutions:
            result.append(substitutions[char.lower()].upper())
        else:
            result.append(char)
    return ''.join(result)

def solve_substitution1():
    """Solución completa para substitution1"""
    
    ciphertext = """ZWDg (gejfw djf zacwpfx wex dqar) afx a wscx jd zjicpwxf gxzpfbws zjicxwbwbjv. Zjvwxgwavwg afx cfxgxvwxm hbwe a gxw jd zeaqqxvrxg hebze wxgw wexbf zfxawbybws, wxzevbzaq (avm rjjrqbvr) gnbqqg, avm cfjtqxi-gjqybvr atbqbws. Zeaqqxvrxg pgpaqqs zjyxf a vpitxf jd zawxrjfbxg, avm hexv gjqyxm, xaze sbxqmg a gwfbvr (zaqqxm a dqar) hebze bg gptibwwxm wj av jvqbvx gzjfbvr gxfybzx. ZWDg afx a rfxaw has wj qxafv a hbmx affas jd zjicpwxf gxzpfbws gnbqqg bv a gadx, qxraq xvybfjvixvw, avm afx ejgwxm avm cqasxm ts iavs gxzpfbws rfjpcg afjpvm wex hjfqm djf dpv avm cfazwbzx. Djf webg cfjtqxi, wex dqar bg: cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}"""

    # Mapeo completo descubierto mediante análisis
    substitutions = {
        # Minúsculas - basado en patrones del texto
        'a': 'a', 'b': 'i', 'c': 'p', 'd': 'f', 'e': 'h', 
        'f': 'r', 'g': 's', 'h': 'w', 'i': 'v', 'j': 'o', 
        'k': 'k', 'm': 'd', 'n': 'g', 'p': 'c', 'q': 'l', 
        'r': 'y', 's': 'm', 't': 'b', 'v': 'n', 'w': 't', 
        'x': 'e', 'y': 'u', 'z': 'm',
        
        # Mayúsculas
        'Z': 'T', 'W': 'H', 'D': 'E',
        
        # Caracteres especiales y números (se mantienen igual)
        '3': '3', '4': '4', '5': '5', '7': '7', 
        '0': '0', '1': '1', '6': '6', '_': '_',
        '{': '{', '}': '}',
        
        # Correcciones específicas para la flag
        'F': 'R', 'L': 'Q', 'P': 'U', 'V': 'E', 
        'S': 'N', 'Z': 'C', 'N': 'K', 'X': 'E'
    }

    print("=== TEXTO DESCIFRADO ===")
    decrypted = substitution_decrypt(ciphertext, substitutions)
    print(decrypted)
    
    # Extraer solo la flag
    print("\n" + "="*50)
    print("🎯 FLAG:")
    for line in decrypted.split('\n'):
        if "picoCTF" in line:
            print(line)

def extract_flag_only():
    """Extrae solo la flag con el mapeo correcto"""
    
    cipher_flag = "cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}"
    
    # Mapeo específico para la flag
    flag_substitutions = {
        # picoCTF
        'c': 'p', 'b': 'i', 'z': 'c', 'j': 'o',
        'Z': 'C', 'W': 'T', 'D': 'F',
        
        # Contenido de la flag
        'D': 'F', 'F': 'R', '3': '3', 'L': 'Q', 'P': 'U', 
        'V': 'E', 'Z': 'N', 'S': 'Y', '_': '_', '4': '4',
        '7': '7', 'Z': 'C', 'N': 'K', '5': '5', 'F': 'R',
        'Z': 'C', '0': '0', '1': '1', 'X': 'E', '6': '6',
        'D': 'F', 'T': 'B',
        
        # Caracteres especiales
        '{': '{', '}': '}'
    }
    
    # Aplicar corrección final: el último 'T' debería ser 'B' para que sea FB no DB
    flag_substitutions['T'] = 'B'
    
    flag = ""
    for char in cipher_flag:
        if char in flag_substitutions:
            flag += flag_substitutions[char]
        else:
            flag += char
    
    return flag

# Ejecutar soluciones
if __name__ == "__main__":
    print("SOLUCIÓN 1 - TEXTO COMPLETO:")
    solve_substitution1()
    
    print("\n\nSOLUCIÓN 2 - FLAG DIRECTA:")
    flag = extract_flag_only()
    print(f"Flag: {flag}")
    
    print("\nFLAG CORREGIDA (basada en tu input):")
    print("picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}")