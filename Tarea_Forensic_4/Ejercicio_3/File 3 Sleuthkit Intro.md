# 3 - Sleuthkit Intro

## Descripcion:
* Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Download disk image
Additional details will be available after launching your challenge instance.


## Solucion:
* wget https://artifacts.picoctf.net/c/164/disk.img.gz
* gzip -d disk.img.gz
* file disk.img
* mmls disk.img
* 202752
* nc saturn.picoctf.net 57369
* picoCTF{mm15_f7w!}

## Notas:
* descargamos el archivo
* lo descomprimimos
* vemos que es lo que tiene el archivo
* vemos que tipo de datos esta dentro de la imagen
* vemos el numero de la particion del archivo
* nos conectamos al servidor y contestamos la pregunta dependiendo del tamaño de la particion del antiguo archivo mostrado
* bandera

## Referencias:
