# 20 - First Find

## Descripcion:
* Unzip this archive and find the file named 'uber-secret.txt'

## Solucion:
* wget https://artifacts.picoctf.net/c/500/files.zip
* ls
* unzip files.zip
* grep -r pico files
* picoCTF{f1nd_15_f457_ab443fd1}

## Notas:
* primero descargamos el .zip
* despues buscamos el contenido de como se llama la carpeta .zip
* descomprimimos
* despues buscamos la carpeta indicada y ponemos el grep -r pico files que es en la carpeta que requerimos 
* y nos enseñara la bandera

## Referencias: