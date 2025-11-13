# 7 - Picker IV

## Descripcion:
* Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
* With Python, there are no binaries. With compiled languages like C, there is source code, and there are binaries. Binaries are created from source code, they are a conversion from the human-readable source code, to the highly efficient machine language, in this case: x86_64.
* How can you find the address that win is at?
* Connect to the program with netcat:
* $ nc saturn.picoctf.net 60267
* The program's source code can be downloaded here. The binary can be downloaded here.

## Solucion:
* wget https://artifacts.picoctf.net/c/528/picker-IV
* wget https://artifacts.picoctf.net/c/528/picker-IV.c
* picker 4.py
* picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_14bc5444}

## Notas:
* descargamos los archivos
* ejecutamos un script en pyton para que busque nuestra bandera
* bandera

## Referencias: