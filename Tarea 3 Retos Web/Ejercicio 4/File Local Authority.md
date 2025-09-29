#  - Local Authority

## Descripcion:
* Can you get the flag?
Additional details will be available after launching your challenge instance.
* How is the password checked on this website?

## Solucion:
* http://saturn.picoctf.net:60991
* http://saturn.picoctf.net:60991/login.php
* http://saturn.picoctf.net:60991/secure.js
* if( username === 'admin' && password === 'strongPassword098765' )
* picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}

## Notas:
* entramos a la pagina web
* vemos que se redireccionan todos los usuarios a login.php
* vemos que pasa en la pagina y no tiene nada asi que otra ves inspeccionamos el codigo
* nos manda a un js donde nos dice que el admin tiene una contraseña
* la insertamos en la pagina 
* nos da la bandera

## Referencias: