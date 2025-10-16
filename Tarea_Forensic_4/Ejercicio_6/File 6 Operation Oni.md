# 6 - Operation Oni

## Descripcion:
* Download this disk image, find the key and log into the remote machine.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
Additional details will be available after launching your challenge instance.
* Download disk image
* Remote machine: ssh -i key_file -p 55856 ctf-player@saturn.picoctf.net

## Solucion:
* wget https://artifacts.picoctf.net/c/71/disk.img.gz
* gzip -d disk.img.gz
* mmls disk.img 
* fls -o 206848 disk.img
* fls -o 206848 disk.img 470
* fls -o 206848 disk.img 3916
* icat -o 206848 disk.img 2345 > id_rsa
* chmod 600 id_rsa
* ssh -i id_rsa -p 64715 ctf-player@saturn.picoctf.net
* ls
* cat flag.txt
* picoCTF{k3y_5l3u7h_af277f77}

## Notas:
* descargamos el archivo
* descomprimimos el archivo
* mostramos la bandera
* mostramos los datos de la bandera
* buscamos las llaves
* agregamos los datos de la llave
* verificamos los datos
* conectamos al puerto
* vemos los datos vemos lo que tiene el txt
* bandera

## Referencias:
