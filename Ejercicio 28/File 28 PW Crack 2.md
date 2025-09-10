# 28 - PW Crack 2

## Descripcion:
* Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

## Solucion:
* wget https://artifacts.picoctf.net/c/13/level2.py
* wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
* cat level2.py
* chr(0x64) = d (hex 64 = decimal 100)
* chr(0x65) = e (hex 65 = decimal 101)
* chr(0x37) = 7 (hex 37 = decimal 55)
* chr(0x36) = 6 (hex 36 = decimal 54)
* de76
* picoCTF{tr45h_51ng1ng_489dea9a}

## Notas:
* descargamos los 2 archivos
* vemos que contienen los archivos
* vemos que la contraseña es desimal
* ponemos la contraseña
* nos dan la bandera

## Referencias: