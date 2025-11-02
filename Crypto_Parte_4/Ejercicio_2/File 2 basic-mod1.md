# 2 - basic-mod1

## Descripcion:
* Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
* Do you know what mod 37 means?
* mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Solucion:
* wget https://artifacts.picoctf.net/c/127/message.txt
* open basic mod1.py
* picoCTF{R0UND_N_R0UND_79C18FB3}

## Notas:
descargamos el archivo .txt, vemos que esta codigicado en ascii
entramos al script de python
bandera

## Referencias: