# 1 - Crack the Power

## Descripcion:
* We received an encrypted message. The modulus is built from primes large enough that factoring them isn’t an option, at least not today. See if you can make sense of the numbers and reveal the flag.
Download the message.
* When certain values in the encryption setup are smaller than usual, it opens up unexpected shortcuts to recover the plaintext
* Consider whether you can invert the encryption without factoring n.
* Read more about Coppersmith's_attack here

## Solucion:
* wget https://challenge-files.picoctf.net/c_amiable_citadel/17844e1db2c883adfc82f6601dfed7514cfbfce479cf0f0e63b32abb4aab8fc5/message.txt
* Crack the power.py
* picoCTF{t1ny_e_af0d7666}

## Notas:
* descargamos el mensaje
* vemos sus variables y creamos un script con los datos que nos dio
* bandera

## Referencias: