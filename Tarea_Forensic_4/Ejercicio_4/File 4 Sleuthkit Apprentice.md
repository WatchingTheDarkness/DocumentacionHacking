# 4 - Sleuthkit Apprentice

## Descripcion:
* Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
* Download compressed disk image

## Solucion:
* wget https://artifacts.picoctf.net/c/138/disk.flag.img.gz
* gzip -d disk.img.gz 
* mmls disk.flag.img
* fls -o 2048 disk.flag.img 
* fls -o 360448 -r disk.flag.img
* icat  -o 360448 -r disk.flag.img 2371
* picoCTF{by73_5urf3r_2f22df38}

## Notas:
* descargamos el archivo
* lo descomprimimos
* Examinar el tipo de archivo
* Listamos los archivos de la primer partición de Linux con fls
* Al no encontrar nada cambiamos de partición y hacemos un listado recursivo
* Visualizamos el archivo que contiene la bandera en base a su offset con icat
* bandera

## Referencias:
