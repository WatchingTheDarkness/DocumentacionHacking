import hashlib

texto = input("Ingresa el código que quieras generar: ")
hash_md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
print(f"MD5: {hash_md5}")