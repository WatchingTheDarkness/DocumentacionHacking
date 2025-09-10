# 29 - PW Crack 3

## Descripcion:
* Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Solucion:
* wget https://artifacts.picoctf.net/c/16/level3.py
* wget https://artifacts.picoctf.net/c/16/level3.flag.txt.enc
* wget https://artifacts.picoctf.net/c/16/level3.hash.bin
* cat level3.py
* 6997
* 3ac8
* f0ac
* 4b17
* ec27
* 4e66
* 865e
* python3 level3.py
* picoCTF{m45h_fl1ng1ng_2b072a90}

## Notas:
* descargamos los 3 archivos
* vemos que contiene el archivo
* vemos las contraseñas posibles
* ejecutamos el archivo
* probamos las contraseñas
* fue la ultima
* nos da la bandera

## Referencias: