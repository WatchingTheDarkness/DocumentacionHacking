def substitution_decrypt(ciphertext, key):
    """
    Descifra un texto usando sustitución con clave dada
    key: OHNFUMWSVZLXEGCPTAJDYIRKQB (alfabeto cifrado)
    """
    # Alfabeto normal
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = alphabet.lower()
    
    # Limpiar la clave (quitar espacios)
    clean_key = key.replace(" ", "").strip()
    
    # Crear mapeo de descifrado
    decrypt_map = {}
    for i in range(len(clean_key)):
        decrypt_map[clean_key[i]] = alphabet[i]  # Cifrado -> Normal
        decrypt_map[clean_key[i].lower()] = alphabet_lower[i]
    
    # Descifrar el texto
    result = []
    for char in ciphertext:
        if char in decrypt_map:
            result.append(decrypt_map[char])
        else:
            result.append(char)  # Mantener espacios, puntuación, etc.
    
    return ''.join(result)

# Texto cifrado completo
ciphertext = """OHNFUMWSVZLXEGCPTAJDYIRKQB 

Suauypcg Xuwaogf oacju, rvds o waoiu ogf jdoduxq ova, ogf hacywsd eu dsu huudxu
mace o wxojj noju vg rsvns vd roj ugnxcjuf. Vd roj o huoydvmyx jnoaohouyj, ogf, od
dsod dveu, yglgcrg dc godyaoxvjdj—cm ncyaju o wauod pavbu vg o jnvugdvmvn pcvgd
cm ivur. Dsuau ruau drc acygf hxonl jpcdj guoa cgu ukdauevdq cm dsu honl, ogf o
xcgw cgu guoa dsu cdsua. Dsu jnoxuj ruau uknuufvgwxq soaf ogf wxcjjq, rvds oxx dsu
oppuoaognu cm hyagvjsuf wcxf. Dsu ruvwsd cm dsu vgjund roj iuaq aueoalohxu, ogf,
dolvgw oxx dsvgwj vgdc ncgjvfuaodvcg, V ncyxf soafxq hxoeu Zypvdua mca svj cpvgvcg
aujpundvgw vd.

Dsu mxow vj: pvncNDM{5YH5717Y710G_3I0XY710G_03055505}"""

print("=== CIFRADO DE SUSTITUCIÓN ===")

# Separar la clave del texto cifrado
lines = ciphertext.split('\n')
key = lines[0].strip()  # Primera línea es la clave
encrypted_text = '\n'.join(lines[2:])  # El texto empieza después del espacio

print("Clave:", key)
print("Longitud de la clave:", len(key))
print()

print("Texto cifrado:")
print(encrypted_text)
print("\n" + "="*50 + "\n")

# Descifrar
decrypted = substitution_decrypt(encrypted_text, key)

print("Texto descifrado:")
print(decrypted)