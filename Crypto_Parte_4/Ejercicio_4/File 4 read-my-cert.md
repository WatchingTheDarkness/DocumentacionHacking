# 4 - ReadMyCert

## Descripcion:
* How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file here.
* Download the certificate signing request and try to read it.

## Solucion:
* wget https://artifacts.picoctf.net/c/421/readmycert.csr
* openssl req -in readmycert.csr -noout -text
* openssl req -in readmycert.csr -noout -subject
* picoCTF{read_mycert_3aa80090}

## Notas:
* descargamos el archivo
* abrimos lo que contiene el archivo
* vemos unicamente si tiene una caracteristica subject para tener la bandera
* bandera

## Referencias: