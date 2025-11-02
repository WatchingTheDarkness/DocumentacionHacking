def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determinar desplazamiento de la clave
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.isupper():
                plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            key_index += 1
        else:
            plaintext.append(char)
    return ''.join(plaintext)

ciphertext = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}"
key = "CYLAB"

decrypted = vigenere_decrypt(ciphertext, key)
print(decrypted)