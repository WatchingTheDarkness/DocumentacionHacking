# 5 - Picker II

## Descripcion:
* Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
* Can you do what win does with your input to the program?
* Connect to the program with netcat:
* $ nc saturn.picoctf.net 62398
* The program's source code can be downloaded here

## Solucion:
* wget https://artifacts.picoctf.net/c/523/picker-II.py
* pricker-II.py
* nc saturn.picoctf.net 62398
* print(open('flag.txt', 'r').read())
* picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}

## Notas:
* descargamos el archivo
* abrimos el script para encontrar la contraseña
* abrimos el servidor
* ponemos la contraseña
* bandera

## Referencias: