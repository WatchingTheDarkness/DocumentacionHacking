# 4 - hashcrack

## Descripcion:
* A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Additional details will be available after launching your challenge instance.
* Understanding hashes is very crucial. Read more here.
* Can you identify the hash algorithm? Look carefully at the length and structure of each hash identified.
* Tried using any hash cracking tools?
* Access the server using nc verbal-sleep.picoctf.net 57223

## Solucion:
* nc verbal-sleep.picoctf.net 57223
* hashcrack.py
* password123
* segundo hashcrack.py
* letmein
* tercer hashcrack.py
* picoCTF{UseStr0nG_h@shEs_&PaSswDs!_5b836723}

## Notas:
* nos conectamos al servidor
* cramos un script para hacer fuerza bruta y tener el primer hash
* cramos un script para hacer fuerza bruta y tener el segundo hash
* cramos un script para hacer fuerza bruta y tener el tercer hash
* bandera

## Referencias: