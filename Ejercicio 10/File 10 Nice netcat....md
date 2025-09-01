# 10 - Nice netcat...

## Descripcion:
* There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 21135, but it doesn't speak English...

## Solucion:
* nc mercury.picoctf.net 21135
* generamos el codigo ascii en python con los numeros
* codigos_ascii = [
    112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116,
    116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95,
    97, 102, 100, 53, 102, 100, 97, 52, 125, 10
]

* oracion = ''.join(chr(codigo) for codigo in codigos_ascii)
* picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}

## Notas:
generamos el codigo ascii en python

## Referencias: