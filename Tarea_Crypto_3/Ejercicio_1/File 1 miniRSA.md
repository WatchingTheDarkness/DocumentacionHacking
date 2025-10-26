# 1 - miniRSA

## Descripcion:
* Let's decrypt this: ciphertext? Something seems a bit small.
* RSA tutorial
* How could having too small an e affect the security of this 2048 bit key?
* Make sure you don't lose precision, the numbers are pretty big (besides the e value)

## Solucion:
* wget https://jupiter.challenges.picoctf.org/static/eb5e6df8e14c52873cf88c582a1a4008/ciphertext
* enter .py
* valor n, e c
* run
* picoCTF{n33d_a_lArg3r_e_d0cd6eae}

## Notas:
* descargamos el documento
* nos guiamos de un sript de python
* ingresamos los valores que nos dieron en el .text
* corremos el script modificado
* bandera

## Referencias:
* https://en.wikipedia.org/wiki/RSA_cryptosystem
* https://riptutorial.com/python/example/8751/computing-large-integer-roots