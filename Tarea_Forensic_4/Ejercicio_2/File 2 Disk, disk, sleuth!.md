# 2 - Disk, disk, sleuth!

## Descripcion:
* Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz
* Have you ever used `file` to determine what a file was?
* Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
* Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
* Using your own computer, you could use qemu to boot from this disk!

## Solucion:
* wget https://mercury.picoctf.net/static/a734f18939e0aaea9d27bc7a243a0ed0/dds1-alpine.flag.img.gz
* gzip -d dds1-alpine.flag.img.gz
* file dds1-alpine.flag.img
* srch_strings dds1-alpine.flag.img | grep pico
* picoCTF{f0r3ns1c4t0r_n30phyt3_a69a712c}

## Notas:
* descargamos el documento
* lo descomprimimos
* vemos como esta configurado el archivo
* buscamos la bandera con un string con la palabra clave pico señalandolo con grep
* bandera

## Referencias:
