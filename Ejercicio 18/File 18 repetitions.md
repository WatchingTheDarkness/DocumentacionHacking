# 18 - repetitions

## Descripcion:
* Can you make sense of this file?
Download the file here.

## Solucion:
* wget https://artifacts.picoctf.net/c/476/enc_flag
* cat enc_flag
* cat enc_flag | base64 -d
* cat enc_flag | base64 -d | base64 -d
* cat enc_flag | base64 -d | base64 -d | base64 -d
* cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
* cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
* cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
* picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}

## Notas:
* descargamos el archivo, 
* entramos a la carpeta
* descubrimos que es base a 64
* lo repetimos barias veces hasta que ya no este a base 64
* nos da la bandera

## Referencias: