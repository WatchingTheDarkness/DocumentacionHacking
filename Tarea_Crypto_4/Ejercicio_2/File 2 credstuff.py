import codecs

# Contraseña cifrada
encrypted = "cvpbPGS{P7e1S_54I35_71Z3}"

# Aplicar ROT13
decrypted = codecs.encode(encrypted, 'rot_13')

print(f"Texto cifrado: {encrypted}")
print(f"Texto descifrado: {decrypted}")

# Verificar si es válido
if decrypted.startswith("picoCTF{"):
    print("✅ ¡Flag encontrada!")