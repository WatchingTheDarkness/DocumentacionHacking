import base64

encoded_string = "bDNhcm5fdGgzX3IwcDM1"

decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')

print(f"Cadena original: {encoded_string}")
print(f"Decodificado: {decoded_string}")