# 4 - Picker I

## Descripcion:
* This service can provide you with a random number, but can it do anything else?
Additional details will be available after launching your challenge instance.
* Can you point the program to a function that does something useful for you?
* Connect to the program with netcat:
* $ nc saturn.picoctf.net 52423
* The program's source code can be downloaded here.


## Solucion:
* wget https://artifacts.picoctf.net/c/513/picker-I.py
* picker-I.py
* win()
* $ nc saturn.picoctf.net 52423
* picker 1.py
* picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}

## Notas:
* descargamos el archivo
* vemos el archivo descargando donde nos da la clave del servidor
* entramos al servidor, vemos que la bandera esta en ascii
* descodificamos con un script 
* bandera

## Referencias: