01 - Lets Warm Up

Descripcion: 
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

Solucion:
Use una pagina para saber y convertir de hex a scii
https://www.chileoffshore.com/es/toolkits/basic-conversion/hexa-to-ascii

# Forma 1
## picoCTF{p}

# Forma 2
OscarVillegas-picoctf@webshell:~$ python
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x70)
112
>>> chr(112)
'p'
>>> 

Notas:
- ciberchef es una pagina web que sirve para decodificar y resolver problemas 

Referencias:
https://www.chileoffshore.com/es/toolkits/basic-conversion/hexa-to-ascii