# 7 - Java Code Analysis!?!

## Descripcion:
* BookShelf Pico, my premium online book-reading service.
I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!
Additional details will be available after launching your challenge instance.
* Maybe try to find the JWT Signing Key ("secret key") in the source code? Maybe it's hardcoded somewhere? Or maybe try to crack it?
* The 'role' and 'userId' fields in the JWT can be of interest to you!
* The 'controllers', 'services' and 'security' java packages in the given source code might need your attention. We've provided a README.md file that contains some documentation.
* Upgrade your 'role' with the new (cracked) JWT. And re-login for the new role to get reflected in browser's localStorage.

## Solucion:
* entramos a la pagina
* ponemos control + shift + i
* copeamos el archivo que vamos a modificar 
* cambiamos Admin 2 admin
* eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiQWRtaW4iLCJpc3MiOiJib29rc2hlbGYiLCJleHAiOjE3NjA1NjQwNDEsImlhdCI6MTc1OTk1OTI0MSwidXNlcklkIjoyLCJlbWFpbCI6ImFkbWluIn0.7Cd6f8ZKKK697zEFA5H6GiqppN61-3-NbnkPteB1eEU
* pegamos todo y lo modificamos
* recargamos la pagina
* picoCTF{w34k_jwt_n0t_g00d_d72df65e}

## Notas:

## Referencias: