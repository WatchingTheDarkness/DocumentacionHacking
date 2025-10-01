# 2 - Chrono

## Descripcion:
* How to automate tasks to run at intervals on linux servers? Use ssh to connect to this server: Server: saturn.picoctf.net Port: 52861 Username: picoplayer Password: pYkku7iMsS

## Solucion:
* ssh -p 52861 picoplayer@saturn.picoctf.net
* yes
* pYkku7iMsS
* cat /etc/crontab
* picoCTF{Sch3DUL7NG_T45K3_L1NUX_7754e199}

## Notas:
* ingresamos al servidor
* damos permiso de entrar al servidor
* ponemos la contraseña
* buscamos con cat en el directorio etc/contab
* nos da la bandera

## Referencias: