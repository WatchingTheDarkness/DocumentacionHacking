# 3 - logon

## Descripcion:
* The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/13594/ (link) or http://jupiter.challenges.picoctf.org:13594

## Solucion:
* https://jupiter.challenges.picoctf.org/problem/13594/
* pancho pancho
* network
* con cookie editor (admin = true)
* f5
* picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
* curl -X GET https://jupiter.challenges.picoctf.org/problem/13594/flag -H "Cookie: username=admin; password=admin; admin=True;"
* picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}

## Notas:
* ingresamos a la pagina
* nos logramos
* entramos al network para ver si nuestro usuario tiene permisos
* entramos a cookie editor para ponernos permisos
* recargamos la pagina
* nos da la bandera
* el comando nos da lo mismos

## Referencias: