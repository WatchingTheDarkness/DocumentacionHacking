# 3 - EVEN RSA CAN BE BROKEN???

## Descripcion:
* This service provides you an encrypted flag. Can you decrypt it with just N & e?
Additional details will be available after launching your challenge instance.
* How much do we trust randomness?
* Notice anything interesting about N?
* Try comparing N across multiple requests
* $ nc verbal-sleep.picoctf.net 50206
* The program's source code can be downloaded here.

## Solucion:
* wget https://challenge-files.picoctf.net/c_verbal_sleep 2b0f68c54cfcb2dafd4ca90c4abcbe73c208f09edf65af336fc7023e1c13 14ca/encrypt.py
* nc verbal-sleep.picoctf.net 50206
* encrypt.py
* picoCTF{tw0_1$_pr!m31c9046c4}

## Notas:
* descargamos el sript
* vemos que datos nos da el servidor al conectarnos
* modificamos el script
* bandera

## Referencias: