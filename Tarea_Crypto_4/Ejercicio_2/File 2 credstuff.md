# 2 - credstuff

## Descripcion:
* We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.
* Maybe other passwords will have hints about the leak?

## Solucion:
* wget https://artifacts.picoctf.net/c/151/leak.tar
* tar -xf leak.tar
* cd leak
* ls -la
* head usernames.txt
* head passwords.txt
* grep -n "cultiris" usernames.txt
* sed -n '378p' passwords.txt
* cvpbPGS{P7e1S_54I35_71Z3}
* File 2 credstuff.py
* picoCTF{C7r1F_54V35_71M3}

## Notas:
* descargamos el archivo .tar
* lo descomprimimos
* entramos a la capeta
* verificamos los archivo user y password
* verificamos si tiene una contraseña el usuario
* nos da la contraseña
* nos da la flag encriptada
* ejecutamos el script para desencriptar
* bandera

## Referencias: