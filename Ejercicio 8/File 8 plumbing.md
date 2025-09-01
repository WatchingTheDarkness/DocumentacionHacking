# 08 - plumbing

## Descripcion:
* Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

## Solucion:
* nc jupiter.challenges.picoctf.org 7480 | grep picoCTF este comando nos muestra todo el texto pero con grep nos mostrara la bandera
* nc jupiter.challenges.picoctf.org 7480 > bandera
* picoCTF{digital_plumb3r_06e9d954}

## Notas:

## Referencias:
* http://www.linfo.org/pipes.html