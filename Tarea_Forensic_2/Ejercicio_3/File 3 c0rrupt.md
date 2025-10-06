# 3 - c0rrupt

## Descripcion:
* We found this file. Recover the flag.
* Try fixing the file header

## Solucion:
* wget https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery
* mostramos la cabecera del archivo y nos damos cuenta que esta corrupta para ser un png deberia ser 89 50 4E 47 0D 0A 1A 0A
* corregimos pHys, cambiamos aa 00 16 25 00 00 16 25  por 00 00 16 25 00 00 16 25
* corregimos el tamaño del chunk, cambiamos AA AA FF A5 por  00 00 FF A5
* corregir chunk anterior para que diga IDAT , cambiamos AB 44 45 54 por 49 44 41 54
* verificamos y abrimos el archivo para la flag
* file mistery
* open mistery
* picoCTF{c0rrupt10n_1847995}

## Notas:

## Referencias: