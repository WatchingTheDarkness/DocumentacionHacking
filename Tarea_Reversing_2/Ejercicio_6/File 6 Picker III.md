# 6 - Picker III

## Descripcion:
* Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
* Is there any way to modify the function table?
* Connect to the program with netcat:
* $ nc saturn.picoctf.net 52375
* The program's source code can be downloaded here.

## Solucion:
* wget https://artifacts.picoctf.net/c/525/picker-III.py
* picker-III.py
* nc saturn.picoctf.net 52375
* help
* 3
* win
* 2
* 0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x61 0x31 0x38 0x36 0x66 0x39 0x61 0x63 0x7d
* picker 3.py
* picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_a186f9ac}

## Notas:
* descargamos el archivo
* lo analizamos la la futura contraseña
* entramos al servidor
* escribimos el comando help para que nos de las distintas rutas
* escogemos la 3 para que nos pida el nombre de la contraseña
* escribimos win
* escogemos 2 para que nos puestre la bandera
* bandera pero en base 64
* creamos un script donde lo descodificamos 
* bandera

## Referencias: