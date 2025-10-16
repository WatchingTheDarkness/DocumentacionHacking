# 5 - Operation Orchid

## Descripcion:
* Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
* Download compressed disk image

## Solucion:
* wget https://artifacts.picoctf.net/c/214/disk.flag.img.gz
* gzip -d disk.flag.img.gz
* mmls disk.flag.img
* fls -o 411648 disk.flag.img
* icat -i raw -o 411648 disk.flag.img 1875
* icat -o 411648  disk.flag.img 1782
* icat -o 411648  disk.flag.img 1782 > flag.txt.enc
* openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
* cat flag.txt
* picoCTF{h4un71ng_p457_1d02081e}

## Notas:
* descargamos el archivo
* lo descomprimimos
* Listamos las particiones:
* Listamos los archivos en la partición Linux donde estan los dato
* Vemos el archivo con el historial de comandos, para ver como fue encriptada la bandera
* Vemo el archivo que tiene la bandera encriptada:
* Grabamos la bandera encriptada en un archivo local
* Desencriptamos la bandera, haciendo las operaciones inversas que se usaron para encriptarla
* Mostrmos la bandera
* bandera

## Referencias:
