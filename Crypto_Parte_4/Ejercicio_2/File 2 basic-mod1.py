# Mensaje cifrado
numeros = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140]

# Aplicar mod 37 a cada número
modulos = [n % 37 for n in numeros]

# Mapear a caracteres
def mapear_caracter(num):
    if 0 <= num <= 25:
        return chr(num + 65)  # A=65 en ASCII
    elif 26 <= num <= 35:
        return chr(num - 26 + 48)  # 0=48 en ASCII
    elif num == 36:
        return '_'
    else:
        return '?'

# Descifrar el mensaje
mensaje_descifrado = ''.join(mapear_caracter(n) for n in modulos)

# Formatear como flag
flag = f"picoCTF{{{mensaje_descifrado}}}"

print("Números originales:", numeros)
print("Después de mod 37:", modulos)
print("Mensaje descifrado:", mensaje_descifrado)
print("Flag:", flag)