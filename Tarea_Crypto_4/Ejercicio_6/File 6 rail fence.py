def rail_fence_decrypt(ciphertext, rails):
    # Crear una matriz para los rieles
    fence = [[''] * len(ciphertext) for _ in range(rails)]
    
    # Patrón para llenar la valla
    rail = 0
    direction = 1  # 1 para abajo, -1 para arriba
    
    # Marcar las posiciones que tendrán caracteres
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    # Llenar la valla con el texto cifrado
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*':
                fence[i][j] = ciphertext[index]
                index += 1
    
    # Leer en zig-zag para obtener el texto plano
    result = []
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    return ''.join(result)

def rail_fence_decrypt_alternative(ciphertext, rails):
    """Método alternativo para descifrar rail fence"""
    # Crear lista de listas para cada rail
    fence = [[] for _ in range(rails)]
    
    # Calcular el patrón
    pattern = []
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    # Distribuir el texto cifrado según el patrón
    rail_lengths = [pattern.count(i) for i in range(rails)]
    rail_texts = []
    start = 0
    
    for length in rail_lengths:
        rail_texts.append(ciphertext[start:start + length])
        start += length
    
    # Reconstruir el texto plano
    result = []
    rail_positions = [0] * rails
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        result.append(rail_texts[rail][rail_positions[rail]])
        rail_positions[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    
    return ''.join(result)

# Mensaje cifrado
ciphertext = "Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6"

print("Mensaje cifrado:", ciphertext)
print("Longitud:", len(ciphertext))
print()

# Probar con 4 rieles (como dice el problema)
for rails in [4, 3, 5]:  # Probar 4 primero, luego otros si es necesario
    print(f"Probando con {rails} rieles:")
    decrypted = rail_fence_decrypt(ciphertext, rails)
    print(f"Resultado: {decrypted}")
    
    # Verificar si parece un flag válido
    if 'pico' in decrypted.lower() or 'ctf' in decrypted.lower() or '{' in decrypted:
        print("🎯 ¡Posible flag encontrada!")
    
    print()