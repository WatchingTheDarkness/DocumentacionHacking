# 4 - extensions

## Descripcion:
* This is a really weird text file TXT? Can you find the flag?
* How do operating systems know what kind of file it is? (It's not just the ending!
* Make sure to submit the flag as picoCTF{XXXXX}

## Solucion:
* wget https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt
* file flag.txt
* mv flag.txt flag.png
* file flag.png
* sz flag.png
* picoCTF{now_you_know_about_extensions}

## Notas:
* descargamos el archivp
* verificamos si es un .txt
* movemos el archivo png fuera del .txt
* abrimos el archivo 
* descargamos el nuevo archivo png
* vemos que la imagen tiene la bandera

## Referencias: