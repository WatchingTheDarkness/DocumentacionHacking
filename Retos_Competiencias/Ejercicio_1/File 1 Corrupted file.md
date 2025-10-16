# 1 - Corrupted files

## Descripcion:
* This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file here.
* Try checking the file’s header.
* JPEG
* Tools like xxd or hexdump can help you inspect and edit file bytes.

## Solucion:
* file file
* xxd file | head -1
* hexdump -C file | head -1
* printf '\xff\xd8' | dd of=file bs=1 seek=0 count=2 conv=notrunc
* file file
* xdg-open file
* picoCTF{r3st0r1ng_th3_by73s_b67c1558}

## Notas:
* verificamos que archivo es
* muestro a ver si contiene el archivo exadecimal
* vemos que si de pura casualidad el archivo tambien tiene propiedades hexdump con representación ASCII
* reemplaza los primeros 2 bytes del archivo por FF D8
* otra ves verificamos los archivos 
* abrimos el archivo que nos dio
* nos da la bandera

## Referencias:
