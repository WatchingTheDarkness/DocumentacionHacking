# 1 - Irish-Name-Repo 1

## Descripcion:
* There is a website running at https://jupiter.challenges.picoctf.org/problem/50009/ (link) or http://jupiter challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!
* There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
* Try to think about how the website verifies your login.

## Solucion:
* https://jupiter.challenges.picoctf.org/problem/50009/login.html
* codigo fuente
* hidden borramos
* admin'; admin
* 0 = 1
* 
* admin' or 1 = 1;
* picoCTF{s0m3_SQL_fb3fe2ad}

## Notas:
* entramos a la pagina indicada
* entramos al codigo fuente
* vemos que el tipo de texto esta oculto y lo desocultamos
* en el nombre lo ponemos admin'; y contraseña admin
* en la interfaz le ponemos 1
* o
* le ponemos en el nombre admin el siguiente comando
* nos da la contraseña

## Referencias: