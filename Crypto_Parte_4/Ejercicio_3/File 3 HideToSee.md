# 3 - HideToSee

## Descripcion:
* How about some hide and seek heh? Look at this image here.
* Download the image and try to extract it.

## Solucion:
* wget https://artifacts.picoctf.net/c/236/atbash.jpg
* steghide extract -sf atbash.jpg
* cat encrypted.txt
* picoCTF{atbash_crack_ac751ec6}

## Notas:
* descargamos el archivo .png
* verificamos si no tenia datos ocultos en la imagen
* vemos los datos que tenian ocultos
* bandera

## Referencias: