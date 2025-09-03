# 14 - Static ain't always noise

## Descripcion:
* Can you look at the data in this binary: static? This BASH script might help!

## Solucion:
* wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/ltdis.sh
* wget https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static
* file *
* strings static | grep pico
* picoCTF{d15a5m_t34s3r_f5aeda17}

## Notas:
* descargamos todos los archivos que son 2
* vemos todos los archivos
* lo mandamos a llamar con strings y grep los archivos llamados pico
* nos puestran la bandera

## Referencias: