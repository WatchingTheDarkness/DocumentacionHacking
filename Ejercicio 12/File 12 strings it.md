# 12 - Strings It

## Descripcion:
* Can you find the flag in file without running it?

## Solucion:
* wget https://jupiter.challenges.picoctf.org/static/fae9ac5267cd6e44124e559b901df177/strings
* strings strings | grep pico
* picoCTF{5tRIng5_1T_7f766a23}

## Notas:
* tubimos que hacer un strings al archivo llamado strings para que buscara ciertos caracteres en el archivo y los que queremos buscar utilizamos el | grep mas la palabra que es pico
* para poder ejecutar un archivo necesito tener permisos y si no lo tengo podemos hacer o poner el comando chmod +x strings luego ls -la strings para ver que se esta haciendo

## Referencias: