#  - Intro to Burp

## Descripcion:
* Additional details will be available after launching your challenge instance.
* Try using burpsuite to intercept request to capture the flag.
* Try mangling the request, maybe their server-side code doesn't handle malformed requests very well.

## Solucion:
* titan.picoctf.net:50812
* descarga y configuracion de foxyproxy y burp suite
* activamos el proxy de foxyproxy que configuramos
* abrimos la app de burp nos colocamos en proxy y en la pagina web rellenamos los campos
* cuando los rellenemos, en burp le damos en fordward hasta que se actualizce la pagina
* entramos una nueva ves a la pagina web y en contraseña de admin le ponemos la que sea
* entramos otra ves a burp y le damos fordward hasta que nos salga la contraseña que pusimos en la pagina
* modificamos la linea de texto de la contraseña que nos sale para dejarlo sin nada
* otra ves le ponemos forward y entramos a la pagina web
* nos da la bandera
* picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}

## Notas:

## Referencias: