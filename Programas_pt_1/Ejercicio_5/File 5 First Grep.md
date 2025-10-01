# 05 - First Grep

## Descripcion:
* Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

## Solucion:
wget https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file
wc file
grep 'picoCTF' file
picoCTF{grep_is_good_to_find_things_f77e0797}
## Notas:
* Se tendra que generar el comando desde la terminal de linux para que muestre los resultados del comando grep

## Referencias:
* man grep y buscar