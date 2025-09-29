#  - Secrets

## Descripcion:
* We have several pages hidden. Can you find the one with the flag?
Additional details will be available after launching your challenge instance.
* folders folders folders

## Solucion:
* http://saturn.picoctf.net:57310/contact.html
* view-source:saturn.picoctf.net:57310/contact.html
* http://saturn.picoctf.net:57310/secret/
* view-source:saturn.picoctf.net:57310/secret/
* http://saturn.picoctf.net:57310/secret/hidden/
* view-source:saturn.picoctf.net:57310/secret/hidden/
* http://saturn.picoctf.net:57310/secret/hidden/superhidden/login.css
* http://saturn.picoctf.net:57310/secret/hidden/superhidden/
* picoCTF{succ3ss_@h3n1c@10n_39849bcf}

## Notas:
* entramos a la pagina
* inspeccionamos el codigo y vemos que nos señala a otra subpagina llamada secret
* entramos esta nos redirige a otra llamada hidden 
* entramos y esta nos redirige a otra llamada superhidden
* entramos pero vemos que estamos en el login del css y quitamos el css
* entramos a otra pagina y alli en letras blancas esta
* lo seleccionamos y nos dira la bandera

## Referencias: